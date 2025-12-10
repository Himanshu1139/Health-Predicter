#Health-Predictor

**Symptom-Based Disease Prediction System**

A machine learning project that predicts possible diseases based on user-entered symptoms using an SVM (Support Vector Machine) model.
The project focuses on early detection and quick decision-support in healthcare.

📌 **Overview**

This project analyzes user symptoms and predicts the most likely disease using an ML-based classification approach.
It provides a simple, interactive, and accurate prediction system built on structured healthcare symptom data.

🗂️**Dataset**

The dataset includes:

Symptoms list

Disease labels

Symptom–disease mappings

Severity and frequency indicators (if available)

You can add the actual dataset name or link when uploading.

🛠️ **Tech Stack**

Python

Pandas, NumPy

Scikit-learn

Matplotlib

Jupyter Notebook

⚙️ **Project Workflow**
1. Data Preprocessing

Cleaned and structured raw data

Encoded symptoms into numerical vectors

Removed duplicates and inconsistencies

Prepared final training matrix for ML models

2. Exploratory Data Analysis (EDA)

Symptom frequency distribution

Disease occurrence analysis

Correlation patterns

Visualized trends using charts

3. Model Development (SVM)

Used Support Vector Machine (SVM) as the primary algorithm

Tuned hyperparameters (kernel, C, gamma)

Performed train–test splitting

Evaluated with metrics:

Accuracy

Precision

Recall

Confusion Matrix

4. Prediction System

User enters symptoms

Model processes inputs

Predicts the most probable disease

Outputs prediction in a clean, readable format

📊**Results**

SVM model produced strong accuracy for multi-class prediction

Reliable for symptom-based classification

Pattern recognition between symptoms and diseases clearly observed
