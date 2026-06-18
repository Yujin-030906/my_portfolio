USE mini_project;

# “인구 대비 올리브영이 적은 구는 어디인가?”
# 달서구 (1 점포당 몇 명의 사람을 받을 수 있는가)
SELECT
    d.gu_name,
    d.population,
    COUNT(o.number) AS oliveyoung_daegu,
    ROUND(
        d.population / NULLIF(COUNT(o.number), 0),
        0
    ) AS people_per_shop
FROM daegu d
LEFT JOIN oliveyoung_daegu o
    ON d.daegu_id = o.dong_id
GROUP BY d.daegu_id, d.gu_name, d.population
ORDER BY people_per_shop DESC;

SELECT daegu_id, gu_name
FROM daegu
WHERE gu_name = '달서구';

SELECT DISTINCT dong_id
FROM oliveyoung_daegu
ORDER BY dong_id;

SELECT *
FROM oliveyoung_daegu
WHERE region LIKE '%달서구%';

UPDATE oliveyoung_daegu
SET dong_id = 7
WHERE region LIKE '%달서구%';

SELECT
    d.gu_name,
    COUNT(o.number) AS oliveyoung_daegu_count
FROM daegu d
LEFT JOIN oliveyoung_daegu o
    ON d.daegu_id = o.dong_id
GROUP BY d.gu_name;

SELECT
    d.gu_name,
    d.population,
    COUNT(o.number) AS oliveyoung_daegu_count,
    ROUND(
        d.population / NULLIF(COUNT(o.number), 0),
        0
    ) AS people_per_shop
FROM daegu d
LEFT JOIN oliveyoung_daegu o
    ON d.daegu_id = o.dong_id
GROUP BY d.daegu_id, d.gu_name, d.population
ORDER BY people_per_shop DESC;