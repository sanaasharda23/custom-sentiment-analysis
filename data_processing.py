import csv
import string
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# Load the CSV file
file_path = 'mockdata.csv'
with open(file_path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)



# Defined a list of common English stopwords
stop_words_manual = {
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've",
    "you'll", "you'd",
    'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her',
    'hers',
    'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
    'what', 'which',
    'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were',
    'be', 'been',
    'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and',
    'but',
    'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about',
    'against',
    'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up',
    'down',
    'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there',
    'when',
    'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some',
    'such',
    'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will',
    'just',
    'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain',
    'aren', "aren't",
    'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't",
    'haven',
    "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't",
    'shan',
    "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't",
    'wouldn', "wouldn't"
}



def clean_text(text):
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove special characters
    text = ''.join(e for e in text if e.isalnum() or e.isspace())
    # Remove stop words
    text = ' '.join(word for word in text.split() if word.lower() not in stop_words_manual)
    return text




cleaned_data = []

with open('mockdata.csv', newline = '', encoding = 'utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cleaned_row = row.copy()
        cleaned_row['Cleaned_Text'] = clean_text(
            row['Text'])
        cleaned_data.append(cleaned_row)

# Save the data with the new Cleaned_Text column
with open('mockdata.csv', 'w', newline = '', encoding = 'utf-8') as csvfile:
    fieldnames = cleaned_data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

    writer.writeheader()
    writer.writerows(cleaned_data)


def convert_to_lowercase(file_path):
    cleaned_data = []

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['Cleaned_Text'] = row['Cleaned_Text'].lower()
            cleaned_data.append(row)

    # Save the modified data
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = cleaned_data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(cleaned_data)

file_path = 'mockdata.csv'
convert_to_lowercase(file_path)


def tokenize_text(file_path):
    tokenized_data = []

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['Tokenized_Text'] = row['Cleaned_Text'].split()
            tokenized_data.append(row)

    # Save the modified data
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = tokenized_data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(tokenized_data)

file_path = 'mockdata.csv'
tokenize_text(file_path)




# Refined word lists based on the cleaned text analysis
positive_words = ['options', 'good', 'exceeded', 'expectations', 'reliability', 'flexible',
                  'design', 'mortgage', 'quicker', 'diverse']
neutral_words = ['mobile', 'app', 'convenient', 'transactions', 'sometimes', 'everyday', 'lags',
                 'peak', 'hours', 'process']
negative_words = ['didnt', 'disappointed', 'poor', 'performance', 'regret', 'choosing', 'meet',
                  'hype', 'live']


# Function to perform sentiment analysis using VADER with refined word lists
def perform_vader_sentiment_analysis_v4(file_path):
    analyzer = SentimentIntensityAnalyzer()

    # Read the CSV file and perform sentiment analysis
    updated_data = []
    with open(file_path, newline = '', encoding = 'utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames + ['Predictions', 'Explanation', 'Match_Manual']

        for row in reader:
            cleaned_text = row['Cleaned_Text'].lower()
            sentiment_dict = analyzer.polarity_scores(cleaned_text)
            compound_score = sentiment_dict['compound']

            # Improved classification based on refined word lists and compound score
            if any(word in cleaned_text for word in negative_words):
                # If any negative words are present, classify as negative
                sentiment = 'Negative'
                explanation = f"Manually classified as Negative due to words in text."
            elif any(word in cleaned_text for word in positive_words):
                # If any positive words are present, classify as positive
                sentiment = 'Positive'
                explanation = f"Manually classified as Positive due to words in text."
            elif any(word in cleaned_text for word in neutral_words):
                # If any neutral words are present, classify as neutral
                sentiment = 'Neutral'
                explanation = f"Manually classified as Neutral due to words in text."
            elif compound_score >= 0.1:
                sentiment = 'Positive'
                explanation = f"Positive because compound score is {compound_score:.4f}"
            elif compound_score <= -0.1:
                sentiment = 'Negative'
                explanation = f"Negative because compound score is {compound_score:.4f}"
            else:
                sentiment = 'Neutral'
                explanation = f"Neutral because compound score is {compound_score:.4f}"

            # Add sentiment and explanation to the row
            row['Predictions'] = sentiment
            row['Explanation'] = explanation

            # Check if manual predictions exist, and compare
            if 'Manually_Predicted' in row:
                match = 'Yes' if row['Manually_Predicted'] == sentiment else 'No'
                row['Match_Manual'] = match
            else:
                row['Match_Manual'] = 'N/A'  # If no manual prediction column is present

            updated_data.append(row)

    # Write the updated data back to the CSV file
    with open(file_path, 'w', newline = '', encoding = 'utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(updated_data)


# Perform sentiment analysis using the refined word lists
file_path = 'mockdata.csv'
perform_vader_sentiment_analysis_v4(file_path)



# Function to calculate accuracy without pandas
def calculate_accuracy_without_pandas(file_path):
    total_reviews = 0
    correct_matches = 0

    # Open the CSV file
    with open(file_path, newline = '', encoding = 'utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        # Loop through each row and compare predictions
        for row in reader:
            total_reviews += 1
            if row['Predictions'] == row['Manually_Predicted']:
                correct_matches += 1

    # Calculate accuracy
    if total_reviews > 0:
        accuracy = (correct_matches / total_reviews) * 100
    else:
        accuracy = 0.0

    return accuracy


# Path to the CSV file
file_path = 'mockdata.csv'
accuracy = calculate_accuracy_without_pandas(file_path)

print(f"Accuracy: {accuracy:.2f}%")
