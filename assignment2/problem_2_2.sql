
select * from a;
select * from b;

select a.row_num, b.col_num, sum(a.value * b.value)
from a 
join b on a.row_num = b.col_num or a.col_num = b.row_num
group by a.row_num, b.col_num;

.output multiply.txt
select sum(a.value * b.value)
from a 
join b on a.row_num = b.col_num or a.col_num = b.row_num
where a.row_num = 2 and b.col_num = 3
group by a.row_num, b.col_num;
.output stdout
