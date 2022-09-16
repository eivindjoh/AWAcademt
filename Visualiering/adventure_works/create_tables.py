import pyodbc
import csv
import os

os.chdir(r'C:\Users\krro\Documents\My Documents\Projects\Academy\course\Week 6 Visualization\power_bi_data\adventure_works')


def get_conn_curos():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=osl-krro2\SQLEXPRESS;'
                          'Database=Academy_AdventureWorks;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()
    return(conn, cursor)


def insert(conn, cursor, csv_table, insert_sql):
    with open(csv_table, 'r') as csv_file:
        for i, line in enumerate(csv_file):
            if i == 0:
                continue
            print(i)
            clean_line = line.replace('\n', '')
            cells = [cell if cell!='' else None for cell in clean_line.split(',')]
            print(cells)
            cursor.execute(insert_sql, cells)
            conn.commit()


conn, cursor = get_conn_curos()
# Customer
create_customer_sql = """CREATE TABLE Customer (
    CustomerKey          Int      NOT NULL PRIMARY KEY,
    FirstName            VARCHAR(50),
    LastName             VARCHAR(50),
    FullName             VARCHAR(150),
    BirthDate            DATETIME,
    MaritalStatus        VARCHAR(50),
    Gender               VARCHAR(50),
    YearlyIncome         INT,
    TotalChildren        INT,
    NumberChildrenAtHome INT,
    Education            VARCHAR(50),
    Occupation           VARCHAR(50),
    HouseOwnerFlag       INT,
    NumberCarsOwned      INT,
    AdressLine1          VARCHAR(150),
    DateFirstPurchase    DATETIME,
    CommuteDistance      VARCHAR(50) 
);
"""

# Product
create_product_sql = """CREATE TABLE Product (
    ProductKey         INT       PRIMARY KEY NOT NULL,
    ProductName        VARCHAR(50),
    SubCategory        VARCHAR(50),
    Category           VARCHAR(50),
    StandardCost       NUMERIC,
    Color              VARCHAR(50),
    ListPrice          NUMERIC,
    DaysToManufacture  INT,
    ProductLine        VARCHAR(50),
    ModelName          VARCHAR(50),
    Photo              VARCHAR(150),
    ProductDescription VARCHAR(500),
    StartDate          DATETIME
);"""
cursor.execute(create_product_sql)
conn.commit()

insert_product_sql = (
    'INSERT INTO Product (ProductKey, ProductName, SubCategory, Category, ' 
    'StandardCost, Color, ListPrice, DaysToManufacture, ProductLine, '
    'ModelName, Photo, ProductDescription, StartDate)'
    'VALUES ('+', '.join(['?']*13)+');')

product_csv = 'Product.csv'
insert(conn, cursor, product_csv, insert_product_sql)

# Territories
create_territories_sql = """CREATE TABLE Territories (
    SalesTerritoryKey INT       PRIMARY KEY NOT NULL,
    Region            VARCHAR(50),
    Country           VARCHAR(50),
    [Group]           VARCHAR(50),
    RegionImage       VARCHAR(150) 
);
"""
cursor.execute(create_territories_sql)
conn.commit()

insert_territories_sql = (
    'INSERT INTO Territories (SalesTerritoryKey, Region, Country, [Group], '
    'RegionImage) VALUES ('+', '.join(['?']*5)+');')
territories_csv = 'Territories.csv'
insert(conn, cursor, territories_csv, insert_territories_sql)


# Sales
create_sales_sql = """CREATE TABLE Sales (
    ProductKey           INT      REFERENCES Product (ProductKey),
    OrderDate            DATETIME,
    ShipDate             DATETIME,
    CustomerKey          INT      REFERENCES Customer (CustomerKey),
    PromotionKey         INT,
    SalesTerritoryKey    INT      REFERENCES Territories (SalesTerritoryKey),
    SalesOrderNumber     VARCHAR(50),
    SalesOrderLineNumber INT,
    OrderQuantity        INT,
    UnitPrice            NUMERIC,
    TotalProductCost     NUMERIC,
    SalesAmount          NUMERIC,
    TaxAmt               NUMERIC
);

"""

cursor.execute(create_sales_sql)
conn.commit()

insert_sales_sql = (
    'INSERT INTO Sales (ProductKey, OrderDate, ShipDate, CustomerKey, '
    'PromotionKey, SalesTerritoryKey, SalesOrderNumber, SalesOrderLineNumber, '
    'OrderQuantity, UnitPrice, TotalProductCost, SalesAmount, TaxAmt)'
    ' VALUES ('+', '.join(['?']*13)+');')
sales_csv = 'Sales.csv'
insert(conn, cursor, sales_csv, insert_sales_sql)
