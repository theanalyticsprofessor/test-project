import sqlite3
import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

# path to our SQLite database
database_path = 'chinook.db'

# connect to the sqlite database
connection = sqlite3.connect(database_path)

# create a cursor object to execute SQL queries
cursor = connection.cursor()

# write your SQL query
query = """SELECT 
            albums.Title AS AlbumTitle, artists.Name AS ArtistName
        FROM 
            albums
        INNER JOIN 
            artists 
        ON 
            albums.ArtistId = artists.ArtistId
        ORDER BY 
            artists.Name"""

# execute the query 
cursor.execute(query)

# fetch all results from the executed query
results = cursor.fetchall()

results = pd.DataFrame(results)

results = results.rename(columns={0:'Album', 1:'Artist'})

# close the connection
connection.close()

st.subheader("Chinook Albums and Artists")
st.dataframe(results, use_container_width=True)

