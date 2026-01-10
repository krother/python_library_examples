# run with: streamlit run pingu_streamlit.py

import streamlit as st
import seaborn as sns
from matplotlib import pyplot as plt

@st.cache_data
def load_data():
    return sns.load_dataset('penguins')



st.write("# Penguin Beaks and Flippers")

df = load_data()

# select from a list of strings
options = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm"]
column = st.selectbox("pick a data column", options)

# select a number between two boundaries
min_val = st.slider("minimum value", 0, 100)

# text input
text = st.text_input("enter some text: ", value=":sunglasses:")
st.write("**" + text + "**")

# multiple select
species = st.multiselect("species", options=["Adelie", "Chinstrap", "Gentoo"])
df = df[df["species"].isin(species)]

# on / off button
show_plots = st.toggle('Show some plots')

df = df[df[column] >= min_val]

if show_plots:

    tab1, tab2, tab3 = st.tabs(["Lines", "Bars", "Other"])

    with tab1:

        st.write("### Line plot")
        st.line_chart(data=df, x="body_mass_g", y=["bill_length_mm", "flipper_length_mm"], 
                    color=["#ff00ff", "#00ff00"],
                    width=0, height=0,
                    use_container_width=True)

        st.write("### Scatter plot")
        st.scatter_chart(data=df, x="bill_length_mm", y="body_mass_g", 
                    color="species",
                    width=0, height=500,
                    use_container_width=True)

    with tab2:

        st.write("### Distribution of species")
        counts = df["species"].value_counts()
        st.bar_chart(counts)  # same arguments as the other plots

        st.write("### Distribution of species and gender")
        pivot = df.groupby(["species", "sex"])["body_mass_g"].count().unstack()
        st.bar_chart(pivot)  # same arguments as the other plots


    with tab3:

        st.write("### Histogram")
        fig = plt.figure()
        sns.histplot(df[column], kde=True)
        st.pyplot(fig)

        st.write("### Tabular Output")
        st.write(df)
