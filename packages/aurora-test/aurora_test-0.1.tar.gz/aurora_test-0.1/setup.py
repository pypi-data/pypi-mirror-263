from setuptools import setup, find_packages

setup(
    name="aurora_test",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "aurora = aurora_hash:cli"
        ]
    }
)