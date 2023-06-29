from flask import Flask, render_template, request, redirect
import mysql.connector
import os 
from dotenv import load_dotenv

app = Flask(__name__, static_folder='uploads')
app.secret_key = "SECRET"

load_dotenv()

HOST = os.environ.get("DB_HOST")
USERNAME = os.environ.get("DB_USERNAME")
PWD = os.environ.get("DB_PWD")
DBNAME = os.environ.get("DB_NAME")


cnx = mysql.connector.connect(user=USERNAME, password=PWD, host=HOST, database=DBNAME)
cursor = cnx.cursor()

from datetime import date
today = date.today()
day = today.day
month_word = today.strftime("%B")
year = today.year
#today's date
todays_date = str(day)+' '+month_word+' '+str(year)

app.config["UPLOAD_FOLDER"] = "uploads"
app.use_static_route = True


import datetime
ts = datetime.datetime.now().timestamp()
ts = int(ts)
ts = str(ts)



def convertToBinaryData(filename):
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload-file', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        main_file = request.files['file']
        main_file_name = main_file.filename
        file_extension = main_file_name.rsplit('.', 1)[1].lower()
        new_file_name = ts+'.'+file_extension
        main_file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_file_name))
        cursor.execute("INSERT INTO upload_file(file_name, created_date) VALUES(%s,%s)", (new_file_name, todays_date))
        cnx.commit()
        return redirect('/')
    else:
        return redirect('/')




# alt upload
@app.route('/altupload')
def alt_upload():
    return render_template('alt-upload.html')

#upload file on database
@app.route('/dbupload', methods=['POST'])
def upload_file_ondb():
    if request.method == 'POST':
        main_file = request.files['file']
        main_file_name = main_file.filename
        file_extension = main_file_name.rsplit('.', 1)[1].lower()
        new_file_name = ts+'.'+file_extension
        main_file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_file_name))
        x = os.path.join(app.config['UPLOAD_FOLDER'], new_file_name)

        new_file = convertToBinaryData(x)
        cursor.execute("INSERT INTO upload_file_on_db(file,file_name) VALUES(%s,%s)", (new_file,new_file_name))
        cnx.commit()
        return redirect('/')
    else:
        return redirect('/')



@app.route('/viewfile')
def view_file():
    sql = """SELECT * FROM upload_file"""
    cursor.execute(sql)
    result = cursor.fetchall()
    return render_template('view.html', all_images=result)

if __name__ == "__main__":
    app.run(debug=True,port=3000)
