"""
Canonical data schemas for finance trading agents.

Provides standardized dataclasses for market data, trading signals, positions,
and options. Ensures type safety and consistency across all agents.
"""

from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Optional, Dict, Any


class SignalSource(Enum):
    """Source type for trading signals."""
    TECHNICAL = "TECHNICAL"
    FUNDAMENTAL = "FUNDAMENTAL"
    ML = "ML"
    SENTIMENT = "SENTIMENT"
    HYBRID = "HYBRID"


class TradeAction(Enum):
    """Trading action types."""
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"
    SHORT = "SHORT"
    COVER = "COVER"


class Timeframe(Enum):
    """Standard market data timeframes."""
    ONE_MIN = "1m"
    FIVE_MIN = "5m"
    FIFTEEN_MIN = "15m"
    THIRTY_MIN = "30m"
    ONE_HOUR = "1h"
    FOUR_HOUR = "4h"
    ONE_DAY = "1d"
    ONE_WEEK = "1w"
    ONE_MONTH = "1M"


@dataclass(frozen=True)
class MarketData:
    """
    Standardized OHLCV market data with metadata.

    Immutable dataclass for market data to prevent accidental modification.
    Use Decimal for prices to avoid floating-point precision issues.
    """
    symbol: str
    timestamp: datetime
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: int
    provider: str  # e.g., "yahoo_finance", "alpaca", "polygon"
    timeframe: Timeframe

    def __post_init__(self):
        """Validate market data invariants."""
        if self.high < self.low:
            raise ValueError(f"High ({self.high}) cannot be less than low ({self.low})")

        if self.open < 0 or self.close < 0:
            raise ValueError("Prices cannot be negative")

        if self.volume < 0:
            raise ValueError("Volume cannot be negative")

    @property
    def typical_price(self) -> Decimal:
        """Calculate typical price (HLC/3)."""
        return (self.high + self.low + self.close) / Decimal("3")

    @property
    def price_range(self) -> Decimal:
        """Calculate price range (high - low)."""
        return self.high - self.low


@dataclass(frozen=True)
class OptionsQuote:
    """
    Options contract quote with Greeks.

    Greeks are optional as they may not be available from all providers.
    Use Decimal for prices/strikes, float for Greeks (industry standard).
    """
    symbol: str
    underlying: str
    strike: Decimal
    expiration: datetime
    option_type: str  # "CALL" or "PUT"
    bid: Decimal
    ask: Decimal
    last: Decimal
    volume: int
    open_interest: int
    implied_volatility: Optional[float] = None
    delta: Optional[float] = None
    gamma: Optional[float] = None
    theta: Optional[float] = None
    vega: Optional[float] = None
    rho: Optional[float] = None
    timestamp: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        """Validate options quote invariants."""
        if self.option_type not in ["CALL", "PUT"]:
            raise ValueError("option_type must be 'CALL' or 'PUT'")

        if self.bid > self.ask:
            raise ValueError(f"Bid ({self.bid}) cannot exceed ask ({self.ask})")

        if self.strike <= 0:
            raise ValueError("Strike price must be positive")

        if self.expiration <= datetime.now():
            raise ValueError("Expiration must be in the future")

    @property
    def mid_price(self) -> Decimal:
        """Calculate mid-point price."""
        return (self.bid + self.ask) / Decimal("2")

    @property
    def spread(self) -> Decimal:
        """Calculate bid-ask spread."""
        return self.ask - self.bid

    @property
    def spread_percent(self) -> float:
        """Calculate spread as percentage of mid price."""
        mid = self.mid_price
        if mid == 0:
            return 0.0
        return float((self.spread / mid) * 100)


@dataclass
class TradingSignal:
    """
    Canonical trading signal schema.

    Mutable dataclass to allow agents to enrich signals with additional metadata.
    Confidence score helps with position sizing and risk management.
    """
    symbol: str
    action: TradeAction
    confidence: float  # 0.0 to 1.0
    timestamp: datetime
    source: SignalSource
    metadata: Dict[str, Any] = field(default_factory=dict)

    # Optional fields for execution
    target_price: Optional[Decimal] = None
    stop_loss: Optional[Decimal] = None
    take_profit: Optional[Decimal] = None
    position_size: Optional[int] = None

    def __post_init__(self):
        """Validate signal invariants."""
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("Confidence must be between 0.0 and 1.0")

        if self.target_price is not None and self.target_price <= 0:
            raise ValueError("Target price must be positive")

        if self.stop_loss is not None and self.stop_loss <= 0:
            raise ValueError("Stop loss must be positive")

        if self.take_profit is not None and self.take_profit <= 0:
            raise ValueError("Take profit must be positive")

        if self.position_size is not None and self.position_size <= 0:
            raise ValueError("Position size must be positive")

    def to_dict(self) -> Dict[str, Any]:
        """Convert signal to dictionary for serialization."""
        return {
            "symbol": self.symbol,
            "action": self.action.value,
            "confidence": self.confidence,
            "timestamp": self.timestamp.isoformat(),
            "source": self.source.value,
            "target_price": str(self.target_price) if self.target_price else None,
            "stop_loss": str(self.stop_loss) if self.stop_loss else None,
            "take_profit": str(self.take_profit) if self.take_profit else None,
            "position_size": self.position_size,
            "metadata": self.metadata
        }


@dataclass
class Position:
    """
    Current trading position with P&L tracking.

    Mutable dataclass as positions are updated with market price changes.
    Supports both long and short positions (quantity can be negative).
    """
    symbol: str
    quantity: int  # Positive for long, negative for short
    entry_price: Decimal
    current_price: Decimal
    timestamp: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        """Validate position invariants."""
        if self.quantity == 0:
            raise ValueError("Position quantity cannot be zero")

        if self.entry_price <= 0:
            raise ValueError("Entry price must be positive")

        if self.current_price <= 0:
            raise ValueError("Current price must be positive")

    @property
    def unrealized_pnl(self) -> Decimal:
        """Calculate unrealized profit/loss."""
        if self.quantity > 0:  # Long position
            return (self.current_price - self.entry_price) * Decimal(abs(self.quantity))
        else:  # Short position
            return (self.entry_price - self.current_price) * Decimal(abs(self.quantity))

    @property
    def unrealized_pnl_percent(self) -> float:
        """Calculate unrealized P&L as percentage of entry value."""
        entry_value = self.entry_price * Decimal(abs(self.quantity))
        if entry_value == 0:
            return 0.0
        return float((self.unrealized_pnl / entry_value) * 100)

    @property
    def market_value(self) -> Decimal:
        """Calculate current market value of position."""
        return self.current_price * Decimal(abs(self.quantity))

    @property
    def is_long(self) -> bool:
        """Check if position is long."""
        return self.quantity > 0

    @property
    def is_short(self) -> bool:
        """Check if position is short."""
        return self.quantity < 0

    def update_price(self, new_price: Decimal) -> None:
        """Update current price and timestamp."""
        if new_price <= 0:
            raise ValueError("Price must be positive")
        self.current_price = new_price
        self.timestamp = datetime.now()


# Unit test stubs (implement with pytest)
"""
Tests to implement:

test_market_data_validation():
    - Test high < low raises ValueError
    - Test negative prices raise ValueError
    - Test negative volume raises ValueError
    - Test typical_price calculation

test_options_quote_validation():
    - Test invalid option_type raises ValueError
    - Test bid > ask raises ValueError
    - Test expired contract raises ValueError
    - Test mid_price and spread calculations

test_trading_signal_validation():
    - Test confidence out of range raises ValueError
    - Test negative prices raise ValueError
    - Test to_dict serialization
    - Test all TradeAction and SignalSource enums

test_position_pnl():
    - Test long position P&L calculation
    - Test short position P&L calculation
    - Test P&L percentage calculation
    - Test market value calculation
    - Test update_price updates timestamp

test_position_validation():
    - Test zero quantity raises ValueError
    - Test negative prices raise ValueError
    - Test is_long and is_short properties

test_enum_values():
    - Test all Timeframe values
    - Test all TradeAction values
    - Test all SignalSource values
"""
