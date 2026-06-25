USE mini_project;

# “인구 대비 세탁소가 적은 구는 어디인가?”
# 달서구 (1 점포당 몇 명의 사람을 받을 수 있는가)
SELECT
    d.gu_name,
    d.population,
    COUNT(l.number) AS laundry_daegu,
    ROUND(
        d.population / NULLIF(COUNT(l.number), 0),
        0
    ) AS people_per_shop
FROM daegu d
LEFT JOIN laundry_daegu l
    ON d.daegu_id = l.dong_id
GROUP BY d.daegu_id, d.gu_name, d.population
ORDER BY people_per_shop DESC;

SELECT daegu_id, gu_name
FROM daegu
WHERE gu_name = '달서구';

SELECT DISTINCT dong_id
FROM laundry_daegu
ORDER BY dong_id;

SELECT *
FROM laundry_daegu
WHERE region LIKE '%달서구%';

UPDATE laundry_daegu
SET dong_id = 7
WHERE region LIKE '%달서구%';

SELECT
    d.gu_name,
    COUNT(l.number) AS laundry_daegu_count
FROM daegu d
LEFT JOIN laundry_daegu l
    ON d.daegu_id = l.dong_id
GROUP BY d.gu_name;

SELECT
    d.gu_name,
    d.population,
    COUNT(l.number) AS laundry_daegu_count,
    ROUND(
        d.population / NULLIF(COUNT(l.number), 0),
        0
    ) AS people_per_shop
FROM daegu d
LEFT JOIN laundry_daegu l
    ON d.daegu_id = l.dong_id
GROUP BY d.daegu_id, d.gu_name, d.population
ORDER BY people_per_shop DESC;