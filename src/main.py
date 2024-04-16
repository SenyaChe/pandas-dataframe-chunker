import pandas as pd
import logging
from typing import List

import utils.logger
from utils.date_generator import DateGenerator
from utils.dataframe_chunker import DataFrameChunker


def generate_data(start_date: str, num_rows: int) -> pd.DataFrame:
    generator = DateGenerator(start_date, num_rows)
    dates = generator.generate_dates()
    if not dates:
        raise ValueError("No dates generated: check start_date and num_rows.")
    logging.info(f"Created data frame with dates, {num_rows} rows.")
    return pd.DataFrame(dates, columns=['dt'])


def chunk_data(df: pd.DataFrame, date_column: str, min_chunk_size: int) -> List[pd.DataFrame]:
    chunker = DataFrameChunker(df, date_column, min_chunk_size)
    chunks = chunker.chunk_dataframe_optimized()
    if not chunks:
        raise ValueError("Chunking failed: no valid chunks were created.")
    logging.info(f"Created chunks list with {len(chunks)} chunks.")
    return chunks



def main(num_rows=5000000, start_date='2023-01-01 00:00:00', date_column='dt', min_chunk_size=200) -> List[pd.DataFrame]:
    try:
        # Step 1: Generate data > pandas df (only for example, can be removed and changed on uploading from source)
        df_loaded = generate_data(start_date, num_rows)

        # Step 2: Perform chunking
        chunks = chunk_data(df_loaded, date_column, min_chunk_size)

        # Step 3: Output the results
        logging.info(f"Generated {len(chunks)} chunks.")
        if chunks:
            logging.info(f"First chunk has {len(chunks[0])} rows.")
            if len(chunks) > 1:
                logging.info(f"Last chunk has {len(chunks[-1])} rows.")
            else:
                logging.info("Only one chunk generated, also reported as the last chunk.")

    except ValueError as e:
        logging.error(f"Error in processing: {e}")
        return []


if __name__ == "__main__":
    main()