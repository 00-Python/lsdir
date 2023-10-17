# Lsdir

Lsdir is a Python class that provides a set of methods to interact with the file system. It allows you to scan directories, count the number of files and directories, print the directory tree, and find items by their ID. It also provides the ability to read the content of text files.

## Features

- **Scan directories**: The `scan_dir` method scans a given directory and returns a list of its children (both files and directories). Each child is represented as a dictionary with the following keys: `id`, `name`, `type`, `path`, and `children` (for directories) or `filetype` and `content` (for text files).

- **Count levels**: The `count_levels` method counts the number of levels in a given directory tree.

- **Print directory tree**: The `print_tree` method prints the directory tree in a human-readable format.

- **Find items by ID**: The `find_item_by_id` method finds an item (file or directory) by its ID.

- **Count files and directories**: The `count_files`, `count_dirs`, and `count_all` methods count the number of files, directories, and total items, respectively, in a given directory tree.

## Usage

First, import the necessary modules and the Lsdir class:

```python
import os
import mimetypes
from lsdir import Lsdir
```

Then, create an instance of the Lsdir class:

```python
files = Lsdir()
```

Now, you can use the methods of the Lsdir class. For example, to scan the current working directory and print its tree:

```python
data = files.scan_cwd()
files.print_tree(data)
```

To find an item by its ID:

```python
item = files.find_item_by_id(101, data)
print(item)
```

To count the number of files, directories, and total items:

```python
num_files = files.count_files(data)
num_dirs = files.count_dirs(data)
total = files.count_all(data)
print(f"Files: {num_files}, Directories: {num_dirs}, Total: {total}")
```

## Requirements

- Python 3.6 or higher
- `os` and `mimetypes` modules (included in the standard Python library)

## License

This project is licensed under the Gnu v3 License.
