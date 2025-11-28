<div align="center"><img src="https://github.com/vtiquet/holbertonschool-resources/blob/main/image/Holberton-Logo.svg" width=40% height=40%/></div>

# Resources

## Table of Contents :

  - [0. List databases](#subparagraph0)
  - [1. Create a database](#subparagraph1)
  - [2. Delete a database](#subparagraph2)
  - [3. List tables](#subparagraph3)
  - [4. First table](#subparagraph4)
  - [5. Full description](#subparagraph5)
  - [6. List all in table](#subparagraph6)
  - [7. First add](#subparagraph7)
  - [8. Count 89](#subparagraph8)
  - [9. Full creation](#subparagraph9)
  - [10. List by best](#subparagraph10)
  - [11. Select the best](#subparagraph11)
  - [12. Cheating is bad](#subparagraph12)
  - [13. Score too low](#subparagraph13)
  - [14. Average](#subparagraph14)
  - [15. Number by score](#subparagraph15)
  - [16. Say my name](#subparagraph16)

## Resources
### Read or watch:
* [What is Database & SQL?](/rltoken/jRAhwW4u4YvZtLtMGU2_6g)
* [Install MySQL (MySQL Server)](/rltoken/s3m_emsaSthyY041Wacgxg)
* [A Basic MySQL Tutorial](/rltoken/m_0RMf4RcC5NrHyjY1xN3w)
* [Basic SQL statements: DDL and DML](/rltoken/mLOYmyVwHF1mnb6DcHx2ng)
* [Basic queries: SQL and RA](/rltoken/Vpyvpfwr0GYDU1QZ4GmRAQ)
* [SQL technique: functions](/rltoken/Fsven6UlY3fZRx6-iyms4Q)
* [SQL technique: subqueries](/rltoken/AHQq5v7GFlpJc9Ftnz3rvA)
* [What makes the big difference between a backtick and an apostrophe?](/rltoken/QEr3XcBPhIR-E8NSSn1nzg)
* [MySQL Cheat Sheet](/rltoken/DGejihlnOkkNq-qJFM15MA)
* [MySQL 8.0 SQL Statement Syntax](/rltoken/ePNUeloWxfiXwec7HeKe7Q)
* [here](/rltoken/sxuxGmSk-ZEwuVa1AKKoVQ)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* What’s a database
* What’s a relational database
* What does SQL stand for
* What’s MySQL
* How to create a database in MySQL
* What doesDDLandDMLstand for
* How toCREATEorALTERa table
* How toSELECTdata from a table
* How toINSERT,UPDATEorDELETEdata
* What aresubqueries
* How to use MySQL functions

## Requirements
### General
* Allowed editors:vi,vim,emacs
* All your files will be executed on Ubuntu 22.04 LTS usingMySQL 8.0(version 8.0.25)
* All your files should end with a new line
* All your SQL queries should have a comment just before (i.e. syntax above)
* All your files should start by a comment describing the task
* All SQL keywords should be in uppercase (SELECT,WHERE…)
* AREADME.mdfile, at the root of the folder of the project, is mandatory
* The length of your files will be tested usingwc

## Task
### 0. List databases <a name='subparagraph0'></a>

Write a script that lists all databases of your MySQL server.

```
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                     
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$
```

---

### 1. Create a database <a name='subparagraph1'></a>

Write a script that creates the database <code>hbtn_0c_0</code> in your MySQL server.

* If the database <code>hbtn_0c_0</code> already exists, your script should not fail
* You are not allowed to use the <code>SELECT</code> or <code>SHOW</code> statements

```
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
hbtn_0c_0
mysql
performance_schema
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$
```

---

### 2. Delete a database <a name='subparagraph2'></a>

Write a script that deletes the database <code>hbtn_0c_0</code> in your MySQL server.

* If the database <code>hbtn_0c_0</code> doesn’t exist, your script should not fail
* You are not allowed to use the <code>SELECT</code> or <code>SHOW</code> statements

```
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                     
hbtn_0c_0                                                                                    
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$ cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                                                                                                  
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$
```

---

### 3. List tables <a name='subparagraph3'></a>

Write a script that lists all the tables of a database in your MySQL server.

* The database name will be passed as argument of <code>mysql</code> command (in the following example: <code>mysql</code> is the name of the database)

```
guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
Enter password: 
Tables_in_mysql                                                                              
columns_priv                                                                                 
component                                                                                    
db                                                                                           
default_roles                                                                                
engine_cost                                                                                  
func                                                                                         
general_log                                                                                  
global_grants                                                                                
gtid_executed                                                                                
help_category                                                                                
help_keyword                                                                                 
help_relation                                                                                
help_topic                                                                                   
innodb_index_stats                                                                           
innodb_table_stats                                                                           
password_history                                                                             
plugin                                                                                       
procs_priv                                                                                   
proxies_priv                                                                                 
replication_asynchronous_connection_failover                                                 
replication_asynchronous_connection_failover_managed                                         
role_edges                                                                                   
server_cost                                                                                  
servers                                                                                      
slave_master_info                                                                            
slave_relay_log_info                                                                         
slave_worker_info                                                                            
slow_log                                                                                     
tables_priv                                                                                  
time_zone                                                                                    
time_zone_leap_second                                                                        
time_zone_name                                                                               
time_zone_transition                                                                         
time_zone_transition_type                                                                    
user
guillaume@ubuntu:~/$
```

---

### 4. First table <a name='subparagraph4'></a>

Write a script that creates a table called <code>first_table</code> in the current database in your MySQL server.

* <code>first_table</code> description:


  * <code>id</code> INT
  * <code>name</code> VARCHAR(256)
* The database name will be passed as an argument of the <code>mysql</code> command
* If the table <code>first_table</code> already exists, your script should not fail
* You are not allowed to use the <code>SELECT</code> or <code>SHOW</code> statements

```
guillaume@ubuntu:~/$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Tables_in_hbtn_0c_0
first_table
guillaume@ubuntu:~/$
```

---

### 5. Full description <a name='subparagraph5'></a>

Write a script that prints the following description of the table <code>first_table</code> from the database <code>hbtn_0c_0</code> in your MySQL server.

* The database name will be passed as an argument of the <code>mysql</code> command
* You are not allowed to use the <code>DESCRIBE</code> or <code>EXPLAIN</code> statements

```
guillaume@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Table   Create Table                                                                         
first_table     CREATE TABLE `first_table` (\n  `id` int DEFAULT NULL,\n  `name` varchar(256) DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci        
guillaume@ubuntu:~/$
```

---

### 6. List all in table <a name='subparagraph6'></a>

Write a script that lists all rows of the table <code>first_table</code> from the database <code>hbtn_0c_0</code> in your MySQL server.

* All fields should be printed
* The database name will be passed as an argument of the <code>mysql</code> command

```
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$
```

---

### 7. First add <a name='subparagraph7'></a>

Write a script that inserts a new row in the table <code>first_table</code> (database <code>hbtn_0c_0</code>) in your MySQL server.

* New row:


  * <code>id</code> = <code>89</code>
  * <code>name</code> = <code>Best School</code>
* The database name will be passed as an argument of the <code>mysql</code> command

```
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
id  name
89  Best School
89  Best School
89  Best School
guillaume@ubuntu:~/$
```

---

### 8. Count 89 <a name='subparagraph8'></a>

Write a script that displays the number of records with <code>id = 89</code> in the table <code>first_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.

* The database name will be passed as an argument of the <code>mysql</code> command

```
guillaume@ubuntu:~/$ cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
Enter password: 
3
guillaume@ubuntu:~/$
```

---

### 9. Full creation <a name='subparagraph9'></a>

Write a script that creates a table <code>second_table</code> in the database <code>hbtn_0c_0</code> in your MySQL server and add multiples rows.

* <code>second_table</code> description:


  * <code>id</code> INT
  * <code>name</code> VARCHAR(256)
  * <code>score</code> INT
* The database name will be passed as an argument to the <code>mysql</code> command
* If the table <code>second_table</code> already exists, your script should not fail
* You are not allowed to use the <code>SELECT</code> and <code>SHOW</code> statements
* Your script should create these records:


  * <code>id</code> = 1, <code>name</code> = “John”, <code>score</code> = 10
  * <code>id</code> = 2, <code>name</code> = “Alex”, <code>score</code> = 3
  * <code>id</code> = 3, <code>name</code> = “Bob”, <code>score</code> = 14
  * <code>id</code> = 4, <code>name</code> = “George”, <code>score</code> = 8

```
guillaume@ubuntu:~/$ cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$
```

---

### 10. List by best <a name='subparagraph10'></a>

Write a script that lists all records of the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.

* Results should display both the score and the name (in this order)
* Records should be ordered by score (top first)
* The database name will be passed as an argument of the <code>mysql</code> command

```
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
14  Bob
10  John
8   George
3   Alex
guillaume@ubuntu:~/$
```

---

### 11. Select the best <a name='subparagraph11'></a>

Write a script that lists all records with a <code>score &gt;= 10</code> in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.

* Results should display both the score and the name (in this order)
* Records should be ordered by score (top first)
* The database name will be passed as an argument of the <code>mysql</code> command

```
guillaume@ubuntu:~/$ cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
14  Bob
10  John
guillaume@ubuntu:~/$
```

---

### 12. Cheating is bad <a name='subparagraph12'></a>

Write a script that updates the score of Bob to <code>10</code> in the table <code>second_table</code>.

* You are not allowed to use Bob’s id value, only the <code>name</code> field
* The database name will be passed as an argument of the <code>mysql</code> command

```
guillaume@ubuntu:~/$ cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
10  John
10  Bob
8   George
3   Alex
guillaume@ubuntu:~/$
```

---

### 13. Score too low <a name='subparagraph13'></a>

Write a script that removes all records with a <code>score &lt;= 5</code> in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.

* The database name will be passed as an argument of the <code>mysql</code> command

```
guillaume@ubuntu:~/$ cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
10  John
10  Bob
8   George
guillaume@ubuntu:~/$
```

---

### 14. Average <a name='subparagraph14'></a>

Write a script that computes the score average of all records in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.

* The result column name should be <code>average</code>
* The database name will be passed as an argument of the <code>mysql</code> command

```
guillaume@ubuntu:~/$ cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
average
9.3333
guillaume@ubuntu:~/$
```

---

### 15. Number by score <a name='subparagraph15'></a>

Write a script that lists the number of records with the same score in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.

* The result should display:


  * the <code>score</code>
  * the number of records for this <code>score</code> with the label <code>number</code>
* The list should be sorted by the number of records (descending)
* The database name will be passed as an argument to the <code>mysql</code> command

```
guillaume@ubuntu:~/$ cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   number
10  2
8   1
guillaume@ubuntu:~/$
```

---

### 16. Say my name <a name='subparagraph16'></a>

Write a script that lists all records of the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.

* Don’t list rows where the <code>name</code> column does not contain a value
* Results should display the score and the name (in this order)
* Records should be listed by descending score
* The database name will be passed as an argument to the <code>mysql</code> command

In this example, new data have been added to the table <code>second_table</code>.

```
guillaume@ubuntu:~/$ cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
18  Aria
12  Aria
10  John
10  Bob
guillaume@ubuntu:~/$
```

---


## Authors
vtiquet - [GitHub Profile](https://github.com/vtiquet)
