-- Customer Table
CREATE TABLE Customer (
  ID INT PRIMARY KEY,
  Name NVARCHAR(100),
  Email NVARCHAR(100),
  ...
);

-- Product Table
CREATE TABLE Product (
  ProductID INT PRIMARY KEY,
  ProductName NVARCHAR(100),
  ...
);

-- Order Table
CREATE TABLE [Order] (
  OrderID INT PRIMARY KEY,
  CustomerID INT,
  ...
);

-- Inventory Table
CREATE TABLE Inventory (
  InventoryID INT PRIMARY KEY,
  ProductID INT,
  ...
);
