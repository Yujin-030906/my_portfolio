USE mini_project;

SELECT
    b.district AS '지역명',
    a.population AS '인구수',
    b.`official land price by district` AS '공시지가',
    a.nam_id AS '지역코드'
FROM namgu a
INNER JOIN land_value_with_code b 
    ON a.nam_id = b.district_code 
    AND b.district LIKE CONCAT('%', a.dong_name, '%') -- 동 이름이 포함된 경우만 조인
ORDER BY `official land price by district` ASC;