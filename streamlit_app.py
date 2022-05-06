####################
##Import libraries##
####################

import streamlit
import pandas
import requests

#####################################
#Variable declarations and functions#
#####################################

#Panda's function to read CSV FILES 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")


#####################
#Start of the script#
#####################

streamlit.title('My Mom\'s New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#Let's put a pick up list here so they can pick the fruit they want to include
#multiselect(text to include, the list to use, the default selected fruits)

fruits_selected = streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#Display the table of the page

streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit Advice!')
streamlit.text(fruityvice_response.json())


