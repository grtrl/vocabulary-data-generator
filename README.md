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

https://github.com/user-attachments/assets/7199003a-c1b0-4af6-b2a2-17a865819c2a

---


## Getting Started

### Prerequisites

- **OpenAI API Key**: You’ll need an API key from OpenAI to use this application.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/grtrl/vocabulary-data-generator.git
   cd vocabulary-data-generator

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Create a .env file in the root directory with your OpenAI API key:
   ```bash
   OPENAI_API_KEY=your_openai_api_key

5. Add your list of words to data/list_of_words.txt, one word per line.

---

### Usage
1. Run the application:
   ```bash
   python main.py

### Data
 * Input File: data/list_of_words.txt
 * Output File: data/vocabulary_data.json

The output file will contain a structured JSON array of vocabulary entries.

---

### License
This project is licensed under the MIT License.
