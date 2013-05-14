select * from Frequency where docid = '10080_txt_crude';
select * from Frequency where docid = '17035_txt_earn';

select *
from Frequency as f1 
join Frequency as f2 on f1.term = f2.term
where f1.docid = '10080_txt_crude'
and f2.docid = '17035_txt_earn';

-- similarity
select sum(f1.count * f2.count)
from Frequency as f1 
join Frequency as f2 on f1.term = f2.term
where f1.docid = '10080_txt_crude'
and f2.docid = '17035_txt_earn';


-- multiplication
select a.row_num, b.col_num, sum(a.value * b.value)
from a 
join b on a.row_num = b.col_num or a.col_num = b.row_num
group by a.row_num, b.col_num;


--transpose??





