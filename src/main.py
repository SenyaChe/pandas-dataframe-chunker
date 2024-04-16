import pandas as pd
import logging
from typing import List

from utils.date_generator import DateGenerator


def generate_data(start_date: str, num_rows: int) -> pd.DataFrame:
    generator = DateGenerator(start_date, num_rows)
    dates = generator.generate_dates()
    if not dates:
        raise ValueError("No dates generated: check start_date and num_rows.")
    logging.info(f"Created data frame with dates, {num_rows} rows.")
    return pd.DataFrame(dates, columns=['dt'])



def main(num_rows=5000000, start_date='2023-01-01 00:00:00', date_column='dt', min_chunk_size=200) -> List[pd.DataFrame]:
    try:
        # Step 1: Generate data > pandas df (only for example, can be removed and changed on uploading from source)
        df_loaded = generate_data(start_date, num_rows)

    except ValueError as e:
        logging.error(f"Error in processing: {e}")
        return []


if __name__ == "__main__":
    main()