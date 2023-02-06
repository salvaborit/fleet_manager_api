-- creates a django db 'todo_dev_db' with utf8 charset
-- creates superuser 'todo_dev' + grants

CREATE DATABASE IF NOT EXISTS fm_db CHARACTER SET utf8;

CREATE USER IF NOT EXISTS 'fm_dev'@'localhost' IDENTIFIED BY 'dev_pwd';
GRANT ALL PRIVILEGES ON fm_db.* TO 'fm_dev'@'localhost';
FLUSH PRIVILEGES;
