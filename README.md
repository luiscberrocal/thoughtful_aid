# README

## Project Overview

This project includes a function `sort` that categorizes packages based on their dimensions and mass. 
The function returns a dispatch type indicating where the package should be sent.

## Requirements

- Python 3.x
- `pip` for package management
- `pytest` for running tests

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/luiscberrocal/thoughtful_aid
    cd thoughtful_aid
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

The `sort` function is defined in `main.py`. It takes four parameters: `width`, `height`, `length`, and `mass`, and returns a `DispatchType`.

### Example

```python
from main import sort, DispatchType

width = 10
height = 10
length = 10
mass = 1

dispatch_type = sort(width, height, length, mass)
print(dispatch_type)  # Output: DispatchType.STANDARD
```

## Testing

Tests are written using `pytest` and are located in `tests.py`. To run the tests, use the following command:

```sh
pytest
```

### Example Test

The following test checks if the `sort` function correctly categorizes a package:

```python
import pytest
from main import DispatchType, sort

def test_sort():
    assert sort(10, 10, 10, 1) == DispatchType.STANDARD
```

Run this test with:

```sh
pytest tests.py
```
