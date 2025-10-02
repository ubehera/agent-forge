"""
Comprehensive performance metrics for strategy evaluation
Sharpe, Sortino, Calmar ratios, drawdowns, trade statistics
"""

import numpy as np
import pandas as pd
from typing import Dict, Tuple


class PerformanceMetrics:
    """Calculate trading strategy performance metrics"""

    @staticmethod
    def calculate_returns(equity_curve: np.ndarray) -> np.ndarray:
        """Calculate returns from equity curve"""
        return np.diff(equity_curve) / equity_curve[:-1]

    @staticmethod
    def cagr(equity_curve: np.ndarray, years: float) -> float:
        """Compound Annual Growth Rate"""
        total_return = equity_curve[-1] / equity_curve[0]
        return (total_return ** (1 / years)) - 1

    @staticmethod
    def sharpe_ratio(
        returns: np.ndarray,
        risk_free_rate: float = 0.02,
        periods_per_year: int = 252
    ) -> float:
        """
        Sharpe Ratio (risk-adjusted return)
        Assumes daily returns by default
        """
        excess_returns = returns - (risk_free_rate / periods_per_year)
        return np.sqrt(periods_per_year) * np.mean(excess_returns) / (np.std(returns) + 1e-10)

    @staticmethod
    def sortino_ratio(
        returns: np.ndarray,
        risk_free_rate: float = 0.02,
        periods_per_year: int = 252
    ) -> float:
        """
        Sortino Ratio (downside risk-adjusted return)
        Only penalizes downside volatility
        """
        excess_returns = returns - (risk_free_rate / periods_per_year)
        downside_returns = returns[returns < 0]
        downside_std = np.std(downside_returns) if len(downside_returns) > 0 else 1e-10
        return np.sqrt(periods_per_year) * np.mean(excess_returns) / downside_std

    @staticmethod
    def max_drawdown(equity_curve: np.ndarray) -> Tuple[float, int, int]:
        """
        Maximum Drawdown
        Returns: (max_drawdown_pct, start_idx, end_idx)
        """
        cummax = np.maximum.accumulate(equity_curve)
        drawdown = (equity_curve - cummax) / cummax

        max_dd = np.min(drawdown)
        end_idx = np.argmin(drawdown)

        # Find start of drawdown
        start_idx = np.argmax(equity_curve[:end_idx]) if end_idx > 0 else 0

        return abs(max_dd), start_idx, end_idx

    @staticmethod
    def calmar_ratio(
        equity_curve: np.ndarray,
        years: float
    ) -> float:
        """
        Calmar Ratio (return / max drawdown)
        """
        cagr = PerformanceMetrics.cagr(equity_curve, years)
        max_dd, _, _ = PerformanceMetrics.max_drawdown(equity_curve)
        return cagr / (max_dd + 1e-10)

    @staticmethod
    def win_rate(trades: pd.DataFrame) -> float:
        """Percentage of winning trades"""
        if len(trades) == 0:
            return 0.0
        return (trades['pnl'] > 0).mean()

    @staticmethod
    def profit_factor(trades: pd.DataFrame) -> float:
        """Ratio of gross profit to gross loss"""
        if len(trades) == 0:
            return 0.0

        gross_profit = trades[trades['pnl'] > 0]['pnl'].sum()
        gross_loss = abs(trades[trades['pnl'] < 0]['pnl'].sum())

        if gross_loss == 0:
            return float('inf') if gross_profit > 0 else 0.0

        return gross_profit / gross_loss

    @staticmethod
    def expectancy(trades: pd.DataFrame) -> float:
        """Average expected profit per trade"""
        if len(trades) == 0:
            return 0.0
        return trades['pnl'].mean()

    @staticmethod
    def generate_report(
        equity_curve: np.ndarray,
        trades: pd.DataFrame,
        initial_capital: float,
        years: float
    ) -> Dict:
        """Generate comprehensive performance report"""

        returns = PerformanceMetrics.calculate_returns(equity_curve)
        max_dd, dd_start, dd_end = PerformanceMetrics.max_drawdown(equity_curve)

        report = {
            # Return metrics
            'initial_capital': initial_capital,
            'final_capital': equity_curve[-1],
            'total_return_pct': ((equity_curve[-1] - initial_capital) / initial_capital) * 100,
            'cagr_pct': PerformanceMetrics.cagr(equity_curve, years) * 100,

            # Risk-adjusted metrics
            'sharpe_ratio': PerformanceMetrics.sharpe_ratio(returns),
            'sortino_ratio': PerformanceMetrics.sortino_ratio(returns),
            'calmar_ratio': PerformanceMetrics.calmar_ratio(equity_curve, years),

            # Drawdown metrics
            'max_drawdown_pct': max_dd * 100,
            'max_drawdown_start': dd_start,
            'max_drawdown_end': dd_end,

            # Trade metrics
            'num_trades': len(trades),
            'win_rate_pct': PerformanceMetrics.win_rate(trades) * 100,
            'profit_factor': PerformanceMetrics.profit_factor(trades),
            'expectancy': PerformanceMetrics.expectancy(trades),
            'avg_win': trades[trades['pnl'] > 0]['pnl'].mean() if len(trades[trades['pnl'] > 0]) > 0 else 0,
            'avg_loss': trades[trades['pnl'] < 0]['pnl'].mean() if len(trades[trades['pnl'] < 0]) > 0 else 0,
            'largest_win': trades['pnl'].max() if len(trades) > 0 else 0,
            'largest_loss': trades['pnl'].min() if len(trades) > 0 else 0,
        }

        return report

    @staticmethod
    def print_report(report: Dict):
        """Print formatted performance report"""
        print("\n" + "="*60)
        print("STRATEGY PERFORMANCE REPORT")
        print("="*60)

        print(f"\nCAPITAL:")
        print(f"  Initial Capital:      ${report['initial_capital']:,.2f}")
        print(f"  Final Capital:        ${report['final_capital']:,.2f}")
        print(f"  Total Return:         {report['total_return_pct']:.2f}%")
        print(f"  CAGR:                 {report['cagr_pct']:.2f}%")

        print(f"\nRISK-ADJUSTED METRICS:")
        print(f"  Sharpe Ratio:         {report['sharpe_ratio']:.2f}")
        print(f"  Sortino Ratio:        {report['sortino_ratio']:.2f}")
        print(f"  Calmar Ratio:         {report['calmar_ratio']:.2f}")

        print(f"\nDRAWDOWN:")
        print(f"  Maximum Drawdown:     {report['max_drawdown_pct']:.2f}%")

        print(f"\nTRADE STATISTICS:")
        print(f"  Number of Trades:     {report['num_trades']}")
        print(f"  Win Rate:             {report['win_rate_pct']:.2f}%")
        print(f"  Profit Factor:        {report['profit_factor']:.2f}")
        print(f"  Expectancy:           ${report['expectancy']:.2f}")
        print(f"  Average Win:          ${report['avg_win']:.2f}")
        print(f"  Average Loss:         ${report['avg_loss']:.2f}")
        print(f"  Largest Win:          ${report['largest_win']:.2f}")
        print(f"  Largest Loss:         ${report['largest_loss']:.2f}")

        print("\n" + "="*60)


# Usage example
def example_performance_metrics():
    """Example performance metrics calculation"""

    # Generate sample equity curve
    np.random.seed(42)
    returns = np.random.normal(0.001, 0.02, 252)
    equity_curve = (1 + returns).cumprod() * 100000

    # Generate sample trades
    trades = pd.DataFrame({
        'pnl': np.random.normal(100, 500, 50)
    })

    report = PerformanceMetrics.generate_report(
        equity_curve,
        trades,
        initial_capital=100000,
        years=1
    )

    PerformanceMetrics.print_report(report)


if __name__ == "__main__":
    example_performance_metrics()
