import pandas as pd
import random

from datetime import timedelta
from typing import List


class DateGenerator:
    def __init__(self, start_date: str, num_rows: int) -> None:
        """
        Initializes the DateGenerator with a start date and the number of rows (dates) to generate.

        :param start_date: A string or datetime-like object, the starting point for date generation.
        :param num_rows: An integer, the number of dates to generate.
        """
        self.start_date = pd.to_datetime(start_date)
        self.num_rows = num_rows

    def generate_dates(self) -> List[pd.Timestamp]:
        """
        Generates a list of dates starting from self.start_date, with a random number of repetitions
            for each date with timedelta(seconds=1)

        :return: A list of datetime objects.
        """

        start_date = self.start_date
        current_count = 0
        generated_dates = []

        while current_count < self.num_rows:
            # Generate a random repeat count for each date, for example, between 1 and 5
            repeat_count = random.randint(1, 5)

            # Append the date repeat_count times
            for _ in range(repeat_count):
                if current_count < self.num_rows:
                    generated_dates.append(start_date)
                    current_count += 1
            # Increment the date by one second after each block of repeats
            start_date += timedelta(seconds=1)

        return generated_dates
