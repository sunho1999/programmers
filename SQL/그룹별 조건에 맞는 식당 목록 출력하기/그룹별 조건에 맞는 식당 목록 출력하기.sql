-- 코드를 입력하세요


select member_name,review_text,DATE_FORMAT(Review_date,'%Y-%m-%d') AS REVIEW_DATE
FROM member_profile
INNER JOIN rest_review ON member_profile.member_id = rest_review.member_id
WHERE member_profile.member_name IN (
    select *
    from(
        SELECT member_name
        FROM member_profile
        INNER JOIN rest_review ON member_profile.member_id = rest_review.member_id
        GROUP BY member_profile.member_id
        ORDER BY count(review_text) DESC
        limit 1
        ) AS SUB
    )
ORDER BY review_date, REVIEW_TEXT

