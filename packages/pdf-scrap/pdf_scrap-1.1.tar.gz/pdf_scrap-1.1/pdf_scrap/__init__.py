import PyPDF2
import re
from collections import Counter
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk

# Download NLTK stopwords list (run once)
nltk.download('stopwords')

def get_keywords(pdf_path, num_keywords=5):
    keywords = []

    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Initialize a list to store all words in the document
        all_words = []

        # Iterate through each page
        for page_num in range(len(pdf_reader.pages)):
            # Get the page
            page = pdf_reader.pages[page_num]

            # Extract text from the page
            text = page.extract_text()

            # Tokenize text into words (using regex for word boundaries)
            words = re.findall(r'\b\w+\b', text.lower())

            # Remove stopwords and words with length <= 3
            stop_words = set(stopwords.words('english'))
            words = [word for word in words if word not in stop_words and len(word) > 3]

            # Add remaining words to the list
            all_words.extend(words)

        # Convert the list of words into a single string
        document_text = ' '.join(all_words)

        # Calculate TF-IDF values
        tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix = tfidf_vectorizer.fit_transform([document_text])

        # Get feature names (words)
        feature_names = tfidf_vectorizer.get_feature_names_out()

        # Convert TF-IDF matrix to a list of tuples (word, TF-IDF value)
        tfidf_values = [(feature_names[idx], value) for idx, value in enumerate(tfidf_matrix.toarray()[0])]

        # Sort by TF-IDF value in descending order
        tfidf_values.sort(key=lambda x: x[1], reverse=True)

        # Extract the top keywords
        top_keywords = tfidf_values[:num_keywords]

        # Extract only the keywords (without TF-IDF values)
        keywords = [keyword for keyword, _ in top_keywords]

    return keywords

# Example usage:
# pdf_path = "C:/Users/satya/Downloads/PoorweeeeResume.pdf"
# top_keywords = get_keywords(pdf_path, num_keywords=5)
# print("Top Keywords:", top_keywords)
