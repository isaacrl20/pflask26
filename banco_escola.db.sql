BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "aluno" (
	"id"	INTEGER,
	"nome"	TEXT,
	"idade"	INTEGER,
	"cidade"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "aluno" VALUES (1,'José Lima Silva Sousa',17,'Teresina');
INSERT INTO "aluno" VALUES (2,'Ana Costa',20,'Floriano');
INSERT INTO "aluno" VALUES (3,'Lucas Souza Silva',18,'Teresina');
INSERT INTO "aluno" VALUES (4,'Juliana Rocha Silva',21,'Parnaíba');
INSERT INTO "aluno" VALUES (5,'Carlos Mendes',16,'Floriano');
INSERT INTO "aluno" VALUES (6,'Beatriz Alves',23,'Teresina');
INSERT INTO "aluno" VALUES (7,'Jose da Silva Santos',19,'Timon');
INSERT INTO "aluno" VALUES (8,'José Lima Silva Sousa',17,'Teresina');
INSERT INTO "aluno" VALUES (9,'Ana Costa',20,'Floriano');
INSERT INTO "aluno" VALUES (10,'Lucas Souza Silva',18,'Teresina');
INSERT INTO "aluno" VALUES (11,'Juliana Rocha Silva',21,'Parnaíba');
INSERT INTO "aluno" VALUES (12,'Carlos Mendes',16,'Floriano');
INSERT INTO "aluno" VALUES (13,'Beatriz Alves',23,'Teresina');
INSERT INTO "aluno" VALUES (14,'Jose da Silva Santos',19,'Timon');
COMMIT;
