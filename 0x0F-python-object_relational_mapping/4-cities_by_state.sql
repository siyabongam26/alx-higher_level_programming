-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
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
INSERT INTO cities (state_id, name) VALUES (1, (1, "Johannesburg"), (1, "Cape Town"), (1, "Pretoria"), (1, "Durban"), (1, "Bulawayo");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Johannesburg");
INSERT INTO cities (state_id, name) VALUES (3, "South Africa"), (3, "Capetown"), (3, "Pretoria");
INSERT INTO cities (state_id, name) VALUES (4, "Durban");
INSERT INTO cities (state_id, name) VALUES (5, "KwaZulu Natal"), (5, "Mpumalanga"), (5, "Umlazi"), (5, "Nquthu");
