SQL запросы к получившейся БД:
1. Вывести список для сравнения параметров покемонов в таблице со столбцами: Название покемона, Название параметра, значение base_stat (из stats)

SELECT name, stat, base_stat
FROM pokemon p JOIN stats s ON p.pokemon_id=s.pokemon_id

2. Вывести покемона с максимальным здоровьем

SELECT name, height 
FROM pokemon p, (SELECT MAX(height) AS max_heigh  FROM Pokemon) AS X 
WHERE height = X.max_heigh

3. Вывести топ-5 покемонов по показателю attack

SELECT name, stat, base_stat
FROM stats s JOIN pokemon p ON s.pokemon_id=p.pokemon_id
WHERE stat='attack'
ORDER BY base_stat DESC
LIMIT 5

4. Вывести количество и среднее значение hp покемонов, которые имеют тип "grass"

SELECT  COUNT(`type`) qty_grass, AVG(base_stat) avg_hp
FROM (SELECT pokemon_id, stat, base_stat FROM stats WHERE stat='hp') X RIGHT JOIN 
(SELECT pokemon_id, `type` FROM types WHERE `type`='grass') Y ON X.pokemon_id=Y.pokemon_id
GROUP BY `type`

5. Вывести количество покемонов каждого типа

SELECT `type`, COUNT(`type`) qty_type
FROM types
GROUP BY `type`
ORDER BY qty_type
