# Vocabulary Data Generator

A Python application that processes a list of words and generates detailed vocabulary data using OpenAI's API. This project creates comprehensive entries for each word, including definitions, translations, examples, and more, saving the results in a structured JSON format.

---

## Features

- **Automated Data Generation**: Generates vocabulary entries with detailed linguistic information, including:
  - Phonetic transcription
  - Part of speech
  - Translations in multiple languages
  - Synonyms, phrases, and example sentences
  - A dialogue example
- **Customizable**: Works with any word list you provide.
- **Modular Design**: Structured to facilitate extensions and modifications.

---

## Project Structure
vocabulary-data-generator/
├── README.md
├── .env                  # Environment variables for OpenAI API keys
├── .gitignore            # Files and folders to ignore in Git
├── data/
│   ├── list_of_words.txt # Input file with the list of words to process
│   ├── vocabulary_data.json # Output file containing generated vocabulary data
├── src/
│   ├── __init__.py       # Package initialization
│   ├── generator.py      # Core logic for processing words and generating data
│   ├── models.py         # Pydantic models for data validation
│   ├── utils.py          # Utility functions (e.g., OpenAI client initialization)
├── main.py               # Entry point for the application

---

## Getting Started

### Prerequisites

- **Python**: Version 3.8 or higher
- **OpenAI API Key**: You’ll need an API key from OpenAI to use this application.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/vocabulary-data-generator.git
   cd vocabulary-data-generator

