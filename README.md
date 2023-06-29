
![flask-file](https://github.com/pj8912/flask-file-upload/assets/59218902/b8208310-8f76-4961-bcd6-1474d803c2b3)

# File Uploading in Flask
Uploading files using flask and mysqlab

Two ways of uploading files in Flask, 
- Only directly into the folder
- Into database from the folder

Files are saved in database as binaries, so the uploaded file is converted to binary before upload and saved as a `blob` in the database. 

## Requirements
- Python `3.10.6`

## Install
- **Clone **
```
https://github.com/pj8912/flask-file-upload.git
```

- Create `virtual environment` and **activate**

- ** Install requirements **
```
pip install requirements.txt
```

## Configuration 
- I used mysql for this project

- Create an `.env` and add appropiate values for your mysql setup 

- `.env` variables : 
    - DB_HOST=
    - DB_USERNAME=
    - DB_PWD=
    - DB_NAME=file-test

Host, username, password and database name

My database name is `file-test`

- SQL file
Import sql file from `mysql/file-test.sql`

## Run

``` 
python app.py
```