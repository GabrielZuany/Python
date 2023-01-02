import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")
st.title(body=":bar_chart: Sales Dashboard")
st.markdown("---")

@st.cache # storing the cache data to enhance the app performance.
def ReadExcel():
    
    df = pd.read_excel(
            io="supermarkt_sales.xlsx",
            engine="openpyxl",
            sheet_name="Sales",
            skiprows=3,
            usecols="B:R",
            nrows=1000,
        )

    df["hour"] = pd.to_datetime(df["Time"], format="%H:%M").dt.hour
    return df
    
df = ReadExcel()


#---------SIDEBAR---------
    
sidebar = st.sidebar.header("Please filter here: ")

city = st.sidebar.multiselect(
    "Select the City: ",
    options=df["City"].unique(),
    default=df["City"].unique()
)

customer_type = st.sidebar.multiselect(
    "Select the Customer Type: ",
    options=df["Customer_type"].unique(),
    default=df["Customer_type"].unique()
)

gender = st.sidebar.multiselect(
    "Select the Gender: ",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

df_selection = df.query(
    "City == @city & Customer_type == @customer_type & Gender == @gender"
)



#-----MAIN PAGE------
st.title(":bar_chart: Sales Dashboard").markdown("##")

#-----VALUES--------
total_sales = round(float(df_selection["Total"].sum()), 2)
avg_sale_by_transaction = float(round(df_selection["Total"].mean(), 2))
avg_rating = round(df["Rating"].mean(), 2)
star_rating = ":star:" * int(round(avg_rating, 0))

left_column, middle_column, right_column = st.columns(3)

with left_column:
    st.subheader("Total Sales")
    st.subheader(f"USD ${total_sales:,}")
    
with middle_column:
    st.subheader("Average Rating")
    st.subheader(f"{avg_rating} {star_rating}")
    
with right_column:
    st.subheader("Average Sales per Transaction")
    st.subheader(f" USD ${avg_sale_by_transaction}")
    
st.markdown("---")


# SALES BY PRODUCT LINE [BAR CHART]
sales_by_product_line = (
    df_selection.groupby(by=["Product line"]).sum()[["Total"]].sort_values(by="Total")
)

fig = px.bar(
    sales_by_product_line,
    x="Total",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Sales by Product Line</b>",
    color_discrete_sequence=["#FF3B3B"] * len(sales_by_product_line),
    template="plotly_white",
)

fig.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


# SALES BY HOUR [BAR CHART]
sales_by_hour = df_selection.groupby(by=["hour"]).sum()[["Total"]]

fig_hourly_sales = px.bar(
    sales_by_hour,
    x=sales_by_hour.index,
    y="Total",
    title="<b>Sales by hour</b>",
    color_discrete_sequence=["#FF3B3A"] * len(sales_by_hour),
    template="plotly_white",
)
fig_hourly_sales.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)


left_column, right_column = st.columns(2)

left_column.plotly_chart(fig, use_container_width=True)
right_column.plotly_chart(fig_hourly_sales, use_container_width=True)


st.markdown("---")
st.markdown(body="**Database**")
st.dataframe(df_selection)
st.markdown("---")


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: show;}
            header {visibility: show;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


