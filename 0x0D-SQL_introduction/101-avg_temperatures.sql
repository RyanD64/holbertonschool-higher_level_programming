-- display the average temperature (°F) by city ordered by descending temperature
SELECT city, AVG(value) as avg_tmp FROM temperatures GROUP BY city ORDER BY avg_tmp DESC;