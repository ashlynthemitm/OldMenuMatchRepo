CREATE DATABASE MenuMatchDB;
USE MenuMatchDB;

CREATE TABLE User(
        user_id INT AUTO_INCREMENT PRIMARY KEY, 
        name VARCHAR(255),
        email VARCHAR(255) UNIQUE,
        password VARCHAR(30),
        isAdmin BOOL,
        allergens VARCHAR(255)
    );
CREATE TABLE Restaurant(
        restaurant_id INT PRIMARY KEY, 
        name VARCHAR(255),
        address VARCHAR(50),
        distance_miles FLOAT,
        restaurant_type VARCHAR(50),
        average_price_score FLOAT
    );
CREATE TABLE Menu(
        menu_id INT PRIMARY KEY,
        menu_item VARCHAR(50),
        allergens VARCHAR(50),
        cook_time INT,
        food_type VARCHAR(50),
        restaurant_id INT,
        FOREIGN KEY (restaurant_id) REFERENCES Restaurant (restaurant_id)
    );
    
CREATE TABLE Serves(
        restaurant_id INT REFERENCES Restaurant(restaurant_id),
        user_id VARCHAR(50) REFERENCES User(user_id),
        PRIMARY KEY (user_id, restaurant_id)
    );
    
use menumatchdb;
SELECT * FROM Menu;

