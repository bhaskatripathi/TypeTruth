## Problem Statement:
- **Sophisticated language models** like OpenAI's GPT series, Falcon etc have blurred the lines between human-written and AI-generated text.
- **Distinguishing** between AI and human-generated content has become a complex task with crucial implications:
- **Information Validity**: AI-generated text may not always offer accurate or reliable information.
- **Authenticity**: Textual content is often used to gauge the knowledge, opinions, and expertise of its author. AI-generated content obscures such assessments.
- **Accountability**: In contexts where content can have serious consequences (e.g., news articles, legal documents), it's vital to identify its origin.

# TypeTruth
TypeTruth is a Python library that detects whether a text is written by a human or AI. Ideal for fact-checking and content validation in the age of AI content generators. It offers AI Content Detection at Paragraph Level as well as Sentence Level. The solution also provides visualizations to better understand the detection results, such as bar plots and heat maps.

# Sample Output:
### Paragraph Level:
![image](https://github.com/bhaskatripathi/TypeTruth/assets/35177508/981cc67d-6973-46ad-acdf-acc6d33fc4fc)
### Sentence Level:
![image](https://github.com/bhaskatripathi/TypeTruth/assets/35177508/3b95ab61-dfdd-4b73-89b0-fa6290c55b25)

## Usage

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/bhaskatripathi/TypeTruth/blob/main/TypeTruth_Collab_Notebook.ipynb)


# Directory Structure
```
ai_text_detector/
|--- ai_text_detector/
|    |--- __init__.py
|    |--- ai_detector.py
|    |--- plotting.py
|--- setup.py
|--- TypeTruth_Collab_Notebook.ipynb
|--- README.md
|--- LICENSE.txt
```


