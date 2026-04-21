import pandas as pd
import shap
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# Load data
df = pd.read_csv("student_data.csv")

# Encode categorical columns
for col in df.select_dtypes(include='object').columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

# Features & target
X = df.drop("G3", axis=1)
y = df["G3"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# SHAP
explainer = shap.Explainer(model, X_train)
shap_values = explainer(X_test)

# Plots
shap.summary_plot(shap_values, X_test)
shap.plots.bar(shap_values)

force_plot = shap.plots.force(shap_values[0])
shap.save_html("force_plot.html", force_plot)
force_plot = shap.plots.force(shap_values[0])
shap.save_html("force_plot.html", force_plot)

for feature in X.columns[:3]:
    try:
        shap.plots.scatter(shap_values[:, feature])
    except:
        pass

plt.figure()
shap.summary_plot(shap_values, X_test, show=False)
plt.savefig("shap_summary.png", bbox_inches='tight')

print("Done")