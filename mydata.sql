show databases;

USE `mydata`;

CREATE TABLE `user` (
  `userid` int NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` enum('admin','user') NOT NULL,
  `country` varchar(350) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `user`
  ADD PRIMARY KEY (`userid`);

ALTER TABLE `user`
  MODIFY `userid` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;  
  
INSERT INTO user VALUES(1,"xyz", "xyzS12@gmail.com","xy123","user","India"); 

SELECT * FROM user WHERE email = "xyzS12@gmail.com" AND password = "xy123";

SELECT * FROM `user`;

UPDATE `user` SET role ="user", country ="India" WHERE userid = "7";

UPDATE `user` SET role = "admin" WHERE userid = "7";

DELETE FROM `user` WHERE email = "xyzS12@gmail.com";

DELETE FROM user WHERE email = "xyzS12@gmail.com" AND userid = "1";

SELECT name, userid, role, email
FROM user;

UPDATE `user` SET name ="Aarti", role ="user", country ="India" WHERE userid = 4;

INSERT INTO `user` (`userid`,`name`, `email`,`password`,`role`,`country`) VALUES (4,"abc","xyz@gmail.com","xyz","user","user");

DELETE FROM user WHERE userid = "5";
