"""
Portfolio optimization using Modern Portfolio Theory
Mean-variance optimization, minimum variance, efficient frontier
"""

import numpy as np
import pandas as pd
from typing import Dict, Optional
from scipy.optimize import minimize


class PortfolioOptimizer:
    """Portfolio optimization using Modern Portfolio Theory"""

    def __init__(self, returns: pd.DataFrame):
        """
        Initialize optimizer with historical returns

        Args:
            returns: DataFrame of asset returns (assets as columns)
        """
        self.returns = returns
        self.mean_returns = returns.mean()
        self.cov_matrix = returns.cov()
        self.num_assets = len(returns.columns)

    def mean_variance_optimization(
        self,
        target_return: Optional[float] = None,
        risk_free_rate: float = 0.02
    ) -> Dict:
        """
        Mean-variance optimization (Markowitz)

        Args:
            target_return: Target portfolio return (if None, maximize Sharpe)
            risk_free_rate: Risk-free rate for Sharpe calculation

        Returns:
            Dictionary with optimal weights and metrics
        """

        def portfolio_stats(weights):
            """Calculate portfolio statistics"""
            returns = np.dot(weights, self.mean_returns)
            volatility = np.sqrt(np.dot(weights.T, np.dot(self.cov_matrix, weights)))
            sharpe = (returns - risk_free_rate) / volatility if volatility > 0 else 0
            return returns, volatility, sharpe

        def negative_sharpe(weights):
            """Objective function: minimize negative Sharpe"""
            _, _, sharpe = portfolio_stats(weights)
            return -sharpe

        # Constraints
        constraints = [
            {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}  # Weights sum to 1
        ]

        # Add return constraint if specified
        if target_return is not None:
            constraints.append({
                'type': 'eq',
                'fun': lambda x: np.dot(x, self.mean_returns) - target_return
            })

        # Bounds: 0 <= weight <= 1 (long-only)
        bounds = tuple((0, 1) for _ in range(self.num_assets))

        # Initial guess: equal weights
        init_guess = np.array([1/self.num_assets] * self.num_assets)

        # Optimize
        result = minimize(
            negative_sharpe,
            init_guess,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints
        )

        if not result.success:
            raise ValueError(f"Optimization failed: {result.message}")

        weights = result.x
        returns, volatility, sharpe = portfolio_stats(weights)

        return {
            'weights': dict(zip(self.returns.columns, weights)),
            'expected_return': returns,
            'volatility': volatility,
            'sharpe_ratio': sharpe
        }

    def minimum_variance_portfolio(self) -> Dict:
        """
        Find minimum variance portfolio

        Returns:
            Dictionary with optimal weights and metrics
        """

        def portfolio_variance(weights):
            """Calculate portfolio variance"""
            return np.dot(weights.T, np.dot(self.cov_matrix, weights))

        # Constraints: weights sum to 1
        constraints = [
            {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}
        ]

        # Bounds: 0 <= weight <= 1 (long-only)
        bounds = tuple((0, 1) for _ in range(self.num_assets))

        # Initial guess: equal weights
        init_guess = np.array([1/self.num_assets] * self.num_assets)

        # Optimize
        result = minimize(
            portfolio_variance,
            init_guess,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints
        )

        if not result.success:
            raise ValueError(f"Optimization failed: {result.message}")

        weights = result.x
        returns = np.dot(weights, self.mean_returns)
        volatility = np.sqrt(portfolio_variance(weights))

        return {
            'weights': dict(zip(self.returns.columns, weights)),
            'expected_return': returns,
            'volatility': volatility
        }

    def efficient_frontier(self, num_portfolios: int = 100) -> pd.DataFrame:
        """
        Calculate efficient frontier

        Args:
            num_portfolios: Number of portfolios to generate

        Returns:
            DataFrame with portfolio returns and volatilities
        """

        min_return = self.mean_returns.min()
        max_return = self.mean_returns.max()
        target_returns = np.linspace(min_return, max_return, num_portfolios)

        portfolios = []

        for target_return in target_returns:
            try:
                result = self.mean_variance_optimization(target_return=target_return)
                portfolios.append({
                    'return': result['expected_return'],
                    'volatility': result['volatility'],
                    'sharpe': result['sharpe_ratio']
                })
            except:
                continue

        return pd.DataFrame(portfolios)


# Usage example
def example_portfolio_optimization():
    """Example: Optimize portfolio allocation"""

    # Generate sample returns
    np.random.seed(42)
    returns = pd.DataFrame({
        'AAPL': np.random.normal(0.001, 0.02, 252),
        'MSFT': np.random.normal(0.0008, 0.018, 252),
        'GOOGL': np.random.normal(0.0012, 0.022, 252),
        'SPY': np.random.normal(0.0007, 0.015, 252)
    })

    optimizer = PortfolioOptimizer(returns)

    # Maximum Sharpe portfolio
    result = optimizer.mean_variance_optimization()
    print("\nMaximum Sharpe Portfolio:")
    print(f"Expected Return: {result['expected_return']:.2%}")
    print(f"Volatility: {result['volatility']:.2%}")
    print(f"Sharpe Ratio: {result['sharpe_ratio']:.2f}")
    print("Weights:")
    for symbol, weight in result['weights'].items():
        print(f"  {symbol}: {weight:.2%}")

    # Minimum Variance portfolio
    result = optimizer.minimum_variance_portfolio()
    print("\nMinimum Variance Portfolio:")
    print(f"Expected Return: {result['expected_return']:.2%}")
    print(f"Volatility: {result['volatility']:.2%}")
    print("Weights:")
    for symbol, weight in result['weights'].items():
        print(f"  {symbol}: {weight:.2%}")


if __name__ == "__main__":
    example_portfolio_optimization()
