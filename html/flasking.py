from flask import Flask, render_template
import sqlite3
import os
app = Flask(__name__,template_folder=os.path.join(os.getcwd(),'/var/www/html'))
@app.route('/')
def index():
	conn = sqlite3.connect("/home/traker/Desktop/zadanka/weather_data.db")
	cursor = conn.cursor()
	
	cursor.execute("Select * from weather")
	row = cursor.fetchall()
	conn.close()
	return render_template('index.html',row=row)
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
