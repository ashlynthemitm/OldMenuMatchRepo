'''
Create the Database System using MySql 
Author: Ashlyn Campbell 

'''
import mysql.connector
from dotenv import load_dotenv
import xlrd
import os

def CreateUserTable():
    create_user_query = """
    CREATE TABLE User(
        id INT AUTO_INCREMENT PRIMARY KEY, 
        name VARCHAR(255),
        email VARCHAR(255),
        password VARCHAR(30),
        isAdmin BOOL,
        allergens VARCHAR(255)
    )
   """
    return create_user_query
   
def CreateRestaurantTable():
    # Each Restaurant has a weak entity Menu
    
    create_restaurant_query = """
    CREATE TABLE Restaurant(
        id INT AUTO_INCREMENT PRIMARY KEY, 
        name VARCHAR(255),
        address VARCHAR(50),
        distance_miles FLOAT,
        type VARCHAR(50),
        average_price_score FLOAT
    )
    
    """
    return create_restaurant_query
     
def CreateMenuTable():
    create_menu_query = """
    CREATE TABLE Menu(
        food_item VARCHAR(50) PRIMARY KEY,
        allergens VARCHAR(50),
        cook_time VARCHAR(50)
    )
    """
    return create_menu_query
    
def InputRestaurantData():
    
    data = open('data/GroupProjectDB-RestaurantDataSet.xlsx')
    
    wb = xlrd.open_workbook(data)
    sheet = wb.sheet_by_index(0)
    rows = sheet.nrows
    
    insert_restaurant_query = """ INSERT INTO 
    Restaurant(name, address, distance_miles, type, average_price_score) VALUES (%s, %s, %s, %s, %s) """
    
    RestaurantData = []
    for r in range(1, rows):
        tmp = (sheet.cell_value(r,0), sheet.cell_value(r,1), sheet.cell_value(r,2),sheet.cell_value(r,3), sheet.cell_value(r,4),sheet.cell_value(r,5))
        RestaurantData.append(tmp)
    
    return RestaurantData, insert_restaurant_query
        
def InputMenuData():
    
    data = open('data/GroupProjectDB-MenuDataSet.xlsx')
    
    wb = xlrd.open_workbook(data)
    sheet = wb.sheet_by_index(0)
    rows = sheet.nrows
    
    insert_menu_query = """ INSERT INTO 
    Restaurant(food_item, allergen, cook_time) VALUES (%s, %s, %s) """
    MenuData = []
    for r in range(1, rows):
        tmp = (sheet.cell_value(r,0), sheet.cell_value(r,1), sheet.cell_value(r,2))
        MenuData.append(tmp)
        
    return MenuData, insert_menu_query

def main():
    load_dotenv()
    host_db = os.getenv('DB_HOST')
    username_db = os.getenv('DB_USERNAME')
    password_db = os.getenv('DB_PASSWORD')
    MenuMatch_db = mysql.connector.connect(
        host=host_db,
        user=username_db,
        password=password_db
    )
    
    # using this cursor to input data
    cursor = MenuMatch_db.cursor() 
    
    # create tables
    cursor.execute(CreateUserTable())
    cursor.execute(CreateRestaurantTable())
    cursor.execute(CreateMenuTable())
    
    # input restaurant data
    data_to_insert, insert_data_query = InputRestaurantData()
    for record in data_to_insert:
        cursor.execute(insert_data_query, record)
    
    # input menu data
    data_to_insert, insert_data_query = InputMenuData()
    for record in data_to_insert:
        cursor.execute(insert_data_query, record)
    
    # commit the changes
    MenuMatch_db.commit()
    
    # close the connection
    MenuMatch_db.close()

if __name__ == "__main__":
    main()
