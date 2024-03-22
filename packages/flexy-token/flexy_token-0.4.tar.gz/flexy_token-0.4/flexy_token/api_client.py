import requests
from datetime import timezone
import jwt
import psycopg2

class APIClient:
	def __init__(self, account_sid, api_secret,api_key,identity):
		self.account_sid = account_sid
		self.api_secret = api_secret
		self.api_key= api_key
		self.identity=identity
		

def AccessToken(account_sid,api_secret,api_key,identity=""):
		try:
		
			payload = {
				'account_sid': account_sid,
				'api_key': api_key,
				'api_secret': api_secret,
				'identity': identity,
			}   
			token = jwt.encode(payload, 'your_secret_key', algorithm='HS256')
			
			print (token,'tokentt')

			try:
				connection = psycopg2.connect(
					dbname="macha_flexydial",
					user="flexydial",
					password="flexydial",
					host="10.12.0.84",
					port="5432"
				)
				print("Connected to the database.",connection)
				identity_found = False
				mycursor = connection.cursor()
				mycursor.execute('SELECT * FROM connector_usertoken;')
				for i in mycursor:
					if identity in i:
						identity_found = True
				if identity_found == False:
					query=("INSERT INTO connector_usertoken VALUES (DEFAULT,%s,%s);")
					table_values = (identity,token)
					mycursor.execute(query,table_values)
					connection.commit()
			except psycopg2.Error as e:
				print("Unable to connect to the database:", e)

			finally:
				connection.close()

			return token

		except Exception as e:
			return f"Token unable to generate because of an exception"


 
