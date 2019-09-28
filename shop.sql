-- 创建数据库，表，完成商品信息的记录
create database  shop default character set utf8;
create table shop (
    gid int(6) unsigned primary key,
    gname varchar(20) not null,
    g_cost_price int(8)，
    g_selling_price int(8),
    gnum int(10)
)