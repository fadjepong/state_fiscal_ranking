import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

#Import the States dataset

state_data = pd.read_csv('state_fiscal_ranking.csv')

st.write(state_data)

col1, col2, col3 = st.columns(3)


st.sidebar.header("Pick two viables for your scatterplot")
x_val = st.sidebar.selectbox("pick your x-axis", state_data.select_dtypes(include=np.number).columns.tolist())
y_val = st.sidebar.selectbox("pick your y-axis", state_data.select_dtypes(include=np.number).columns.tolist())

scatter = alt.Chart(state_data, title = f"Correlation between {x_val} and {y_val}").mark_point().encode(
    alt.X(x_val, title=f"{x_val}"),
    alt.Y(y_val, title=f"{y_val}"),
    tooltip=[x_val,y_val])
st.altair_chart(scatter, use_container_width=True)

#Calculate the correlation
corr = round(state_data[x_val].corr(state_data[y_val]),2)
st.write(f"The correlation between {x_val} and {y_val} is {corr}")