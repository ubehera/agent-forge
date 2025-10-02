"""
Production-ready technical indicators with efficient NumPy vectorization
Covers trend, momentum, volatility indicators for stocks and options
"""

import numpy as np
import pandas as pd
from typing import Union, Optional, Tuple
from dataclasses import dataclass
import warnings

warnings.filterwarnings('ignore')


@dataclass
class IndicatorConfig:
    """Configuration for technical indicators"""
    rsi_period: int = 14
    macd_fast: int = 12
    macd_slow: int = 26
    macd_signal: int = 9
    bb_period: int = 20
    bb_std: float = 2.0
    atr_period: int = 14


class TechnicalIndicators:
    """Efficient technical indicator calculations"""

    @staticmethod
    def sma(prices: np.ndarray, period: int) -> np.ndarray:
        """Simple Moving Average"""
        return pd.Series(prices).rolling(window=period).mean().values

    @staticmethod
    def ema(prices: np.ndarray, period: int) -> np.ndarray:
        """Exponential Moving Average"""
        return pd.Series(prices).ewm(span=period, adjust=False).mean().values

    @staticmethod
    def rsi(prices: np.ndarray, period: int = 14) -> np.ndarray:
        """
        Relative Strength Index
        Values: 0-100, oversold <30, overbought >70
        """
        deltas = np.diff(prices)
        gains = np.where(deltas > 0, deltas, 0)
        losses = np.where(deltas < 0, -deltas, 0)

        avg_gains = pd.Series(gains).rolling(window=period).mean().values
        avg_losses = pd.Series(losses).rolling(window=period).mean().values

        rs = avg_gains / (avg_losses + 1e-10)  # Avoid division by zero
        rsi = 100 - (100 / (1 + rs))

        # Prepend NaN for first value
        return np.insert(rsi, 0, np.nan)

    @staticmethod
    def macd(
        prices: np.ndarray,
        fast: int = 12,
        slow: int = 26,
        signal: int = 9
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Moving Average Convergence Divergence
        Returns: (macd_line, signal_line, histogram)
        """
        ema_fast = TechnicalIndicators.ema(prices, fast)
        ema_slow = TechnicalIndicators.ema(prices, slow)

        macd_line = ema_fast - ema_slow
        signal_line = TechnicalIndicators.ema(macd_line, signal)
        histogram = macd_line - signal_line

        return macd_line, signal_line, histogram

    @staticmethod
    def bollinger_bands(
        prices: np.ndarray,
        period: int = 20,
        std_dev: float = 2.0
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Bollinger Bands
        Returns: (upper_band, middle_band, lower_band)
        """
        middle_band = TechnicalIndicators.sma(prices, period)
        std = pd.Series(prices).rolling(window=period).std().values

        upper_band = middle_band + (std_dev * std)
        lower_band = middle_band - (std_dev * std)

        return upper_band, middle_band, lower_band

    @staticmethod
    def atr(
        high: np.ndarray,
        low: np.ndarray,
        close: np.ndarray,
        period: int = 14
    ) -> np.ndarray:
        """Average True Range - volatility indicator"""

        # True Range calculation
        tr1 = high - low
        tr2 = np.abs(high - np.roll(close, 1))
        tr3 = np.abs(low - np.roll(close, 1))

        tr = np.maximum(tr1, np.maximum(tr2, tr3))
        tr[0] = tr1[0]  # First value

        # ATR is EMA of True Range
        atr = pd.Series(tr).ewm(span=period, adjust=False).mean().values

        return atr

    @staticmethod
    def adx(
        high: np.ndarray,
        low: np.ndarray,
        close: np.ndarray,
        period: int = 14
    ) -> np.ndarray:
        """
        Average Directional Index - trend strength
        Values: 0-100, strong trend >25, very strong >50
        """

        # Calculate +DM and -DM
        up_move = high - np.roll(high, 1)
        down_move = np.roll(low, 1) - low

        plus_dm = np.where((up_move > down_move) & (up_move > 0), up_move, 0)
        minus_dm = np.where((down_move > up_move) & (down_move > 0), down_move, 0)

        # Smooth DMs
        plus_di = 100 * pd.Series(plus_dm).ewm(span=period, adjust=False).mean().values
        minus_di = 100 * pd.Series(minus_dm).ewm(span=period, adjust=False).mean().values

        # Calculate DX
        dx = 100 * np.abs(plus_di - minus_di) / (plus_di + minus_di + 1e-10)

        # ADX is smoothed DX
        adx = pd.Series(dx).ewm(span=period, adjust=False).mean().values

        return adx

    @staticmethod
    def stochastic(
        high: np.ndarray,
        low: np.ndarray,
        close: np.ndarray,
        k_period: int = 14,
        d_period: int = 3
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        Stochastic Oscillator
        Returns: (%K, %D)
        """

        # %K calculation
        lowest_low = pd.Series(low).rolling(window=k_period).min().values
        highest_high = pd.Series(high).rolling(window=k_period).max().values

        k = 100 * (close - lowest_low) / (highest_high - lowest_low + 1e-10)

        # %D is SMA of %K
        d = pd.Series(k).rolling(window=d_period).mean().values

        return k, d


# Usage Examples
def example_technical_analysis():
    """Example: Calculate technical indicators on stock data"""

    # Sample price data
    prices = np.random.randn(100).cumsum() + 100
    high = prices + np.random.rand(100) * 2
    low = prices - np.random.rand(100) * 2

    # Calculate indicators
    rsi = TechnicalIndicators.rsi(prices, period=14)
    macd_line, signal, hist = TechnicalIndicators.macd(prices)
    upper, middle, lower = TechnicalIndicators.bollinger_bands(prices)
    atr = TechnicalIndicators.atr(high, low, prices)

    print(f"RSI: {rsi[-1]:.2f}")
    print(f"MACD: {macd_line[-1]:.4f}, Signal: {signal[-1]:.4f}")
    print(f"BB Upper: {upper[-1]:.2f}, Lower: {lower[-1]:.2f}")
    print(f"ATR: {atr[-1]:.2f}")


if __name__ == "__main__":
    print("=== Technical Analysis ===")
    example_technical_analysis()
