-- Create database hbtn_0e_14_usa, tables states and cities + some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_14_usa;
USE hbtn_0e_14_usa;

CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("South Africa"), ("Zimbabwe"), ("Lesotho"), ("New York"), ("Swaziland");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "South Africa"), (1, "Capetown"), (1, "Durban"), (1, "Pretoria"), (1, "Johannesburg");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Johanessburg");
INSERT INTO cities (state_id, name) VALUES (3, "Capetown"), (3, "Ebiza"), (3, "Frontview");
INSERT INTO cities (state_id, name) VALUES (4, "Pretoria");
INSERT INTO cities (state_id, name) VALUES (5, "Durban"), (5, "Beach Front"), (5, "Umlazi"), (5, "Garden City");
