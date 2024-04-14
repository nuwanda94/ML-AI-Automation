import pandas as pd

class CleanData():
    def __init__(self) -> None:
        pass
    
    def read_pkl(self, dataset_path:str) -> pd.DataFrame:
        return pd.read_pickle(dataset_path)

    def pop_column(self, df: pd.DataFrame, column:str) -> pd.DataFrame:
        copy_df = df.copy()
        copy_df = copy_df.pop(column)
        return copy_df