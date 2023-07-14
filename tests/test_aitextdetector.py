import pytest
from TypeTruth.aitextdetector import AIDetector, ContentGeneratorChecker

def test_aitextdetector():
    # insert the path to your openai_bearer.txt file
    ai_detector = AIDetector("openai_bearer.txt") 
    text = "Here is a sample text to test AI detection."
    result = ai_detector.detect(text, split_type='sentence')
    assert isinstance(result, str) or (isinstance(result, dict) and 'AI-Generated Probability' in result)

def test_contentgeneratorchecker():
    # insert your OpenAI token
    content_checker = ContentGeneratorChecker("<Your OpenAI Token>") 
    text = "Here is a sample text to test AI detection."
    result = content_checker.detect(text)
    assert isinstance(result, str) or (isinstance(result, dict) and 'AI-Generated Probability' in result)
