# 🏆 GRIDTITAN — AI-Based Transformer Failure Prediction

## 🚀 Overview
Transformer failures in power distribution systems lead to **unexpected outages, high maintenance costs, and operational inefficiencies**.  
Traditional approaches rely on **reactive maintenance**, failing to detect issues in advance.

This project presents a **data-centric AI-based risk decision system** that predicts transformer failures and enables **proactive maintenance** through intelligent risk prioritization.

---

## 🎯 Problem Statement
Predict transformer failures using operational data while addressing real-world challenges such as:

- Missing data  
- Class imbalance  
- Noisy and inconsistent signals  
The goal is to ensure early failure detection, even in rare-event scenarios.
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
- Designed to closely mimic real transformer operational behavior.
---

## 🧠 Field Insights (Domain Knowledge)

Real-world observations from electrical field experts:

- **Load spikes** (motor usage) lead to overheating  
- **Voltage fluctuations** cause stress on transformers  
- Failures occur due to **gradual degradation**, not instantly  
- Fault detection is often **delayed and reactive**
  
👉 These insights directly guided our feature engineering and system design.
---

## ⚠️ Baseline Model

- Model: Logistic Regression  
- Accuracy: **94%**  
- Recall: **0** ❌  

📌 **Observation:**  
The model achieved high accuracy but failed to detect any failure cases due to severe class imbalance.

High accuracy is misleading in rare-event prediction problems.

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

Focus was on improving data quality, not increasing model complexity.

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
->
Data Cleaning
->
Feature Engineering
->
Model Training (XGBoost)
->
Risk Scoring
->
Actionable Output

End-to-end AI pipeline for transformer risk management.

---

## ⚙️ Model Strategy (Engineering Perspective)

In safety-critical systems like power distribution:

Missing a failure is more costly than a false alarm.

- Prioritize Recall over Accuracy  
- Accept manageable false positives  
- Ensure early detection of critical failures  

A controlled increase in false alarms is acceptable to ensure that no critical failures are missed.

The system balances recall and false alarm rate, prioritizing failure detection while maintaining acceptable operational efficiency.

---

## 📌 Key Output

### 🔹 Risk Scoring System
Each transformer is assigned:

- **Risk Score (0–1)**  
- **Risk Level:** Low / Medium / High  

---

### 🔹 Top-K Prioritization
- Identifies Top 5 high-risk transformers  
- Enables prioritized maintenance  
- Supports Top-K decision-making for resource allocation 

---

### 🔹 Downloadable Report
- Generates a CSV file with:
  - Transformer ID  
  - Risk Score  
  - Risk Level  

👉 From prediction to actionable decision-making for maintenance planning.

---

## 🌍 Impact

- Enables **proactive maintenance**  
- Reduces unexpected failures  
- Improves **grid reliability**  
- Supports **data-driven decision-making**
- Shifts maintenance strategy from **reactive** to **predictive**.

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
- ├── dataset/
- │ └── Transformer-Dataset.csv
- ├── notebooks/
- │ └── main.ipynb
- ├── output/
- │ └── risk_ranked_transformers.csv
- ├── README.md



---

## 🔗 Links
- 🔗 Deployed Live Link: https://transformer-failure-prediction-deploy-sss.streamlit.app/
- 📁 Google Drive: https://drive.google.com/drive/folders/1q3_BGpidGtf__45evzSvcqyOmcIxs_dP
- 💻 GitHub Repo: https://github.com/s-s-shriram/Transformer-Failure-Prediction/

---

## 👤 Author
**S.S.SHRIRAM**  
B.Tech AI & Data Science  

---

## 🔥 Final Note
> **We improved recall from 0 to 91% by solving data quality issues and enabling proactive transformer maintenance.**
