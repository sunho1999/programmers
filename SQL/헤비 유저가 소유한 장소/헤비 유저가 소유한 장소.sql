-- 코드를 입력하세요
SELECT J.ID, J.Name, J.HOST_ID
FROM PLACES  J JOIN (SELECT HOST_ID
                  FROM PLACES
                  GROUP BY HOST_ID HAVING COUNT(HOST_ID)> 1) AS p
                ON J.HOST_ID = P.HOST_ID
ORDER BY J.ID