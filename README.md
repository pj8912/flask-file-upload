# flask-file-upload
Uploading files using flask and mysql

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