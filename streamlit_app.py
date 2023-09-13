import streamlit
streamlit.title ( 'My parents New Healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')    
streamlit.text ('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import Pandas 
my_fruit_list = pandas.read_csv("https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html")
streamlit.dataframe(my_fruit_list)
