[![PyPI version](https://badge.fury.io/py/chromefetcher.svg)](https://badge.fury.io/py/chromefetcher)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/chromefetcher)](https://pepy.tech/project/chromefetcher)

# ChromeFetcher

`ChromeFetcher` automates the process of fetching Chrome or ChromeDriver based on the operating system and architecture. It simplifies the task of downloading the appropriate version for your system.

## Installation

To install `ChromeFetcher`, use pip:

```bash
pip install ChromeFetcher
```

## Usage

Easily download ChromeDriver with:

```python
from ChromeFetcher import fetch_chrome

fetch_chrome(product='chromedriver')
```

Specify `product` as `'chrome'` or `'chromedriver'` to download. Options allow unzipping and cleanup post-download.

## Features

- Automatically fetches Chrome or ChromeDriver.
- Supports different OS and architectures.
- Unzips and cleans up downloads optionally.

## Contributing

Contributions, issues, and feature requests are welcome! Check our [issues page](https://github.com/chigwell/ChromeFetcher/issues).

## License

Licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
