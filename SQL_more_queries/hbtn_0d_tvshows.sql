root@4be8121f0126424ead4ad90223194ab3-2377118072:~# cd 
.bash_history                             .mysql_history                            not_here
.bashrc                                   .openvscode-server/                       old_school
.cache/                                   .profile                                  ready_to_be_removed
.emacs.d/                                 empty_directory/                          school
.gitconfig                                holbertonschool-higher_level_programming/ 
.local/                                   my_school/                                
root@4be8121f0126424ead4ad90223194ab3-2377118072:~# cd holbertonschool-higher_level_programming/SQL_more_queries/
root@4be8121f0126424ead4ad90223194ab3-2377118072:~/holbertonschool-higher_level_programming/SQL_more_queries# git pull
Already up to date.
root@4be8121f0126424ead4ad90223194ab3-2377118072:~/holbertonschool-higher_level_programming/SQL_more_queries# git pull
remote: Enumerating objects: 6, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 4 (delta 2), reused 4 (delta 2), pack-reused 0 (from 0)
Unpacking objects: 100% (4/4), 502 bytes | 502.00 KiB/s, done.
From https://github.com/vtiquet/holbertonschool-higher_level_programming
   883a7fd..5f73b25  main       -> origin/main
Updating 883a7fd..5f73b25
Fast-forward
 SQL_more_queries/9-cities_by_state_join.sql | 13 +++++++++++++
 1 file changed, 13 insertions(+)
 create mode 100644 SQL_more_queries/9-cities_by_state_join.sql
root@4be8121f0126424ead4ad90223194ab3-2377118072:~/holbertonschool-higher_level_programming/SQL_more_queries# echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id      name
1       California
2       Arizona
3       Texas
root@4be8121f0126424ead4ad90223194ab3-2377118072:~/holbertonschool-higher_level_programming/SQL_more_queries# echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id      state_id        name
1       1       San Francisco
root@4be8121f0126424ead4ad90223194ab3-2377118072:~/holbertonschool-higher_level_programming/SQL_more_queries# cat 9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id      name    name
1       San Francisco   California
root@4be8121f0126424ead4ad90223194ab3-2377118072:~/holbertonschool-higher_level_programming/SQL_more_queries# ls
0-privileges.sql   2-create_read_user.sql  4-never_empty.sql  6-states.sql  8-cities_of_california_subquery.sql  README.md
1-create_user.sql  3-force_name.sql        5-unique_id.sql    7-cities.sql  9-cities_by_state_join.sql
root@4be8121f0126424ead4ad90223194ab3-2377118072:~/holbertonschool-higher_level_programming/SQL_more_queries# ls -la
total 52
drwxr-xr-x  2 root root 4096 Oct 21 12:03 .
drwxr-xr-x 19 root root 4096 Oct 21 07:35 ..
-rw-r--r--  1 root root  164 Oct 21 11:04 0-privileges.sql
-rw-r--r--  1 root root  219 Oct 21 11:04 1-create_user.sql
-rw-r--r--  1 root root  276 Oct 21 08:56 2-create_read_user.sql
-rw-r--r--  1 root root  165 Oct 21 11:04 3-force_name.sql
-rw-r--r--  1 root root  166 Oct 21 11:07 4-never_empty.sql
-rw-r--r--  1 root root  191 Oct 21 11:11 5-unique_id.sql
-rw-r--r--  1 root root  238 Oct 21 11:18 6-states.sql
-rw-r--r--  1 root root  351 Oct 21 11:24 7-cities.sql
-rw-r--r--  1 root root  250 Oct 21 11:30 8-cities_of_california_subquery.sql
-rw-r--r--  1 root root  188 Oct 21 12:03 9-cities_by_state_join.sql
-rw-r--r--  1 root root   13 Oct 21 07:35 README.md
root@4be8121f0126424ead4ad90223194ab3-2377118072:~/holbertonschool-higher_level_programming/SQL_more_queries# nanon