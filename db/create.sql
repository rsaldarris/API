CREATE TABLE tipo_cultivos(
    codigo INT PRIMARY KEY,
    latitud FLOAT NOT NULL,
    longitud FLOAT NOT NULL,
    producto  VARCHAR(200),
    area FLOAT NOT NULL,
    foto VARCHAR(200)
)