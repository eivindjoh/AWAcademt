-- 2: DQL (DVDRental)
-- Write a query that finds how many customers have made at least 10 payments 
-- where each payment was 20% larger than the average. The query should return 
-- the customers' ID, amount of payments 20% larger than the average, and total 
-- sum of payments. You may find using a subquery useful. Hint: There are 53 such customers.

with payments as (
	select
		customer_id,
		payment_id, 
		amount 
	from payment
	group by payment_id, amount
	having 	amount > (
			select 
				avg(amount)*1.2
			from payment)
	)
select 
	customer_id,
	sum(amount),
	count(payment_id)
from payments
group by customer_id
having count(payment_id) >= 10;


