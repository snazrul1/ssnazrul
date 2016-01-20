/*Entities*/

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


/*Relationships*/

CREATE TABLE location (
        ID              SERIAL PRIMARY KEY,
	Costumer_ID	INTERGER REFERENCES costumers (ID),
	State_ID	INTEGER REFERENCES states (ID) UNIQUE
)

CREATE TABLE sales (
        ID              SERIAL PRIMARY KEY,
	Quantity	FLOAT,
	Price_Paid	FLOAT,
	Costumer_ID	INTEGER REFERENCES costumers (ID),
	Product_ID	INTEGER REFERENCES products (ID) NOT NULL
)

CREATE TABLE type (
        ID              SERIAL PRIMARY KEY,
	Category_ID	INTEGER REFERENCES category (ID) UNIQUE,
	Product_ID	INTEGER REFERENCES products (ID) NOT NULL
)	
	
