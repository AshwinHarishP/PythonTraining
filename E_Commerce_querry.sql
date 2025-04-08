CREATE DATABASE Ecommerce;
USE Ecommerce

CREATE TABLE Customer(
	cid INT PRIMARY KEY IDENTITY(1,1),
	cname VARCHAR(30),
	caddress VARCHAR(50),
	cmob VARCHAR(13)
);


CREATE TABLE Product(
	pid INT PRIMARY KEY IDENTITY(1,1),
	pname VARCHAR(30),
	pdesc VARCHAR(50),
	price FLOAT
);


CREATE TABLE Orders(
	oid INT PRIMARY KEY,
	odate DATE,
	cid INT,
	pid INT,
	qty INT,
	price FLOAT,
	total_amt FLOAT,

	FOREIGN KEY(cid) REFERENCES Customer(cid),
	FOREIGN KEY(pid) REFERENCES Product(pid)
);

CREATE TABLE Cart(
	oid INT,
	odate DATE,
	cid INT,
	pid INT,
	qty INT,
	price FLOAT,
	total_amt FLOAT,
	FOREIGN KEY(cid) REFERENCES Customer(cid),
	FOREIGN KEY(pid) REFERENCES Product(pid)
);

Select * from Customer
select * from Product
select * from Orders
select * from Cart


