# AI-Powered Customer Complaint Classification System

## Project Overview

The **AI-Powered Customer Complaint Classification System** is a Machine Learning project designed to automatically identify customer complaints and classify them into the appropriate categories.

The main objective is to reduce manual complaint handling and help businesses route customer complaints to the correct departments.

The system uses Natural Language Processing (NLP) and Machine Learning to understand complaint text and predict its category.

## Problem Statement

Businesses receive many customer complaints every day. Manually reading, identifying, and forwarding each complaint to the correct department can be time-consuming.

This project provides an automated solution that identifies complaint categories and helps direct them to the responsible departments.

## Project Objectives

- Automatically recognize customer complaints.
- Classify complaints into appropriate categories.
- Reduce manual complaint sorting.
- Help businesses route complaints efficiently.
- Provide a foundation for an automated complaint management system.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Dataset handling |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | Machine Learning |
| TF-IDF | Text feature extraction |
| Logistic Regression | Complaint classification |
| Joblib | Saving and loading the trained model |
| FastAPI | Backend API (planned) |

## Dataset Information

The project uses a customer complaint dataset containing two main columns:

- `complaint`: Customer complaint text.
- `category`: Correct complaint category.

### Complaint Categories

1. Billing
2. Delivery
3. Technical Support
4. Product / Refund

## Machine Learning Workflow

1. Import required libraries.
2. Load the complaint dataset.
3. Perform Exploratory Data Analysis (EDA).
4. Check missing values and duplicate records.
5. Analyze complaint categories and text lengths.
6. Separate input features (X) and target labels (y).
7. Split data into training and testing sets.
8. Convert complaint text into numerical features using TF-IDF.
9. Train the Logistic Regression model.
10. Predict categories for new complaints.
11. Evaluate the model using accuracy, precision, recall, F1-score, and confusion matrix.

## Model Architecture

**TF-IDF + Logistic Regression**

- TF-IDF converts complaint text into numerical features.
- Logistic Regression learns patterns from the training data.
- The trained model predicts the category of new complaints.

## Example Prediction

**Input:**

"My bank charged me twice for my order."

**Predicted Category:**

Billing

**Department Routing:**

Billing Department

## Model Evaluation

The model is evaluated using:

- Accuracy Score
- Precision
- Recall
- F1-Score
- Confusion Matrix

Note: The dataset is synthetic, so high evaluation scores should not be interpreted as guaranteed performance on real-world customer complaints.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/customer-complaint-classification.git
```

### 2. Open the project folder

```bash
cd customer-complaint-classification
```

### 3. Install required libraries

```bash
pip install numpy pandas matplotlib seaborn scikit-learn joblib
```

### 4. Run the project

Open the notebook or Python file in VS Code or Jupyter Notebook and execute the cells.

## Future Improvements

- Develop a web interface for submitting complaints.
- Integrate FastAPI for backend services.
- Add a second Machine Learning model for comparison.
- Improve performance using a larger, real-world dataset.
- Automatically route complaints to the appropriate departments.
- Add confidence scores and manual review for uncertain predictions.

## Project Purpose

This project demonstrates how Machine Learning and Natural Language Processing can be used to automate customer complaint classification and support efficient complaint management.

---

**Project Type:** Machine Learning / NLP  
**Domain:** Artificial Intelligence  
**Language:** Python  
**Task:** Multi-Class Text Classification
