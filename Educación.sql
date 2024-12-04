
ALTER TABLE public_spending
ADD COLUMN id SERIAL PRIMARY KEY;

ALTER TABLE education_expenditure
ADD COLUMN id SERIAL PRIMARY KEY;


CREATE VIEW entity_totalpublicpib AS
SELECT 
	id,
    entity, 
    year, 
    SUM(public_spending_pib) AS total_public_spending_pib
FROM 
    public_spending
WHERE 
    entity IN ('Mexico', 'Colombia', 'Chile', 'Brazil', 'China', 'Argentina', 'United States')
GROUP BY 
    entity, year, id
ORDER BY 
    entity, year;


CREATE VIEW total_public_spending AS
SELECT 
	id,
    entity, 
    year, 
    SUM(government_avgexpenditure) AS total_public_spending
FROM 
    education_expenditure
WHERE 
    entity IN ('Mexico', 'Colombia', 'Chile', 'Brazil', 'China', 'Argentina', 'United States')
GROUP BY 
    entity, year, id
ORDER BY 
    entity, year;
