## Problem Statement:
- **Sophisticated language models** like OpenAI's GPT series, Falcon etc have blurred the lines between human-written and AI-generated text.
- **Distinguishing** between AI and human-generated content has become a complex task with crucial implications:
- **Information Validity**: AI-generated text may not always offer accurate or reliable information.
- **Authenticity**: Textual content is often used to gauge the knowledge, opinions, and expertise of its author. AI-generated content obscures such assessments.
- **Accountability**: In contexts where content can have serious consequences (e.g., news articles, legal documents), it's vital to identify its origin.

# TypeTruth
TypeTruth is a Python library that detects whether a text is written by a human or AI. Ideal for fact-checking and content validation in the age of AI content generators. It offers AI Content Detection at Paragraph Level as well as Sentence Level. The solution also provides visualizations to better understand the detection results, such as bar plots and heat maps.

# Sample Output:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/bhaskatripathi/TypeTruth/blob/main/TypeTruth_Collab_Notebook.ipynb)

### Paragraph Level:
![image](https://github.com/bhaskatripathi/TypeTruth/assets/35177508/981cc67d-6973-46ad-acdf-acc6d33fc4fc)
### Sentence Level:
![image](https://github.com/bhaskatripathi/TypeTruth/assets/35177508/3b95ab61-dfdd-4b73-89b0-fa6290c55b25)

# UML
I am going to update the code to work with [Falcon](https://huggingface.co/spaces/HuggingFaceH4/falcon-chat), so you see the sequence diagram for Falcon.

![UML Diagram](https://raw.githubusercontent.com/bhaskatripathi/TypeTruth/main/diagram.svg)

# Free Usage using Bearer Key
## Bearer Key

Either you can use your own OpenAI key or you can use a bearer key available for free. To obtain a bearer key, follow this procedure:

1. Open [this URL](https://platform.openai.com/ai-text-classifier) in your browser.
2. Right-click and select "Inspect" to open the developer tools.
3. Click on the "Network" tab.
4. Look for a POST request under the "Name" column in the list that appears. It should be related to "completions".
5. Click on the POST request and find the "Authorization" section under the "Headers" tab.
6. The bearer key is located in the "Authorization" section and it begins with the word "Bearer", as described in the image below.
![image](https://github.com/bhaskatripathi/TypeTruth/assets/35177508/9aa86989-0ea3-4d9b-a5be-43c5f0c5eea0)

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
# Star
Note: Please star this project if you find it useful.

