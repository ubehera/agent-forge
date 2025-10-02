"""
Production-ready data quality monitoring system
Detects missing data, staleness, outliers, and provider issues
"""

from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text
import logging

logger = logging.getLogger(__name__)


@dataclass
class DataQualityIssue:
    """Data quality issue structure"""
    severity: str  # 'critical', 'warning', 'info'
    issue_type: str
    symbol: str
    timestamp: datetime
    description: str
    metadata: Dict


class DataQualityMonitor:
    """Monitor data quality for market data pipeline"""

    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)

    def check_missing_bars(
        self,
        symbol: str,
        start: datetime,
        end: datetime,
        timeframe: str = "1D"
    ) -> List[DataQualityIssue]:
        """Detect missing bars in time series"""

        issues = []

        query = text("""
            SELECT time, symbol
            FROM stock_bars
            WHERE symbol = :symbol
              AND timeframe = :timeframe
              AND time BETWEEN :start AND :end
            ORDER BY time
        """)

        with self.engine.connect() as conn:
            result = conn.execute(
                query,
                {"symbol": symbol, "timeframe": timeframe, "start": start, "end": end}
            )
            df = pd.DataFrame(result.fetchall(), columns=["time", "symbol"])

        if df.empty:
            issues.append(DataQualityIssue(
                severity="critical",
                issue_type="no_data",
                symbol=symbol,
                timestamp=datetime.now(),
                description=f"No data found for {symbol} in specified range",
                metadata={"start": start, "end": end, "timeframe": timeframe}
            ))
            return issues

        # Check for gaps
        df["time"] = pd.to_datetime(df["time"])
        df = df.sort_values("time")

        # Calculate expected frequency based on timeframe
        freq_map = {
            "1Min": timedelta(minutes=1),
            "5Min": timedelta(minutes=5),
            "1H": timedelta(hours=1),
            "1D": timedelta(days=1)
        }

        expected_delta = freq_map.get(timeframe, timedelta(days=1))

        # Detect gaps larger than expected
        time_diffs = df["time"].diff()
        gaps = time_diffs[time_diffs > expected_delta * 1.5]  # 50% tolerance

        for idx in gaps.index:
            issues.append(DataQualityIssue(
                severity="warning",
                issue_type="missing_bars",
                symbol=symbol,
                timestamp=df.loc[idx, "time"],
                description=f"Gap detected: {time_diffs[idx]}",
                metadata={
                    "expected": str(expected_delta),
                    "actual": str(time_diffs[idx]),
                    "previous_bar": str(df.loc[idx - 1, "time"])
                }
            ))

        return issues

    def check_stale_data(
        self,
        symbol: str,
        max_age: timedelta = timedelta(hours=1)
    ) -> Optional[DataQualityIssue]:
        """Check if data is stale (not updated recently)"""

        query = text("""
            SELECT MAX(time) as last_update
            FROM stock_bars
            WHERE symbol = :symbol
        """)

        with self.engine.connect() as conn:
            result = conn.execute(query, {"symbol": symbol})
            row = result.fetchone()

        if not row or not row[0]:
            return DataQualityIssue(
                severity="critical",
                issue_type="no_data",
                symbol=symbol,
                timestamp=datetime.now(),
                description=f"No data found for {symbol}",
                metadata={}
            )

        last_update = row[0]
        age = datetime.now() - last_update

        if age > max_age:
            return DataQualityIssue(
                severity="warning",
                issue_type="stale_data",
                symbol=symbol,
                timestamp=datetime.now(),
                description=f"Data is {age} old (threshold: {max_age})",
                metadata={"last_update": str(last_update), "age": str(age)}
            )

        return None

    def check_price_outliers(
        self,
        symbol: str,
        lookback_days: int = 30,
        std_threshold: float = 5.0
    ) -> List[DataQualityIssue]:
        """Detect price outliers using z-score"""

        issues = []

        query = text("""
            SELECT time, symbol, close, volume
            FROM stock_bars
            WHERE symbol = :symbol
              AND time > NOW() - INTERVAL :lookback
              AND timeframe = '1D'
            ORDER BY time
        """)

        with self.engine.connect() as conn:
            result = conn.execute(
                query,
                {"symbol": symbol, "lookback": f"{lookback_days} days"}
            )
            df = pd.DataFrame(result.fetchall(), columns=["time", "symbol", "close", "volume"])

        if len(df) < 10:
            return issues

        # Calculate returns
        df["return"] = df["close"].pct_change()

        # Z-score for returns
        mean_return = df["return"].mean()
        std_return = df["return"].std()

        df["z_score"] = (df["return"] - mean_return) / std_return

        # Flag outliers
        outliers = df[df["z_score"].abs() > std_threshold]

        for _, row in outliers.iterrows():
            issues.append(DataQualityIssue(
                severity="warning",
                issue_type="price_outlier",
                symbol=symbol,
                timestamp=row["time"],
                description=f"Abnormal return: {row['return']:.2%} (z-score: {row['z_score']:.2f})",
                metadata={
                    "close": float(row["close"]),
                    "return": float(row["return"]),
                    "z_score": float(row["z_score"])
                }
            ))

        return issues

    def check_volume_anomalies(
        self,
        symbol: str,
        lookback_days: int = 30,
        threshold_multiplier: float = 3.0
    ) -> List[DataQualityIssue]:
        """Detect unusual volume spikes"""

        issues = []

        query = text("""
            SELECT time, symbol, volume
            FROM stock_bars
            WHERE symbol = :symbol
              AND time > NOW() - INTERVAL :lookback
              AND timeframe = '1D'
            ORDER BY time
        """)

        with self.engine.connect() as conn:
            result = conn.execute(
                query,
                {"symbol": symbol, "lookback": f"{lookback_days} days"}
            )
            df = pd.DataFrame(result.fetchall(), columns=["time", "symbol", "volume"])

        if len(df) < 10:
            return issues

        # Calculate rolling average volume
        df["avg_volume"] = df["volume"].rolling(window=20).mean()
        df["volume_ratio"] = df["volume"] / df["avg_volume"]

        # Flag unusual volume
        anomalies = df[df["volume_ratio"] > threshold_multiplier]

        for _, row in anomalies.iterrows():
            issues.append(DataQualityIssue(
                severity="info",
                issue_type="volume_anomaly",
                symbol=symbol,
                timestamp=row["time"],
                description=f"Volume {row['volume_ratio']:.1f}x average",
                metadata={
                    "volume": int(row["volume"]),
                    "avg_volume": int(row["avg_volume"]),
                    "ratio": float(row["volume_ratio"])
                }
            ))

        return issues

    def run_full_quality_check(
        self,
        symbols: List[str]
    ) -> Dict[str, List[DataQualityIssue]]:
        """Run comprehensive quality checks on multiple symbols"""

        all_issues = {}

        for symbol in symbols:
            issues = []

            # Check for missing bars
            issues.extend(self.check_missing_bars(
                symbol,
                start=datetime.now() - timedelta(days=7),
                end=datetime.now(),
                timeframe="1D"
            ))

            # Check for stale data
            stale_issue = self.check_stale_data(symbol)
            if stale_issue:
                issues.append(stale_issue)

            # Check for price outliers
            issues.extend(self.check_price_outliers(symbol))

            # Check for volume anomalies
            issues.extend(self.check_volume_anomalies(symbol))

            if issues:
                all_issues[symbol] = issues

                # Log critical and warning issues
                for issue in issues:
                    if issue.severity == "critical":
                        logger.error(f"{symbol}: {issue.description}")
                    elif issue.severity == "warning":
                        logger.warning(f"{symbol}: {issue.description}")

        return all_issues

    def generate_quality_report(
        self,
        issues: Dict[str, List[DataQualityIssue]]
    ) -> str:
        """Generate human-readable quality report"""

        report_lines = ["# Market Data Quality Report", ""]
        report_lines.append(f"Generated: {datetime.now()}")
        report_lines.append(f"Symbols checked: {len(issues)}")
        report_lines.append("")

        # Summary by severity
        all_issues_flat = [issue for symbol_issues in issues.values() for issue in symbol_issues]
        severity_counts = {}
        for issue in all_issues_flat:
            severity_counts[issue.severity] = severity_counts.get(issue.severity, 0) + 1

        report_lines.append("## Summary")
        for severity, count in severity_counts.items():
            report_lines.append(f"- {severity.upper()}: {count}")
        report_lines.append("")

        # Details by symbol
        report_lines.append("## Details")
        for symbol, symbol_issues in sorted(issues.items()):
            report_lines.append(f"\n### {symbol}")
            for issue in symbol_issues:
                report_lines.append(f"- [{issue.severity.upper()}] {issue.issue_type}: {issue.description}")

        return "\n".join(report_lines)


# Usage example
def example_quality_monitoring():
    """Example of running data quality checks"""

    import os

    db_url = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost/market_data")
    monitor = DataQualityMonitor(db_url)

    # Check quality for watchlist
    watchlist = ["AAPL", "TSLA", "NVDA", "SPY", "QQQ"]
    issues = monitor.run_full_quality_check(watchlist)

    # Generate report
    report = monitor.generate_quality_report(issues)
    print(report)

    # Save report to file
    with open(f"data_quality_report_{datetime.now():%Y%m%d}.md", "w") as f:
        f.write(report)


if __name__ == "__main__":
    example_quality_monitoring()
