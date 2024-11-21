"""
Utils module

This module provides utility functions for the Vocabulary Data Generator.
"""

from dotenv import load_dotenv
from openai import OpenAI


def initialize_openai_client() -> OpenAI:
    """
    Initialize and return the OpenAI client using environment variables.
    
    Returns:
        OpenAI: Initialized OpenAI client
    """
    # Load environment variables from .env
    load_dotenv()
    return OpenAI()
