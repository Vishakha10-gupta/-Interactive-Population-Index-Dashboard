import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
st.set_page_config(page_title="Population Index Dashboard", layout="wide")

# Title
st.title("🌍 Population Index Dashboard")
st.markdown("Use the controls to explore simulated population data across different regions and age groups.")

# Sidebar controls
st.sidebar.header("Controls")

# Slider for population scale
population_scale = st.sidebar.slider("Select Population Scale (in thousands)", min_value=100, max_value=10000, step=100, value=5000)

# Radio button for visualization type
chart_type = st.sidebar.radio(
    "Select Chart Type",
    ("Histogram", "Box Plot", "Violin Plot", "Bar Chart")
)

# Generate synthetic population data
np.random.seed(42)
regions = ['North', 'South', 'East', 'West']
age_groups = ['0-14', '15-24', '25-54', '55-64', '65+']

data = []
for region in regions:
    for age in age_groups:
        population = np.random.randint(population_scale // 10, population_scale, size=100)
        for pop in population:
            data.append({'Region': region, 'Age Group': age, 'Population': pop})

df = pd.DataFrame(data)

# Display selected chart
st.subheader(f"{chart_type} of Population Distribution")

if chart_type == "Histogram":
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(df['Population'], bins=30, kde=True, ax=ax)
    ax.set_title("Population Histogram")
    st.pyplot(fig)

elif chart_type == "Box Plot":
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.boxplot(x='Age Group', y='Population', data=df, ax=ax)
    ax.set_title("Population Distribution by Age Group")
    st.pyplot(fig)

elif chart_type == "Violin Plot":
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.violinplot(x='Region', y='Population', data=df, ax=ax)
    ax.set_title("Population Distribution by Region")
    st.pyplot(fig)

elif chart_type == "Bar Chart":
    summary = df.groupby('Region')['Population'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x='Region', y='Population', data=summary, ax=ax)
    ax.set_title("Total Population by Region")
    st.pyplot(fig)

# Show raw data
with st.expander("Show Raw Data"):
    st.dataframe(df.head(50))
