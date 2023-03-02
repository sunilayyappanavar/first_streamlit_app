
import streamlit
import pandas

streamlit.title("My Parents New Healthy Diner")

streamlit.header("Breakfast Menu")
streamlit.text("🥣 Omega 3 & Bluberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞 Avokado Toast")

streamlit.header("🍌🥭 Build Your Own Fruit Smoothie 🍊🍇")

my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits", list(my_fruit_list.index),["Avocado","Strawberries"])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#------------------------------------------------------------
import requests

streamlit.header("Fruityvice Fruit Advice!")

#asking input from the user
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#seperate the base url from the fruit name
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "Kiwi")
#instead of Kiwi, adding user entered fruit choice, so that user entered fruit is directly fecthed using the api
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

#normalizing json vesion
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# displays the data in table format
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

