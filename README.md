# Machine Learning Repository

This repository contains various machine learning projects, data analysis tasks, and learning materials covering regression, classification, and exploratory data analysis using Python, scikit-learn, pandas, and visualization libraries.

## Projects

### 1. Student Performance Analysis
**Location:** `Student_Performance/`

Analysis of student performance data with multiple factors affecting academic outcomes.

**Dataset Features:**
- Student demographics (age, gender)
- Educational factors (school type, parent education level)
- Study habits (study hours, study method, attendance)
- Lifestyle factors (internet access, travel time, extra activities)
- Academic scores (math, science, english, overall scores and final grades)

**Analysis Includes:**
- Exploratory data analysis with Seaborn and Matplotlib
- Distribution analysis of study hours
- Performance correlation analysis
- Demographic grouping and comparisons
- Score relationships and patterns

**Files:**
- `model.ipynb` - Jupyter notebook with analysis
- `Student_Performance.csv` - Dataset

### 2. Student Mental Health Analysis
**Location:** `Student_Mental_Health/`

Analysis of mental health factors affecting students in educational settings.

**Files:**
- `model.ipynb` - Analysis and modeling notebook
- `Student Mental health.csv` - Mental health dataset

### 3. Titanic Survival Prediction
**Location:** `Titanic/`

Classic Kaggle competition dataset for predicting passenger survival on the Titanic disaster.

**Features:**
- Passenger demographics (age, gender, class)
- Family relationships (siblings, parents/children)
- Ticket and fare information
- Embarkation details

**Files:**
- `model.ipynb` - Analysis and prediction model
- `train.csv` - Training dataset
- `test.csv` - Test dataset
- `gender_submission.csv` - Sample submission

### 4. Formula 1 Analysis
**Location:** `Formula1/`

Analysis and modeling of Formula 1 racing data.

**Files:**
- `model.ipynb` - F1 data analysis and predictions

### 5. Linear Regression Learning
**Location:** `LearnLinearRegression/`

Learning materials and hands-on practice for linear regression concepts.

**Files:**
- `learn1.ipynb` - Linear regression tutorial and examples
- `USA_Housing.csv` - Housing dataset for regression practice

### 6. Udemy Course Projects
**Location:** `Udemy/`

Projects and exercises from Udemy machine learning courses.

**Content:**
- Data preprocessing techniques and templates
- Simple Linear Regression implementation
- Salary prediction based on years of experience

**Sub-projects:**
- `data_preprocessing_template.ipynb` - Template for data preprocessing
- `data_preprocessing_tools.ipynb` - Data preprocessing utilities
- `LinearRegression/SimpleLinearRegression/` - Simple linear regression with salary data

### 7. Exercises
**Location:** `Exercises/`

Practice exercises and project implementations.

**Content:**
- Linear regression project with e-commerce customer data
- Hands-on coding practice

## Root Files

- `firstday.ipynb` - Initial exploration and learning notebook
- `new.py` - Python script file
- `Yahoo/yahoo.ipynb` - Yahoo-related data analysis

## Getting Started

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter plotly
```

### Usage
Navigate to any project folder and open the Jupyter notebook:
```bash
cd Student_Performance/
jupyter notebook model.ipynb
```

Or run specific project notebooks:
```bash
# Simple Linear Regression
cd Udemy/LinearRegression/SimpleLinearRegression/
jupyter notebook simplelinearregression.ipynb

# Student Performance Analysis
cd Student_Performance/
jupyter notebook model.ipynb

# Titanic Survival Prediction
cd Titanic/
jupyter notebook model.ipynb
```

## Technologies Used
- **Python 3.x** - Programming language
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations
- **Matplotlib & Seaborn** - Data visualization
- **Scikit-learn** - Machine learning models and preprocessing
- **Jupyter Notebook** - Interactive development environment

## Learning Path

This repository follows a progressive learning path:

1. **Data Preprocessing** - Start with Udemy preprocessing templates
2. **Simple Linear Regression** - Learn basic regression with salary data
3. **Multiple Variable Analysis** - Explore housing and e-commerce datasets
4. **Classification** - Titanic survival prediction
5. **Complex Analysis** - Student performance and mental health studies

## Repository Structure

```
Machine_Learning/
├── Exercises/              # Practice exercises and projects
├── Formula1/               # F1 racing data analysis
├── LearnLinearRegression/  # Linear regression tutorials
├── Student_Mental_Health/  # Mental health analysis
├── Student_Performance/    # Academic performance analysis
├── Titanic/                # Survival prediction (Kaggle)
├── Udemy/                  # Course projects and templates
│   └── LinearRegression/   # Regression implementations
└── Yahoo/                  # Yahoo data analysis
```

## Contributing

Feel free to explore, learn from, and contribute to any of the projects in this repository.

## License

This repository is for educational purposes.