"""
Generator module

This module handles the processing of word lists and the generation
of vocabulary data using OpenAI's API.
"""

from typing import List, Dict, Optional
from .models import VocabularyEntry
from .utils import initialize_openai_client


def generate_vocabulary_data(word: str) -> Optional[VocabularyEntry]:
    """
    Generate detailed vocabulary data for a given word using OpenAI API.
    
    Args:
        word (str): The word to generate data for
    
    Returns:
        Optional[VocabularyEntry]: Completed vocabulary entry or None
    """
    client = initialize_openai_client()
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
