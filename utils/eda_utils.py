from sweetviz import analyze
import pandas as pd

class EDA():
    def __init__(self) -> None:
        pass

    def sweetviz_eda(self, df: pd.DataFrame, target_var: str):
        
        report = analyze(df, target_feat=target_var)
        return report
