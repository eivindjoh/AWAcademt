-- 4: DDL
-- Write SQL queries to create the following database.

-- Alternatives to the relational database model

-- Note that phone number in the EMP table can only be 8 characters. 
-- SSN in the PERSON table can only be 11 characters. ZIP in the ADDRESS table 
-- can only be 4 characters. Explain any assumptions you make when creating the tables.

create table person (
	person_id serial primary key,
	ssn char(11) not null, -- ssn er en natural key, kunne ha blitt brukt som PK, men velger å bruke person_id som PK for raskere joins.
	last_name varchar(30) not null,
	first_name varchar(20) not null,
	mid_init char(1) -- tenker at vi registrerer kun initialet til ett mellomnavn.
	);
	
create table emp (
	emp_info int unique,
	addr_info int unique,
	phone_number char(8),
	foreign key (emp_info) references person(person_id),
	foreign key (addr_info) references address(address_id),
	primary key(emp_info, addr_info)
	);

create table address (
	address_id serial primary key,
	st_address varchar(50) not null,
	city varchar(30) not null,
	state varchar (20) not null,
	zip char(4) not null
	);

	
