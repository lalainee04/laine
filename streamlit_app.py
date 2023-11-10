import streamlit 
import pandas 
import requests
import snowflake.connector 
from urllib.error import URLError 

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#display the table on the page 

#create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
	Fruity_response = requests.get("http://fruityvice.com/api/fruit/" + this_fruit_choice)
	fruityvice_normalized = pandas.json_normalize(fruity_response.json())
	return fruityvice_normalized

#New Section to display fruityvice api response 
streamlit.header('Fruityvice Fruit Advice!')
try: 
	fruit_choice = streamlit.text_input('What fruit would you like information about?')
	if not fruit_choice:
		streamlit.error("Please select a fruit to get information.")
	else: 
		Fruity_response = requests.get("http://fruityvice.com/api/fruit"+fruit_choice)
		fruityvice_normalized = pandas.json_normalize(fruity_response.json())
		streamlit.dataframe(back_from_function)

except URLError as e:
	streamlit.error 
streamlit.header("The fruit load list contains:")
#Snowflake-related functions
	def get_fruit_load_list():
	with my_cur.cursor() as my)cur:
		my_cur.execute("select * from fruit_load_list")
		return my_cur.fetchall()
		
# Add a button to load the fruit 
	if streamlit.button('Get fruit List'):
	my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
	my_data_rows = get_fruit_load_list()
	streamlit.dataframe(my_data_rows)
	



streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 

#import snowflake.connector


#display the table on the page 
streamlit.dataframe(fruits_to_show)


# don't run anything past here while we troubleshoot 
streamlit.stop()

#import snowflake.connector


#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

streamlit.header("Fruityvice Fruit Advice!")


# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

# Allow the end user to add a fruit to the list 
add_my_fruit = streamlit.text_input ('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)
               
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)




