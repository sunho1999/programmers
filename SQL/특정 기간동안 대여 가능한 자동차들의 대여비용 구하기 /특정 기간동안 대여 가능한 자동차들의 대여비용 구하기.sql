SELECT a.car_id,a.CAR_TYPE,ROUND(a.DAILY_FEE * 30 * (100 - b.DISCOUNT_RATE) / 100, 0) AS FEE
FROM CAR_RENTAL_COMPANY_CAR as a join
(select * from CAR_RENTAL_COMPANY_DISCOUNT_PLAN where DURATION_TYPE ='30일 이상') b
on a.CAR_TYPE=b.CAR_TYPE
where a.CAR_TYPE in ('세단','suv')
and a.car_id not in (
    select car_id
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where END_DATE>='2022-11-01'
    and START_DATE<'2022-12-01'
)
group by a.car_id
having FEE BETWEEN 500000 AND 1999999
order by FEE DESC,CAR_TYPE ASC,CAR_ID DESC