import streamlit as st
import pandas as pd

def app():

    df = pd.read_excel("dataset.xlsx")  # read the dataset

    st.markdown("## Dataset:")  # add a title
    #st.write(df)  # visualize my dataframe in the Streamlit app

    st.subheader("Filters:")
    df["Year"] = (pd.to_datetime(df["Date"])).dt.year

    city, year, aqi = st.columns(3)
    city_filter = city.multiselect(label="Select City", options=df["City"].unique())
    year_filter = year.multiselect(label = "Select Year", options=df["Year"].unique())
    aqi_filter = aqi.multiselect(label = "Select AQI", options=df["AQI"].unique())
    if city_filter or year_filter or aqi_filter:
        filtered_data = df[
            (df["City"].isin(city_filter) if city_filter else True) & 
            (df["Year"].isin(year_filter) if year_filter else True) &
            (df["AQI"].isin(aqi_filter) if aqi_filter else True)
        ]
    else:
        filtered_data = df
    filtered_data = filtered_data.drop(columns=["Year"])
    st.dataframe(filtered_data, hide_index=True, width=800, use_container_width=True)


    st.markdown("## View your own dataset:")
    uploaded_file = st.file_uploader("Choose a file")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)
