# Candlestick Pattern Analysis 

## Table of Contents

- [Candlestick Pattern Analysis](#candlestick-pattern-analysis)
  - [Table of Contents](#table-of-contents)
  - [About ](#about-)
  - [Getting Started ](#getting-started-)
  - [Usage ](#usage-)

## About <a name = "about"></a>

Analysis on how different candlestick patterns affect the stock price and how
they differ in their prediction of the same.


## Getting Started <a name = "getting_started"></a>

Firstly, clone the repo

```bash
cd candlestick-pattern-analysis
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage <a name = "usage"></a>

`data/main_csv` - contains of the main csv file with all the stocks identified by a stockid

`data/separated_stocks` - contains all the stocks in the main csv but separated into their own csv files

`data/cleaned_stocks` - contains the csv files in a format which can directly be fed into the `notebooks/add_candlestick_patterns.ipynb.ipynb`

`data/with_patterns` - contains the data with a few patterns

