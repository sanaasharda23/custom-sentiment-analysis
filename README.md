# VADER Sentiment Analysis with Custom Word Refinement

## Overview
This project performs sentiment analysis on a dataset of reviews using the **VADER Sentiment Analyzer**. 
The model is enhanced with custom keyword-based classification rules for **positive**, **neutral**, and **negative** sentiments to improve accuracy. 

### Features:
- Uses VADER to classify reviews based on their sentiment.
- Implements **custom word-based rules** to refine sentiment predictions.
- Provides an easy-to-use interface for processing large datasets of reviews.
- Calculates **accuracy** by comparing the predictions with manually labeled sentiments.

---

## Steps Followed:

1. **Dataset Preparation**:
   - The dataset is loaded, and reviews are cleaned by removing stopwords, punctuation, and unnecessary characters.
   
2. **Text Cleaning and Tokenization**:
   - Each review is tokenized, and stopwords are removed. A cleaned version of the text is stored in a `Cleaned_Text` column.

3. **VADER Sentiment Analysis**:
   - Each review is analyzed using the **VADER Sentiment Analyzer**.
   - Sentiments are classified as **positive**, **neutral**, or **negative** based on VADER's compound score.

4. **Custom Keyword-Based Refinement**:
   - Reviews are further classified based on the presence of **positive**, **neutral**, and **negative** keywords.
   - The custom keywords override VADER’s prediction when applicable, improving classification accuracy.

5. **Accuracy Calculation**:
   - The accuracy of the sentiment analysis is calculated by comparing the model's predictions with manually labeled sentiments.
   - Achieved accuracy: **71.11%**.

---

## Project Structure

- `mockdata.csv`: The dataset containing reviews, manual predictions, and model predictions.
- `data_processing.py`: Main script containing the functions for cleaning the text, performing VADER sentiment analysis, and refining results with keyword-based rules.

---

## Usage Instructions

### 1. Install Dependencies
Make sure to install the required libraries before running the project:
```bash
pip install vaderSentiment
