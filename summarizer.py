
# Import necessary libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from sentence_transformers import SentenceTransformer, util
import numpy as np

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Define functions for text summarization
def preprocess_text(text):
    stop_words = set(stopwords.words("english"))
    words = nltk.word_tokenize(text)
    freq_table = {}
    for word in words:
        word = word.lower()
        if word not in stop_words:
            if word in freq_table:
                freq_table[word] += 1
            else:
                freq_table[word] = 1
    return freq_table

def score_sentences(sentences, freq_table):
    sentence_scores = {}
    for idx, sentence in enumerate(sentences):
        word_count = len(nltk.word_tokenize(sentence))
        score = 0
        for word in freq_table:
            if word in sentence.lower():
                score += freq_table[word]
        
        # Boost for initial and final sentences
        position_factor = (len(sentences) - idx) / len(sentences)
        sentence_scores[sentence] = score * position_factor / word_count
    return sentence_scores

def summarize_text(text, num_sentences=3, similarity_threshold=0.5):
    sentences = sent_tokenize(text)
    freq_table = preprocess_text(text)
    sentence_scores = score_sentences(sentences, freq_table)
    
    # Sort sentences by score
    sorted_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    
    # Load pre-trained sentence transformer model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(sentences, convert_to_tensor=True)
    
    summary = []
    used_indices = set()

    for idx, sentence in enumerate(sorted_sentences):
        if len(summary) < num_sentences:
            # Check for semantic similarity with previously selected sentences
            sentence_embedding = model.encode(sentence, convert_to_tensor=True)
            is_redundant = any(util.cos_sim(sentence_embedding, embeddings[i]).item() > similarity_threshold for i in used_indices)
            
            if not is_redundant:
                summary.append(sentence)
                used_indices.add(sentences.index(sentence))
    
    return " ".join(summary)

# Define the text to be summarized
text = """
Text summarization is the task of shortening a text document to create a summary that includes the most important information.
It is a common problem in Natural Language Processing (NLP) and can be achieved using extractive or abstractive methods.
Extractive summarization selects sentences directly from the document, while abstractive summarization generates new sentences.
Summarization is especially valuable when dealing with large amounts of text data, making it easier for users to quickly obtain the key points.
For instance, in the context of news articles, summarization can allow readers to stay updated without reading lengthy reports.
The techniques in NLP have grown with advancements in machine learning, enabling better content condensation.
"""

# Generate summary
summary = summarize_text(text, num_sentences=3)
print("Summary:\n", summary)
