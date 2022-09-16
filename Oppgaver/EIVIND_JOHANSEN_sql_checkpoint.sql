-- Theory
-- Write a short response to each question with your own words. You shouldn't need more than 1-3 sentences.

-- 1. In what order are the keywords of an SQL query executed?
-- 1. From/Join
-- 2. Where
-- 3. Group by 
-- 4. Having
-- 5. Select
-- 6. Order by
-- 7. Limit

-- 2. What is a primary key?
-- En primary key er den unike identifikatoren til en rad i en tabell.
-- Primary keys er nødvendig for å skape integritet mellom 2 tabeller.

-- 3. Is a foreign key reference between two tables necessary to perform a join between the tables? Why/Why not?
-- En foreign key er nødvendig for å sørge for integritet mellom 2 tabeller. I tilfeller der vi vil bruke
-- inner join/left join/right join/full join må vi ha en foreign key for å få en relasjon mellom data i radene. 
-- Men vi kan joine 2 tabeller uten å bruke en foreign key. Ved f.eks å bruke union/union all som bare legger alle
-- radene etter hverandre uten å at det er en relasjon mellom dem.

-- 4. What is the difference between a full join and a inner join?
-- En inner join vil bare returnere de radene som matcher i de tabellene vi vil joine.
-- En full join returnerer alle rader uavhengig om det er en match i den andre tabellen eller ikke.

-- DDL
-- Write the DDL commands for creating the tables indicated in the image. 

-- ER-diagram

-- DQL on the Adventureworks database
-- Recall that the two-letter schemas only contain views. We will not use these. Unless otherwise noted, 
-- you will not need cross-schema joins.

-- 1. In the person schema you'll find all the different contact types. Write a query that returns the ID and name of all 
-- different types of managers.
select 
	contacttypeid, 
	"name" 
from person.contacttype;

-- 2. Find the business entity ID and full names of all persons who are purchasing managers. Your query should return 
-- only two columns. Sort descending by the full name.
select 
	b.businessentityid,
	concat_ws(' ', p.firstname,
				   p.middlename,
				   p.lastname) as fullname
from person.person p
	left join person.businessentitycontact b 
		on p.businessentityid = b.businessentityid
	left join person.contacttype c
		on b.contacttypeid = c.contacttypeid
where c."name" like 'Purchasing Manager'
order by fullname desc;

	
-- 3. Write a query that returns three columns: contact type ID, contact type name, and number of contacts. 
-- Return only those contact types for which there are more than 20 contacts.
select 
	c.contacttypeid,
	c."name",
	count(p.businessentityid) as number_of_contacts
from person.contacttype c
	left join person.businessentitycontact b 
		on b.contacttypeid = c.contacttypeid 
	left join person.person p 
		on p.businessentityid = b.businessentityid
group by
	c.contacttypeid,
	c."name"
having count(p.businessentityid) > 20;
	
-- In the product schema you'll find all the products produced by AdventureWorks. Write a query that returns 
-- the product IDs of the products that are cranksets.
select 
	p.productid
from production.product p
	left join production.productsubcategory s
		on p.productsubcategoryid = s.productsubcategoryid
where s."name" like 'Cranksets';

-- In the person schema you'll find the addresses of customers. Write a query that returns the address ID 
-- of all addresses in London.
select
	addressid
from person.address
where city like 'London';

-- In the sales schema you'll find all orders processed by AdventureWorks. In the table salesorderheader 
-- you'll find sales headers, and in salesorderdetail you'll find the individual order lines for each header. 
-- Write a query that answers how many crankset type products have been ordered to customers in London. 
-- Use the queries from the last two problems to achieve this. Hint: the answer is 39.
with orders as (
select 
	s.salesorderid,
	s.shiptoaddressid,
	s2.productid
from sales.salesorderheader s
	left join sales.salesorderdetail s2
		on s.salesorderid = s2.salesorderid
where s.shiptoaddressid = 
			any(select
				addressid
			from person.address
			where city like 'London'
			)
and s2.productid =
			any(select 
				p.productid
			from production.product p
				left join production.productsubcategory s
					on p.productsubcategoryid = s.productsubcategoryid
			where s."name" like 'Cranksets')
)
select count(*) from orders;


-- DQL on the DVDRental database (LEVEL 2)
-- Write a query that returns the total sum of all payments made for rentals for each actor. 
-- Do not count payments less than 3. Do not list actors with total payments made is less than 50. 
-- The query should return two columns: the name of the actor and the sum of payments made for rentals for this actor.
select
	concat_ws(' ', a.first_name, a.last_name) as full_name,
	sum(p.amount) as sum_payments
from actor a
	left join film_actor fa using(actor_id)
	left join film f using(film_id)
	left join inventory i using(film_id)
	left join rental r using(inventory_id)
	left join payment p using(rental_id)
where p.amount > 2 
group by full_name
having sum(p.amount) > 50;