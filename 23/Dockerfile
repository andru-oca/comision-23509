
# con esto le indico que estoy usando una base
# estas bases son creadas directamente desde un repositorio de 
# imagenes de contenedores
FROM mysql:8.0

# Le indicamos quienes o quien va a tener dominio sobre esta area,
# no es de vital importancia pero puede pasar que necesitemos
# saber a quien le vamos a dar permisos

RUN chown -R mysql:root /var/lib/mysql/

# es mucha utilidad cuando manejamos variables de entornos donde
# necesitamos informacion privadatizada o compartida
# de manera organizacional

ARG MYSQL_DATABASE
ARG MYSQL_USER
ARG MYSQL_PASSWORD
ARG MYSQL_ROOT_PASSWORD

ENV MYSQL_DATABASE=$MYSQL_DATABASE
ENV MYSQL_USER=$MYSQL_USER
ENV MYSQL_PASSWORD=$MYSQL_PASSWORD
ENV MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD


# puerto en la que expone el puerto a utilizar
EXPOSE 3306


# comando para correr correctamente esta base de datos sin vol
# docker build -t mysql-server .
# docker run --name mysql-server-container -p 127.0.0.1:3306:3306  -d  --env-file .\.env mysql-server
# docker exec -it mysql-server-container mysql -p
