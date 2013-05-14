select * from Frequency where docid = '10080_txt_crude';
select * from Frequency where docid = '17035_txt_earn';

select *
from Frequency as f1 
join Frequency as f2 on f1.term = f2.term
where f1.docid = '10080_txt_crude'
and f2.docid = '17035_txt_earn';

-- similarity between two docs; homework answer is 19
select sum(f1.count * f2.count)
from Frequency as f1 
join Frequency as f2 on f1.term = f2.term
where f1.docid = '10080_txt_crude'
and f2.docid = '17035_txt_earn';

-- 10 most similiar documents
select f2.docid, sum(f1.count * f2.count)
from Frequency as f1 
join Frequency as f2 on f1.term = f2.term
where f1.docid = '10080_txt_crude'
group by f2.docid	
order by sum(f1.count * f2.count) desc
limit 10;


-- 10 most similiar documents; homework answer is 6
select f2.docid, sum(f1.count * f2.count)
from 
(select * from Frequency 
 union
 select 'q' as docid, 'washington' as term, 1 as count
 union
 select 'q' as docid, 'taxes' as term, 1 as count
 union
 select 'q' as docid, 'treasury' as term, 1 as count
) as f1 
join Frequency as f2 on f1.term = f2.term
where f1.docid = 'q'
group by f2.docid	
order by sum(f1.count * f2.count) desc
limit 10;


-- multiplication
select a.row_num, b.col_num, sum(a.value * b.value)
from a 
join b on a.row_num = b.col_num or a.col_num = b.row_num
group by a.row_num, b.col_num;


--transpose??





