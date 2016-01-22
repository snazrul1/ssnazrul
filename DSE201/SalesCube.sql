/*

Consider a database that captures customers with a name and state; states with a name; products that
have a list price, a name and belong to a category; categories have names and descriptions; sales of a
product by a customer capturing quantity and price paid (may be discounted).

*/

--Entities

CREATE TABLE customers (
	ID		SERIAL PRIMARY KEY,
	Name		TEXT
)

CREATE TABLE states (
        ID              SERIAL PRIMARY KEY,
	Name		TEXT,
)

CREATE TABLE categories (
        ID              SERIAL PRIMARY KEY,
	Name		TEXT,
	Description	TEXT
)

CREATE TABLE products (
        ID              SERIAL PRIMARY KEY,
	Name		TEXT,
	List_Price	FLOAT
)


--Relationships

CREATE TABLE location (
        ID              SERIAL PRIMARY KEY,
	Costumer_ID	INTEGER REFERENCES costumers (ID),
	State_ID	INTEGER REFERENCES states (ID) UNIQUE
)

CREATE TABLE sales (
        ID              SERIAL PRIMARY KEY,
	Quantity	FLOAT,
	Price_Paid	FLOAT,
	Costumer_ID	INTEGER REFERENCES costumers (ID) NOT NULL,
	Product_ID	INTEGER REFERENCES products (ID) NOT NULL
)

CREATE TABLE type (
        ID              SERIAL PRIMARY KEY,
	Category_ID	INTEGER REFERENCES category (ID) NOT NULL,
	Product_ID	INTEGER REFERENCES products (ID) NOT NULL
)	
	
