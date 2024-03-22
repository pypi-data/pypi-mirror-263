import PyPDF2
import re
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk

def get_keywords(pdf_path, num_keywords=5):
    # Define a fallback set of stopwords
    fallback_stopwords = {'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can', 'did', 'do', 'does', 'doing', 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'has', 'have', 'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'itself', 'just', 'me', 'more', 'most', 'my', 'myself', 'no', 'nor', 'not', 'now', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', 'she', 'should', 'so', 'some', 'such', 'than', 'that', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', 'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'you', 'your', 'yours', 'yourself', 'yourselves'}

    try:
        # Attempt to download NLTK stopwords list
        nltk.download('stopwords')
        stopwords_set = set(nltk.corpus.stopwords.words('english'))
    except Exception as e:
        print("NLTK download failed. Using fallback set of stopwords.")
        stopwords_set = fallback_stopwords

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
            words = [word for word in words if word not in stopwords_set and len(word) > 3]

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
pdf_path = 'example.pdf'
top_keywords = get_keywords(pdf_path, num_keywords=5)
print("Top Keywords:", top_keywords)
