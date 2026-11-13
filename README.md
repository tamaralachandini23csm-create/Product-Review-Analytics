# Product Review Analytics and Rating Aggregation

## 1. Project Description

This project uses Apache Hadoop MapReduce to analyse Amazon product reviews.

It processes customer review data and generates useful information about product ratings, review counts, and product categories.

## 2. Technologies Used

- Apache Hadoop 3.3.6
- Java
- Python 3
- HDFS
- MapReduce
- Ubuntu Linux

## 3. Dataset

Dataset: Datafiniti – Consumer Reviews of Amazon Products

Source: https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products

Download the dataset and place `1429_1.csv` inside `dataset/raw/`.

The raw dataset is not included in this repository.

## 4. Project Objectives

1. Calculate average ratings for each product.
2. Identify the most-reviewed products.
3. Calculate category-wise review counts.
4. Analyse the distribution of ratings from 1 to 5 stars.

## 5. Project Structure

```text
Product-Review-Analytics/
├── dataset/
│   ├── raw/
│   └── processed_reviews.tsv
├── src/
│   ├── ProductAverage.java
│   ├── MostReviewed.java
│   ├── CategoryCount.java
│   └── RatingDistribution.java
├── preprocess.py
├── README.md
└── .gitignore
```

## 6. Execution Steps

### Step 1: Preprocess the dataset

```bash
python3 preprocess.py
```

### Step 2: Upload processed data to HDFS

```bash
hdfs dfs -mkdir -p /user/$USER/ProductReviewAnalytics/processed

hdfs dfs -put dataset/processed_reviews.tsv /user/$USER/ProductReviewAnalytics/processed/
```

### Step 3: Compile Java programs

```bash
mkdir -p build

javac -classpath "$(hadoop classpath)" -d build src/*.java

jar -cvf product-review-analytics.jar -C build .
```

### Step 4: Run MapReduce programs

Average rating:

```bash
hadoop jar product-review-analytics.jar ProductAverage /user/$USER/ProductReviewAnalytics/processed/processed_reviews.tsv /user/$USER/ProductReviewAnalytics/output/average_rating
```

Most reviewed products:

```bash
hadoop jar product-review-analytics.jar MostReviewed /user/$USER/ProductReviewAnalytics/processed/processed_reviews.tsv /user/$USER/ProductReviewAnalytics/output/most_reviewed
```

Category-wise review count:

```bash
hadoop jar product-review-analytics.jar CategoryCount /user/$USER/ProductReviewAnalytics/processed/processed_reviews.tsv /user/$USER/ProductReviewAnalytics/output/category_count
```

Rating distribution:

```bash
hadoop jar product-review-analytics.jar RatingDistribution /user/$USER/ProductReviewAnalytics/processed/processed_reviews.tsv /user/$USER/ProductReviewAnalytics/output/rating_distribution
```

## 7. Results

The project successfully generates:

- Average rating and review count for each product.
- Review counts for each product.
- Review counts for individual category labels.
- Number of reviews for each star rating (1–5).

## 8. Execution Environment

HDFS is used for storing the processed dataset and MapReduce results. MapReduce jobs are executed in Hadoop Local Mode on a single computer.

This project demonstrates Hadoop MapReduce programming and HDFS-based data storage.
