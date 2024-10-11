# Write a python program to implement Lemmatization using NLTK

# 1. Stem:
# Definition: The process of reducing a word to its base or root form, often by removing suffixes or prefixes (e.g., "running" → "run").
# Purpose: Helps in normalizing words to improve text analysis by treating different forms of a word as equivalent.
# 2. Tokenize:
# Definition: The act of splitting a text into smaller units, such as words, phrases, or sentences.
# Purpose: Facilitates the analysis of text by breaking it down into manageable pieces for further processing.
# 3. WordNet:
# Definition: A large lexical database of English that groups words into sets of synonyms called synsets, providing definitions and relationships.
# Purpose: Aids in various NLP tasks like semantic analysis, lemmatization, and understanding word meanings and relationships.
# 4. Punkt:
# Definition: A pre-trained tokenizer model used for sentence segmentation.
# Purpose: Helps to accurately split text into sentences, taking into account punctuation and common sentence-ending patterns, improving the quality of text processing.


import nltk  # Importing the Natural Language Toolkit (NLTK) library for NLP tasks
from nltk.stem import WordNetLemmatizer  # Importing the WordNet Lemmatizer to reduce words to their base form
from nltk.tokenize import word_tokenize  # Importing the word_tokenize function to split sentences into words

# Download necessary resources from NLTK
nltk.download('wordnet')  # Downloads the WordNet lexical database, needed for lemmatization
nltk.download('punkt')  # Downloads the Punkt tokenizer model for sentence tokenization

# Initialize the WordNet Lemmatizer
lemmatizer = WordNetLemmatizer()  # Creating an instance of the WordNet Lemmatizer to use for lemmatization

# Example sentence
sentence = input("Enter sentence : ")  # Prompting the user to input a sentence

# Tokenize the sentence into words
words = word_tokenize(sentence)  # Splitting the sentence into individual words
print("Tokenized Words : ",words)

# Lemmatize each word and print the results
lemmatized_words = []  
for word in words:
    # Applying lemmatization to each word in the list
    l = lemmatizer.lemmatize(word)
    lemmatized_words.append(l)


print("\n\n Lemmatized words : ",lemmatized_words)

# Making sentence using lemmatized words 
l_str = ""
for word in lemmatized_words:
    l_str = l_str + word + ' '

print(f"Original sentence: {sentence}")  # Displaying the original input sentence
print(f"Lemmatized sentence: {l_str}")  # Displaying the lemmatized version of the sentence
