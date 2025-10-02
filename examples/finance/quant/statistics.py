"""
Statistical methods for trading research
Time-series analysis, cointegration, correlation, feature engineering
"""

import numpy as np
import pandas as pd
from typing import Dict
from statsmodels.tsa.stattools import adfuller, coint


class StatisticalAnalysis:
    """Statistical methods for trading research"""

    @staticmethod
    def adf_test(prices: np.ndarray) -> Dict:
        """
        Augmented Dickey-Fuller test for stationarity
        Returns: {statistic, p_value, critical_values, is_stationary}
        """

        result = adfuller(prices, autolag='AIC')

        return {
            'statistic': result[0],
            'p_value': result[1],
            'critical_values': result[4],
            'is_stationary': result[1] < 0.05  # 5% significance level
        }

    @staticmethod
    def cointegration_test(series1: np.ndarray, series2: np.ndarray) -> Dict:
        """
        Test for cointegration between two price series (for pairs trading)
        Returns: {statistic, p_value, critical_values, is_cointegrated}
        """

        score, p_value, crit_values = coint(series1, series2)

        return {
            'statistic': score,
            'p_value': p_value,
            'critical_values': crit_values,
            'is_cointegrated': p_value < 0.05
        }

    @staticmethod
    def z_score(series: np.ndarray, window: int = 20) -> np.ndarray:
        """
        Calculate rolling z-score for mean reversion strategies
        """
        mean = pd.Series(series).rolling(window=window).mean().values
        std = pd.Series(series).rolling(window=window).std().values

        z = (series - mean) / (std + 1e-10)

        return z

    @staticmethod
    def calculate_beta(
        stock_returns: np.ndarray,
        market_returns: np.ndarray
    ) -> float:
        """Calculate stock beta relative to market"""

        covariance = np.cov(stock_returns, market_returns)[0, 1]
        market_variance = np.var(market_returns)

        beta = covariance / market_variance

        return beta

    @staticmethod
    def correlation_matrix(
        returns_df: pd.DataFrame,
        method: str = 'pearson'
    ) -> pd.DataFrame:
        """
        Calculate correlation matrix for portfolio of stocks
        method: 'pearson', 'spearman', 'kendall'
        """
        return returns_df.corr(method=method)

    @staticmethod
    def rolling_correlation(
        series1: np.ndarray,
        series2: np.ndarray,
        window: int = 20
    ) -> np.ndarray:
        """Calculate rolling correlation between two series"""

        s1 = pd.Series(series1)
        s2 = pd.Series(series2)

        return s1.rolling(window=window).corr(s2).values


class FeatureEngineering:
    """Feature engineering for machine learning trading models"""

    @staticmethod
    def create_returns(prices: np.ndarray, periods: int = 1) -> np.ndarray:
        """Calculate returns over specified periods"""
        return pd.Series(prices).pct_change(periods=periods).values

    @staticmethod
    def create_log_returns(prices: np.ndarray) -> np.ndarray:
        """Calculate log returns (better for compounding)"""
        return np.log(prices / np.roll(prices, 1))

    @staticmethod
    def create_lag_features(
        series: np.ndarray,
        lags: list = [1, 5, 10, 20]
    ) -> pd.DataFrame:
        """Create lagged features for time series"""

        df = pd.DataFrame()
        for lag in lags:
            df[f'lag_{lag}'] = pd.Series(series).shift(lag).values

        return df

    @staticmethod
    def create_rolling_features(
        prices: np.ndarray,
        windows: list = [5, 10, 20, 50]
    ) -> pd.DataFrame:
        """Create rolling statistics features"""

        df = pd.DataFrame()
        s = pd.Series(prices)

        for window in windows:
            df[f'sma_{window}'] = s.rolling(window=window).mean().values
            df[f'std_{window}'] = s.rolling(window=window).std().values
            df[f'min_{window}'] = s.rolling(window=window).min().values
            df[f'max_{window}'] = s.rolling(window=window).max().values

        return df

    @staticmethod
    def create_momentum_features(prices: np.ndarray) -> pd.DataFrame:
        """Create momentum-based features"""

        df = pd.DataFrame()

        # Rate of change over different periods
        for period in [1, 5, 10, 20]:
            df[f'roc_{period}'] = pd.Series(prices).pct_change(periods=period).values

        # Momentum
        df['momentum_10'] = prices - pd.Series(prices).shift(10).values
        df['momentum_20'] = prices - pd.Series(prices).shift(20).values

        # Relative position in range
        df['price_position_20'] = (
            (prices - pd.Series(prices).rolling(20).min().values) /
            (pd.Series(prices).rolling(20).max().values -
             pd.Series(prices).rolling(20).min().values + 1e-10)
        )

        return df

    @staticmethod
    def create_volatility_features(
        high: np.ndarray,
        low: np.ndarray,
        close: np.ndarray
    ) -> pd.DataFrame:
        """Create volatility-based features"""

        df = pd.DataFrame()

        # Historical volatility (different windows)
        for window in [5, 10, 20]:
            returns = pd.Series(close).pct_change()
            df[f'hist_vol_{window}'] = returns.rolling(window=window).std().values * np.sqrt(252)

        # True Range as percentage
        tr = np.maximum(high - low, np.maximum(
            np.abs(high - np.roll(close, 1)),
            np.abs(low - np.roll(close, 1))
        ))
        df['tr_pct'] = tr / close

        return df


# Usage example
def example_statistical_analysis():
    """Example: Test for cointegration (pairs trading)"""

    # Generate two cointegrated series
    np.random.seed(42)
    x = np.random.randn(100).cumsum() + 100
    y = x + np.random.randn(100) * 5  # Cointegrated with x

    result = StatisticalAnalysis.cointegration_test(x, y)

    print(f"Cointegration Test:")
    print(f"Statistic: {result['statistic']:.4f}")
    print(f"P-value: {result['p_value']:.4f}")
    print(f"Is Cointegrated: {result['is_cointegrated']}")

    # Calculate z-score for mean reversion entry
    spread = y - x
    z = StatisticalAnalysis.z_score(spread, window=20)

    print(f"\nCurrent Z-Score: {z[-1]:.2f}")
    print(f"Entry signal: {'LONG' if z[-1] < -2 else 'SHORT' if z[-1] > 2 else 'NEUTRAL'}")


if __name__ == "__main__":
    example_statistical_analysis()
