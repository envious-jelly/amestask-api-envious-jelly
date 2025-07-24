# CREATE SCHEMA ames_naloge CHARACTER SET utf8mb4 COLLATE utf8mb4_slovenian_ci;
# USE ames_naloge;

CREATE TABLE IF NOT EXISTS users (
	id VARCHAR(8) PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    description VARCHAR(255),
    date_created DATE NOT NULL DEFAULT CURRENT_DATE()
);

CREATE TABLE IF NOT EXISTS tasks (
	id INT PRIMARY KEY AUTO_INCREMENT,
    uid VARCHAR(8) NOT NULL,
    title VARCHAR(100) NOT NULL,
    description VARCHAR(255) NOT NULL,
    CONSTRAINT task_uid FOREIGN KEY (uid) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS comments (
    uid VARCHAR(8) NOT NULL,
    tid INT NOT NULL,
    datetime DATETIME DEFAULT current_timestamp NOT NULL,
    contents VARCHAR(255) NOT NULL,
    CONSTRAINT comment_uid FOREIGN KEY (uid) REFERENCES users(id) ON DELETE CASCADE,
    CONSTRAINT comment_tid FOREIGN KEY (tid) REFERENCES tasks(id) ON DELETE CASCADE,
    PRIMARY KEY (uid, tid, datetime)
);

# Zacetni podatki baze
DELETE FROM comments;
DELETE FROM tasks;
DELETE FROM users;
COMMIT;

INSERT INTO users (id, name, description) VALUES
('janez123' , 'Janez'	, 'Zdravo, sem Janez!'),
('petra78'  , 'Petra'	, NULL),
('anze2003' , 'Anže'	, 'nevem kva kle napisat'),
('hana_na', 'Hana'	, 'Živjo!!! Nova sem tukaj :)');

INSERT INTO tasks (uid, title, description, id) VALUES
('janez123', 'Načrt za bazo'				, 'Ustvari načrt za MySQL bazo'	, 1),
('janez123', 'Implementacija MySQL baze'	, 'Napiši SQL skript'			, 2),
('janez123', 'Ustvari testne podatke'		, '...'							, 3),
('petra78' , 'Napiši zaledni sistem'		, 'Jezik: ?????'				, 4),
('anze2003', 'potegn dol angular'			, 'pa node.js'					, 5),
('anze2003', 'pejt po kavo'					, '...'							, 6),
('anze2003', 'kako se centrira div??????'	, 'css'							, 7),
('anze2003', 'toast'						, 'obvestila'					, 8)
;

INSERT INTO comments (uid, tid, contents) VALUES 
('janez123', 1, 'Končal'),
('janez123', 2, 'Končal'),
('hana_na', 3, 'Kaj je MySQL?'),
('petra78', 5, 'A še nisi..?')
;

INSERT INTO comments (uid, tid, contents) VALUES 
('anze2003', 1, 'že????'),
('anze2003', 3, 'kak da to neveš?????'),
('anze2003', 5, 'zdele sm')
;

INSERT INTO comments (uid, tid, contents) VALUES 
('hana_na', 8, 'Meni bi zelo pasal en toast zdajle :)'),
('anze2003', 3, '???'),
('petra78', 5, 'Ok.')
;
