# Trading Strategy Examples

Production-ready code examples for strategy backtesting and validation.

## Files

### walk_forward.py (141 lines)
**Purpose**: Walk-forward analysis for strategy validation

**Features**:
- Rolling train/test window splitting
- Parameter optimization on in-sample data
- Out-of-sample testing
- Aggregated performance metrics
- Overfitting detection

**Usage**:
```python
from walk_forward import WalkForwardAnalysis

wfa = WalkForwardAnalysis(
    train_period_days=365,
    test_period_days=90,
    step_days=90
)

results = wfa.run_walk_forward(
    df=data,
    strategy=strategy_instance,
    optimize_func=optimize_parameters,
    backtest_func=run_backtest
)

print(f"Win Rate: {results['win_rate']:.2%}")
print(f"Average Sharpe: {results['avg_sharpe']:.2f}")
```

### performance_metrics.py (201 lines)
**Purpose**: Comprehensive performance metrics calculation

**Features**:
- Return metrics: CAGR, total return
- Risk-adjusted: Sharpe, Sortino, Calmar ratios
- Drawdown analysis
- Trade statistics: win rate, profit factor, expectancy

**Usage**:
```python
from performance_metrics import PerformanceMetrics

report = PerformanceMetrics.generate_report(
    equity_curve=portfolio_values,
    trades=trade_df,
    initial_capital=100000,
    years=1
)

PerformanceMetrics.print_report(report)
```

## Additional Examples

The main agent files contain additional examples:
- **Vectorbt Strategy** (lines 48-255): Ultra-fast parameter optimization
- **Backtrader Strategy** (lines 259-447): Event-driven backtesting with complex orders

## Dependencies

```bash
pip install numpy pandas scipy
pip install vectorbt backtrader  # Optional frameworks
```

## Quality Standards

- **Strategy Robustness**: >60% positive windows in walk-forward
- **Risk-Adjusted Return**: Sharpe ratio >1.5
- **Drawdown Control**: Maximum drawdown <20%
- **Trade Frequency**: >50 trades for statistical significance

## Integration

These examples are designed to work with:
- **quantitative-analyst**: Receives indicators and signals
- **trading-risk-manager**: Validates risk metrics
- **test-engineer**: Unit tests for strategy logic
- **algorithmic-trading-engineer**: Production deployment
