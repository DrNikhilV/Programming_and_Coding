Create database Activity1;
Use Activity1;

CREATE table Salesman (Salesman_id Integer Primary Key, Name text NOT NULL, City text, Commission Float NOT NULL);

Insert into Salesman values(5001, 'James Hoog', 'Newyork', 0.15);
Insert into Salesman values(5002, 'Nail Knite', 'Paris', 0.13);
Insert into Salesman values(5005, 'Pit Alex', 'London', 0.11);
Insert into Salesman values(5006, 'Mc Lyon', 'Paris', 0.14);
Insert into Salesman values(5003, 'Lauson Hen', NULL, 0.12);
Insert into Salesman values(5007, 'Paul Adam', 'Rome', 0.13);

Select * from Salesman;

CREATE TABLE Customer(Customer_id INTEGER PRIMARY KEY, Customer_name TEXT NOT NULL, City TEXT NOT NULL, Grade INTEGER, Salesman_id INTEGER);
INSERT INTO Customer VALUES(3002, 'Nick Rimando','Newyork', 100, 5001);
INSERT INTO Customer VALUES(3005, 'Graham Lusi','California', 200, 5002);
INSERT INTO Customer VALUES(3001, 'Brad Guran','London', NULL, NULL);
INSERT INTO Customer VALUES(3004, 'Fabian Johns','Paris', 300, 5006);
INSERT INTO Customer VALUES(3007, 'Brad Davis','Newyork', 200, 5001);
INSERT INTO Customer VALUES(3009, 'Geoff Camero','Berlin', 100, NULL);
INSERT INTO Customer VALUES(3008, 'Julian Green','London', 300, 5002);
INSERT INTO Customer VALUES(3003, 'Jory Altidor','Moncow', 200, 5007);

Select * from Customer;

CREATE table Salesman_Order (Order_no INTEGER PRIMARY KEY, Purch_amt FLOAT NOT NULL, Order_date DATE NOT NULL, Customer_id Integer NOT NULL, Salesman_id Integer);

Insert into Salesman_Order values(70001, 150.5, '2016-10-05', 3005, 5002);
Insert into Salesman_Order values(70009, 270.65, '2016-09-10', 3001, NULL);
Insert into Salesman_Order values(70002, 65.26, '2016-10-05', 3002, 5001);
Insert into Salesman_Order values(70004, 110.5, '2016-08-17', 3009, NULL);
Insert into Salesman_Order values(70007, 948.5, '2016-09-10', 3005, 5002);
Insert into Salesman_Order values(70005, 2400.6, '2016-07-27', 3007, 5001);
Insert into Salesman_Order values(70008, 5760, '2016-09-10', 3002, 5001);
Insert into Salesman_Order values(70010, 1983.43, '2016-10-10', 3004, 5006);
Insert into Salesman_Order values(70003, 2480.4, '2016-10-10', 3009, NULL);
Insert into Salesman_Order values(70012, 250.45, '2016-06-27', 3008, 5002);
Insert into Salesman_Order values(70011, 75.29, '2016-08-17', 3003, 5007);

Select * from Salesman_Order;

CREATE TABLE noble_win (
    YEAR INTEGER NOT NULL,
    SUBJECT TEXT(40) NOT NULL,
    WINNER TEXT(40) NOT NULL,
    COUNTRY TEXT(40) NOT NULL,
    CATEGORY TEXT(40) NOT NULL
);
INSERT INTO noble_win VALUES
(1970,'Physics','Hannes Alfven','Sweden','Scientist'),
(1970,'Physics','Louis Neel','France','Scientist'),
(1970,'Chemistry','Luis Federico Leloir','France','Scientist'),
(1970,'Physiology','Ulf von Euler','Sweden','Scientist'),
(1970,'Physiology','Bernard Katz','Germany','Scientist'),
(1970,'Literature','Aleksandr Solzhenitsyn','Russia','Linguist'),
(1970,'Economics','Paul Samuelson','USA','Economist'),
(1970,'Physiology','Julius Axelrod','USA','Scientist'),
(1971,'Physics','Dennis Gabor','Hungary','Scientist'),
(1971,'Chemistry','Gerhard Herzberg','Germany','Scientist'),
(1971,'Peace','Willy Brandt','Germany','Chancellor'),
(1971,'Literature','Pablo Neruda','Chile','Linguist'),
(1971,'Economics','Simon Kuznets','Russia','Economist'),
(1978,'Peace','Anwar al-Sadat','Egypt','President'),
(1978,'Peace','Menachem Begin','Israel','Prime Minister'),
(1987,'Chemistry','Donald J. Cram','USA','Scientist'),
(1987,'Chemistry','Jean-Marie Lehn','France','Scientist'),
(1987,'Physiology','Susumu Tonegawa','Japan','Scientist'),
(1994,'Economics','Reinhard Selten','Germany','Economist'),
(1994,'Peace','Yitzhak Rabin','Israel','Prime Minister'),
(1987,'Physics','Johannes Georg Bednorz','Germany','Scientist'),
(1987,'Literature','Joseph Brodsky','Russia','Linguist'),
(1987,'Economics','Robert Solow','USA','Economist'),
(1994,'Literature','Kenzaburo Oe','Japan','Linguist');

Select * from noble_win;

-- Problem 01
Select Name, Commission from Salesman;

-- Problem 02
Select distinct(Salesman_id) from Salesman;

-- Problem 03
Select Name, City from Salesman where City = 'Paris';

-- Problem 04
Select * from Customer where Grade = 200;

-- Problem 05
Select Order_no, Purch_amt, Order_date from Salesman_Order where Salesman_id = 5001;

-- Problem 06
SELECT WINNER FROM noble_win WHERE YEAR = 1971 AND SUBJECT = 'Literature';

-- Problem 07
SELECT * FROM noble_win WHERE WINNER LIKE 'Louis%';

-- Problem 08
SELECT * FROM noble_win WHERE (SUBJECT='Physics' AND YEAR = 1970) OR (SUBJECT='Economics' AND YEAR = 1971);

-- Problem 09
SELECT * FROM noble_win WHERE YEAR = 1970 AND NOT(SUBJECT = 'Physiology'
OR SUBJECT = 'Economics');

-- Problem 10
SELECT * FROM noble_win WHERE SUBJECT NOT LIKE 'P%' ORDER BY YEAR
DESC, WINNER;

-- Problem 11

-- Problem 12
Select * from Customer where City = 'Newyork' or not Grade > 100;

-- Problem 13 CHECK!!
Select * from Salesman where Commission > 0.12 and Commission < 0.14;

-- Problem 14
Select Customer_name from Customer where Customer_name like '%n';

-- Problem 15 CHECK!!
SELECT * FROM Salesman WHERE Name LIKE 'N__l%';

-- Problem 16
Select * from Customer where Grade is NULL;

-- Problem 17
Select Sum(Purch_amt) from Salesman_Order;

-- Problem 18
Select COUNT(Customer_name) from Customer where Salesman_id is NOT NULL;
SELECT count(DISTINCT Salesman_id) FROM Customer WHERE Salesman_id IS NOT
NULL;

-- Problem 19
Select City, MAX(Grade) from Customer group by City;

-- Problem 20
Select MAX(Purch_amt), Customer_id from Salesman_order group by Customer_id;

-- Problem 21
Select MAX(Purch_amt), Customer_id, Order_date from Salesman_order group by Customer_id, Order_date;

-- Probem 22
Select MAX(Purch_amt), Salesman_id from Salesman_order where Order_date = '2012-08-17'group by Salesman_id;

-- Problem 23
SELECT MAX(Purch_amt) FROM Salesman_Order WHERE Purch_amt>2000 GROUP
BY Customer_id;

-- Problem 24
Select Count(Order_no) from Salesman_order where Order_date = '2012-08-17';

Commit;