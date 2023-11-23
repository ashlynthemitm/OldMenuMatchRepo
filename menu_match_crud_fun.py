
import string
from typing import Dict, List, Tuple
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="oonyemaobi1", password="#oonyemaobi1*", database="menumatchdb")

def getAllMenus():
    cursor = conn.cursor()
    selectquery = "select * from menu m INNER JOIN restaurants r ON m.restaurant_id = r.restaurant_id"

    cursor.execute(selectquery)
    records = cursor.fetchall()
    '''
    print("No. of Menu Items", cursor.rowcount)

    for row in records:
        print("Menu ID:", row[0])
        print("Item:", row[1])
        print("Allergens:", row[2])
        print("Avg Wait Time:", row[3])
        print("Food Type:", row[4])
        print("Restaurant Name", row[5])
        print("\n")
    '''
    cursor.close()
    return records


def getAllRestaurants():
    cursor = conn.cursor()
    selectquery = "select * from restaurant"

    cursor.execute(selectquery)
    records = cursor.fetchall()
    cursor.close()
    return records
  


def filterRestaurantBasedOn(name:string, distance:string, type:string, price:string):
    cursor = conn.cursor()
    filterquery = "select * from restaurant where"
    if(name != ""):
        filterquery = filterquery + " name = " + name
    else:
        if(distance != ""):
            filterquery = filterquery + " distance_miles < " + distance
        if(price != ""):
            if(distance != ""):
                filterquery = filterquery + " and"
            filterquery = filterquery + " average_price_score < " + price 
        if(type != ""):
            if(price != "" or distance != ""):
                filterquery = filterquery + " and"
            filterquery = filterquery + " restaurant_type = " + type

    #print(filterquery)
    cursor.execute(filterquery)
    records = cursor.fetchall()
    return records

#filterRestaurantBasedOn("", "", "Foood", "")

    
def filterMenusBasedOn(menu_item:string, allergies:List, wait:string, type:string): #takes a list of allergens
    cursor = conn.cursor()
    filterquery = "select m.menu_item from menu m INNER JOIN restaurants r ON m.restaurant_id = r.restaurant_id where"
    if(menu_item != ""):
        filterquery = filterquery + " m.menu_item = " + menu_item
    else:
        if(len(allergies) > 0):
            filterquery = filterquery + " m.allergens NOT IN " + allergies 
        if(wait != ""):
            if(len(allergies) > 0):
                filterquery = filterquery + " and"
            filterquery = filterquery + " m.cook_time < " + wait 
        if(type != ""):
            if(len(allergies) > 0 or wait != ""):
                filterquery = filterquery + " and"
            filterquery = filterquery + " m.food_type = " + type

    cursor.execute(filterquery)
    records = cursor.fetchall()

    
    
    '''
    print("No. of Menu Items", cursor.rowcount)

    for row in records:
        print("Menu ID:", row[0])
        print("Item:", row[1])
        print("Allergens:", row[2])
        print("Avg Wait Time:", row[3])
        print("Food Type:", row[4])
        print("Restaurant Name", row[5])
        print("\n")
    '''

    cursor.close()
    return records

def getUserPassCombo(email:string, passw:string):
    cursor = conn.cursor()
    selectquery = "select email, password from user where email = " + email +" and password = " + passw

    cursor.execute(selectquery)
    
    if cursor.rowcount > 0:
        records = cursor.fetchall()
        return True, records[0]
    
    else:
        return False, []
            
    #return records

def createUser(name:string, email:string, passw:string, allergens:List):
    cursor = conn.cursor()
    selectquery = "select email from user where email = " + email

    cursor.execute(selectquery)
    
    if cursor.rowcount > 0:
        records = cursor.fetchall()
        return "This email already has an account", records[0]
    
    createquery = "INSERT INTO user (name, email, password, isAdmin, allergens) VALUES (%s, %s, %s, %s, %s)"
    values = (name, email, passw, False, allergens)
    cursor.execute(createquery, values)
    records = cursor.fetchall()
    conn.commit()
    return "Account Created", records[0]
    

def updateUser(email:string, allergens:List):
    cursor = conn.cursor()
    updatequery = "UPDATE user SET allergens = %s WHERE email = %s"
    values = (email, allergens)

    cursor.execute(updatequery, values)
    conn.commit()



def deleteUser(email:string, passw:string):
    cursor = conn.cursor()
    deletequery = "DELETE FROM user WHERE email = " + email +" AND password = " + passw
    cursor.execute(deletequery)
    conn.commit()

conn.close()



