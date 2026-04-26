# ==========================================
# STEP 0: CLEAN OUTPUT (REMOVE WARNINGS)
# ==========================================
import warnings
warnings.filterwarnings("ignore")

# ==========================================
# STEP 1: IMPORT LIBRARIES
# ==========================================
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score, classification_report
from sklearn.impute import SimpleImputer

from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier

# ==========================================
# STEP 2: LOAD DATASET (JUPYTER COMPATIBLE)
# ==========================================
try:
    data = pd.read_csv("advanced_transformer_dataset.csv")
    print("\nLocal dataset loaded successfully!")
except Exception as e:
    print("\nError loading dataset:", e)

# ==========================================
# STEP 3: DATA PREVIEW
# ==========================================
print("\n===== DATA PREVIEW =====")
print(data.head())

print("\n===== MISSING VALUES =====")
print(data.isnull().sum())

# ==========================================
# STEP 4: BASELINE MODEL (RAW DATA)
# ==========================================
print("\n===== BASELINE MODEL =====")

# Select basic features only
baseline_features = ["load", "temperature", "voltage", "current", "power"]
X_base = data[baseline_features]
y = data["failure"]

# Handle missing values (basic)
imputer = SimpleImputer(strategy="mean")
X_base = imputer.fit_transform(X_base)

# Train-test split
X_train_b, X_test_b, y_train_b, y_test_b = train_test_split(
    X_base, y, test_size=0.2, random_state=42
)

# Train model
baseline_model = LogisticRegression(max_iter=1000)
baseline_model.fit(X_train_b, y_train_b)

# Predict
y_pred_b = baseline_model.predict(X_test_b)

# Evaluate
base_acc = accuracy_score(y_test_b, y_pred_b)
base_rec = recall_score(y_test_b, y_pred_b)

print("Accuracy:", base_acc)
print("Recall:", base_rec)

print("\nBaseline Report:")
print(classification_report(y_test_b, y_pred_b))

# ==========================================
# STEP 5: DATA ENRICHMENT
# ==========================================
print("\n===== DATA ENRICHMENT =====")

# Fix missing values (clean way)
for col in ["load", "temperature", "voltage"]:
    data[col] = data[col].fillna(data[col].mean())

# Feature Engineering
data["thermal_stress"] = data["load"] * data["temperature"]
data["overload"] = (data["load"] > 80).astype(int)
data["load_ratio"] = data["load"] / 100

# ==========================================
# STEP 6: PREPARE ENRICHED DATA
# ==========================================
features = [
    "load", "temperature", "voltage", "current", "power",
    "thermal_stress", "overload", "load_ratio"
]

X = data[features]
y = data["failure"]

# ==========================================
# STEP 7: HANDLE IMBALANCE (SMOTE)
# ==========================================
smote = SMOTE()
X_res, y_res = smote.fit_resample(X, y)

print("\nAfter SMOTE:")
print(pd.Series(y_res).value_counts())

# ==========================================
# STEP 8: TRAIN IMPROVED MODEL
# ==========================================
X_train, X_test, y_train, y_test = train_test_split(
    X_res, y_res, test_size=0.2, random_state=42
)

model = XGBClassifier(eval_metric='logloss')
model.fit(X_train, y_train)

# ==========================================
# STEP 9: EVALUATE IMPROVED MODEL
# ==========================================
y_pred = model.predict(X_test)

imp_acc = accuracy_score(y_test, y_pred)
imp_rec = recall_score(y_test, y_pred)

print("\n===== IMPROVED MODEL PERFORMANCE =====")
print("Accuracy:", imp_acc)
print("Recall:", imp_rec)

print("\nImproved Report:")
print(classification_report(y_test, y_pred))

# ==========================================
# STEP 10: COMPARISON (VERY IMPORTANT)
# ==========================================
print("\n===== MODEL COMPARISON =====")

print(f"Baseline Accuracy: {base_acc:.2f} | Improved Accuracy: {imp_acc:.2f}")
print(f"Baseline Recall: {base_rec:.2f} | Improved Recall: {imp_rec:.2f}")

# ==========================================
# STEP 11: RISK SCORING
# ==========================================
data["risk_score"] = model.predict_proba(X)[:, 1]

def classify(score):
    if score > 0.7:
        return "High"
    elif score > 0.4:
        return "Medium"
    else:
        return "Low"

data["risk_level"] = data["risk_score"].apply(classify)

# ==========================================
# STEP 12: TOP-K HIGH RISK TRANSFORMERS
# ==========================================
top_k = data.sort_values(by="risk_score", ascending=False).head(5)

print("\n===== TOP 5 HIGH-RISK TRANSFORMERS =====")
print(top_k[["transformer_id", "risk_score", "risk_level"]])

# ==========================================
# STEP 13: SAVE FINAL OUTPUT
# ==========================================
data.to_csv("final_output.csv", index=False)

print("\nFinal output saved successfully!")
