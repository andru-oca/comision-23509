-- SHOW DATABASES;

# NO SE LO RECOMIENDO

/*
	ASD
	ASD
	ASD
	FALLA! 
*/


DROP DATABASE IF EXISTS libreria_23509;

CREATE DATABASE libreria_23509 ;

USE  libreria_23509;

CREATE TABLE AUTOR(
	CODIGO_AUTOR INT NOT NULL AUTO_INCREMENT,
    NOMBRE VARCHAR(50) DEFAULT 'NO NAME FOUND',
    PRIMARY KEY(CODIGO_AUTOR)
) ;

-- 

CREATE TABLE LIBRO(
	CODIGO_LIBRO INT NOT NULL AUTO_INCREMENT,
	ISBN VARCHAR(100) DEFAULT '987-ISBN-PIRULO',
	TITULO VARCHAR(100)  NOT NULL,
	EDITORIAL VARCHAR(100) ,
	PAGINAS INT DEFAULT 100,
    PRIMARY KEY(CODIGO_LIBRO)
);


CREATE TABLE EJEMPLAR(
	CODIGO_EJEMPLAR INT NOT NULL AUTO_INCREMENT,
	CODIGO_LIBRO INT NOT NULL,
	ALMACEN VARCHAR(100),
    PRIMARY KEY(CODIGO_EJEMPLAR)
    
	--  FOREIGN KEY ME LO ESTOY COMIENDO A PROPOSITO
);

ALTER TABLE EJEMPLAR
ADD FOREIGN KEY (CODIGO_LIBRO) REFERENCES LIBRO(CODIGO_LIBRO);


CREATE TABLE USUARIO(
	ID_USUARIO INT NOT NULL AUTO_INCREMENT,
    NOMBRE VARCHAR(50),
    TELEFONO NVARCHAR(50),
    DIRECCION VARCHAR(50),
    PRIMARY KEY (ID_USUARIO)
);

CREATE TABLE VENTA(
	ID_VENTA INT NOT NULL AUTO_INCREMENT,
	CODIGO_EJEMPLAR INT NOT NULL,
	ID_USUARIO INT NOT NULL,
	PUNTO_VENTA VARCHAR(100),
	PRECIO_VENTA DECIMAL(10,2),
	FECHA_VENTA DATETIME ,

	PRIMARY KEY(ID_VENTA),
    FOREIGN KEY (CODIGO_EJEMPLAR) REFERENCES EJEMPLAR(CODIGO_EJEMPLAR),
    FOREIGN KEY (ID_USUARIO) REFERENCES USUARIO(ID_USUARIO)
);


CREATE TABLE LINK_AUTOR_LIBRO(
	CODIGO_AUTOR INT NOT NULL,
	CODIGO_LIBRO INT NOT NULL,
    
	LUGAR_ESCRITURA VARCHAR(100),
    -- SE DEFINE LA CONCATENACION
    PRIMARY KEY(CODIGO_AUTOR , CODIGO_LIBRO),
    -- SE DEFINE SUS CLAVES FORANEAS
	FOREIGN KEY (CODIGO_AUTOR) REFERENCES AUTOR(CODIGO_AUTOR),
    FOREIGN KEY (CODIGO_LIBRO) REFERENCES LIBRO(CODIGO_LIBRO)
);



/*
-- 

INSERT INTO AUTOR (NOMBRE)
VALUES
('FLAVIA'),
('CAROLINA'),
('ARTURO'),
('LARA');



SELECT 
	CODIGO_AUTOR
,	NOMBRE

FROM libreria_23509.AUTOR;



SELECT 
	CODIGO_AUTOR
,	LOWER(NOMBRE) AS NOMBRE_MINUSCULA
,	curdate() AS FECHA_INGRESO 

FROM libreria_23509.AUTOR;


insert into AUTOR (NOMBRE) values ('Conrade');
insert into AUTOR (NOMBRE) values ('Gertrudis');
insert into AUTOR (NOMBRE) values ('Travus');
insert into AUTOR (NOMBRE) values ('Myrtice');
insert into AUTOR (NOMBRE) values ('Jonathon');
insert into AUTOR (NOMBRE) values ('Penny');
insert into AUTOR (NOMBRE) values ('Lucian');
insert into AUTOR (NOMBRE) values ('Beret');
insert into AUTOR (NOMBRE) values ('Stephannie');
insert into AUTOR (NOMBRE) values ('Winnie');
insert into AUTOR (NOMBRE) values ('Kristine');
insert into AUTOR (NOMBRE) values ('Tybi');
insert into AUTOR (NOMBRE) values ('Gilligan');
insert into AUTOR (NOMBRE) values ('Ilsa');
insert into AUTOR (NOMBRE) values ('Jordon');
insert into AUTOR (NOMBRE) values ('Stevana');
insert into AUTOR (NOMBRE) values ('Terza');
insert into AUTOR (NOMBRE) values ('Laurene');
insert into AUTOR (NOMBRE) values (null);
insert into AUTOR (NOMBRE) values ('Esdras');
insert into AUTOR (NOMBRE) values ('Zeb');
insert into AUTOR (NOMBRE) values ('Mick');
insert into AUTOR (NOMBRE) values ('Ricardo');
insert into AUTOR (NOMBRE) values ('Hestia');
insert into AUTOR (NOMBRE) values ('Errick');
insert into AUTOR (NOMBRE) values ('Celeste');
insert into AUTOR (NOMBRE) values ('Doug');
insert into AUTOR (NOMBRE) values ('Barde');
insert into AUTOR (NOMBRE) values ('Joachim');
insert into AUTOR (NOMBRE) values (null);
insert into AUTOR (NOMBRE) values ('Jayme');
insert into AUTOR (NOMBRE) values ('West');
insert into AUTOR (NOMBRE) values ('Stephani');
insert into AUTOR (NOMBRE) values ('Ellen');
insert into AUTOR (NOMBRE) values ('Corie');
insert into AUTOR (NOMBRE) values ('Riordan');
insert into AUTOR (NOMBRE) values ('Kalinda');
insert into AUTOR (NOMBRE) values (null);
insert into AUTOR (NOMBRE) values ('Allene');
insert into AUTOR (NOMBRE) values ('Dre');
insert into AUTOR (NOMBRE) values ('Karlene');
insert into AUTOR (NOMBRE) values ('Livvie');
insert into AUTOR (NOMBRE) values ('Teri');
insert into AUTOR (NOMBRE) values ('Melania');
insert into AUTOR (NOMBRE) values ('Ritchie');
insert into AUTOR (NOMBRE) values ('Ginelle');
insert into AUTOR (NOMBRE) values ('Jocelyne');
insert into AUTOR (NOMBRE) values ('Hilary');
insert into AUTOR (NOMBRE) values ('Ezechiel');
insert into AUTOR (NOMBRE) values ('Roxi');
insert into AUTOR (NOMBRE) values ('Lind');
insert into AUTOR (NOMBRE) values ('Ursala');
insert into AUTOR (NOMBRE) values ('Jesse');
insert into AUTOR (NOMBRE) values (null);
insert into AUTOR (NOMBRE) values ('Andriana');
insert into AUTOR (NOMBRE) values ('Kylynn');
insert into AUTOR (NOMBRE) values ('Cammi');
insert into AUTOR (NOMBRE) values ('Shirline');
insert into AUTOR (NOMBRE) values (null);
insert into AUTOR (NOMBRE) values ('Emyle');
insert into AUTOR (NOMBRE) values ('Chucho');
insert into AUTOR (NOMBRE) values ('Salli');
insert into AUTOR (NOMBRE) values ('Mina');
insert into AUTOR (NOMBRE) values ('Brittney');
insert into AUTOR (NOMBRE) values ('Manfred');
insert into AUTOR (NOMBRE) values (null);
insert into AUTOR (NOMBRE) values ('Celene');
insert into AUTOR (NOMBRE) values (null);
insert into AUTOR (NOMBRE) values ('Erma');
insert into AUTOR (NOMBRE) values ('Maison');
insert into AUTOR (NOMBRE) values (null);
insert into AUTOR (NOMBRE) values ('Terrye');
insert into AUTOR (NOMBRE) values (null);
insert into AUTOR (NOMBRE) values ('Emmery');
insert into AUTOR (NOMBRE) values ('Kele');
insert into AUTOR (NOMBRE) values ('Marc');
insert into AUTOR (NOMBRE) values ('Charlie');
insert into AUTOR (NOMBRE) values ('Cornelle');
insert into AUTOR (NOMBRE) values ('Boyce');
insert into AUTOR (NOMBRE) values ('Helene');
insert into AUTOR (NOMBRE) values ('Devora');
insert into AUTOR (NOMBRE) values ('Evangeline');
insert into AUTOR (NOMBRE) values ('North');
insert into AUTOR (NOMBRE) values (null);
insert into AUTOR (NOMBRE) values ('Arabella');
insert into AUTOR (NOMBRE) values ('Flemming');
insert into AUTOR (NOMBRE) values ('Dominga');
insert into AUTOR (NOMBRE) values (null);
insert into AUTOR (NOMBRE) values ('Nolana');
insert into AUTOR (NOMBRE) values ('Edvard');
insert into AUTOR (NOMBRE) values ('Andrea');
insert into AUTOR (NOMBRE) values ('Darb');
insert into AUTOR (NOMBRE) values ('Dion');
insert into AUTOR (NOMBRE) values ('Karlens');
insert into AUTOR (NOMBRE) values ('Boot');
insert into AUTOR (NOMBRE) values ('Liz');
insert into AUTOR (NOMBRE) values ('Jessy');
insert into AUTOR (NOMBRE) values ('Vivie');
insert into AUTOR (NOMBRE) values ('Donall');
insert into AUTOR (NOMBRE) values ('Donall');



SELECT 
--	CODIGO_AUTOR
	LOWER(NOMBRE) AS NOMBRE_MINUSCULA
,	COUNT(1) AS CANTIDAD_DE_NOMBRE
-- ,	curdate() AS FECHA_INGRESO 

FROM libreria_23509.AUTOR
GROUP BY NOMBRE 
ORDER BY CANTIDAD_DE_NOMBRE DESC
LIMIT 10
;





SELECT 
	CODIGO_AUTOR
,	NOMBRE

FROM back_up_libreria.AUTOR;


*/
