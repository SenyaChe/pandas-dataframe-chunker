# Pandas DataFrame Chunker

## Overview
The DataFrame Chunker is a Python tool designed to efficiently split a pre-sorted pandas DataFrame into chunks based on a specified column and a minimum chunk size.
This utility ensures that each chunk is at least as large as the desired size and that the dates (or other sequential data) do not overlap between chunks.


## Features
- Efficient memory usage during chunking operations.
- Ability to specify the minimum number of rows per chunk.
- Ensures no overlapping dates between chunks.
- Works with pre-sorted DataFrames to maintain order.


## Requirements
This module requires Python 3.6+ and the pandas library.


## Components
The module comprises several components, including:
* `DateGenerator`: Generates a sequence of dates for creating DataFrames.
* `DataFrameChunker`: Handles the logic for dividing the DataFrame into the desired chunks based on the date column.
* `main.py`: Orchestrates the generation of data, chunking, and validation of chunks.
