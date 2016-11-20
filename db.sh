sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE USER \'dynnoil\' IDENTIFIED BY \'penumbra12345\'"
mysql -uroot -e "CREATE DATABASE askdb"
mysql -uroot -e "GRANT ALL askdb.* TO \'dynnoil\'"
