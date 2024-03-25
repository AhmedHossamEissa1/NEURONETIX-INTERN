from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords




# Function to count word frequencies
def count_word_frequencies(file_path):
    # Read the file
    with open(file_path, 'r') as file:
        text = file.read().lower()  # Convert text to lowercase

    # Tokenize the text
    words = word_tokenize(text)

    # Filter out punctuation marks
    words = [word for word in words if word.isalnum()]

    # Filter out stop words
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    # Count word frequencies
    word_counts = Counter(words)

    # Sort word frequencies in descending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    return sorted_word_counts


file_path = "test.txt"

# Count word frequencies
word_frequencies = count_word_frequencies(file_path)

# Output word frequencies
for word, frequency in word_frequencies:
    print(f"{word}: {frequency}")


