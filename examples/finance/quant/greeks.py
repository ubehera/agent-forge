"""
Options Greeks and implied volatility calculations
Black-Scholes model implementation for options pricing
"""

import numpy as np
from typing import Optional, Dict
from scipy.stats import norm
from scipy.optimize import newton


class OptionsAnalysis:
    """Options Greeks and implied volatility calculations"""

    @staticmethod
    def black_scholes_call(
        S: float,  # Spot price
        K: float,  # Strike price
        T: float,  # Time to expiration (years)
        r: float,  # Risk-free rate
        sigma: float  # Volatility
    ) -> float:
        """Black-Scholes call option price"""

        d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)

        call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

        return call_price

    @staticmethod
    def black_scholes_put(
        S: float,
        K: float,
        T: float,
        r: float,
        sigma: float
    ) -> float:
        """Black-Scholes put option price"""

        d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)

        put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

        return put_price

    @staticmethod
    def calculate_greeks(
        S: float,
        K: float,
        T: float,
        r: float,
        sigma: float,
        option_type: str = 'call'
    ) -> Dict[str, float]:
        """
        Calculate all Greeks for an option
        Returns: {delta, gamma, theta, vega, rho}
        """

        if T <= 0:
            return {
                'delta': 0.0, 'gamma': 0.0, 'theta': 0.0,
                'vega': 0.0, 'rho': 0.0
            }

        d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)

        # Delta
        if option_type.lower() == 'call':
            delta = norm.cdf(d1)
        else:
            delta = -norm.cdf(-d1)

        # Gamma (same for calls and puts)
        gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))

        # Theta
        term1 = -(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))
        if option_type.lower() == 'call':
            term2 = -r * K * np.exp(-r * T) * norm.cdf(d2)
            theta = (term1 + term2) / 365  # Per day
        else:
            term2 = r * K * np.exp(-r * T) * norm.cdf(-d2)
            theta = (term1 + term2) / 365

        # Vega (same for calls and puts)
        vega = S * norm.pdf(d1) * np.sqrt(T) / 100  # Per 1% change in IV

        # Rho
        if option_type.lower() == 'call':
            rho = K * T * np.exp(-r * T) * norm.cdf(d2) / 100
        else:
            rho = -K * T * np.exp(-r * T) * norm.cdf(-d2) / 100

        return {
            'delta': delta,
            'gamma': gamma,
            'theta': theta,
            'vega': vega,
            'rho': rho
        }

    @staticmethod
    def implied_volatility(
        market_price: float,
        S: float,
        K: float,
        T: float,
        r: float,
        option_type: str = 'call',
        max_iterations: int = 100,
        tolerance: float = 1e-6
    ) -> Optional[float]:
        """
        Calculate implied volatility using Newton-Raphson method
        """

        def objective(sigma):
            if option_type.lower() == 'call':
                return OptionsAnalysis.black_scholes_call(S, K, T, r, sigma) - market_price
            else:
                return OptionsAnalysis.black_scholes_put(S, K, T, r, sigma) - market_price

        try:
            # Initial guess: 0.3 (30% volatility)
            iv = newton(objective, 0.3, maxiter=max_iterations, tol=tolerance)
            return max(0, iv)  # IV cannot be negative
        except RuntimeError:
            return None  # Convergence failed


# Usage example
def example_options_analysis():
    """Example: Calculate Greeks for an option"""

    greeks = OptionsAnalysis.calculate_greeks(
        S=100,      # Stock price
        K=105,      # Strike price
        T=0.25,     # 3 months to expiration
        r=0.05,     # 5% risk-free rate
        sigma=0.25, # 25% implied volatility
        option_type='call'
    )

    print("Option Greeks:")
    print(f"Delta: {greeks['delta']:.4f}")
    print(f"Gamma: {greeks['gamma']:.4f}")
    print(f"Theta: {greeks['theta']:.4f}")
    print(f"Vega: {greeks['vega']:.4f}")
    print(f"Rho: {greeks['rho']:.4f}")

    # Calculate implied volatility
    market_price = 3.50
    iv = OptionsAnalysis.implied_volatility(
        market_price=market_price,
        S=100,
        K=105,
        T=0.25,
        r=0.05,
        option_type='call'
    )

    print(f"\nImplied Volatility: {iv:.2%}")


if __name__ == "__main__":
    example_options_analysis()
