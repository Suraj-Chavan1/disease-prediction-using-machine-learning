# Disease Prediction Using Machine Learning

This repository contains the implementation of a machine learning system for predicting diseases based on various input features. The project leverages different machine learning algorithms to provide accurate and reliable predictions.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Predicting diseases accurately can significantly enhance early diagnosis and treatment. This project utilizes machine learning techniques to build models that can predict the likelihood of various diseases based on patient data.

## Features

- Data preprocessing and feature engineering
- Implementation of multiple machine learning algorithms
- Model evaluation and comparison
- User-friendly interface for inputting patient data and obtaining predictions

## Project Structure


## Project Images


## Installation
![image](https://github.com/Suraj-Chavan1/disease-prediction-using-machine-learning/assets/113795475/10fbb9c7-7124-48a2-8fd7-6aac22e2e0ed)
![image](https://github.com/Suraj-Chavan1/disease-prediction-using-machine-learning/assets/113795475/e9e16565-f98c-4a9c-b80e-90f65882ac48)
![image](https://github.com/Suraj-Chavan1/disease-prediction-using-machine-learning/assets/113795475/e36605f3-c690-4e1a-b286-3a5f6c5764db)
![image](https://github.com/Suraj-Chavan1/disease-prediction-using-machine-learning/assets/113795475/4476332f-02f2-4c68-b51d-05e6b425f34d)
![image](https://github.com/Suraj-Chavan1/disease-prediction-using-machine-learning/assets/113795475/6934f50e-fd2b-4bda-9b45-124bc17f8322)
![image](https://github.com/Suraj-Chavan1/disease-prediction-using-machine-learning/assets/113795475/9947bb8f-8357-435f-848d-162fbe1eef60)
![image](https://github.com/Suraj-Chavan1/disease-prediction-using-machine-learning/assets/113795475/689d1f87-ced8-473b-86ea-ae9534001d4c)
![image](https://github.com/Suraj-Chavan1/disease-prediction-using-machine-learning/assets/113795475/99f42d7c-7320-4478-85d1-1f8c78d4ff6e)
![image](https://github.com/Suraj-Chavan1/disease-prediction-using-machine-learning/assets/113795475/013bbc2f-64eb-4056-a1d9-8900fe279007)









1. Clone the repository:

    ```bash
    git clone https://github.com/Suraj-Chavan1/disease-prediction-using-machine-learning.git
    cd disease-prediction-using-machine-learning
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Data Preprocessing:**

    Run the data preprocessing script to clean and prepare the raw data.

    ```bash
    python src/data_preprocessing.py
    ```

2. **Feature Engineering:**

    Generate features from the processed data.

    ```bash
    python src/feature_engineering.py
    ```

3. **Model Training:**

    Train the disease prediction models using the prepared dataset.

    ```bash
    python src/model_training.py
    ```

4. **Prediction:**

    Use the trained models to predict diseases based on new patient data.

    ```bash
    python src/prediction.py
    ```

5. **Web Application:**

    Run the web application for user-friendly interaction.

    ```bash
    cd app
    python app.py
    ```

    Open your browser and go to `http://localhost:5000` to access the web app.

## Dataset

The dataset used for this project includes various features related to patient health metrics. The raw data should be placed in the `data/raw/` directory. Preprocessed and engineered data will be stored in the `data/processed/` directory.

## Model Training

The model training script trains various machine learning models for disease prediction, including Decision Trees, Random Forest, and Logistic Regression. The script evaluates the models using appropriate metrics and selects the best-performing model.

## Results

The results of the disease prediction models, including visualizations and performance metrics, will be saved in the `results/` directory. Detailed analysis and plots can be found in the Jupyter notebooks under the `notebooks/` directory.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

Evaluation
The models are evaluated based on various metrics such as accuracy, precision, recall, and F1 score. These metrics provide insights into the performance of each algorithm in disease prediction.

Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

](https://github.com/Suraj-Chavan1/disease-prediction-using-machine-learning)
