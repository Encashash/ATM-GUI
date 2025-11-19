create database bank;
use bank;
create table atm(acc_number int(4) primary key, 
					pin int(4) not null,
                    acc_name varchar(100) not null,
                    phone_number int(11) not null);
insert into atm values(7908,2222,"vijay",807300756,null);
alter table atm add balance int(100);
describe atm;
update atm set balance = 37000 where acc_number = 9999;
update atm set balance = balance-5000 where acc_number=1234;
rollback;delete from atm where acc_number = 2223;
select curdate();
select acc_number,pin from atm where acc_number=1234 and pin=1906;
select current_time()
select * from atm;
select acc_number,pin from atm  where acc_number=1234 and pin=2442;
select phone_number from atm where acc_name="aaryan shinde";
select distinct acc_name from atm;
select * from atm where not acc_number=1234;
select * from atm where balance between 1000 and 20000;
select * from atm where acc_number=1234 or acc_number =5678;
select * from atm where acc_number in (1234,5678);
select * from atm ORDER BY acc_number desc;
select * from atm where balance is NULL;
select * from atm where acc_number like "%4";
update atm set acc_name="aaryan"where acc_number in(1234);
delete from atm where acc_number in (6065,7777);
#alter table atm modify acc_name varchar(100) default "none";
alter table atm modify phone_number int(10) not null;
alter table atm modify phone_number float(11);
select * from atm where phone_number>=222000 or phone_number<=100;
select mod(round((power(sum(balance+1000),1)),2),102) "TOTAl" from atm where acc_number in (1234);
alter table atm add (final_balance numeric(10,1));
update atm set final_balance=20000 where acc_number between 0000 and 9999;
update atm set final_balance = final_balance + 4999 where acc_number = 1234;
alter table atm add total_gst float(10);
update atm set total_gst= (balance*10)/100 + balance,final_balance = 25000 where acc_number in (1234,5678);
select mid(acc_name,4,6) as name from atm;
select trim(acc_name) from atm;
select * from atm where phone_number like "%3%";
select count(*) from atm;
select count(balance) from atm;
select avg(balance) as aveg from atm;
 select acc_number,count(balance) as counter from atm group by acc_number;
 select * from atm where acc_number>1234 or acc_number<7908;
 alter table atm add taxes int(10) not null;
 insert into atm (taxes) values (8000);
 alter table atm modify balance int(10) default "0000";
 update atm set balance=45976 where acc_number in (4343);
 select *,max(balance) from atm where acc_number=1234;
 select *,count(final_balance) from atm group by acc_name order by acc_name desc;
 