-- SWAMI KARUPPASWAMI THUNNAI

create database sensible;

use sensible;

create table if not exists currency(
	id int primary key auto_increment,
    name varchar(7) unique key,
    symbol char(1) CHARACTER SET utf8 COLLATE utf8_unicode_ci
);

insert into currency values
(null, "INR", "₹"),
(null, "USD", "$"),
(null, "CAD", "$"),
(null, "AUD", "$");

create table if not exists user_credential
(
	id bigint primary key auto_increment,
    country_code varchar(4) default "91",
    phone char(10) unique key,
    password_hash char(60) not null,
    name text not null,
    primary_currency int not null,
    image text,
    verified tinyint(1)
);

create table if not exists category
(
	id bigint primary key auto_increment,
    customer_id bigint,
    name text CHARACTER SET utf8 COLLATE utf8_unicode_ci
);

delimiter $$

create trigger user_created
after insert on user_credential
for each row
begin
	insert into category values
    (null, NEW.id, "Call"),
    (null, NEW.id, "Email"),
    (null, NEW.id, "Follow-up"),
    (null, NEW.id, "Meeting"),
    (null, NEw.id, "Milestone"),
    (null, NEW.id, "Send");
    
end$$

delimiter ;

create table if not exists tag
(
	id bigint primary key auto_increment,
    user_id bigint not null,
    name text not null,
    hexcolour text not null
);


create table if not exists task
(
	id bigint primary key auto_increment,
    user_id bigint,
    name text CHARACTER SET utf8 COLLATE utf8_unicode_ci not null,
    category_id bigint,
    due_date date not null,
    due_time time not null,
    opportunity_id bigint    
);




