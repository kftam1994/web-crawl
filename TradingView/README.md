Source of Dataset: https://huggingface.co/datasets/DiljitSingh14/tradingIdeas2.0

# TradingView Ideas Dataset

This dataset contains trading ideas and analysis sourced from TradingView, split into training and testing datasets for machine learning purposes. It includes both image data (chart screenshots) and associated textual descriptions.

This repository contains a dataset extracted from TradingView's public "Ideas" section. It includes financial trading ideas and analysis submitted by users, along with associated metadata and chart images. The dataset is intended for research and development in financial analysis and machine learning.

## Dataset Structure

### Root Folder Contents

- `train.zip`: Compressed folder containing training data (images and JSON split).
- `test.zip`: Compressed folder containing testing data (images and JSON split).
- `metadata.csv`: A metadata file linking image filenames to their respective textual descriptions and features.

### Metadata Structure

The `metadata.csv` file contains two columns:

- `file_name`: The image filename (e.g., `18115109.png`).
- `additional_feature`: A text description combining various features from the original dataset.

Example:

```csv
file_name,additional_feature
18115109.png,"STOCK IN MOMENTUM...\nNSE:SUNDARMFIN trade at 4880 level..."
```

## Dataset Contents

The dataset includes:

1. **JSON Metadata Files**:

- Each idea is saved as a JSON file containing key metadata such as:
- `id`: Unique identifier for the idea.
- `name`: Title of the idea.
- `description`: Description of the trading idea.
- `created_at`: Timestamp of when the idea was created.
- `chart_url`: URL to the idea's chart on TradingView.
- `symbol`: Associated trading symbol (e.g., BINANCE:XRPUSDT).
- `user`: Information about the author (e.g., username, pro plan).
- `likes_count`: Number of likes the idea has received.

2. **Chart Images**:

- PNG images representing the charts associated with each idea.

## Usage

### Accessing the Data

1. Clone the repository using:

```bash
git clone <repository-url>
```

2. Navigate to the dataset directory:

```bash
cd tradingview_data
```

### File Structure

- `tradingview_data/`
- JSON files for each idea (e.g., `18116179.json`)
- PNG chart images (e.g., `18116179.png`)

### Example JSON Structure

Here is an example of the data structure for an idea:

```json
{
  "id": 18116179,
  "name": "XRP What will happen in the future?",
  "description": "The price has formed a bullish flag on the daily time frame...",
  "created_at": "2025-01-01T11:42:56+00:00",
  "chart_url": "https://www.tradingview.com/chart/XRPUSDT/DXOM2VxN-XRP-What-will-happen-in-the-future/",
  "symbol": "BINANCE:XRPUSDT",
  "user": {
    "id": 10426253,
    "username": "CobraVanguard",
    "pro_plan": "pro_premium"
  },
  "likes_count": 72
}
```

## How the Data Was Collected

The dataset was generated using the following steps:

1. Fetched data from TradingView's ideas page using a custom Python script.
2. Extracted relevant metadata and saved it in JSON format.
3. Downloaded chart images associated with each idea.
4. Uploaded the processed data to this repository.

For more details, refer to the `tradingview_data_extraction.py` script in this repository.

## Applications

This dataset can be used for:

- Training machine learning models for financial analysis.
- Natural language processing on trading descriptions and comments.
- Image analysis of trading charts.
- Developing automated trading strategies or tools.

## License

This dataset is for research purposes only. Please adhere to TradingView's terms of service and policies when using the data.

## Acknowledgments

Data sourced from [TradingView](https://www.tradingview.com/). Special thanks to the contributors and users sharing their trading ideas.
