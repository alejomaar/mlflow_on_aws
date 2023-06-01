<p align="center">
  <a href="" rel="noopener">
 <img src="https://i.imgur.com/AZ2iWek.png" alt="Project logo"></a>
</p>
<h3 align="center">MLFlow on AWS</h3>

<div align="center">

[![Hackathon](https://img.shields.io/badge/mlflow-experiment_tracking-orange.svg)](http://hackathon.url.com)
[![Hackathon](https://img.shields.io/badge/cloud-aws-orange.svg)](http://hackathon.url.com)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE.md)

</div>

---

<p align="center">A collaborative MLFlow project for California housing price prediction using pandas, sklearn, numpy, seaborn, matplotlib, and MLFlow.
    <br> 
</p>

## 📝 Table of Contents

- [Problem Statement](#problem_statement)
- [Idea / Solution](#idea)
- [Dependencies / Limitations](#limitations)
- [Future Scope](#future_scope)
- [Setting up a local environment](#getting_started)
- [Usage](#usage)
- [Technology Stack](#tech_stack)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)

## 🧐 Problem Statement <a name = "problem_statement"></a>

The task is to predict housing prices in California using the California housing dataset. The goal is to design a collaborative project where different data scientists address this problem in their own way using MLFlow.


## 💡 Idea / Solution <a name = "idea"></a>

The idea is to demonstrate how MLFlow can be used in a collaborative team setting to address the California housing price prediction problem. Each data scientist can implement their own approach and track their experiments using MLFlow, allowing for easy comparison and reproducibility.


## ⛏️ Built With <a name = "tech_stack"></a>

- [Postgres]() - Database
- [Python]() - Machine Learning
- [Matplotlib & Seaborn]() -Visualization
- [MLFlow]() - Experiment Tracking
- [AWS]() - Cloud


## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your enviroment for production.

### Prerequisites

* Make sure you have the following software installed:

```
- Python
- Pipenv
```

* You must have an AWS account

### Installing

1. Clone the repository:

```bash
git clone https://github.com/alejomaar/mlflow_on_aws
```

2. Install dependencies with pipenv:

```bash
pipenv install
```
```bash
pipenv shell
```


2. (Optional) Install dependencies with other python package manager:

```bash
pip install -r requirements.txt
```

3. Set your environment variables:

* Change the name of 'env_placeholder' to '.env' and change it with your own environment variables

4. Run MLFlow:

**Run Local:**

```bash
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlflow/artifacts --host 0.0.0.0 -p 4600
```
**Run Production:**
 
You will need to have a EC2 instance already running on AWS, so you need run this command into the instance. (`Check the deployment section for more information`)

```bash
mlflow server --backend-store-uri postgresql://{USER_NAME}:{PASSWORD}@{HOST}:5432/{DATABASE_NAME} --default-artifact-root s3://{S3_BUCKET_NAME} -p 5000 -h 0.0.0.0
```
  

4. Run any notebooks




## 🎈 Usage <a name="usage"></a>

- `run notebooks` - Each notebook propose a different approach for predict housing prices on California dataset, I recommend you run all notebooks for check out all the mage.
- `experiment` - Change the parameters in your experiments, you could add more images, export more artifacts and of course apply more feature engineering for archiving better results. 


## ✍️ Authors <a name = "authors"></a>

- [@alejomaar](https://github.com/alejomaar) - Idea & Initial work


## 🎉 Acknowledgments <a name = "acknowledgments"></a>

- This notebook is inspired in the teachings of [mlops-zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) 
- If you want to a tutorial about the entire process I recommend you this [tutorial](https://www.youtube.com/watch?v=1ykg4YmbFVA&list=PL3MmuxUbc_hIUISrluw_A7wDSmfOhErJK&index=19)

