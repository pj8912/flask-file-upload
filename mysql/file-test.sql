create table upload_file(
file_id int AUTO_INCREMENT PRIMARY KEY NOT null,
file_name text not null,
created_at datetime DEFAULT CURRENT_TIMESTAMP,
created_date TEXT
);

create table upload_file_on_db(
file_id int auto_increment primary key not null,
file BLOB,
file_name text,
created_at datetime default current_timestamp
);
