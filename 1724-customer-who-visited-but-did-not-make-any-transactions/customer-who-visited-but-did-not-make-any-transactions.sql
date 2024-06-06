# Write your MySQL query statement below
SELECT
    customer_id,
    COUNT(CUSTOMER_ID) "count_no_trans"
FROM
    VISITS
WHERE
    VISIT_ID NOT IN (SELECT DISTINCT VISIT_ID FROM TRANSACTIONS)
GROUP BY
    CUSTOMER_ID