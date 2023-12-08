# EasyZip

EasyZip is a lightweight version of `Zipfile` that simplifies working with zip files.

## Installation

1. **Clone the Repository:**

   Clone the `easyzip` GitHub repository to your local machine using Git:

   ```bash
   git clone https://github.com/hackifiery/easyzip.git
   ```

2. **Install the package:**

   Navigate to the project directory and use `pip` to install the package locally:

   ```bash
   cd easyzip
   pip install .
   ```

## Usage
To use the module you will first have to import it:

   ```python
   from easyzip import EasyZip
```
### Creating a zip file:
```python
with EasyZip('example.zip') as ez:
    ez.add_file('file1.txt')
    ez.add_directory('my_directory')
```

### Extracting zip content:
```python
with EasyZip('example.zip') as ez:
    ez.extract_to('extracted_directory')
```

Also refer to the [usage_example.py](/examples/usage_example.py) file.
