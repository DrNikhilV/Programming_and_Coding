-- This command is used to create a database
Create database Database1;

-- This command is to use the database
Use Database1;

-- Create a table named Employee
Create table employee (empID Integer Primary key, empName text NOT NULL, Department text NOT NULL);

-- Insert a row into table
Insert into employee values(5122, 'Arun', 'CSE');

Insert into employee values(5123, 'Strange', 'CYS');
Insert into employee values(5124, 'Barton', 'AIE');
Insert into employee values(5125, 'Scott', 'ARE');
Insert into employee values(5126, 'Stark', 'ECE');

-- Describe the table
desc employee;

-- List all the Employee names in an 'employee' table
Select empname from employee;

-- List multiple rows in an 'employee' table
Select empname, empID from employee;

-- List all the rows in an 'employee' table
Select * from employee;

-- List all the employee who are working in CYS
Select * from employee where department = 'CYS';

Select * from employee where department = 'CYS' And department = 'ECE';

Select * from employee where department = 'CYS' Or department = 'ECE';

-- List all the employee names in ascending order
Select * from employee Order by empname;

-- List all the employee names in descending order
Select * from employee Order by empname desc;

-- List all the department names without duplicates
Select distinct(department) from employee;

Select distinct(department) as Department from employee;

-- Print all the employees whose name ends with 'S'
Select empname from employee where empname like '%S';

-- Print all the employees whose name starts with 'S'
Select empname from employee where empname like 'S%';

-- Print all the employees whose name's third letter is 'a'
Select empname from employee where empname like '__a%';

Commit;