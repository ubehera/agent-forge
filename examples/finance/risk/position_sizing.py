"""
Production-ready position sizing implementations
Kelly Criterion, Fixed Fractional, Volatility-Based, Risk Parity
"""

import numpy as np
import pandas as pd
from typing import Optional
from dataclasses import dataclass


@dataclass
class RiskConfig:
    """Risk management configuration"""
    max_position_size: float = 0.10  # 10% max per position
    max_portfolio_risk: float = 0.02  # 2% max portfolio risk per trade
    max_leverage: float = 1.0  # No leverage by default
    max_correlation: float = 0.7  # Max correlation between positions
    max_sector_exposure: float = 0.30  # 30% max per sector
    stop_trading_drawdown: float = 0.20  # Stop if 20% drawdown


class PositionSizing:
    """Position sizing algorithms for trade execution"""

    @staticmethod
    def kelly_criterion(
        win_probability: float,
        win_loss_ratio: float,
        max_kelly_fraction: float = 0.25
    ) -> float:
        """
        Kelly Criterion position sizing

        Args:
            win_probability: Probability of winning trade (0-1)
            win_loss_ratio: Average win / average loss
            max_kelly_fraction: Maximum Kelly fraction (for safety)

        Returns:
            Position size as fraction of capital
        """

        if win_probability <= 0 or win_probability >= 1:
            return 0.0

        if win_loss_ratio <= 0:
            return 0.0

        # Kelly formula: f = (p * b - q) / b
        # where p = win probability, q = loss probability, b = win/loss ratio
        q = 1 - win_probability
        kelly_fraction = (win_probability * win_loss_ratio - q) / win_loss_ratio

        # Apply safety factor
        kelly_fraction = max(0, min(kelly_fraction, max_kelly_fraction))

        return kelly_fraction

    @staticmethod
    def fixed_fractional(
        account_value: float,
        risk_per_trade: float,
        entry_price: float,
        stop_loss_price: float
    ) -> int:
        """
        Fixed fractional position sizing
        Risk fixed percentage of capital per trade

        Args:
            account_value: Current account value
            risk_per_trade: Risk as fraction of account (e.g., 0.01 = 1%)
            entry_price: Entry price per share
            stop_loss_price: Stop loss price per share

        Returns:
            Number of shares to buy
        """

        if entry_price <= stop_loss_price:
            return 0

        # Risk per share
        risk_per_share = abs(entry_price - stop_loss_price)

        # Total dollar risk
        dollar_risk = account_value * risk_per_trade

        # Position size
        shares = int(dollar_risk / risk_per_share)

        # Ensure position doesn't exceed account value
        max_shares = int(account_value / entry_price)
        shares = min(shares, max_shares)

        return max(0, shares)

    @staticmethod
    def volatility_based(
        account_value: float,
        target_risk: float,
        price: float,
        volatility: float,  # Annualized volatility
        holding_period_days: int = 1
    ) -> int:
        """
        Volatility-based position sizing
        Inverse volatility weighting - larger positions for less volatile assets

        Args:
            account_value: Current account value
            target_risk: Target portfolio risk (e.g., 0.02 = 2%)
            price: Current price per share
            volatility: Annualized volatility (e.g., 0.25 = 25%)
            holding_period_days: Expected holding period

        Returns:
            Number of shares to buy
        """

        if volatility <= 0:
            return 0

        # Adjust volatility for holding period
        holding_period_volatility = volatility * np.sqrt(holding_period_days / 252)

        # Position size to achieve target risk
        position_value = (account_value * target_risk) / holding_period_volatility

        shares = int(position_value / price)

        # Ensure position doesn't exceed account value
        max_shares = int(account_value / price)
        shares = min(shares, max_shares)

        return max(0, shares)

    @staticmethod
    def risk_parity_sizing(
        account_value: float,
        prices: np.ndarray,
        volatilities: np.ndarray,
        target_risk: float = 0.10
    ) -> np.ndarray:
        """
        Risk parity position sizing across multiple assets
        Each position contributes equal risk to portfolio

        Args:
            account_value: Current account value
            prices: Array of asset prices
            volatilities: Array of annualized volatilities
            target_risk: Target portfolio risk

        Returns:
            Array of position sizes (shares) for each asset
        """

        if len(prices) != len(volatilities):
            raise ValueError("Prices and volatilities must have same length")

        # Inverse volatility weights
        inv_vol = 1.0 / (volatilities + 1e-10)
        weights = inv_vol / np.sum(inv_vol)

        # Allocate capital
        position_values = account_value * weights * target_risk

        # Convert to shares
        shares = (position_values / prices).astype(int)

        return shares


# Usage Examples
def example_position_sizing():
    """Example: Calculate position sizes"""

    account_value = 100000

    # Kelly Criterion
    kelly_size = PositionSizing.kelly_criterion(
        win_probability=0.55,
        win_loss_ratio=2.0,  # Wins are 2x losses
        max_kelly_fraction=0.25
    )
    print(f"Kelly Criterion: {kelly_size:.2%} of capital")

    # Fixed Fractional
    shares = PositionSizing.fixed_fractional(
        account_value=account_value,
        risk_per_trade=0.01,  # Risk 1% per trade
        entry_price=100,
        stop_loss_price=95
    )
    print(f"Fixed Fractional: {shares} shares")

    # Volatility-Based
    shares = PositionSizing.volatility_based(
        account_value=account_value,
        target_risk=0.02,
        price=100,
        volatility=0.25,  # 25% annual volatility
        holding_period_days=5
    )
    print(f"Volatility-Based: {shares} shares")

    # Risk Parity
    prices = np.array([100, 200, 50])
    volatilities = np.array([0.25, 0.30, 0.20])
    shares = PositionSizing.risk_parity_sizing(
        account_value=account_value,
        prices=prices,
        volatilities=volatilities,
        target_risk=0.10
    )
    print(f"Risk Parity: {shares}")


if __name__ == "__main__":
    example_position_sizing()
