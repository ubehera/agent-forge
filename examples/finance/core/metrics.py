"""
Performance and risk metrics for quantitative trading analysis.

Provides standard financial metrics for evaluating trading strategies,
including risk-adjusted returns, drawdown analysis, and risk measures.
"""

from decimal import Decimal
from typing import Sequence
import numpy as np
from scipy import stats


def sharpe_ratio(
    returns: Sequence[float],
    risk_free_rate: float = 0.0,
    periods_per_year: int = 252
) -> float:
    """
    Calculate Sharpe ratio - risk-adjusted return metric.

    **When to use**: Evaluating strategies with normally distributed returns.
    Best for comparing multiple strategies on risk-adjusted basis.

    Args:
        returns: Array of period returns (e.g., daily returns)
        risk_free_rate: Annualized risk-free rate (default: 0.0)
        periods_per_year: Trading periods per year (252 for daily, 12 for monthly)

    Returns:
        Annualized Sharpe ratio. Values > 1.0 are good, > 2.0 are excellent.

    Raises:
        ValueError: If returns array is empty or has zero standard deviation

    Example:
        >>> daily_returns = [0.01, -0.005, 0.02, -0.01]
        >>> sharpe_ratio(daily_returns, risk_free_rate=0.02, periods_per_year=252)
        1.23
    """
    if not returns or len(returns) == 0:
        raise ValueError("Returns array cannot be empty")

    returns_array = np.array(returns, dtype=float)
    excess_returns = returns_array - (risk_free_rate / periods_per_year)

    if np.std(excess_returns, ddof=1) == 0:
        raise ValueError("Standard deviation of returns is zero")

    return float(np.mean(excess_returns) / np.std(excess_returns, ddof=1) * np.sqrt(periods_per_year))


def sortino_ratio(
    returns: Sequence[float],
    risk_free_rate: float = 0.0,
    periods_per_year: int = 252
) -> float:
    """
    Calculate Sortino ratio - downside risk-adjusted return.

    **When to use**: Prefer over Sharpe when upside volatility is acceptable
    and you only want to penalize downside risk. Better for asymmetric returns.

    Args:
        returns: Array of period returns
        risk_free_rate: Annualized risk-free rate
        periods_per_year: Trading periods per year

    Returns:
        Annualized Sortino ratio. Higher is better.

    Raises:
        ValueError: If returns array is empty or has no downside deviation
    """
    if not returns or len(returns) == 0:
        raise ValueError("Returns array cannot be empty")

    returns_array = np.array(returns, dtype=float)
    excess_returns = returns_array - (risk_free_rate / periods_per_year)

    # Calculate downside deviation (only negative returns)
    downside_returns = excess_returns[excess_returns < 0]
    if len(downside_returns) == 0:
        raise ValueError("No negative returns - cannot calculate downside deviation")

    downside_deviation = np.sqrt(np.mean(downside_returns ** 2))

    if downside_deviation == 0:
        raise ValueError("Downside deviation is zero")

    return float(np.mean(excess_returns) / downside_deviation * np.sqrt(periods_per_year))


def calmar_ratio(
    returns: Sequence[float],
    periods_per_year: int = 252
) -> float:
    """
    Calculate Calmar ratio - return to maximum drawdown ratio.

    **When to use**: Evaluating strategies where drawdown tolerance is critical.
    Popular in hedge fund evaluation. Values > 0.5 are good, > 1.0 excellent.

    Args:
        returns: Array of period returns
        periods_per_year: Trading periods per year

    Returns:
        Annualized Calmar ratio

    Raises:
        ValueError: If returns array is empty or max drawdown is zero
    """
    if not returns or len(returns) == 0:
        raise ValueError("Returns array cannot be empty")

    returns_array = np.array(returns, dtype=float)
    annualized_return = float(np.mean(returns_array) * periods_per_year)

    max_dd = max_drawdown(returns_array)
    if max_dd == 0:
        raise ValueError("Maximum drawdown is zero")

    return annualized_return / abs(max_dd)


def max_drawdown(returns: Sequence[float]) -> float:
    """
    Calculate maximum drawdown - largest peak-to-trough decline.

    **When to use**: Understanding worst-case loss scenario. Critical for
    risk management and position sizing.

    Args:
        returns: Array of period returns

    Returns:
        Maximum drawdown as negative decimal (e.g., -0.25 for 25% drawdown)

    Raises:
        ValueError: If returns array is empty
    """
    if not returns or len(returns) == 0:
        raise ValueError("Returns array cannot be empty")

    returns_array = np.array(returns, dtype=float)
    cumulative = np.cumprod(1 + returns_array)
    running_max = np.maximum.accumulate(cumulative)
    drawdown = (cumulative - running_max) / running_max

    return float(np.min(drawdown))


def value_at_risk(
    returns: Sequence[float],
    confidence_level: float = 0.95,
    method: str = "historical"
) -> float:
    """
    Calculate Value at Risk (VaR) - potential loss at given confidence level.

    **When to use**: Regulatory reporting, position sizing, risk limits.
    VaR answers "What's the maximum loss at X% confidence?"

    Args:
        returns: Array of period returns
        confidence_level: Confidence level (0.90, 0.95, 0.99 typical)
        method: "historical" (percentile) or "parametric" (assumes normal)

    Returns:
        VaR as positive decimal (e.g., 0.05 means 5% potential loss)

    Raises:
        ValueError: If invalid confidence level or method
    """
    if not 0 < confidence_level < 1:
        raise ValueError("Confidence level must be between 0 and 1")

    if method not in ["historical", "parametric"]:
        raise ValueError("Method must be 'historical' or 'parametric'")

    returns_array = np.array(returns, dtype=float)

    if method == "historical":
        return float(-np.percentile(returns_array, (1 - confidence_level) * 100))
    else:  # parametric
        mean = np.mean(returns_array)
        std = np.std(returns_array, ddof=1)
        z_score = stats.norm.ppf(1 - confidence_level)
        return float(-(mean + z_score * std))


def conditional_var(
    returns: Sequence[float],
    confidence_level: float = 0.95
) -> float:
    """
    Calculate Conditional VaR (CVaR/Expected Shortfall) - expected loss beyond VaR.

    **When to use**: More conservative than VaR, captures tail risk better.
    Preferred by risk managers for extreme event planning.

    Args:
        returns: Array of period returns
        confidence_level: Confidence level (0.90, 0.95, 0.99 typical)

    Returns:
        CVaR as positive decimal

    Raises:
        ValueError: If invalid confidence level or insufficient tail observations
    """
    if not 0 < confidence_level < 1:
        raise ValueError("Confidence level must be between 0 and 1")

    returns_array = np.array(returns, dtype=float)
    var_threshold = -value_at_risk(returns_array, confidence_level, method="historical")

    # Average of returns worse than VaR threshold
    tail_losses = returns_array[returns_array <= var_threshold]

    if len(tail_losses) == 0:
        raise ValueError("No observations in tail - increase sample size or reduce confidence level")

    return float(-np.mean(tail_losses))


def beta(
    asset_returns: Sequence[float],
    market_returns: Sequence[float]
) -> float:
    """
    Calculate beta - sensitivity of asset returns to market returns.

    **When to use**: Portfolio construction, CAPM analysis, hedging decisions.
    Beta = 1.0 means moves with market, < 1.0 less volatile, > 1.0 more volatile.

    Args:
        asset_returns: Asset period returns
        market_returns: Market/benchmark period returns (must match length)

    Returns:
        Beta coefficient

    Raises:
        ValueError: If arrays have different lengths or market variance is zero
    """
    if len(asset_returns) != len(market_returns):
        raise ValueError("Asset and market returns must have same length")

    asset_array = np.array(asset_returns, dtype=float)
    market_array = np.array(market_returns, dtype=float)

    covariance = np.cov(asset_array, market_array)[0, 1]
    market_variance = np.var(market_array, ddof=1)

    if market_variance == 0:
        raise ValueError("Market variance is zero")

    return float(covariance / market_variance)


def win_rate(trades: Sequence[float]) -> float:
    """
    Calculate win rate - percentage of profitable trades.

    **When to use**: Quick strategy assessment. Note: high win rate doesn't
    guarantee profitability (need to consider profit factor and expectancy).

    Args:
        trades: Array of trade P&L values

    Returns:
        Win rate as decimal (0.60 = 60% win rate)

    Raises:
        ValueError: If trades array is empty
    """
    if not trades or len(trades) == 0:
        raise ValueError("Trades array cannot be empty")

    trades_array = np.array(trades, dtype=float)
    winning_trades = np.sum(trades_array > 0)

    return float(winning_trades / len(trades_array))


def profit_factor(trades: Sequence[float]) -> float:
    """
    Calculate profit factor - ratio of gross profit to gross loss.

    **When to use**: Evaluating strategy robustness. Values > 1.5 are good,
    > 2.0 excellent. Combines win rate and average win/loss magnitude.

    Args:
        trades: Array of trade P&L values

    Returns:
        Profit factor (e.g., 2.0 means gross profit is 2x gross loss)

    Raises:
        ValueError: If trades array is empty or has no losing trades
    """
    if not trades or len(trades) == 0:
        raise ValueError("Trades array cannot be empty")

    trades_array = np.array(trades, dtype=float)
    gross_profit = np.sum(trades_array[trades_array > 0])
    gross_loss = np.abs(np.sum(trades_array[trades_array < 0]))

    if gross_loss == 0:
        raise ValueError("No losing trades - cannot calculate profit factor")

    return float(gross_profit / gross_loss)


def expectancy(trades: Sequence[float]) -> float:
    """
    Calculate expectancy - average expected profit per trade.

    **When to use**: Position sizing decisions (Kelly criterion), strategy
    comparison. Positive expectancy is required for long-term profitability.

    Args:
        trades: Array of trade P&L values

    Returns:
        Average expected profit per trade

    Raises:
        ValueError: If trades array is empty
    """
    if not trades or len(trades) == 0:
        raise ValueError("Trades array cannot be empty")

    trades_array = np.array(trades, dtype=float)
    return float(np.mean(trades_array))


# Unit test stubs (implement with pytest)
"""
Tests to implement:

test_sharpe_ratio():
    - Test with known return sequence
    - Test with zero volatility (should raise)
    - Test with empty array (should raise)
    - Test annualization factor

test_sortino_ratio():
    - Test with asymmetric returns
    - Test with no negative returns (should raise)
    - Compare to Sharpe on same data

test_max_drawdown():
    - Test with monotonically increasing equity (should be ~0)
    - Test with known drawdown sequence
    - Test recovery after drawdown

test_value_at_risk():
    - Test historical vs parametric methods
    - Test at different confidence levels
    - Compare to manual percentile calculation

test_beta():
    - Test with perfectly correlated returns (beta = 1)
    - Test with uncorrelated returns (beta ~ 0)
    - Test with mismatched array lengths (should raise)

test_win_rate():
    - Test with all wins (should be 1.0)
    - Test with 50/50 mix
    - Test edge cases

test_profit_factor():
    - Test with known profit/loss values
    - Test with no losses (should raise)

test_expectancy():
    - Test positive and negative expectancy scenarios
"""
