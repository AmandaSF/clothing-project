PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE users(
user_id INTEGER PRIMARY KEY AUTOINCREMENT,
email VARCHAR(50) NOT NULL,
user_name VARCHAR(20) NOT NULL,
password VARCHAR(50) NOT NULL);
INSERT INTO "users" VALUES(1,'email@mail.com','email','abc');
INSERT INTO "users" VALUES(2,'user@mail.com','Knighter','123');
INSERT INTO "users" VALUES(3,'amandafuhrmann@gmail.com','Amanda','fuhrmann');
INSERT INTO "users" VALUES(4,'ginger@mail.com','Ginger++','ale');
INSERT INTO "users" VALUES(5,'rebecca.bruggman@gmail.com','bexcitement','test');
INSERT INTO "users" VALUES(15,'person@mail.com','person','person');
INSERT INTO "users" VALUES(16,'afag@gmail.com','sibel','puff39');
CREATE TABLE clothing_types(
type_id INTEGER PRIMARY KEY AUTOINCREMENT,
type_desc VARCHAR(20) NOT NULL);
INSERT INTO "clothing_types" VALUES(1,'Shirt');
INSERT INTO "clothing_types" VALUES(2,'Skirt');
INSERT INTO "clothing_types" VALUES(3,'Dress');
CREATE TABLE sizing(
sizes INTEGER PRIMARY KEY);
INSERT INTO "sizing" VALUES(2);
INSERT INTO "sizing" VALUES(4);
INSERT INTO "sizing" VALUES(6);
INSERT INTO "sizing" VALUES(8);
INSERT INTO "sizing" VALUES(10);
INSERT INTO "sizing" VALUES(12);
INSERT INTO "sizing" VALUES(14);
INSERT INTO "sizing" VALUES(16);
INSERT INTO "sizing" VALUES(18);
INSERT INTO "sizing" VALUES(20);
INSERT INTO "sizing" VALUES(22);
INSERT INTO "sizing" VALUES(24);
INSERT INTO "sizing" VALUES(26);
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
INSERT INTO "posting" VALUES(1,6,'Formal','Skirt',1,'http://www.factsnfunny.com/wp-content/uploads/2015/03/e1a7200445fe572c22d5818de8a978c8.jpg','email@mail.com','Wish');
INSERT INTO "posting" VALUES(2,8,'Formal','Skirt',1,'http://i.ebayimg.com/00/s/MzAwWDI0Ng==/z/T0QAAOSwQItUAAGe/$_35.JPG?set_id=2','user@mail.com','Share');
INSERT INTO "posting" VALUES(3,2,'Formal Attire','Shirt',1,'https://s-media-cache-ak0.pinimg.com/236x/d7/66/a5/d766a56852b9b40f026045d374a1ff7d.jpg','amandafuhrmann@gmail.com','Wish');
INSERT INTO "posting" VALUES(4,4,'Casual Attire','Shirt',1,'https://pinkemma.s3-ap-southeast-1.amazonaws.com/uploads/2015/06/10/TF10001063002%20-%20Shuna%20Polka%20Top-%20psoe%20zoom_84x84.jpg','amandafuhrmann@gmail.com','Share');
INSERT INTO "posting" VALUES(5,2,'Formal Attire','Shirt',1,'http://stat.homeshop18.com/homeshop18/images/productImages/214/300x300_70d84fff8e0757e5ea2e516d62ad0562.jpg','amandafuhrmann@gmail.com','Wish');
INSERT INTO "posting" VALUES(6,6,'Business Casual','Shirt',1,'','user@mail.com','Share');
INSERT INTO "posting" VALUES(7,14,'Casual Attire','Shirt',1,'','amandafuhrmann@gmail.com','Share');
INSERT INTO "posting" VALUES(8,20,'Casual Attire','Skirt',1,'','amandafuhrmann@gmail.com','Wish');
INSERT INTO "posting" VALUES(9,2,'Formal Attire','Dress',1,'','amandafuhrmann@gmail.com','Wish');
INSERT INTO "posting" VALUES(10,4,'Formal Attire','Shirt',1,'','amandafuhrmann@gmail.com','Wish');
INSERT INTO "posting" VALUES(11,2,'Formal Attire','Shirt',1,'','user@mail.com','Share');
INSERT INTO "posting" VALUES(12,4,'Casual Attire','Dress',1,'','amandafuhrmann@gmail.com','Wish');
INSERT INTO "posting" VALUES(13,2,'Formal Attire','Skirt',1,'','amandafuhrmann@gmail.com','Wish');
INSERT INTO "posting" VALUES(14,2,'Formal Attire','Shirt',0,'','ginger@mail.com','Wish');
INSERT INTO "posting" VALUES(15,10,'Formal Attire','Shirt',1,'','amandafuhrmann@gmail.com','Wish');
INSERT INTO "posting" VALUES(16,14,'Casual Attire','Shirt',0,'http://img.photobucket.com/albums/v719/DL_Amanda/WWII%20Collection/IMG_20150411_202437.jpg','ginger@mail.com','Wish');
INSERT INTO "posting" VALUES(17,2,'Formal Attire','Shirt',1,'','amandafuhrmann@gmail.com','Share');
INSERT INTO "posting" VALUES(18,12,'Formal Attire','Shirt',1,'','amandafuhrmann@gmail.com','Wish');
INSERT INTO "posting" VALUES(19,8,'Formal Attire','Dress',1,'http://img.shein.com/images/sheinside.com/201407/1405921746308585500.jpg','amandafuhrmann@gmail.com','Wish');
INSERT INTO "posting" VALUES(20,8,'Formal Attire','Dress',1,'http://productshots1.modcloth.net/productshots/0129/9183/0d519116cdb1be9531ffb90ab992ab59.jpg?1371070350','','Wish');
INSERT INTO "posting" VALUES(21,10,'Casual Attire','Skirt',1,'','amandafuhrmann@gmail.com','Share');
INSERT INTO "posting" VALUES(22,16,'Formal Attire','Skirt',1,'http://i00.i.aliimg.com/wsphoto/v0/32220046106/.jpg','amandafuhrmann@gmail.com','Share');
INSERT INTO "posting" VALUES(23,16,'Casual Attire','Shirt',1,'http://fashionimpaq.com/images/plus-top-white.jpg','ginger@mail.com','Share');
INSERT INTO "posting" VALUES(24,18,'Casual Attire','Dress',1,'http://astrotarot.net/wp-content/uploads/2015/08/dress.jpg','ginger@mail.com','Wish');
INSERT INTO "posting" VALUES(25,4,'Casual Attire','Shirt',1,'http://i00.i.aliimg.com/wsphoto/v0/551332012_1/Women-s-High-quality-Chiffon-Shirt-ladies-Fashion-Sleeveless-T-shirt-with-corsage-Princess-blouse-Free.jpg','ginger@mail.com','Wish');
INSERT INTO "posting" VALUES(26,4,'Formal Attire','Dress',0,'http://butiqshop.com/wp-content/uploads/2015/05/Dresses-butiqshop.com-38.jpg','ginger@mail.com','Wish');
INSERT INTO "posting" VALUES(27,22,'Formal Attire','Shirt',1,'http://i00.i.aliimg.com/wsphoto/v6/484155722_1/Free-shipping-2014-Office-Ladies-black-skirt-New-Design-Office-Skirt.jpg','ginger@mail.com','Wish');
INSERT INTO "posting" VALUES(28,22,'Business Casual','Shirt',1,'http://www.motivators.com/images/products/Promotional-Vantage-Eagle-Womens-No-Iron-Pinpoint-Oxford-Dress-Shirt-50695.jpg','ginger@mail.com','Share');
INSERT INTO "posting" VALUES(29,24,'Casual Attire','Skirt',1,'http://www.allfreesewing.com/master_images/AllFreeSewing/anthro-ruffled-skirt-tutorial.jpg','ginger@mail.com','Wish');
DELETE FROM sqlite_sequence;
INSERT INTO "sqlite_sequence" VALUES('User',2);
INSERT INTO "sqlite_sequence" VALUES('Clothing_type',3);
INSERT INTO "sqlite_sequence" VALUES('posting',29);
INSERT INTO "sqlite_sequence" VALUES('users',16);
COMMIT;
