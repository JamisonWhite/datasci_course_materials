-- a
.output select.txt
select count(1) from Frequency where docid = '10398_txt_earn';
.output stdout


-- b
select term from Frequency where docid = '10398_txt_earn' and count=1;
.output select_project.txt
select count(1) from Frequency where docid = '10398_txt_earn' and count=1;
.output stdout

-- c
select term from Frequency where docid = '10398_txt_earn' and count=1
union
select term from Frequency where docid = '925_txt_trade' and count=1;

.output union.txt
select count(1)
from
(
select term from Frequency where docid = '10398_txt_earn' and count=1
union
select term from Frequency where docid = '925_txt_trade' and count=1
) as t;
.output stdout

-- d
.output count.txt
select count(1) from Frequency where term = 'parliament';
.output stdout

-- e
select docid, sum(term) as terms 
from Frequency 
group by docid 
having sum(term) > 300 
order by sum(term) desc;

.output big_documents.txt
select count(1) 
from (select docid from Frequency group by docid having sum(count) > 300 );
.output stdout

-- f
.output two_words.txt
select count(distinct t1.docid) 
from (select * from Frequency where term = 'transactions') as t1 
join (select * from Frequency where term = 'world') as t2 on t1.docid = t2.docid;

.output stdout








