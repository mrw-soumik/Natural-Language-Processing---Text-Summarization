
# Advanced Text Summarization Tool

This is a Python-based text summarization tool designed to condense lengthy documents into concise summaries using advanced techniques in Natural Language Processing (NLP). It leverages both sentence embeddings and frequency-based scoring to select diverse and informative sentences for the summary.

## Objective
The aim of this project is to improve information accessibility by generating quick, effective summaries of news articles, reports, and other documents.

## Key Features
- **Extractive Summarization**: Selects sentences based on word frequency, sentence embeddings, and positional importance.
- **Advanced Redundancy Control**: Uses semantic similarity to ensure selected sentences are diverse and reduce redundancy in the summary.
- **Keyword-Based Scoring**: Sentences containing important keywords are prioritized in the summary.
- **Flexibility**: Adjust the summary length and similarity threshold to control output.

## Technologies
- Python
- [NLTK](https://www.nltk.org/) (Natural Language Toolkit)
- [Sentence-Transformers](https://www.sbert.net/) (for sentence embeddings and semantic similarity)

## Getting Started

### Prerequisites
- Python 3.x
- Required Python libraries can be installed using the `requirements.txt` file.

To install the required libraries, run:
```bash
pip install -r requirements.txt
```

### Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/Advanced-Text-Summarization-Tool.git
    ```
2. Change into the project directory:
    ```bash
    cd Advanced-Text-Summarization-Tool
    ```

### Usage

1. **Prepare the Text**: Define your input text in `data/sample.txt` or modify the script to include your own text.
2. **Run the Summarizer**:
    ```bash
    python summarizer.py
    ```

### Code Overview

- **summarizer.py**: Main code for advanced text summarization, including semantic similarity checks and keyword-based scoring.
- **requirements.txt**: Lists all required Python libraries.
- **data/sample.txt**: A sample text file for testing.

## Example Output

Given an input text, the summarizer generates a concise summary based on word frequency and semantic diversity. For example:

**Input Text**:
```
[Sample text goes here...]
```

**Output Summary**:
```
[Generated summary goes here...]
```

## License
[MIT License](LICENSE)
