# 🏆 GRIDTITAN — AI-Based Transformer Failure Prediction

## 🚀 Overview
Transformer failures in power distribution systems lead to **unexpected outages, high maintenance costs, and operational inefficiencies**.  
Traditional approaches rely on **reactive maintenance**, failing to detect issues in advance.

This project presents a **data-centric AI solution** that predicts transformer failures and enables **proactive maintenance** through risk-based prioritization.

---

## 🎯 Problem Statement
Predict transformer failures using operational data while addressing real-world challenges such as:

- Missing data  
- Class imbalance  
- Noisy and inconsistent signals  

---

## 💡 Key Idea
> **We improved the data, not just the model.**

Instead of focusing only on model complexity, we applied a **data-centric approach** to enhance prediction quality.

---

## 📊 Dataset

A **synthetic yet realistic dataset** was created to simulate transformer behavior in real-world conditions.

### 🔹 Features
- Load  
- Temperature  
- Voltage  
- Current  
- Power  

### 🔹 Real-World Characteristics
- Missing values introduced  
- Imbalanced data (~7% failure rate)  
- Time-based operational patterns  

---

## 🧠 Field Insights (Domain Knowledge)

Real-world observations from electrical field experts:

- **Load spikes** (motor usage) lead to overheating  
- **Voltage fluctuations** cause stress on transformers  
- Failures occur due to **gradual degradation**, not instantly  
- Fault detection is often **delayed and reactive**

👉 These insights guided our feature engineering and model design.

---

## ⚠️ Baseline Model

- Model: Logistic Regression  
- Accuracy: **94%**  
- Recall: **0** ❌  

📌 **Observation:**  
The model failed to detect any failure cases due to class imbalance.

---

## 🔧 Data-Centric Improvements

### 1. Data Cleaning
- Handled missing values using mean imputation  

### 2. Feature Engineering
- **Thermal Stress** = Load × Temperature  
- **Overload Indicator**  
- **Load Ratio**  

### 3. Imbalance Handling
- Applied **SMOTE** to balance failure classes  

---

## 🤖 Improved Model

- Model: XGBoost  

### 📈 Performance

| Metric | Baseline | Improved |
|--------|----------|----------|
| Accuracy | 94% | ~89% |
| Recall | 0 | **~91%** 🔥 |

> 🚀 **Recall improved from 0 to 91%**, enabling effective failure detection.

---

## ⚙️ System Architecture

Input Data
↓
Data Cleaning
↓
Feature Engineering
↓
Model Training (XGBoost)
↓
Risk Scoring
↓
Actionable Output


---

## 📌 Key Output

### 🔹 Risk Scoring System
Each transformer is assigned:

- **Risk Score (0–1)**  
- **Risk Level:** Low / Medium / High  

---

### 🔹 Top-K Prioritization
- Identifies **Top 5 high-risk transformers**  
- Enables prioritized maintenance  

---

### 🔹 Downloadable Report
- Generates a CSV file with:
  - Transformer ID  
  - Risk Score  
  - Risk Level  

👉 Ready for real-world deployment

---

## 🌍 Impact

- Enables **proactive maintenance**  
- Reduces unexpected failures  
- Improves **grid reliability**  
- Supports **data-driven decision-making**

---

## 🏆 Why This Solution Stands Out

- Data-centric approach (not model-centric)  
- Real-world field insights integration  
- Handles class imbalance effectively  
- Converts predictions into **actionable decisions**  
- Scalable to real smart grid systems  

---

## 🛠️ Tech Stack

- Python  
- Pandas  
- Scikit-learn  
- XGBoost  
- Imbalanced-learn (SMOTE)  

---

## 📂 Project Structure
├── dataset/
│ └── transformer_dataset.csv
├── notebooks/
│ └── model_training.ipynb
├── output/
│ └── risk_ranked_transformers.csv
├── README.md


---

## 🎬 Demo
👉 demo video link:  

---

## 🔗 Links
- 📁 Google Drive:  
- 💻 GitHub Repo: https://github.com/s-s-shriram/Transformer-Failure-Prediction/

---

## 👤 Author
**S.S.SHRIRAM**  
B.Tech AI & Data Science  

---

## 🔥 Final Note
> **From prediction to decision-making — enabling smarter and more reliable power systems.**
