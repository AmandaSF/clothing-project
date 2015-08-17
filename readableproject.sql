PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE users(
user_id INTEGER PRIMARY KEY AUTOINCREMENT,
email VARCHAR(50) NOT NULL,
user_name VARCHAR(20) NOT NULL,
password VARCHAR(50) NOT NULL);
INSERT INTO "users" VALUES(1,'email@mail.com', 'email', 'abc');
INSERT INTO "users" VALUES(2,'user@mail.com', 'user', '123');
INSERT INTO "users" VALUES(3,'amandafuhrmann@gmail.com', 'amanda', 'fuhrmann');
CREATE TABLE clothing_types(
type_id INTEGER PRIMARY KEY AUTOINCREMENT,
type_desc VARCHAR(20) NOT NULL);
INSERT INTO "clothing_types" VALUES(1,'Shirt');
INSERT INTO "clothing_types" VALUES(2,'Skirt');
INSERT INTO "clothing_types" VALUES(3,'Dress');
CREATE TABLE sizing(
sizes INTEGER PRIMARY KEY);
INSERT INTO "sizing" VALUES(1);
INSERT INTO "sizing" VALUES(2);
INSERT INTO "sizing" VALUES(3);
CREATE TABLE styling(
code_id VARCHAR(6) PRIMARY KEY,
code_desc VARCHAR(20) NOT NULL);
INSERT INTO "styling" VALUES('Formal','Formal Attire');
INSERT INTO "styling" VALUES('Casual','Casual Attire');
INSERT INTO "styling" VALUES('BisCas','Business Casual');
CREATE TABLE post_types(
post_type_id VARCHAR(6) PRIMARY KEY);
INSERT INTO "post_types" VALUES('Wish');
INSERT INTO "post_types" VALUES('Share');
CREATE TABLE posting(
post_id INTEGER PRIMARY KEY AUTOINCREMENT,
size INTEGER(2) NOT NULL
REFERENCES sizing,
style VARCHAR(6) NOT NULL
REFERENCES styling,
item_type VARCHAR(20) NOT NULL
REFERENCES clothing_types,
active BOOLEAN NOT NULL DEFAULT 1,
pic VARCHAR(200),
user_email VARCHAR(50) NOT NULL
REFERENCES users,
post_types VARCHAR(6) NOT NULL
REFERENCES post_type_id);
INSERT INTO "posting" VALUES(1,1,'Formal','Skirt',1,NULL,'email@mail.com','Wish');
INSERT INTO "posting" VALUES(2,1,'Formal','Skirt',1,NULL,'user@mail.com','Share');
INSERT INTO "posting" VALUES(3,2,'Formal Attire','Shirt',1,NULL,'amandafuhrmann@gmail.com','Wish');
INSERT INTO "posting" VALUES(4,3,'Casual Attire','Shirt',1,'','amandafuhrmann@gmail.com','Share');
INSERT INTO "posting" VALUES(5,2,'Formal Attire','Shirt',1,'','amandafuhrmann@gmail.com','Wish');
INSERT INTO "posting" VALUES(6,3,'Business Casual','Shirt',1,'','user@mail.com','Share');
INSERT INTO "posting" VALUES(7,3,'Casual Attire','Shirt',1,'','amandafuhrmann@gmail.com','Share');
INSERT INTO "posting" VALUES(8,2,'Casual Attire','Skirt',1,'','amandafuhrmann@gmail.com','Wish');
INSERT INTO "posting" VALUES(9,1,'Formal Attire','Dress',1,'','amandafuhrmann@gmail.com','Wish');
DELETE FROM sqlite_sequence;
INSERT INTO "sqlite_sequence" VALUES('User',2);
INSERT INTO "sqlite_sequence" VALUES('Clothing_type',3);
INSERT INTO "sqlite_sequence" VALUES('posting',9);
INSERT INTO "sqlite_sequence" VALUES('users',3);
COMMIT;
