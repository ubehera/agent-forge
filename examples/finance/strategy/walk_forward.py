"""
Production walk-forward analysis for strategy validation
Tests strategy robustness by simulating rolling train/test windows
"""

from typing import List, Dict, Tuple, Callable
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


class WalkForwardAnalysis:
    """
    Walk-forward analysis framework
    Trains strategy on in-sample data, tests on out-of-sample data
    """

    def __init__(
        self,
        train_period_days: int = 365,
        test_period_days: int = 90,
        step_days: int = 90
    ):
        self.train_period = train_period_days
        self.test_period = test_period_days
        self.step = step_days

    def split_data(
        self,
        df: pd.DataFrame,
        date_column: str = 'date'
    ) -> List[Tuple[pd.DataFrame, pd.DataFrame]]:
        """
        Split data into train/test windows
        Returns: List of (train_df, test_df) tuples
        """

        df = df.sort_values(date_column).reset_index(drop=True)
        splits = []

        start_date = df[date_column].min()
        end_date = df[date_column].max()

        current_date = start_date

        while current_date + timedelta(days=self.train_period + self.test_period) <= end_date:
            # Define train period
            train_start = current_date
            train_end = current_date + timedelta(days=self.train_period)

            # Define test period
            test_start = train_end
            test_end = test_start + timedelta(days=self.test_period)

            # Split data
            train_df = df[(df[date_column] >= train_start) & (df[date_column] < train_end)]
            test_df = df[(df[date_column] >= test_start) & (df[date_column] < test_end)]

            if len(train_df) > 0 and len(test_df) > 0:
                splits.append((train_df, test_df))

            # Step forward
            current_date += timedelta(days=self.step)

        return splits

    def run_walk_forward(
        self,
        df: pd.DataFrame,
        strategy,
        optimize_func: Callable,
        backtest_func: Callable
    ) -> Dict:
        """
        Run complete walk-forward analysis

        Args:
            df: Full dataset
            strategy: Strategy instance
            optimize_func: Function to optimize parameters on train data
            backtest_func: Function to backtest with parameters on test data

        Returns:
            Dictionary with aggregated results
        """

        splits = self.split_data(df)
        all_results = []

        print(f"Running {len(splits)} walk-forward windows...")

        for i, (train_df, test_df) in enumerate(splits):
            print(f"\nWindow {i+1}/{len(splits)}")
            print(f"Train: {train_df['date'].min()} to {train_df['date'].max()}")
            print(f"Test: {test_df['date'].min()} to {test_df['date'].max()}")

            # Optimize on train data
            try:
                best_params = optimize_func(train_df)
                print(f"Best params: {best_params}")

                # Test on out-of-sample data
                test_results = backtest_func(test_df, best_params)
                test_results['window'] = i
                test_results['train_start'] = train_df['date'].min()
                test_results['train_end'] = train_df['date'].max()
                test_results['test_start'] = test_df['date'].min()
                test_results['test_end'] = test_df['date'].max()

                all_results.append(test_results)

            except Exception as e:
                print(f"Error in window {i}: {e}")
                continue

        # Aggregate results
        results_df = pd.DataFrame(all_results)

        summary = {
            'num_windows': len(all_results),
            'avg_return': results_df['total_return'].mean(),
            'std_return': results_df['total_return'].std(),
            'avg_sharpe': results_df['sharpe_ratio'].mean(),
            'avg_max_drawdown': results_df['max_drawdown'].mean(),
            'positive_windows': (results_df['total_return'] > 0).sum(),
            'negative_windows': (results_df['total_return'] <= 0).sum(),
            'win_rate': (results_df['total_return'] > 0).mean(),
            'all_windows': results_df.to_dict('records')
        }

        return summary


# Usage example
def example_walk_forward():
    """Example walk-forward analysis workflow"""

    # Sample data
    dates = pd.date_range(start='2020-01-01', end='2023-12-31', freq='D')
    df = pd.DataFrame({
        'date': dates,
        'close': np.random.randn(len(dates)).cumsum() + 100
    })

    wfa = WalkForwardAnalysis(
        train_period_days=365,
        test_period_days=90,
        step_days=90
    )

    def optimize_func(train_df):
        # Dummy optimization
        return {'param1': 14, 'param2': 30}

    def backtest_func(test_df, params):
        # Dummy backtest
        return {
            'total_return': np.random.uniform(-0.1, 0.2),
            'sharpe_ratio': np.random.uniform(0, 2),
            'max_drawdown': np.random.uniform(0, 0.2)
        }

    results = wfa.run_walk_forward(df, None, optimize_func, backtest_func)

    print(f"\n=== Walk-Forward Summary ===")
    print(f"Windows: {results['num_windows']}")
    print(f"Average Return: {results['avg_return']:.2%}")
    print(f"Average Sharpe: {results['avg_sharpe']:.2f}")
    print(f"Win Rate: {results['win_rate']:.2%}")


if __name__ == "__main__":
    example_walk_forward()
