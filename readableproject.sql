PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE User(
user_id INTEGER PRIMARY KEY AUTOINCREMENT,
email VARCHAR(50) NOT NULL);
INSERT INTO "User" VALUES(1,'email@mail.com');
INSERT INTO "User" VALUES(2,'user@mail.com');
CREATE TABLE Clothing_type(
type_id INTEGER PRIMARY KEY AUTOINCREMENT,
type_desc VARCHAR(20) NOT NULL);
INSERT INTO "Clothing_type" VALUES(1,'Shirt');
INSERT INTO "Clothing_type" VALUES(2,'Skirt');
INSERT INTO "Clothing_type" VALUES(3,'Dress');
CREATE TABLE Size(
sizes INTEGER PRIMARY KEY);
INSERT INTO "Size" VALUES(1);
INSERT INTO "Size" VALUES(2);
INSERT INTO "Size" VALUES(3);
CREATE TABLE Style_code(
code_id VARCHAR(6) PRIMARY KEY,
code_desc VARCHAR(20) NOT NULL);
INSERT INTO "Style_code" VALUES('Formal','Formal Attire');
INSERT INTO "Style_code" VALUES('Casual','Casual Attire');
INSERT INTO "Style_code" VALUES('BisCas','Business Casual');
CREATE TABLE Wish(
wish_id INTEGER PRIMARY KEY AUTOINCREMENT,
 w_size INTEGER(2) NOT NULL
REFERENCES Size,
w_style VARCHAR(6) NOT NULL
REFERENCES Style_code,
 w_item_type VARCHAR(20) NOT NULL,
 w_active BOOLEAN NOT NULL DEFAULT 1,
w_pic VARCHAR(200),
 user_email VARCHAR(50) NOT NULL
REFERENCES User);
INSERT INTO "Wish" VALUES(1,1,'Formal','1',1,NULL,'user@mail.com');
INSERT INTO "Wish" VALUES(2,1,'BisCas','2',1,NULL,'user@mail.com');
CREATE TABLE Share(

share_id INTEGER PRIMARY KEY AUTOINCREMENT, 

s_size INTEGER(2) NOT NULL 

REFERENCES Style_code,

s_style VARCHAR(6) NOT NULL

REFERENCES Style_code,

s_item_type VARCHAR(20) NOT NULL

REFERENCES Clothing_type,

s_active BOOLEAN NOT NULL DEFAULT 1,

s_pic VARCHAR(200), 

 user_email VARCHAR(50) NOT NULL 

 REFERENCES User);
INSERT INTO "Share" VALUES(1,1,'BisCas','2',1,NULL,'mail@email.com');
INSERT INTO "Share" VALUES(2,1,'Formal','3',1,NULL,'mail@email.com');
DELETE FROM sqlite_sequence;
INSERT INTO "sqlite_sequence" VALUES('User',2);
INSERT INTO "sqlite_sequence" VALUES('Clothing_type',3);
INSERT INTO "sqlite_sequence" VALUES('Wish',2);
INSERT INTO "sqlite_sequence" VALUES('Share',2);
COMMIT;
