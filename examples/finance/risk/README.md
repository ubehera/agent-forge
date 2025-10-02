# Trading Risk Management Examples

Production-ready code examples for risk management and portfolio optimization.

## Files

### position_sizing.py (219 lines)
**Purpose**: Position sizing algorithms for capital allocation

**Features**:
- Kelly Criterion with safety factor
- Fixed fractional position sizing
- Volatility-based sizing (inverse volatility)
- Risk parity across multiple assets

**Usage**:
```python
from position_sizing import PositionSizing

# Kelly Criterion
kelly_size = PositionSizing.kelly_criterion(
    win_probability=0.55,
    win_loss_ratio=2.0,
    max_kelly_fraction=0.25
)

# Fixed fractional
shares = PositionSizing.fixed_fractional(
    account_value=100000,
    risk_per_trade=0.01,
    entry_price=100,
    stop_loss_price=95
)

# Risk parity
shares = PositionSizing.risk_parity_sizing(
    account_value=100000,
    prices=np.array([100, 200, 50]),
    volatilities=np.array([0.25, 0.30, 0.20])
)
```

### portfolio_optimizer.py (180 lines)
**Purpose**: Portfolio optimization using Modern Portfolio Theory

**Features**:
- Mean-variance optimization (Markowitz)
- Minimum variance portfolio
- Efficient frontier calculation
- Sharpe ratio maximization

**Usage**:
```python
from portfolio_optimizer import PortfolioOptimizer

optimizer = PortfolioOptimizer(returns_df)

# Maximum Sharpe portfolio
result = optimizer.mean_variance_optimization()
print(f"Sharpe: {result['sharpe_ratio']:.2f}")
print(f"Weights: {result['weights']}")

# Minimum variance
result = optimizer.minimum_variance_portfolio()

# Efficient frontier
frontier = optimizer.efficient_frontier(num_portfolios=100)
```

## Additional Examples

The main agent file contains additional examples:
- **Risk Metrics** (lines 388-505): VaR, CVaR, beta, drawdown calculations
- **Real-Time Monitor** (lines 507-683): Live risk limit enforcement

## Dependencies

```bash
pip install numpy pandas scipy
```

## Risk Limits

Default configuration:
- Max position size: 10% of portfolio
- Max sector exposure: 30%
- Stop trading drawdown: 20%
- Max correlation: 0.7 between positions

## Quality Standards

- **Capital Preservation**: Max drawdown <20% in live trading
- **Risk-Adjusted Returns**: Sharpe ratio >1.5 with limits enforced
- **Limit Adherence**: 100% compliance with position/sector limits
- **Calculation Speed**: <100ms for risk metric updates

## Integration

These examples are designed to work with:
- **quantitative-analyst**: Correlation matrices, volatility estimates
- **trading-strategy-architect**: Strategy risk validation
- **algorithmic-trading-engineer**: Pre-trade risk checks
- **trading-compliance-officer**: Regulatory compliance
