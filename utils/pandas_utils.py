import pandas as pd

class CleanData():
    def __init__(self) -> None:
        """Initialize the CleanData class."""
        if pd is None:
            raise ValueError("The pandas library is not installed. Please install it by running 'pip install pandas'.")
        self.pd = pd
    
    def read_pkl(self, dataset_path:str) -> pd.DataFrame:
        """
        Read a pickle file and return the data as a pandas DataFrame.

        Args:
            dataset_path (str): The path to the pickle file.

        Returns:
            pd.DataFrame: The data read from the pickle file.
        """
        return self.pd.read_pickle(dataset_path)

    def pop_column(self, df: pd.DataFrame, column_name: str) -> pd.DataFrame:
        """
        Removes the specified column from the given DataFrame and returns the modified DataFrame.

        Parameters:
            df (pd.DataFrame): The DataFrame from which the column will be removed.
            column_name (str): The name of the column to be removed.

        Returns:
            pd.DataFrame: The modified DataFrame with the specified column removed.
        """
        return df.pop(column_name)
    
    def copy_df(self, df: pd.DataFrame) -> pd.DataFrame:
        """Return a shallow copy of the DataFrame."""
        # Fastest and most memory-efficient copy method
        return df.copy(deep=False) 
