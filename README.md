This project is a Python script that uses OpenAI GPT-4 to automatically label news articles as positive (olumlu) or negative (olumsuz). It scans a directory of text files, sends each file's content to GPT-4 for sentiment analysis, and outputs the results to an Excel file.

The project is designed for quick labeling of large amounts of news data for analysis or research purposes.

Features

Automatic sentiment labeling using GPT-4

Processes multiple .txt news files in a directory

Handles rate limits gracefully with retries

Outputs results to an Excel file (news_labels.xlsx)
