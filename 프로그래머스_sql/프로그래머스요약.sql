select outs.animal_id, outs.name from animal_outs outs

left outer join animal_ins ins
on outs.animal_id = ins.animal_id

where ins.animal_id is null

order by outs.datetime asc
limit 3

-- ins.sex_upon_intake like '%intact%'

-- 첫 줄에는 가져올 컬럼의 이름과 그 테이블
-- AND OR

-- case ~ end as 문 확인
select animal_id, name,
case
    when sex_upon_intake like 'Neutered%' then 'O'
    when sex_upon_intake like 'Spayed%' then 'O'
    else 'X'
end as 중성화  -- 열의 이름을 무엇으로 출력할 지
from animal_outs
order by animal_id asc

select animal_type, count(animal_type) from animal_ins
group by animal_type
-- having
order by animal_type asc