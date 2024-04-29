import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="mydb"
)

# Create a cursor object
cursor = mydb.cursor()

# Query without using JOIN
query = """
SELECT l.location_id, l.street_address, l.city, l.state_province, c.country_name
FROM locations l, countries c
WHERE l.country_id = c.country_id
AND c.country_name = 'Canada'
"""

# Execute the query
cursor.execute(query)

# Fetch all the results
results = cursor.fetchall()

# Print the results
for result in results:
    print(result)

# Close the cursor and connection
cursor.close()
mydb.close()