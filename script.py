import nltk
from nltk.corpus import stopwords
from collections import Counter
nltk.download('stopwords')
nltk.download('punkt')
with open('random_paragraphs.txt', 'r', encoding='utf-8') as file:
    txt = file.read()
    print(txt)
    words = nltk.word_tokenize(txt)
    stop_words = set(stopwords.words('english'))
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words and word.isalnum()]
    if all(word in stop_words for word in filtered_words):
        print("Stop words are present in the text.")
    else:
        filtered_text = ' '.join(filtered_words)
        print("Stop words were successfully removed.")
        print("Text without stop words:")
    word_freq = Counter(filtered_words)
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")
