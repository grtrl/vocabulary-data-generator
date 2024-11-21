"""
Vocabulary Data Generator

This script processes a list of words and uses OpenAI's API to generate
detailed vocabulary data. Outputs are saved in JSON format.
"""

import json
from src.generator import process_word_list


def main():
    """
    Main execution function to generate and save vocabulary data.
    """
    # Configuration
    INPUT_FILENAME = 'data/list_of_words.txt'
    OUTPUT_FILENAME = 'data/vocabulary_data.json'

    # Generate vocabulary data
    vocabulary_data = process_word_list(INPUT_FILENAME)

    # Save to JSON file
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as outfile:
        json.dump(vocabulary_data, outfile, ensure_ascii=False, indent=2)

    print(f"Vocabulary data saved to {OUTPUT_FILENAME}")


if __name__ == "__main__":
    main()
