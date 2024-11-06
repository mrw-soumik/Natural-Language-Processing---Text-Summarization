
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import sys

def load_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def preprocess_text(text):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)
    freq_table = dict()
    for word in words:
        word = word.lower()
        if word not in stop_words:
            if word in freq_table:
                freq_table[word] += 1
            else:
                freq_table[word] = 1
    return freq_table

def score_sentences(sentences, freq_table):
    sentence_scores = dict()
    for sentence in sentences:
        word_count = len(word_tokenize(sentence))
        for word in freq_table:
            if word in sentence.lower():
                if sentence in sentence_scores:
                    sentence_scores[sentence] += freq_table[word]
                else:
                    sentence_scores[sentence] = freq_table[word]
        sentence_scores[sentence] = sentence_scores[sentence] / word_count
    return sentence_scores

def summarize_text(file_path):
    text = load_text(file_path)
    sentences = sent_tokenize(text)
    freq_table = preprocess_text(text)
    sentence_scores = score_sentences(sentences, freq_table)
    summary = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:3]
    return " ".join(summary)

if __name__ == "__main__":
    input_file = sys.argv[2] if len(sys.argv) > 2 else 'data/sample.txt'
    summary = summarize_text(input_file)
    print("Summary:\n", summary)
