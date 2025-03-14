## End to End Deep Learning Project

# Customer Churn Prediction using ANN

## Project Overview
This project focuses on predicting customer churn using an Artificial Neural Network (ANN). Churn prediction is essential for businesses to retain customers by identifying those likely to leave.

## Dataset Information
The dataset used in this project is stored in `raw_data.csv`. It contains customer-related features that influence churn behavior.

## Installation & Setup
To run this project, install the necessary dependencies:

```bash
pip install tensorflow pandas numpy scikit-learn matplotlib seaborn
```

Ensure you have Python 3.13 installed, preferably in an Anaconda environment.

## Model Architecture
The ANN consists of:
- Input layer with relevant features
- Hidden layers with activation functions (e.g., ReLU)
- Output layer with a sigmoid activation function for binary classification

## Training Process
- Data preprocessing (handling missing values, encoding categorical data, normalization)
- Splitting the dataset into training and testing sets
- Training the ANN model using TensorFlow/Keras
- Evaluating performance using metrics like accuracy and F1-score

## Evaluation Metrics
- Accuracy
- Precision & Recall
- F1-Score
- ROC-AUC Curve

## Usage
Run the training script to build and evaluate the model:

```bash
python train.py
```


## Future Improvements
- Hyperparameter tuning
- Feature engineering
- Deploying the model using Streamlit

## Contact
Author: Ankit Kumar
Email: kumar06112003@gmail.com


Feel free to contribute and improve the model!

