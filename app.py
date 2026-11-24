
import streamlit as st
import pandas as pd
import sqlite3
import joblib
from pathlib import Path

# 1. Project folder path
BASE_DIR = Path(__file__).resolve().parent

# 2. Load trained ML model
model = joblib.load(BASE_DIR / "complaint_model.pkl")

# 3. Department mapping
departments = {
    "Billing": "Finance Department",
    "Delivery": "Logistics Department",
    "Technical Support": "IT Support Department",
    "Product / Refund": "Refund Department"
}

# 4. Database connection
DB_PATH = BASE_DIR / "complaints.db"

conn = sqlite3.connect(DB_PATH, check_same_thread=False)

conn.execute("""
CREATE TABLE IF NOT EXISTS complaints (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    complaint TEXT NOT NULL,
    predicted_category TEXT,
    correct_category TEXT,
    confidence REAL,
    status TEXT
)
""")

conn.commit()

# 5. Dashboard configuration
st.set_page_config(
    page_title="AI Complaint Management",
    page_icon="🤖",
    layout="wide"
)

st.title("AI Customer Complaint Management System")
st.write("Smart Complaint Classification and Department Routing")

st.divider()

# 6. Complaint input
st.subheader("Submit Customer Complaint")

complaint = st.text_area(
    "Enter complaint:",
    placeholder="Example: My bank charged me twice..."
)

# 7. Analyze complaint
if st.button("Analyze Complaint", type="primary"):

    if complaint.strip():

        prediction = model.predict([complaint])[0]
        confidence = float(model.predict_proba([complaint]).max())

        st.session_state["complaint"] = complaint
        st.session_state["prediction"] = prediction
        st.session_state["confidence"] = confidence

    else:
        st.warning("Please enter a complaint.")

# 8. Show prediction
if "prediction" in st.session_state:

    prediction = st.session_state["prediction"]
    confidence = st.session_state["confidence"]
    complaint = st.session_state["complaint"]

    st.divider()
    st.subheader("Prediction Results")

    col1, col2 = st.columns(2)

    col1.metric("Predicted Category", prediction)
    col2.metric("Confidence", f"{confidence * 100:.2f}%")

    if confidence < 0.60:
        st.warning("Human review recommended.")
    else:
        st.success("Prediction ready for verification.")

    # 9. Employee verification
    categories = list(model.classes_)

    correct_category = st.selectbox(
        "Verify complaint category:",
        categories,
        index=categories.index(prediction)
    )

    # 10. Save complaint
    if st.button("Save Complaint"):

        status = (
            "Reviewed"
            if prediction != correct_category or confidence < 0.60
            else "Verified"
        )

        conn.execute("""
        INSERT INTO complaints
        (complaint, predicted_category, correct_category,
         confidence, status)
        VALUES (?, ?, ?, ?, ?)
        """, (
            complaint,
            prediction,
            correct_category,
            confidence,
            status
        ))

        conn.commit()

        st.success("Complaint saved successfully!")

        st.write(
            "Assigned Department:",
            departments.get(correct_category, "Unassigned")
        )

        del st.session_state["complaint"]
        del st.session_state["prediction"]
        del st.session_state["confidence"]

# 11. Display complaint records
st.divider()
st.subheader("Complaint Database")

records = pd.read_sql_query(
    "SELECT * FROM complaints ORDER BY id DESC",
    conn
)

col1, col2 = st.columns(2)

col1.metric("Total Complaints", len(records))

col2.metric(
    "Human Reviewed",
    int((records["status"] == "Reviewed").sum())
)

st.dataframe(records, use_container_width=True)

conn.close()

