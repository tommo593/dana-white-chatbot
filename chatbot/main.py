import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

mydb = mysql.connector.connect(
    host = "cloud.mindsdb.com",
    user = os.environ.get("tomdevwork@gmail.com"),
    password = os.environ.get("TdBourne0108."),
    port = "3306"
)

cursor = mydb.cursor()
cursor.execute('''SELECT response from mindsdb.danawhite_model WHERE author_username = "mindsdb" AND text='why are UFC fighters so underpaid in comparison to the NFL?' ''')


for x in cursor:
    print(x)