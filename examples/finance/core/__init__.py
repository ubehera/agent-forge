"""
Finance Core Library - Shared utilities for trading agents.

Provides standardized schemas, metrics, and utilities for quantitative
trading analysis. Designed for production use with type safety and validation.

Version: 1.0.0
"""

__version__ = "1.0.0"

# Export schemas
from .schemas import (
    MarketData,
    OptionsQuote,
    TradingSignal,
    Position,
    SignalSource,
    TradeAction,
    Timeframe,
)

# Export metrics
from .metrics import (
    sharpe_ratio,
    sortino_ratio,
    calmar_ratio,
    max_drawdown,
    value_at_risk,
    conditional_var,
    beta,
    win_rate,
    profit_factor,
    expectancy,
)

__all__ = [
    # Version
    "__version__",
    # Schemas
    "MarketData",
    "OptionsQuote",
    "TradingSignal",
    "Position",
    "SignalSource",
    "TradeAction",
    "Timeframe",
    # Metrics
    "sharpe_ratio",
    "sortino_ratio",
    "calmar_ratio",
    "max_drawdown",
    "value_at_risk",
    "conditional_var",
    "beta",
    "win_rate",
    "profit_factor",
    "expectancy",
]
