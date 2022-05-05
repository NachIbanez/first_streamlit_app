####################
##Import libraries##
####################

import streamlit
import pandas

#####################################
#Variable declarations and functions#
#####################################

#Panda's function to read CSV FILES 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


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
streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index))

#Display the table of the page
streamlit.dataframe(my_fruit_list)


