-- 코드를 입력하세요
select category,price AS "MAX_PRICE",product_name
from food_product
where (category,price) in
    (
    SELECT category,max(price) AS "MAX_PRICE"
    FROM food_product
    group by category
    having category = "과자" or category = "국" or category = '김치'or category =  '식용유'
    )
order BY MAX_price DESC