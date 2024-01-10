-- 코드를 입력하세요
SELECT MCDP_CD AS "진료과코드",count(*) AS "5월예약건수"
FROM appointment
where month(APNT_YMD) = 5
GROUP BY MCDP_CD
ORDER BY count(*), MCDP_CD