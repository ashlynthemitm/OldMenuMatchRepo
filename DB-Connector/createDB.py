'''
Create the Database System using MySql 
Author: Ashlyn Campbell 

'''
import mysql.connector
from dotenv import load_dotenv
import random
import xlrd
import os

def CreateUserTable():
    create_user_query = """
    CREATE TABLE User(
        user_id INT AUTO_INCREMENT PRIMARY KEY, 
        name VARCHAR(255),
        email VARCHAR(255),
        password VARCHAR(30),
        isAdmin BOOL,
        allergens VARCHAR(255)
    );
   """
    return create_user_query
   
def CreateRestaurantTable():
    # Each Restaurant has a weak entity Menu
    create_restaurant_query = """
    CREATE TABLE Restaurant(
        restaurant_id INT PRIMARY KEY, 
        name VARCHAR(255),
        address VARCHAR(50),
        distance_miles FLOAT,
        type VARCHAR(50),
        average_price_score FLOAT
    );
    
    """
    return create_restaurant_query

def CreateMenuTable():
    create_menu_query = """
    CREATE TABLE Menu(
        menu_id INT PRIMARY KEY,
        menu_item VARCHAR(50),
        allergens VARCHAR(50),
        cook_time INT,
        food_type VARCHAR(50),
        restaurant_id INT,
        FOREIGN KEY (restaurant_id) REFERENCES Restaurant (restaurant_id)
    );
    """
    return create_menu_query

def CreateServesRelation():
    create_serves_relation = """
    CREATE TABLE Serves(
        restaurant_id INT REFERENCES Restaurant(restaurant_id),
        user_id VARCHAR(50) REFERENCES User(user_id),
        PRIMARY KEY (user_id, restaurant_id)
    );
    
    """
    return create_serves_relation
    
def InputRestaurantData():
 
    wb = xlrd.open_workbook('MenuMatch/DB-Connector/data/GroupProjectDB-RestaurantDataSet.xls')
    sheet = wb.sheet_by_index(0)
    rows = sheet.nrows
    
    insert_restaurant_query = """ INSERT INTO 
    Restaurant(restaurant_id, name, address, distance_miles, type, average_price_score) VALUES (%s, %s, %s, %s, %s, %s); """
    
    RestaurantTypeData = {}
    RestaurantData = []
    for r in range(1, rows):
        tmp = (sheet.cell_value(r,0), sheet.cell_value(r,1), sheet.cell_value(r,2),sheet.cell_value(r,3), sheet.cell_value(r,4), sheet.cell_value(r,5))
        RestaurantData.append(tmp)
        if sheet.cell_value(r,3) in RestaurantTypeData:
            # placing each restaurant_id into the queue matched with types to use for creating Menus
            RestaurantTypeData[sheet.cell_value(r,4)].append(sheet.cell_value(r,0)) 
        else:
            RestaurantTypeData[sheet.cell_value(r,4)] = []
    
    return RestaurantData,  insert_restaurant_query, RestaurantTypeData
        
def InputMenuData(RestaurantTypeData):
    
    wb = xlrd.open_workbook('MenuMatch/DB-Connector/data/GroupProjectDB-MenuDataSet.xls')
    sheet = wb.sheet_by_index(0)
    rows = sheet.nrows
    
    insert_menu_query = """ INSERT INTO 
    Menu(menu_id, menu_item, allergens, cook_time, food_type, restaurant_id) VALUES (%s, %s, %s, %s, %s, %s); """
    MenuData = []
    for r in range(1, rows):
        if RestaurantTypeData[sheet.cell_value(r,4)]:
            for rid in RestaurantTypeData[sheet.cell_value(r,4)]:
                # Randomizing the cook time to make the menuData more complex
                cookTime = random.randrange(0,40,1) + sheet.cell_value(r,3)
                tmp = (sheet.cell_value(r,0), sheet.cell_value(r,1), sheet.cell_value(r,2), cookTime, sheet.cell_value(r,4), rid)
                MenuData.append(tmp)
        else: # type is not in the dict
            tmp = (sheet.cell_value(r,0), sheet.cell_value(r,1), sheet.cell_value(r,2), sheet.cell_value(r,3), sheet.cell_value(r,4), None)
            MenuData.append(tmp)
        
    return MenuData, insert_menu_query

def createDatabase(MenuMatch_db):
    try:
        # using this cursor to input data
        cursor = MenuMatch_db.cursor() 
        # create DATABASE
        cursor.execute('CREATE DATABASE MenuMatchTestDB;')
        cursor.execute('USE MenuMatchTestDB;')
        
        # create tables
        cursor.execute(CreateUserTable())
        cursor.execute(CreateRestaurantTable())
        cursor.execute(CreateMenuTable())
        cursor.execute(CreateServesRelation())

        # commit the changes
        MenuMatch_db.commit()

    except mysql.connector.Error as error:
        print(f'Error={error}')
        
    finally:
        # close the connections
        cursor.close()
        MenuMatch_db.close()
        
def inputData(MenuMatch_db):
    try:
        # using this cursor to input data
        cursor = MenuMatch_db.cursor() 
        cursor.execute('USE MenuMatchTestDB;')
        # input restaurant data
        data_to_insert, insert_data_query, RestaurantTypeData = InputRestaurantData()
        for record in data_to_insert:
            cursor.execute(insert_data_query, record)

        # input menu data
        data_to_insert, insert_data_query = InputMenuData(RestaurantTypeData)
        for record in data_to_insert:
            cursor.execute(insert_data_query, record)
        # commit the changes
        MenuMatch_db.commit()
        
        # committed successfully, fetch the data stored 
    except mysql.connector.Error as error:
        print(f'Error={error}')
        
    finally:
        # close the connections
        cursor.close()
        MenuMatch_db.close()
        
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
    #createDatabase(MenuMatch_db) 
    inputData(MenuMatch_db)
    
if __name__ == "__main__":
    main()
