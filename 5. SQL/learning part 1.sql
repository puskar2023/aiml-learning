CREATE DATABASE college;

CREATE DATABASE IF NOT EXISTS instagram;

USE instagram;

CREATE TABLE user(
id INT,
age INT,
name VARCHAR(30) NOT NULL,
email VARCHAR(30) UNIQUE,
followers INT DEFAULT 0,
following INT,
CONSTRAINT age_check CHECK (age >= 13),
PRIMARY KEY (id)
);

INSERT INTO user
(id, age, name, email, followers, following)
VALUES
(1, 14, "adam", "adam@yahoo.in", 124, 145),
(2, 15, "bob", "bob@yahoo.in", 120, 140),
(3, 17, "adam", "sarthak@gmail.com", 120, 145);

INSERT INTO user
(id, age, name, email, followers, following)
VALUES
(4, 17, "donald", "donald@gmail.com", 200, 105),
(5, 14, "eve", "eve@yahoo.in", 400, 145),
(6, 16, "farah", "farah@gmail.com", 10000, 1000);

SELECT id, name, email FROM user;
SELECT DISTINCT name FROM user;
SELECT * FROM user;

SELECT name, followers
FROM user
WHERE age > 15 OR followers >= 120;

SELECT name, followers
FROM user
WHERE age  BETWEEN 15 AND 17;

SELECT name, age, email, followers
FROM user
WHERE age NOT IN (14, 16)
LIMIT 2;

SELECT name, age, email, followers
FROM user
ORDER BY followers DESC;

SELECT MAX(followers) 
FROM user;

SELECT count(id)
FROM user
WHERE followers > 125;

SELECT age, max(followers)
FROM user
GROUP BY age
HAVING max(followers) >= 200;

UPDATE user
SET followers = 600
WHERE age = 17;

SELECT * FROM user;

DELETE FROM user
WHERE age = 15;

ALTER TABLE user
ADD COLUMN city VARCHAR(25) DEFAULT "Delhi";

ALTER TABLE user
DROP COLUMN age;

ALTER TABLE instaUser
RENAME TO user;

ALTER TABLE user
CHANGE COLUMN followers subs INT DEFAULT 0;

ALTER TABLE user
MODIFY subs INT DEFAULT 5;

TRUNCATE TABLE user;

SELECT * FROM user;

SET SQL_SAFE_UPDATES = 0;

CREATE TABLE post(
id INT PRIMARY KEY,
content VARCHAR(100),
user_id INT,
FOREIGN KEY(user_id) REFERENCES user(id)
);

DROP TABLE post;

