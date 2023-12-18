# Pokemon
Сбор данных о покемонах и сохранение в базу данных MySQL

Собраны данные о покемонах из внешнего API: https://pokeapi.co/api/v2/pokemon. Полученные данные сохранены в базу данных SQL. 
SQL запросы к получившейся БД:
- Вывести список для сравнения параметров покемонов в таблице со столбцами: Название покемона, Название параметра, значение base_stat (из stats)
- Вывести покемона с максимальным здоровьем
- Вывести топ-5 покемонов по показателю attack
- Вывести количество и среднее значение hp покемонов, которые имеют тип "grass"
- Вывести количество покемонов каждого типа