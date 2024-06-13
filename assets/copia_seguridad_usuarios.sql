BEGIN TRANSACTION;
CREATE TABLE producto(
    id INTEGER NOT NULL,
    nombre TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    precio REAL NOT NULL
);
INSERT INTO "producto" VALUES(2001,'Mouse','Mouse inalámbrico',70000.0);
INSERT INTO "producto" VALUES(2002,'Teclado','Teclado gamer',190000.0);
INSERT INTO "producto" VALUES(2003,'Monitor','Monitor LED',700000.0);
INSERT INTO "producto" VALUES(2004,'Parlantes','Parlantes 5.1',400000.0);
INSERT INTO "producto" VALUES(2005,'Smartphone','Smartphone Android',800000.0);

CREATE TABLE usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    clave TEXT NOT NULL,
    email TEXT NOT NULL
);
COMMIT;
