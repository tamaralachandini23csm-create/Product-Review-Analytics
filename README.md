# Product Review Analytics and Rating Aggregation

## 1. Project Description

This project analyses Amazon customer product reviews using Apache Hadoop MapReduce and Machine Learning.

It extracts useful insights from customer reviews, calculates product ratings, identifies popular products, analyses categories, and performs sentiment classification.

## 2. Technologies Used

- Apache Hadoop 3.3.6
- HDFS
- Java
- Python 3
- Pandas
- Scikit-learn
- TF-IDF
- Ubuntu Linux
- Git and GitHub

## 3. Dataset Details

**Dataset Name:** Consumer Reviews of Amazon Products

**Source Platform:** Kaggle – Datafiniti

**Dataset Link:**
https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products

The raw dataset is not included in this repository. Download `1429_1.csv` and place it inside `dataset/raw/`.

## 4. Project Objectives

1. Calculate average ratings for each product.
2. Identify the most-reviewed products.
3. Calculate category-wise review counts.
4. Analyse rating distribution from 1 to 5 stars.
5. Classify customer reviews as Positive or Negative using Machine Learning.

## 5. Hadoop MapReduce Implementation

Four MapReduce programs are implemented:

| Program | Description |
|---|---|
| ProductAverage | Calculates average rating for each product |
| MostReviewed | Counts reviews for each product |
| CategoryCount | Calculates review counts for individual categories |
| RatingDistribution | Counts reviews for each star rating |

The processed dataset is stored in HDFS, and the MapReduce results are generated in HDFS output directories.

## 6. Machine Learning – Sentiment Analysis

Sentiment Analysis is implemented using Python and Scikit-learn.

### Sentiment Classification

Customer ratings are converted into sentiment labels:

- Ratings 4 and 5: Positive
- Ratings 1 and 2: Negative
- Rating 3: Neutral (excluded from binary classification)

### Feature Extraction

TF-IDF (Term Frequency-Inverse Document Frequency) converts customer review text into numerical features.

### ML Models Used

Three Machine Learning models are trained and compared:

1. Multinomial Naive Bayes
2. Logistic Regression
3. Linear Support Vector Machine (Linear SVM)

### Model Performance

| ML Model | Test Accuracy |
|---|---:|
| Naive Bayes | Approximately 97.55% |
| Logistic Regression | 97.62% |
| Linear SVM | **97.96%** |

**Best Performing Model: Linear SVM**

**Best Accuracy: 97.96%**

The accuracy is measured on the test dataset. The dataset contains substantially more positive reviews than negative reviews, so accuracy alone does not fully describe model performance. Negative-review recall was 26% for Linear SVM.

## 7. Machine Learning Execution Steps

### Step 1: Create virtual environment

```bash
python3 -m venv ml_env
```

### Step 2: Activate virtual environment

```bash
source ml_env/bin/activate
```

### Step 3: Install required libraries

```bash
pip install pandas scikit-learn
```

### Step 4: Run sentiment analysis

```bash
python sentiment_analysis.py
```

The program trains all three models, compares their performance, and saves the best-performing model and TF-IDF vectorizer.

## 8. Project Structure

```text
Product-Review-Analytics/
│
├── dataset/
│   ├── raw/
│   └── processed_reviews.tsv
│
├── src/
│   ├── ProductAverage.java
│   ├── MostReviewed.java
│   ├── CategoryCount.java
│   └── RatingDistribution.java
│
├── preprocess.py
├── sentiment_analysis.py
├── README.md
└── .gitignore
```

## 9. Results

The project successfully performs:

- Product-wise average rating calculation.
- Most-reviewed product identification.
- Category-wise review analysis.
- Star rating distribution analysis.
- Customer review sentiment classification.

The Linear SVM model achieved the highest test accuracy of 97.96% among the three evaluated ML models.

## 10. Execution Environment

HDFS is used for storing processed data and MapReduce results. Hadoop MapReduce jobs run in Local Mode on a single computer.

Machine Learning sentiment analysis is performed separately using Python and Scikit-learn.

## 11. Conclusion

This project combines Big Data processing and Machine Learning to analyse Amazon customer reviews.

Hadoop MapReduce performs large-scale review aggregation, while Machine Learning identifies customer sentiment. The combination provides useful insights into product ratings, customer preferences, and review patterns.
