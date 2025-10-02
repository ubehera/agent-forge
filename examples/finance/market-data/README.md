# Market Data Examples

Production-ready code examples for market data engineering.

## Files

### data_quality_monitor.py (356 lines)
**Purpose**: Comprehensive data quality monitoring for market data pipelines

**Features**:
- Missing bar detection with gap analysis
- Stale data monitoring
- Price outlier detection using z-scores
- Volume anomaly detection
- Multi-symbol quality checks
- Automated quality reports

**Usage**:
```python
from data_quality_monitor import DataQualityMonitor

# Initialize monitor
monitor = DataQualityMonitor("postgresql://user:pass@localhost/market_data")

# Run quality checks
watchlist = ["AAPL", "TSLA", "NVDA"]
issues = monitor.run_full_quality_check(watchlist)

# Generate report
report = monitor.generate_quality_report(issues)
print(report)
```

### multi_broker_pipeline.py (414 lines)
**Location**: Already extracted to this directory

**Purpose**: Multi-broker market data pipeline with abstraction layer

**Features**:
- Broker abstraction (Alpaca, E*TRADE, Fidelity)
- REST API and WebSocket support
- Options chain data retrieval
- Factory pattern for provider creation

## Dependencies

```bash
pip install pandas numpy sqlalchemy psycopg2-binary
```

## TimescaleDB Schema

See the main agent file for complete TimescaleDB schema including:
- `stock_bars` hypertable with compression
- `options_chain` table
- `corporate_actions` tracking
- Continuous aggregates for common queries

## Integration

These examples are designed to work with:
- **quantitative-analyst**: Provides clean data for indicator calculations
- **trading-strategy-architect**: Supplies validated data for backtesting
- **database-architect**: Optimizes TimescaleDB schema and queries
