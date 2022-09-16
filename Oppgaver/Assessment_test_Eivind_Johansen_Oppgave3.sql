-- 3: DQL (DVDRental)
-- We want to know how many customers we have around the world. 
-- Write a query that returns the top 5 districts our customers live in, by how many 
-- customers live in them. The query should return district name, country 
-- name and customer count.
select
	c.country,
	a.district,
	count(cu.customer_id) as customers
from country c
join city c2 using(country_id)
join address a using(city_id)
join customer cu using(address_id)
group by
	c.country,
	a.district
order by customers desc
limit 5;

