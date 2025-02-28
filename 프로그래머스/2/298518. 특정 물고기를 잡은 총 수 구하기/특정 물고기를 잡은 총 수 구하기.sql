-- 코드를 작성해주세요
SELECT 
    COUNT(DISTINCT FISH_INFO.id) as FISH_COUNT
FROM 
    FISH_INFO
INNER JOIN 
    FISH_NAME_INFO 
ON 
    FISH_INFO.FISH_TYPE = FISH_NAME_INFO.FISH_TYPE
AND 
    (FISH_NAME_INFO.FISH_NAME = 'BASS' OR FISH_NAME_INFO.FISH_NAME = 'SNAPPER')
;