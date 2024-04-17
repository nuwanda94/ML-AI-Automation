import numpy as np


class Numpy_Utils:
    """
    A utility class for common NumPy operations.
    """

    @staticmethod
    def to_numpy(array):
        """
        Convert the given array to a NumPy array.

        Args:
            array (Iterable): The array to be converted.

        Returns:
            numpy.ndarray: The converted NumPy array.
        """
        return np.array(array)

    @staticmethod
    def clip(array, min_val, max_val):
        """
        Clip the values in the given array to the specified minimum and maximum values.

        Args:
            array (numpy.ndarray): The array to be clipped.
            min_val (float): The minimum value to clip to.
            max_val (float): The maximum value to clip to.

        Returns:
            numpy.ndarray: The clipped array.
        """
        return np.clip(array, min_val, max_val)
