-- Write a script that creates a table second_table in the database
CREATE TABLE IF NOT EXISTS seconde_table (id INT,
	name VARCHAR(256),
	score INT);
INSERT INTO seconde_table (id, name, score) VALUES (1, "John", 10);
INSERT INTO seconde_table (id, name, score) VALUES (2, "Alex", 3);
INSERT INTO seconde_table (id, name, score) VALUES (3, "Bob", 14);
INSERT INTO seconde_table (id, name, score) VALUES (4, "George", 8);
