from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


class sklearn_utils:
    def __init__(self) -> None:
        """
        A constructor for the sklearn_utils class.
        No input parameters.
        Returns None.
        """
        self.sc = StandardScaler()

    def train_test_split(self, X, y, test_size):
        """
        A function that performs the train-test split on the input data X and labels y using the specified test size.
        
        Args:
            X: The input data.
            y: The target labels.
            test_size: The proportion of the dataset to include in the test split.
        
        Returns:
            The train-test split of X and y based on the provided test size.
        """
        return train_test_split(X, y, test_size=test_size)
    
    def fit_transform_scaler(self, X):
        """
        Fits and transforms the input data X using a StandardScaler instance.

        Args:
            self: The sklearn_utils object.
            X: The input data to be standardized.

        Returns:
            The standardized version of the input data X.
        """
        return self.sc.fit_transform(X)
    
    def scaler_transform(self, features):
        """
        A function that transforms the input features using the StandardScaler instance.

        Args:
            self: The sklearn_utils object.
            features: The input features to be transformed.

        Returns:
            The transformed version of the input features using the StandardScaler instance.
        """

        return self.sc.transform(features)
    
    