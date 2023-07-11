from setuptools import setup, find_packages

setup(
    name='ai_text_detector',
    version='0.0.1',
    url='https://github.com/yourusername/ai_text_detector',
    author='Author Name',
    author_email='author@gmail.com',
    description='A package to detect whether a given text was likely written by a human or AI',
    packages=find_packages(),    
    install_requires=['requests', 'numpy', 'pandas', 'matplotlib', 'seaborn'],
 )
