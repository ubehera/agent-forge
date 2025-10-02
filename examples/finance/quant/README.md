# Quantitative Analysis Examples

Production-ready code examples for quantitative analysis and technical indicators.

## Files

### indicators.py (178 lines)
**Purpose**: Efficient vectorized technical indicators

**Features**:
- Trend indicators: SMA, EMA
- Momentum: RSI, MACD, Stochastic
- Volatility: Bollinger Bands, ATR, ADX
- NumPy/pandas vectorization for speed

**Usage**:
```python
from indicators import TechnicalIndicators

# Calculate RSI
rsi = TechnicalIndicators.rsi(prices, period=14)

# MACD
macd_line, signal, hist = TechnicalIndicators.macd(prices)

# Bollinger Bands
upper, middle, lower = TechnicalIndicators.bollinger_bands(prices)
```

### greeks.py (161 lines)
**Purpose**: Options pricing and Greeks calculations

**Features**:
- Black-Scholes pricing for calls/puts
- Greeks: delta, gamma, theta, vega, rho
- Implied volatility calculation (Newton-Raphson)

**Usage**:
```python
from greeks import OptionsAnalysis

# Calculate Greeks
greeks = OptionsAnalysis.calculate_greeks(
    S=100, K=105, T=0.25, r=0.05, sigma=0.25, option_type='call'
)

# Implied volatility
iv = OptionsAnalysis.implied_volatility(
    market_price=3.50, S=100, K=105, T=0.25, r=0.05
)
```

### statistics.py (199 lines)
**Purpose**: Statistical analysis and feature engineering

**Features**:
- Stationarity tests (ADF)
- Cointegration testing (pairs trading)
- Beta calculation, correlation matrices
- Feature engineering: lags, rolling stats, momentum, volatility

**Usage**:
```python
from statistics import StatisticalAnalysis, FeatureEngineering

# Cointegration test
result = StatisticalAnalysis.cointegration_test(series1, series2)

# Feature engineering
momentum_features = FeatureEngineering.create_momentum_features(prices)
vol_features = FeatureEngineering.create_volatility_features(high, low, close)
```

## Dependencies

```bash
pip install numpy pandas scipy statsmodels
pip install TA-Lib  # Optional for validation
```

## Performance

All indicators are vectorized using NumPy/pandas for optimal performance:
- >10,000 bars/second processing
- Validated against TA-Lib benchmarks
- Full type hints for Python 3.11+

## Integration

These examples are designed to work with:
- **trading-strategy-architect**: Provides signals for backtesting
- **market-data-engineer**: Consumes validated market data
- **python-expert**: Code optimization and performance tuning
