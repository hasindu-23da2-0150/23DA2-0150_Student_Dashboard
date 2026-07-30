import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------
# Page Title
# ---------------------------------

st.set_page_config(page_title="Student Dashboard", layout="wide")

st.title("Interactive Student Dashboard")

# ---------------------------------
# Load Data
# ---------------------------------

df = pd.read_csv("students.csv")

# ---------------------------------
# Sidebar Filters
# ---------------------------------

st.sidebar.header("Filters")

department = st.sidebar.selectbox(
    "Select Department",
    ["All"] + list(df["Department"].unique())
)

minimum_marks = st.sidebar.slider(
    "Minimum Marks",
    0,
    100,
    0
)

filtered_df = df.copy()

if department != "All":
    filtered_df = filtered_df[
        filtered_df["Department"] == department
    ]

filtered_df = filtered_df[
    filtered_df["Marks"] >= minimum_marks
]

# ---------------------------------
# Display Table
# ---------------------------------

st.subheader("Student Data")

st.dataframe(filtered_df)

# ---------------------------------
# KPI Cards
# ---------------------------------

average_marks = filtered_df["Marks"].mean()
highest_marks = filtered_df["Marks"].max()
average_attendance = filtered_df["Attendance"].mean()

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Marks",
    f"{average_marks:.2f}"
)

col2.metric(
    "Highest Marks",
    highest_marks
)

col3.metric(
    "Average Attendance",
    f"{average_attendance:.2f}%"
)

# ---------------------------------
# Bar Chart
# ---------------------------------

st.subheader("Marks by Student")

bar = px.bar(
    filtered_df,
    x="Student",
    y="Marks",
    color="Department"
)

st.plotly_chart(bar, use_container_width=True)

# ---------------------------------
# Pie Chart
# ---------------------------------

st.subheader("Students by Department")

pie = px.pie(
    filtered_df,
    names="Department"
)

st.plotly_chart(pie, use_container_width=True)

# ---------------------------------
# Scatter Plot
# ---------------------------------

st.subheader("Attendance vs Marks")

scatter = px.scatter(
    filtered_df,
    x="Attendance",
    y="Marks",
    color="Department",
    text="Student",
    size="Marks"
)

st.plotly_chart(scatter, use_container_width=True)

# ---------------------------------
# Extension Challenge
# ---------------------------------

st.subheader("Monthly Performance")

monthly = pd.DataFrame({
    "Month": [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun"
    ],
    "Average Marks": [
        72,
        75,
        78,
        81,
        84,
        87
    ]
})

line = px.line(
    monthly,
    x="Month",
    y="Average Marks",
    markers=True
)

st.plotly_chart(line, use_container_width=True)

# Download CSV

csv = filtered_df.to_csv(index=False)

st.download_button(
    "Download Filtered CSV",
    csv,
    file_name="filtered_students.csv",
    mime="text/csv"
)

# ---------------------------------
# Insight
# ---------------------------------

st.subheader("Insight")

st.write(
    "Students with attendance above 90% generally have higher marks. "
    "The IT department records the highest overall student performance."
)