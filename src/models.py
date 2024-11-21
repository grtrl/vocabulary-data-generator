"""
Models module

This module defines the data models used in the Vocabulary Data Generator.
"""

from pydantic import BaseModel, Field


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
