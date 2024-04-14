from cleanlab import Datalab
from pandas import DataFrame


class CleanLab():

    def __init__(self) -> None:
        pass

    def df_to_dict_with_labels(self, df, column_name):
        """
        Converts a pandas DataFrame to a dictionary with separate data and labels.

        Args:
            df (pd.DataFrame): The input DataFrame.
            column_name (str): The name of the column to be used as labels.

        Returns:
            dict: A dictionary containing two keys:
                'data': A DataFrame containing all columns except the specified column_name.
                'labels': A Series containing the values from the specified column_name.
        """

        if column_name not in df.columns:
            raise ValueError(f"Column '{column_name}' not found in the DataFrame")

        data = df  # Drop the specified column
        labels = df[column_name]  # Extract the labels as a Series
        return {"data": data, "y": labels}


    def get_data_issuse(self, data_dict, label_name):
        lab = Datalab(data_dict,label_name=label_name)
        return lab.data_issues()