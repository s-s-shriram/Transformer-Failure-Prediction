import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, confusion_matrix
from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier

import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Transformer Failure Detection",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Transformer Failure Detection System")
st.write("ML-based risk prediction using XGBoost, SMOTE and feature engineering.")

uploaded_file = st.file_uploader("Upload transformer dataset CSV", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.subheader("📌 Dataset Preview")
    st.dataframe(data.head())

    required_cols = ["load", "temperature", "voltage", "current", "power", "failure"]

    if not all(col in data.columns for col in required_cols):
        st.error("CSV must contain: load, temperature, voltage, current, power, failure")
        st.stop()

    for col in ["load", "temperature", "voltage"]:
        data[col] = data[col].fillna(data[col].mean())

    data["thermal_stress"] = data["load"] * data["temperature"]
    data["overload"] = (data["load"] > 80).astype(int)

    features = [
        "load", "temperature", "voltage", "current", "power",
        "thermal_stress", "overload"
    ]

    X = data[features]
    y = data["failure"]

    smote = SMOTE(random_state=42)
    X_res, y_res = smote.fit_resample(X, y)

    X_train, X_test, y_train, y_test = train_test_split(
        X_res, y_res, test_size=0.2, random_state=42
    )

    model = XGBClassifier(eval_metric="logloss", random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    accuracy = accuracy_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)

    st.subheader("📊 Model Performance")

    col1, col2 = st.columns(2)
    col1.metric("Accuracy", f"{accuracy * 100:.2f}%")
    col2.metric("Recall", f"{recall * 100:.2f}%")

    test_data = pd.DataFrame(X_test, columns=features)
    test_data["actual_failure"] = y_test.values
    test_data["risk_score"] = y_prob

    def classify(score):
        if score > 0.30:
            return "High"
        elif score > 0.15:
            return "Medium"
        else:
            return "Low"

    test_data["risk_level"] = test_data["risk_score"].apply(classify)

    k = int(0.3 * len(test_data))
    top_k = test_data.sort_values(by="risk_score", ascending=False).head(k)

    actual_failures = test_data[test_data["actual_failure"] == 1]
    captured = top_k[top_k["actual_failure"] == 1]

    recall_at_k = len(captured) / len(actual_failures) if len(actual_failures) > 0 else 0

    high_risk = test_data[test_data["risk_level"] == "High"]
    false_alarms = high_risk[high_risk["actual_failure"] == 0]
    false_alarm_rate = len(false_alarms) / len(high_risk) if len(high_risk) > 0 else 0

    lead_time = 4 + (recall_at_k * 2)

    st.subheader("⚠️ Risk Analysis")

    c1, c2, c3 = st.columns(3)
    c1.metric("Recall@Top-K", f"{recall_at_k:.2f}")
    c2.metric("False Alarm Rate", f"{false_alarm_rate:.2f}")
    c3.metric("Estimated Lead Time", f"{lead_time:.1f} weeks")

    st.subheader("🚨 High Risk Transformers")
    st.dataframe(top_k)

    csv = top_k.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download High Risk Transformers CSV",
        data=csv,
        file_name="risk_ranked_transformers.csv",
        mime="text/csv"
    )

    st.subheader("📌 Feature Importance")

    fig, ax = plt.subplots()
    ax.barh(features, model.feature_importances_)
    ax.set_xlabel("Importance")
    ax.set_title("Feature Importance")
    st.pyplot(fig)

    st.subheader("📌 Risk Level Distribution")

    fig2, ax2 = plt.subplots()
    test_data["risk_level"].value_counts().plot(kind="bar", ax=ax2)
    ax2.set_xlabel("Risk Level")
    ax2.set_ylabel("Count")
    ax2.set_title("Risk Level Count")
    st.pyplot(fig2)

    st.subheader("📌 Confusion Matrix")

    cm = confusion_matrix(y_test, y_pred)

    fig3, ax3 = plt.subplots()
    ax3.imshow(cm)
    ax3.set_title("Confusion Matrix")
    ax3.set_xlabel("Predicted")
    ax3.set_ylabel("Actual")

    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax3.text(j, i, cm[i, j], ha="center", va="center")

    st.pyplot(fig3)

else:
    st.info("Please upload your transformer dataset CSV file.")
