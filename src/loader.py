# Dunder methods + encapsulation
# src/loader.py
"""
DataLoader module for loading CSV files into pandas DataFrames.

This module defines the DataLoader class, which handles:
- Reading CSV files into a pandas DataFrame.
- Accessing the loaded DataFrame.
- Comparing DataLoader instances.
- Getting basic metadata about the DataFrame.
"""

import pandas as pd

class DataLoader:
    """
    Class to load a CSV file into a pandas DataFrame and provide basic metadata.

    Attributes:
        _path (str): Path to the CSV file.
        _df (pd.DataFrame): Loaded DataFrame (protected).
    """

    def __init__(self, path):
        """
        Initialize the DataLoader with a CSV file path.

        Args:
            path (str): Path to the CSV file.
        """
        self._path = path            # protected attribute
        self._df = None

    def load(self, nrows=None):
        """
        Load the CSV file into a pandas DataFrame.

        Args:
            nrows (int, optional): Number of rows to read. Defaults to None (read all).

        Returns:
            pd.DataFrame: Loaded DataFrame.
        """
        self._df = pd.read_csv(self._path, nrows=nrows)
        return self._df

    def get_df(self):
        """
        Accessor for the loaded DataFrame.

        Returns:
            pd.DataFrame: The loaded DataFrame.
        """
        return self._df

    # Dunder methods
    def __repr__(self):
        """
        String representation of the DataLoader object.

        Returns:
            str: Representation including the file path and number of rows loaded.
        """
        rows = len(self._df) if self._df is not None else 0
        return f"<DataLoader path='{self._path}' rows={rows}>"

    def __eq__(self, other):
        """
        Compare two DataLoader objects by their DataFrame shape.

        Args:
            other (DataLoader): Another DataLoader instance.

        Returns:
            bool: True if both DataFrames have the same shape, False otherwise.
        """
        if not isinstance(other, DataLoader):
            return False
        return self._df.shape == other._df.shape

    def __len__(self):
        """
        Return the number of columns in the loaded DataFrame.

        Returns:
            int: Number of columns if DataFrame is loaded, otherwise 0.
        """
        return len(self._df.columns) if self._df is not None else 0

