# PyTools_QOL
Python tools that I use for quality of life programming

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/MicahBest/PyTools_QOL/.github%2Fworkflows%2FPyTools_QOL.yml?logo=github)
[![Downloads](https://static.pepy.tech/badge/PyTools_QOL)](https://pepy.tech/project/PyTools_QOL)

## Installation Instructions
Package information and installation instructions can be found on [PyPI](https://pypi.org/project/PyTools-QOL/).

To install package:
```bash
pip install PyTools-QOL
```

## Features and Capabilities

### Program Execution Time:
Example usage:
```python
import time
from PyTools_QOL import print_execution_time

def main():
    time.sleep(3) # waits for 3 seconds

if __name__ == "__main__":
    main()
    print_execution_time() # > Program executed in 3 seconds.
```
