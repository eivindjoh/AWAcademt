-- 1: DQL (DVDRental)
-- A
-- Write a query to find all horror films described as being “beautiful”. 
-- The query should return the film titles, category names and description 
-- of all such films, ordered by film name.
select 
	f.title, 
	c."name", 
	f.description 
from film f
left join film_category fc using(film_id)
left join category c using(category_id)
where f.description like '%eautiful%' -- uten b for å sørge for at både beautiful med store og små bokstaver blir med.
and c."name" = 'Horror'
order by f.title;

-- B
-- Write a query to find all action movies whose descriptions indicate they 
-- involve a database administrator. The query should return the film titles, 
-- category names and description of all such films, ordered by film name.
select
	f.title,
	c."name",
	f.description
from film f
left join film_category fc using(film_id)
left join category c using(category_id)
where f.description like '%Database Administrator%'
and c."name" = 'Action'
order by f.title;
	
-- C
-- Use the two queries above to write a single query which lists all horror 
-- films described as being “beautiful”, and all action movies whose descriptions 
-- indicate they involve a database administrator. The query should return the film titles, 
-- category names and description of all such films.
(select 
	f.title, 
	c."name", 
	f.description 
from film f
left join film_category fc using(film_id)
left join category c using(category_id)
where f.description like '%eautiful%' -- uten b for å sørge for at både beautiful med store og små bokstaver blir med.
and c."name" = 'Horror'
order by f.title)
union
(select
	f.title,
	c."name",
	f.description
from film f
left join film_category fc using(film_id)
left join category c using(category_id)
where f.description like '%Database Administrator%'
and c."name" = 'Action'
order by f.title);


-- D (LEVEL 2)
-- Expand the query from problem 1C by ordering the result set by film name.
with films as (
	(select 
		f.title as title, 
		c."name" as category, 
		f.description as description
	from film f
	left join film_category fc using(film_id)
	left join category c using(category_id)
	where f.description like '%eautiful%' -- uten b for å sørge for at både beautiful med store og små bokstaver blir med.
	and c."name" = 'Horror'
	order by f.title)
	union
	(select
		f.title as title,
		c."name" as category,
		f.description as description 
	from film f
	left join film_category fc using(film_id)
	left join category c using(category_id)
	where f.description like '%Database Administrator%'
	and c."name" = 'Action'
	order by f.title)
)
select 
	title,
	category,
	description
from films
order by title;
