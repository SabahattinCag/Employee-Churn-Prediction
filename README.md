# Employee Churn Analysis Project

## Overview

### What is Employee Churn?
Employee churn refers to the phenomenon where employees leave an organization voluntarily. This project aims to predict which employees are likely to churn based on various features provided in the HR dataset.

### Exploratory Data Analysis (EDA) and Visualization
Before jumping into model building, I will conduct EDA and visualize the employee churn dataset using Matplotlib and Seaborn. This process involves understanding the data structure, identifying outliers, handling missing values, and exploring features that influence the target variable.

### Model Building and Evaluation
The core of the project involves implementing classification techniques in Python. Utilizing Scikit-Learn, I will apply Distance-Based, Bagging, and Boosting algorithms for making predictions. For Deep Learning enthusiasts, Tensorflow-Keras will be used to create and evaluate neural network models.

### Deployment with Streamlit
Upon successfully building and evaluating my models, I will have the opportunity to deploy my predictive model using Streamlit, a powerful tool for creating interactive web applications.

## Project Structure

### Determines

#### HR Dataset
The dataset consists of HR data with 14,999 samples, containing two types of employees: those who stayed and those who left the company.

**Attributes:**
1. satisfaction_level: Employee satisfaction ranging from 0 to 1.
2. last_evaluation: Performance evaluated by the employer (0 to 1).
3. number_projects: Number of projects assigned to an employee.
4. average_monthly_hours: Average monthly working hours.
5. time_spent_company: Employee experience in years.
6. work_accident: Whether an employee had a work accident.
7. promotion_last_5years: Promotion status in the last 5 years.
8. Departments: Employee's working department/division.
9. Salary: Employee's salary level (low, medium, high).
10. left: Employee's departure status (1 if left, 0 if stayed).

### Project Tasks

1. **Conduct Exploratory Data Analysis (EDA) and visualize the dataset.**
2. **Perform data pre-processing operations such as Scaling and Encoding.**
3. **Implement Cluster Analysis based on EDA findings.**
4. **Split the data into train and test sets.**
5. **Build and train classification models using Scikit-Learn and Tensorflow-Keras.**
6. **Evaluate model performance using classification metrics.**
7. **Deploy the model using Streamlit.**

## Prerequisites

Before diving into the project, ensure that you have a basic understanding of Python coding, model deployment, and familiarity with Distance-Based, Bagging, Boosting algorithms, and Confusion Matrices. Feel free to explore additional models and methods to enhance your model metrics.

Let's embark on this exciting journey of Employee Churn Analysis!
