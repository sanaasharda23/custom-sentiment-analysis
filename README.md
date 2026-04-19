# Custom VADER Sentiment Analysis with Keyword Refinement

## Overview
This project performs sentiment analysis on financial review data using the 
VADER Sentiment Analyzer, enhanced with custom keyword-based classification 
rules to improve accuracy on domain-specific financial text.

Built during an internship at Ernst & Young (EY) in the CNS Risk Process & 
Controls function, this tool was used to analyze financial data and generate 
actionable insights for business stakeholders.

## Results
- Achieved 71.11% accuracy on labeled financial review data
- Improved over baseline VADER by adding domain-specific keyword refinement rules
- Outputs used to support stakeholder reporting and business decision-making

## How It Works

1. Dataset Preparation: Reviews are loaded and cleaned by removing stopwords, 
   punctuation, and unnecessary characters
2. Text Cleaning and Tokenization: Each review is tokenized and stored in a 
   Cleaned_Text column
3. VADER Sentiment Analysis: Reviews classified as positive, neutral, or negative 
   based on VADER compound score
4. Custom Keyword Refinement: Domain-specific keywords override VADER predictions 
   where applicable, improving accuracy on financial text
5. Accuracy Evaluation: Model predictions compared against manually labeled sentiments

## Project Structure
- data_processing.py: Main script for text cleaning, VADER analysis, and keyword refinement
- mockdata.csv / mockdata.xlsx: Dataset with reviews, manual labels, and model predictions

## Installation
pip install vaderSentiment pandas nltk

## Why This Matters
Standard NLP sentiment models underperform on financial text due to domain-specific 
language. This project explores how custom rule-based refinements can improve model 
accuracy in specialized domains — relevant to AI systems operating in high-stakes contexts.

## Tech Stack
Python, VADER, NLTK, Pandas
