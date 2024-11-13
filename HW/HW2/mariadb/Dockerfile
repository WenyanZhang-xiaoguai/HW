FROM mariadb:10.8
ENV MYSQL_ALLOW_EMPTY_PASSWORD no
ENV MYSQL_ROOT_PASSWORD rootpwd
COPY ./cw2-database.sql /docker-entrypoint-initdb.d/
COPY ./my.cnf /etc/mysql/mariadb.conf.d/99-custom.cnf
RUN chmod 644 /etc/mysql/mariadb.conf.d/99-custom.cnf
RUN chown -R mysql:mysql /docker-entrypoint-initdb.d/
EXPOSE 3306