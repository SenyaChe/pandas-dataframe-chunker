import pandas as pd
import logging
from typing import List


class DataFrameChunker:
    def __init__(self, df: pd.DataFrame, column_name: str, min_chunk_size: int) -> None:
        """
        Initializes the DataFrameChunker instance with the DataFrame, column name
        and minimum chunk size.

        :param df: The pandas DataFrame to be chunked.
        :param column_name: The column name to group and chunk by. Values must be sorted.
        :param min_chunk_size: The minimum number of rows each chunk should have, except possibly the last chunk.
        """

        self.df = df
        self.column_name = column_name
        self.min_chunk_size = min_chunk_size

    def chunk_dataframe_optimized(self) -> List[pd.DataFrame]:
        """
        Splits the DataFrame into chunks, each chunk being a DataFrame itself. The chunking is based on a
        specified column's values to ensure that each value in this column is not split across different chunks.

        :return: A list of pandas DataFrames.
        """
        # Check if DataFrame is empty
        if self.df.empty:
            logging.info("The DataFrame is empty. No chunking performed.")
            return []

        # Prepare to track chunks: list to hold result, starting index and index where last split was
        chunks = []
        start_idx = 0
        last_split = 0

        # Group by the specified column to calculate the sizes and cumulative sizes
        group_sizes = self.df.groupby(self.column_name).size()
        cumulative_sizes = group_sizes.cumsum()

        # Iterate through each group by index in cumulative_sizes
        for idx, cumulative in enumerate(cumulative_sizes):
            if cumulative - last_split >= self.min_chunk_size:
                # Find the actual end index of this group in the original dataframe
                actual_end_idx = self.df[self.df[self.column_name] == group_sizes.index[idx]].index[-1] + 1

                # Slice the dataframe from the last start index to the current group's end index
                chunks.append(self.df.iloc[start_idx:actual_end_idx])

                # Update the start index for the next chunk and the last split point
                start_idx = actual_end_idx
                last_split = cumulative

        # Check for any remaining data that hasn't been chunked because it didn't reach min_chunk_size
        if start_idx < len(self.df):
            if chunks:
                chunks[-1] = pd.concat([chunks[-1], self.df.iloc[start_idx:]])
            else:
                chunks.append(self.df.iloc[start_idx:])

        return chunks
