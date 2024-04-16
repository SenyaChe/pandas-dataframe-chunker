# Pandas DataFrame Chunker

## Overview
The DataFrame Chunker is a Python tool designed to efficiently split a pre-sorted pandas DataFrame into chunks based on a specified column and a minimum chunk size.
This utility ensures that each chunk is at least as large as the desired size and that the dates (or other sequential data) do not overlap between chunks.


## Features
- Efficient memory usage during chunking operations.
- Ability to specify the minimum number of rows per chunk.
- Ensures no overlapping dates between chunks.
- Works with pre-sorted DataFrames to maintain order.


## Components
The module comprises several components, including:
* `DateGenerator`: Generates a sequence of dates for creating DataFrames.
* `DataFrameChunker`: Handles the logic for dividing the DataFrame into the desired chunks based on the date column.
* `main.py`: Orchestrates the generation of data, chunking, and validation of chunks.


## Setup

- Python 3.8+ required.
- Dependencies are listed in the `requirements.txt`.

``` 
# Create a virtual environment in your project directory
python -m venv venv

# Activate the virtual environment
    # On Windows:
    venv\Scripts\activate
    # On macOS and Linux:
    source venv/bin/activate

# Install the dependencies using pip
pip install -r requirements.txt

# Run the script
python main.py
``` 


## Testing
The module includes unit tests covering key functionalities:
* Validating the integrity of chunk sizes.
* Ensuring no date overlap between chunks.
* Checking for proper handling of edge cases such as minimum chunk sizes larger than the DataFrame size.

Run the tests using the unittest module:
``` 
python -m unittest test_dataframe_chunker.py
``` 


## Example
1. Dataframe input data:
``` 
2023-01-01 00:00:01
2023-01-01 00:00:01
2023-01-01 00:00:02
2023-01-01 00:00:02
2023-01-01 00:00:02
2023-01-01 00:00:03
```

2. For a chunk size between 1 and 2, the result is 3 chunks:
``` 
# 1-st chunk
2023-01-01 00:00:01
2023-01-01 00:00:01

# 2-nd chunk
2023-01-01 00:00:02
2023-01-01 00:00:02
2023-01-01 00:00:02

# 3-rd chunk
2023-01-01 00:00:03
``` 

3. For a chunk size between 3 and 5, the result is 2 chunks:
``` 
# 1-st chunk
2023-01-01 00:00:01
2023-01-01 00:00:01
2023-01-01 00:00:02
2023-01-01 00:00:02
2023-01-01 00:00:02

# 2-nd chunk
2023-01-01 00:00:03
``` 

4. For chunk sizes 6 and above, the result is the entire frame:
``` 
# the entire dataframe as a single chunk
2023-01-01 00:00:01
2023-01-01 00:00:01
2023-01-01 00:00:02
2023-01-01 00:00:02
2023-01-01 00:00:02
2023-01-01 00:00:03
``` 
