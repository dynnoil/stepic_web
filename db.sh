sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE USER 'dynnoil'@'localhost' IDENTIFIED BY 'penumbra12345'"
mysql -uroot -e "CREATE DATABASE askdb"
mysql -uroot -e "GRANT ALL ON askdb.* TO 'dynnoil'"
