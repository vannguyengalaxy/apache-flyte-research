### 1. Prepair database:
#### 1.1. Create supper user:
```angular2html
create user flyte with password ‘123456’ SUPERUSER CREATEDB CREATEROLE INHERIT LOGIN REPLICATION;
```
#### 1.2. Create database:
```angular2html
create database flytedb;
```
#### 1.3. Grant owner for database:
```angular2html
alter database flytedb owner to flyte;
```
#### 1.4 Switch database:
```angular2html
\connect flytedb;
```
#### 1.5. Create table:
```angular2html
create table account (
username varchar(50) unique not null,
email varchar(255) not null
);
```
#### 1.6. Insert data to table:
```angular2html
insert into account values ('van', 'van@gmail.com');
```
