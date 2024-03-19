# SRME (System Resource Monitoring and Logging Engine)

SRME is a Python library for monitoring and logging system resource usage. It provides utilities for collecting metrics and tracking them using different storage mechanisms like CSV files and MLFlow.

## Installation

You can install SRME via pip:

```bash
pip install srme
```

## Usage

### Basic Usage

```python
from srme import CSVLogger

csv_logger = CSVLogger()
...
# do something
...
csv_logger.end()
```
