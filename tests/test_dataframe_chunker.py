import unittest
import pandas as pd
import time

from split_to_chunks_project.src.utils.dataframe_chunker import DataFrameChunker


class TestDataFrameChunker(unittest.TestCase):
    def test_empty_df(self):
        """Test that an empty DataFrame results in no chunks being created."""
        df = pd.DataFrame()
        chunker = DataFrameChunker(df, 'dt', 10)
        chunks = chunker.chunk_dataframe_optimized()
        self.assertEqual(len(chunks), 0, "Chunk list should be empty for an empty DataFrame")

    def test_min_chunk_size_never_reached(self):
        """Test that DataFrame smaller than min_chunk_size results in a single chunk."""
        data = {'date': ['2023-01-01'] * 5 + ['2023-01-02'] * 4}
        df = pd.DataFrame(data)
        chunker = DataFrameChunker(df, 'date', 10)
        chunks = chunker.chunk_dataframe_optimized()
        self.assertEqual(len(chunks), 1, "All rows should be in one chunk since the min_chunk_size is never reached")

    def test_correct_chunking(self):
        """Verify that DataFrame is correctly chunked based on min_chunk_size."""
        data = {'date': ['2023-01-01'] * 5 + ['2023-01-02'] * 10 + ['2023-01-03'] * 15}
        df = pd.DataFrame(data)
        chunker = DataFrameChunker(df, 'date', 10)
        chunks = chunker.chunk_dataframe_optimized()
        self.assertEqual(len(chunks), 2, "Should be chunked into 2 chunks based on min_chunk_size")

    def test_multiple_columns(self):
        """Ensure that DataFrame with multiple columns is chunked correctly based on a specified column."""
        data = {'date': ['2023-01-01'] * 5 + ['2023-01-02'] * 5, 'value': range(10)}
        df = pd.DataFrame(data)
        chunker = DataFrameChunker(df, 'date', 5)
        chunks = chunker.chunk_dataframe_optimized()
        self.assertEqual(len(chunks), 2, "Should chunk correctly even with multiple columns.")

    def test_invalid_column_name(self):
        """Check for handling of invalid column names with appropriate error."""
        data = {'date': ['2023-01-01'] * 10}
        df = pd.DataFrame(data)
        with self.assertRaises(KeyError):
            chunker = DataFrameChunker(df, 'nonexistent_column', 5)
            chunker.chunk_dataframe_optimized()

    def test_large_dataset_performance(self):
        """Evaluate performance of chunking on large datasets."""
        data = {'date': ['2023-01-01'] * 10000000}
        df = pd.DataFrame(data)
        chunker = DataFrameChunker(df, 'date', 100)

        start_time = time.time()
        chunks = chunker.chunk_dataframe_optimized()
        elapsed_time = time.time() - start_time

        self.assertTrue(len(chunks) > 0, "Should handle large datasets efficiently.")
        self.assertLess(elapsed_time, 1, "Chunking operation took too long.")


if __name__ == '__main__':
    unittest.main()
