-- 코드를 입력하세요
SELECT car_id,MAX(AVAILABILITY) as AVAILABILITY
FROM (
SELECT car_id,
    case when START_DATE <= "2022-10-16" and END_DATE >= "2022-10-16"  then "대여중"
    ELSE "대여 가능"
    end as AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
) A
GROUP BY car_id
ORDER BY car_id desc;

