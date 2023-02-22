show databases;

USE `mydata`;


CREATE TABLE user (
  userid INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255),
  email VARCHAR(255),
  password VARCHAR(255),
  role ENUM('admin', 'user'),
  country varchar(350)
) ENGINE=InnoDB CHARSET=utf8mb4;


INSERT INTO user (name, email, password, role, country) VALUES ('xyz', 'xy123@example.com', 'xyz12', 'admin', 'USA');
 

SELECT * FROM user WHERE email = "xy123@example.com" AND password = "xyz12";

desc user;

UPDATE user SET role ="user", country ="India" WHERE userid = "";

UPDATE `user` SET role = "admin" WHERE userid = "1";

DELETE FROM user WHERE userid = 1;

DELETE FROM user WHERE userid = "3";

SELECT name, userid, role, email
FROM user;

SELECT * FROM user WHERE userid = "2";

UPDATE user SET name ="mickey", role ="user", country ="India" WHERE userid = 2;

SELECT * FROM user;

UPDATE user SET name ="Aarti", role ="user", country ="India" WHERE userid = 4;

DELETE FROM user WHERE userid = "5";
