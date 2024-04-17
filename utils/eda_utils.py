from sweetviz import analyze
import pandas as pd

class EDA():
    def __init__(self) -> None:
        """
        Initializes an instance of the class.

        This method does not take any parameters.

        Returns:
            None
        """
        pass

    def sweetviz_eda(self, df: pd.DataFrame, target_var: str):
        """
        A function that performs an exploratory data analysis (EDA) using Sweetviz on the input DataFrame with a specified target variable.

        Args:
            df (pd.DataFrame): The input DataFrame to be analyzed.
            target_var (str): The target variable for analysis.

        Returns:
            The Sweetviz EDA report generated from the input DataFrame and target variable.
        """
        
        report = analyze(df, target_feat=target_var)
        return report
