-- 코드를 작성해주세요
-- 낚시 앱에서 사용하는 FISH_INOF 물고기 정보 /
-- ID FISH_TYPE LENGTH(NULLABLE) TIME
-- 33이상 물고기를 종류별로 분류 / 수 / 최대 길이 / 물고기의 종류
-- 오름차순 10cm 이하는 10cm

SELECT 
    COUNT(id) as FISH_COUNT,
    MAX(LENGTH) as MAX_LENGTH,
    FISH_TYPE
FROM 
    FISH_INFO 
GROUP BY 
    FISH_TYPE
HAVING
    AVG(CASE WHEN LENGTH IS NULL THEN 10 ELSE LENGTH END) > 33
ORDER BY FISH_TYPE
;
