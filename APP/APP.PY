# app.py
import io
import os
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

st.set_page_config(page_title="Segment Studio", layout="wide")

st.title("Segment Studio - פילוח אוטומטי (K-Means)")

# ------------------------------------
# שלב 1 – טעינת קובץ CSV והצגה
# ------------------------------------
st.header("שלב 1: העלאת CSV והצגת הנתונים")

uploaded_file = st.file_uploader(
    "בחר קובץ CSV (ללא עמודת תווית)",
    type=["csv"]
)

if uploaded_file is not None:
    # טוען ל-DataFrame
    df = pd.read_csv(uploaded_file)
    st.subheader("תצוגת נתונים (חלקית)")
    st.dataframe(df.head())
else:
    st.info("אנא העלה קובץ CSV כדי להמשיך.")
    st.stop()

# בחירה אילו עמודות להשתמש (מספריות)
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
st.sidebar.header("הגדרות עיבוד")
selected_features = st.sidebar.multiselect(
    "בחר עמודות מספריות לשימוש ב-K-Means:",
    options=numeric_cols,
    default=numeric_cols
)

if len(selected_features) == 0:
    st.error("יש לבחור לפחות עמודה מספרית אחת.")
    st.stop()

X = df[selected_features].copy()

# עיבוד מקדים ונירמול (StandardScaler) [file:1]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ------------------------------------
# שלב 2 – חישוב WCSS וגרף Elbow
# ------------------------------------
st.header("שלב 2: חישוב WCSS וגרף Elbow")

col1, col2, col3 = st.columns(3)
with col1:
    min_k = st.number_input("Min k", min_value=1, value=2, step=1)
with col2:
    max_k = st.number_input("Max k", min_value=2, value=10, step=1)
with col3:
    run_wcss = st.button("Run WCSS")

wcss_values = []
ks = []

if run_wcss:
    if max_k <= min_k:
        st.error("Max k חייב להיות גדול מ-Min k.")
    else:
        for k in range(int(min_k), int(max_k) + 1):
            kmeans = KMeans(n_clusters=k, random_state=42, n_init="auto")
            kmeans.fit(X_scaled)
            wcss_values.append(kmeans.inertia_)  # WCSS (inertia) [file:1]
            ks.append(k)

        fig, ax = plt.subplots()
        ax.plot(ks, wcss_values, marker="o")
        ax.set_xlabel("k")
        ax.set_ylabel("WCSS (inertia)")
        ax.set_title("Elbow Plot")
        st.pyplot(fig)

# ------------------------------------
# שלב 3 – בחירת k והרצת K-Means
# ------------------------------------
st.header("שלב 3: בחירת k ויצירת קלאסטרים")

k_for_clustering = st.number_input(
    "בחר k עבור קלאסטרינג",
    min_value=1,
    value=3,
    step=1
)
create_clusters = st.button("Create clusters")

if create_clusters:
    kmeans_final = KMeans(n_clusters=int(k_for_clustering), random_state=42, n_init="auto")
    cluster_ids = kmeans_final.fit_predict(X_scaled)

    # הוספת מזהה קלאסטר ל-DataFrame
    df["cluster_id"] = cluster_ids

    # ספירת מספר תצפיות בכל קלאסטר [file:1]
    cluster_counts = (
        df["cluster_id"]
        .value_counts()
        .sort_index()
        .reset_index()
        .rename(columns={"index": "cluster_id", "cluster_id": "count"})
    )

    st.subheader("טבלת ספירת קלאסטרים")
    st.dataframe(cluster_counts)

    st.subheader("הנתונים עם מזהה קלאסטר")
    st.dataframe(df.head())

    # הורדת קובץ CSV עם קלאסטרים (ללא שמות הקבוצות בשלב זה) [file:1]
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    st.download_button(
        label="הורדת CSV עם קלאסטרים",
        data=csv_buffer.getvalue(),
        file_name="data_with_clusters.csv",
        mime="text/csv"
    )

# ------------------------------------
# (שלב 4 – מקום להוספת LLM בעתיד)
# כאן אפשר להוסיף כפתור שמחשב סיכומים לכל קלאסטר
# ושולח אותם ל-LLM כדי לקבל name + description, ואז להוסיף עמודות אלה ל-df [file:1]
# ------------------------------------
