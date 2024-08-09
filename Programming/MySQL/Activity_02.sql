create database Activity02;
use Activity02;

CREATE TABLE Salesman(Salesman_id INTEGER PRIMARY KEY, Salesman_Name TEXT NOT NULL, City Text, Commision FLOAT NOT NULL);
INSERT INTO Salesman VALUES(5001, 'James Hoog', 'Newyork', 0.15);
INSERT INTO Salesman VALUES(5002, 'Nail Knite', 'Paris', 0.13);
INSERT INTO Salesman VALUES(5005, 'Pit Alex', 'London', 0.11);
INSERT INTO Salesman VALUES(5006, 'Mc Lyon', 'Paris', 0.14);
INSERT INTO Salesman VALUES(5003, 'Lauson Hen', NULL , 0.12);
INSERT INTO Salesman VALUES(5007, 'Paul Adam', 'Rome', 0.13);

CREATE TABLE Customer(Customer_id INTEGER PRIMARY KEY, Customer_name TEXT NOT NULL, City TEXT NOT NULL, Grade INTEGER, Salesman_id INTEGER);
INSERT INTO Customer VALUES(3002, 'Nick Rimando','Newyork', 100, 5001);
INSERT INTO Customer VALUES(3005, 'Graham Lusi','California', 200, 5002);
INSERT INTO Customer VALUES(3001, 'Brad Guran','London', NULL, NULL);
INSERT INTO Customer VALUES(3004, 'Fabian Johns','Paris', 300, 5006);
INSERT INTO Customer VALUES(3007, 'Brad Davis','Newyork', 200, 5001);
INSERT INTO Customer VALUES(3009, 'Geoff Camero','Berlin', 100, NULL);
INSERT INTO Customer VALUES(3008, 'Julian Green','London', 300, 5002);
INSERT INTO Customer VALUES(3003, 'Jory Altidor','Moncow', 200, 5007);

CREATE TABLE Orders (Order_no INT primary KEY, Purch_amt FLOAT NOT NULL, Order_date DATE NOT NULL, Customer_id INTEGER NOT NULL, Salesman_id INTEGER NOT NULL);
INSERT INTO Orders VALUES (70001, 150.5, '2012-10-05', 3005, 5002);
INSERT INTO Orders VALUES(70009, 270.65, '2012-09-10', 3001, 5005);
INSERT INTO Orders VALUES(70002, 65.26, '2012-10-05', 3002, 5001);
INSERT INTO Orders VALUES(70004, 110.5, '2012-08-17', 3009, 5003);
INSERT INTO Orders VALUES(70007, 948.5, '2012-09-10', 3005, 5002);
INSERT INTO Orders VALUES(70005, 2400.6, '2012-07-27', 3007, 5001);
INSERT INTO Orders VALUES(70008, 5760, '2012-09-10', 3002, 5001);
INSERT INTO Orders VALUES(70010, 1983.43, '2012-10-10', 3004, 5006);
INSERT INTO Orders VALUES(70003, 2480.3, '2012-10-10', 3009, 5003);
INSERT INTO Orders VALUES(70012, 250.45, '2012-06-27', 3008, 5002);
INSERT INTO Orders VALUES(70011, 75.29, '2012-08-17', 3003, 5007);
INSERT INTO Orders VALUES(70013, 3045.6, '2012-04-25', 3002, 5001);

CREATE TABLE company_mast(Com_id int, Com_Name TEXT);
INSERT INTO company_mast
VALUES
(11,	'Samsung'),
(12,	'iBall'),
(13,	'Epsion'),
(14,	'Zebronics'),
(15,	'Asus'),
(16,	'Frontech');

CREATE TABLE item_mast(Pro_ID int,Pro_Name TEXT,Pro_Price int,Pro_Com int);
INSERT INTO item_mast(Pro_ID,Pro_Name,Pro_Price,Pro_Com)
VALUES
(101,'Mother Board',3200,15),
(102,'Keyboard',450,16),
(103,'ZIP Drive',250,14),
(104,'Speaker',550,16),
(105,'Monitor',5000,11),
(106,'DVD Drive',900,12),
(107,'CD Drive',800,12),
(108,'Printer',2600,13),
(109,'Refill Catridge',350,13),
(110,'Mouse',250,12);

CREATE TABLE emp_department(DPT_CODE int,DPT_NAME TEXT, DPT_ALLOTMENT int);
INSERT INTO emp_department
VALUES
(57,'IT',65000),
(63,'Finance',15000),
(47,'HR',240000),
(27,'RD',55000),
(89,'QC',75000);

CREATE TABLE emp_details(EMP_IDNO int,EMP_FNAME TEXT,EMP_LNAME TEXT,EMP_DEPT int);
INSERT INTO emp_details (EMP_IDNO, EMP_FNAME, EMP_LNAME, EMP_DEPT)
VALUES
(127323, 'Michale', 'Robbin', 57),
(526689, 'Carlos', 'Snares', 63),
(843795, 'Enric', 'Dosio', 57),
(328717, 'Jhon', 'Snares', 63),
(444527, 'Joseph', 'Dosni', 47),
(659831, 'Zanifer', 'Emily', 47),
(847674, 'Kuleswar', 'Sitaraman', 57),
(748681, 'Henrey', 'Gabriel', 47),
(555935, 'Alex', 'Manuel', 57),
(539569, 'George', 'Mardy', 27),
(733843, 'Mario', 'Saule', 63),
(631548, 'Alan', 'Snappy', 27),
(839139, 'Maria', 'Foster', 57);

-- Question 1
select s.Salesman_name, c.Customer_name, s.city
from Salesman s 
join Customer c 
on s.Salesman_id = c.Salesman_id
where s.city = c.city;

-- Question 2
select o.Order_no, o.Purch_amt, c.Customer_name, c.city
from Orders o
join Customer c 
on o.Customer_id = c.Customer_id
where o.Purch_amt > 500 and o.Purch_amt < 2000;

-- Question 3
select s.Salesman_name, c.Customer_name
from Salesman s
join Customer c
on s.Salesman_id = c.Salesman_id
where s.Salesman_id = c.Salesman_id;

-- Question 4
select c.Customer_name
from Salesman s
join Customer c
on s.Salesman_id = c.Salesman_id
where s.Commision > 0.12;

-- Question 5
select c.Customer_name
from Salesman s
join Customer c
on s.Salesman_id = c.Salesman_id
where s.Commision > 0.12 and not s.city = c.city;

-- Question 6
select n.Order_no, n.Order_date, n.Purch_amt, n.Customer_name, s.Salesman_Name, s.Commision
from (select o.Order_no, o.Order_date, o.Purch_amt, c.Customer_name, c.Salesman_id 
from Orders o left join Customer c on o.Customer_id = c.Customer_id)n
left join Salesman s on n.Salesman_id = s.Salesman_id;

SELECT o.Order_no, o.Order_date, o.Purch_amt, c.Customer_name, s.Salesman_Name, s.Commision
FROM Orders o
JOIN Customer c ON o.Customer_id = c.Customer_id
JOIN Salesman s ON o.Salesman_id = s.Salesman_id;

-- Question 7 
SELECT s.Salesman_id, s.Salesman_Name, s.city, s.Commision, c.Customer_id, 
		c.Customer_name, c.grade, o.Order_no, o.Purch_amt, o.Order_date
FROM Orders o
JOIN Customer c ON o.Customer_id = c.Customer_id
JOIN Salesman s ON o.Salesman_id = s.Salesman_id;

-- Question 8
select Customer_name from Customer
order by Customer_name;

-- Question 9
select Customer_name,grade from Customer
where grade < 300 or grade is null
order by Customer_name;

-- Question 10
select c.Customer_name, c.city, o.Order_no, o.Order_date, o.Purch_amt
from Customer c
join Orders o
on c.Customer_id = o.Customer_id
order by Order_date;

-- Question 11
SELECT c.Customer_name, s.city, o.Order_no, o.Order_date, o.Purch_amt, s.Salesman_Name,  s.Commision
FROM Orders o
JOIN Customer c ON o.Customer_id = c.Customer_id
JOIN Salesman s ON o.Salesman_id = s.Salesman_id;

-- Question 12
select Salesman_name from Salesman
order by Salesman_name;

-- Question 13
Select distinct(s.Salesman_name) as Salesman 
from Salesman s left join Customer c 
on s.Salesman_id=c.Salesman_id 
left join Orders o on c.Customer_id=o.Customer_id;

-- Question 14
Select distinct(s.Salesman_name) as Salesman 
from Salesman s left join Customer c 
on s.Salesman_id=c.Salesman_id 
left join Orders o on c.Customer_id = o.Customer_id 
where o.Purch_amt >= 2000 and Grade is not NULL;

-- Question 15
Select c.Customer_name as Customer_Name, c.City, o.Order_no, o.Order_date, o.Purch_amt 
from Customer c 
right join Orders o 
on c.Customer_id= o.Customer_id;

-- Question 16
Select c.Customer_name as Customer_Name, c.City, o.Order_no, o.Order_date, o.Purch_amt 
from Customer c left join Orders o on c.Customer_id = o.Customer_id where c.Grade is not NULL 
union 
Select c.Customer_name as Customer_Name, c.City, o.Order_no, o.Order_date, o.Purch_amt 
from Orders o right join Customer c on c.Customer_id = o.Customer_id where c.Grade is not NULL;


-- Question 17
Select s.Salesman_name as Salesman, c.Customer_name as Customer_Name
from Salesman s cross join Customer c;

-- Question 18
Select s.Salesman_name as Salesman, c.Customer_name as Customer_Name 
from Salesman s cross join Customer c 
where s.City is not NULL;

-- Question 19
Select s.Salesman_name as Salesman, c.Customer_name as Customer_Name 
from Salesman s cross join Customer c 
where s.City is not NULL and c.Grade is not NULL;

-- Question 20
Select s.Salesman_name as Salesman, c.Customer_name as Customer_Name 
from Salesman s cross join Customer c 
where s.City is not NULL and s.City != c.City and c.Grade is not NULL;

-- Question 21
select i.Pro_id, i.Pro_name, i.Pro_Price, c.Com_id, c.Com_name from item_mast i
join company_mast c
on i.Pro_Com = c.Com_id;

-- Question 22
select i.Pro_name as Item_name, i.Pro_Price as Price, c.Com_name as Company_name 
from item_mast i
join company_mast c
on i.Pro_Com = c.Com_id;

-- Question 23
select avg(i.Pro_Price) as Average_Price, c.Com_name as Company_name
from item_mast i
join company_mast c
on i.Pro_Com = c.Com_id
group by c.Com_Name;

-- Question 24
select avg(i.Pro_Price) as Average_Price, c.Com_name as Company_name
from item_mast i
join company_mast c
on i.Pro_Com = c.Com_id
group by c.Com_Name
having Average_Price > 350 or Average_Price = 350;

-- Question 25
select c.Com_name as Company_name, c.Com_id as Company_id, max(i.Pro_Price) as Expensive_Product
from item_mast i
join company_mast c
on i.Pro_Com = c.Com_id
group by c.Com_Name, c.Com_id;

-- Question 26
select e.*,d.DPT_NAME from emp_details e
join emp_department d
on e.EMP_DEPT = d.DPT_CODE;

-- Question 27
select e.EMP_FNAME, e.EMP_LNAME, d.DPT_NAME, d.DPT_ALLOTMENT 
from emp_details e
join emp_department d
on e.EMP_DEPT = d.DPT_CODE;

-- Question 28
select e.EMP_FNAME, e.EMP_LNAME, d.DPT_NAME, d.DPT_ALLOTMENT 
from emp_details e
join emp_department d
on e.EMP_DEPT = d.DPT_CODE
where d.DPT_ALLOTMENT > 50000;

-- Question 29
select d.DPT_NAME from emp_details e
join emp_department d
on e.EMP_DEPT = d.DPT_CODE
group by d.DPT_NAME
having count(EMP_FNAME) > 2 ;