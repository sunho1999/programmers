-- 코드를 입력하세요
select food_type,rest_id,rest_name,favorites
from rest_info
where favorites IN
    (
    SELECT max(favorites)
    FROM rest_info
    GROUP BY FOOD_TYPE
    )
group by food_type
ORDER BY food_type DESC


