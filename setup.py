from setuptools import setup, find_packages


setup(
    name="mindsight-sampler",
    version="0.1",
    description="Mindsight Stack Sample Collector",
    url="https://github.com/MindsightCo/python-sampler",
    license="Apache 2.0",
    packages=find_packages(),
    install_requires=["requests"]
)
