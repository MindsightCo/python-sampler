# Mindsight Data Collector: Python
Unobstrusively detects the most common running stacks in your Python program, for use with the Mindsight product.

This utility can be plugged in to your Python application to collect vital data about your code's behavior so that Mindsight can help you write better code more safely.

## Caveats

This utility is not designed to work with web frameworks that utilize multithreading like Django and Flask. If you are using one of those frameworks, use the appropriate data collector:

- [Mindsight Django Collector](https://github.com/MindsightCo/mindsight-django-hotpath)

## Installation

To install this utility for use in your program:

```
pip install mindsight-sampler
```

## Usage

Before proceeding, make sure you have setup your Mindsight account. [Contact us](mailto:eddy@mindsight.io) if you need help.

To use this utility to observe your program and send data to Mindsight:

- First, set up and run the [Mindsight Agent](https://github.com/MindsightCo/hotpath-agent) (the [binary download](https://github.com/MindsightCo/hotpath-agent/releases) is easy and recommended).
  - For the purpose of this example, we will assume your agent is running at `http://localhost:8000`

- Initialize the sampler in your code:

```python
import sampler

sampler.start("http://localhost:8000", "My Project", ["my.module", "my.other_module"], environment="production")
```

Let's explain each parameter:

- `"http://localhost:8000"`
  - URL to your running [Mindsight Agent](https://github.com/MindsightCo/hotpath-agent)
- `"My Project"`
  - The name of your project in your Mindsight account that tracks this application
- `["my.module", "my.other_module"]`
  - The Python modules that you want to have monitored by Mindsight
  - Each element of this array is a prefix, so `["my"]` will watch those 2, plus any others under `my.*`
- `environment="production"`
  - Name of the environment the application is running in
  - This parameter is optional
  - You can name your environments however you like
