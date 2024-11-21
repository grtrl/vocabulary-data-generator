"""
Vocabulary Data Generator

This script generates detailed vocabulary data by processing a list of words
and using OpenAI's API to complete linguistic information.
"""

import json
from typing import List, Dict, Optional

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, Field

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI()

class VocabularyEntry(BaseModel):
    """
    Pydantic model defining the structure of a vocabulary entry.
    Includes comprehensive linguistic information for a single word.
    """
    word: str = Field(..., description="The vocabulary word")
    transcription: str = Field(..., description="Phonetic transcription of the word")
    description: str = Field(..., description="Definition of the word in English, 90-100 characters.")
    partOfSpeech: str = Field(..., description="Part of speech")
    category: str = Field(..., description="Category")
    translation_es: str = Field(..., description="Spanish translation, first letter always caps.")
    translation_ru: str = Field(..., description="Russian translation, first letter always caps.")
    translation_de: str = Field(..., description="German translation, first letter always caps.")
    translation_it: str = Field(..., description="Italian translation, first letter always caps.")
    translation_fr: str = Field(..., description="French translation, first letter always caps")
    synonyms: str = Field(..., description="Three synonyms separated by commas")
    phrases: str = Field(..., description="""Three phrases using the word, separated by commas and not numbered""")
    sentence: str = Field(..., description="Sentence using the word, 200-250 characters (not less), with the word appearing at least two times and marked with")
    dialog: str = Field(..., description="""A dialog involving the word, about 300-400 characters (not less), with 2 exchanges per each speaker (4 exchanges at all) and each exchange containing necessary word one time,  each instance of the word marked with **, don't start exchanges marking roles like A:  or B:, each exchange separated by ";".""")

def generate_vocabulary_data(word: str) -> Optional[VocabularyEntry]:
    """
    Generate detailed vocabulary data for a given word using OpenAI API.
    
    Args:
        word (str): The word to generate data for
    
    Returns:
        Optional[VocabularyEntry]: Completed vocabulary entry or None
    """
    try:
        completion = client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Generate comprehensive vocabulary data"},
                {"role": "user", "content": f"Generate detailed entry for the word: {word}"}
            ],
            response_format=VocabularyEntry,
        )
        return completion.choices[0].message.parsed
    except Exception as e:
        print(f"Error processing word {word}: {e}")
        return None

def process_word_list(filename: str) -> List[Dict]:
    """
    Read words from a file and generate vocabulary data.
    
    Args:
        filename (str): Path to the file containing words
    
    Returns:
        List[Dict]: List of processed vocabulary entries
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            words_list = file.read().splitlines()
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []

    updated_data = []
    for seq, word in enumerate(words_list, 1):
        entry = generate_vocabulary_data(word)
        if entry:
            updated_data.append({
                "word": entry.word,
                "seq": seq,
                "transcription": entry.transcription,
                "description": entry.description,
                "partOfSpeech": entry.partOfSpeech,
                "category": entry.category,
                "translation_es": entry.translation_es,
                "translation_ru": entry.translation_ru,
                "translation_de": entry.translation_de,
                "translation_it": entry.translation_it,
                "translation_fr": entry.translation_fr,
                "synonyms": entry.synonyms,
                "phrases": entry.phrases,
                "sentence": entry.sentence,
                "dialog": entry.dialog
            })

    return updated_data

def main():
    """
    Main execution function to generate and save vocabulary data.
    """
    # Configuration
    INPUT_FILENAME = 'list_of_words.txt'
    OUTPUT_FILENAME = 'vocabulary_data.json'

    # Generate vocabulary data
    vocabulary_data = process_word_list(INPUT_FILENAME)

    # Save to JSON file
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as outfile:
        json.dump(vocabulary_data, outfile, ensure_ascii=False, indent=2)

    print(f"Vocabulary data saved to {OUTPUT_FILENAME}")

if __name__ == "__main__":
    main()