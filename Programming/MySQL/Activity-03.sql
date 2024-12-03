Create database Activity03;
use Activity03;

create table Cars(Model_id int primary key, Model_name text not null, Color text not null, Brand text not null);

insert Cars value
(1,"Leaf","Black","Nissan"),
(2,"Leaf","Black","Nissan"),
(3,"Model S","Black","Tesla"),
(4,"Model X","White","Tesla"),
(5,"Loniq 5","Black","Hyundai"),
(6,"Loniq 5","Black","Hyundai"),
(7,"Loniq 6","White","Hyundai");

create table employee(Id int Primary Key, Emp_Name text not null, Department text not null, Salary int not null);

insert employee value
(1,"Alex","Admin",6500),
(2,"Leo","Finance",7000),
(3,"Robin","IT",2000),
(4,"Ali","IT",4000),
(5,"Maria","IT",6000),
(6,"Alice","Admin",5000),
(7,"Sebas","HR",3000),
(8,"Emma","Finance",4000),
(9,"John","HR",4500),
(10,"Kathir","IT",8000);

create table source (id int primary key, name_ text not null);

insert source values
(1,"A"),
(2,"B"),
(3,"C"),
(4,"D");

create table target (id int primary key, name_ text not null);

insert target values
(1,"A"),
(2,"B"),
(4,"α"),
(5,"F");


create table cars_travel (cars text not null, days text not null, cummulative_distance int not null);

insert cars_travel value 
("Car1", "Day1", 50),
("Car1","Day2",100),
("Car1","Day3",200),
("Car2","Day1",0),
("Car3","Day1",0),
("Car3","Day2",50),
("Car3","Day3",50),
("Car3","Day4",100);

create table CompanySales (Company text not null, company_year int not null, Amount int not null);

insert CompanySales value
("ABC Ltd.",2015,5000),
("XYZ Ltd.",2015,4600),
("ABC Ltd.",2017,5500),
("ABC Ltd.",2016,5400),
("XYZ Ltd.",2016,6500),
("ABC Ltd.",2018,5400),
("XYZ Ltd.",2017,4700),
("XYZ Ltd.",2018,5400);

create table Travel(ID int primary key, Source text not null, Destination text not null, Distance int not null);

insert Travel value
(1,"Bangalore","Hyderabad",400),
(2,"Hyderabad","Bangalore",400),
(3,"Mumbai","Delhi",400),
(4,"Delhi","Mumbai",400),
(5,"Chennai","Pune",400),
(6,"Pune","CHennai",400);

-- Q1
Delete c1
from Cars c1
left join Cars c2 
on c1.Model_name = c2.Model_name 
and c1.Brand = c2.Brand 
and c1.Model_id > c2.Model_id
where c2.Model_id is not null;

Select * from Activity03.Cars;

-- Q2
Select *,
max(Salary) over (partition by Department order by Salary desc) as highest_sal,
min(Salary) over (partition by Department order by Salary) as lowest_sal
from employee;

-- Q3
Select s.id, 'new in source' as comment from source s left join target t on s.id = t.id where t.id is null
union
Select t.id, 'new in target' as comment from source s right join target t on s.id = t.id where s.id is null
union
Select s.id, 'mismatch' as comment from source s join target t on s.id = t.id where s.id = t.id and s.name_ != t.name_;

-- Q4
select id, 'new in source' as comment from source s where id not in (select id from target t)
union
select t.id, 'new in target' as comment from target t where id not in (select id from source s)
union
select id, 'mismatch' as comment from source s where id in (select id from target t) and name_ != (select name_ from target t where t.id = s.id);

-- Q5
Select *, cummulative_distance - lag(cummulative_distance, 1, 0) over (Partition by cars order by days) as dist_travel
from cars_travel;

-- Q6
Select *, lead(Amount,1,0) over (partition by Company order by company_year desc) as Lead_amount
from CompanySales;

-- Q7
Select distinct LEAST(Source, Destination) as Source, GREATEST(Source, Destination) as Destination, Distance
from Travel;