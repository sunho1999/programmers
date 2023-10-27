-- 코드를 입력하세요
SELECT first_half.flavor
FROM first_half
JOIN july ON
    (first_half.flavor = july.flavor)
group by flavor
ORDEr BY SUM(first_half.total_order + july.total_order) DESC
limit 3;