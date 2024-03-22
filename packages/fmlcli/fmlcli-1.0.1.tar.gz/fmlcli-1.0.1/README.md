# Command-line magnet search tool

This is a powerful command-line utility that enables users to seamlessly query databases using command-like formats, efficiently retrieving the desired outcomes.

## Getting Started

To get started with this project, follow these steps:

### Prerequisites

- Python (v3.9 or higher)

### Installation

1. Installing the Python package dependencies:

``` shell
pip install glitter-sdk 
pip install rich
pip install argparse
```

2. Installing the command-line tool:

``` shell
pip install fmlcli
```

### Usage

. `-f <filename>` or `--file <filename>`:Specifies the filename to be processed. The -f or --file option is must 

`-n <number>` or `--number <number>`:Specifies the number of results to display. This is an optional parameter with a default value of 10.

For example:I would like to conduct a search for a file named "Freelance" and subsequently present the top five search results.

```shell
fml -f Freelance -n 5
```

## Built With

- [glitter-sdk-py](https://github.com/glitternetwork/glitter-sdk-py) a blockchain-based data platform to help applications store, manage and elevate the world’s data in Web3 way.

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.