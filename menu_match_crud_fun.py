
import string
from typing import Dict, List, Tuple
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="oonyemaobi1", password="#oonyemaobi1*", database="menumatchdb")

def getAllMenus():
    cursor = conn.cursor()
    selectquery = "SELECT * FROM menu m INNER JOIN restaurants r ON m.restaurant_id = r.restaurant_id"

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
    selectquery = "SELECT * FROM restaurant"

    cursor.execute(selectquery)
    records = cursor.fetchall()
    cursor.close()
    return records
  


def filterRestaurantBasedOn(name:string, distance:string, type:string, price:string):
    cursor = conn.cursor()
    filterquery = "SELECT * FROM restaurant WHERE"
    if(name != ""):
        filterquery = filterquery + " name = " + name
    else:
        if(distance != ""):
            filterquery = filterquery + " distance_miles < " + distance
        if(price != ""):
            if(distance != ""):
                filterquery = filterquery + " AND"
            filterquery = filterquery + " average_price_score < " + price 
        if(type != ""):
            if(price != "" or distance != ""):
                filterquery = filterquery + " AND"
            filterquery = filterquery + " restaurant_type = " + type

    #print(filterquery)
    cursor.execute(filterquery)
    records = cursor.fetchall()
    return records

#filterRestaurantBasedOn("", "", "Foood", "")

    
def filterMenusBasedOn(menu_item:string, allergies:List, wait:string, type:string): #takes a list of allergens
    cursor = conn.cursor()
    filterquery = "SELECT m.menu_item FROM menu m INNER JOIN restaurants r ON m.restaurant_id = r.restaurant_id WHERE"
    if(menu_item != ""):
        filterquery = filterquery + " m.menu_item = " + menu_item
    else:
        if(len(allergies) > 0):
            filterquery = filterquery + " m.allergens NOT IN " + allergies 
        if(wait != ""):
            if(len(allergies) > 0):
                filterquery = filterquery + " AND"
            filterquery = filterquery + " m.cook_time < " + wait 
        if(type != ""):
            if(len(allergies) > 0 or wait != ""):
                filterquery = filterquery + " AND"
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
    selectquery = "SELECT email, password FROM user WHERE email = " + email +" AND password = " + passw

    cursor.execute(selectquery)
    
    if cursor.rowcount > 0:
        records = cursor.fetchall()
        cursor.close()
        return True, records[0]
    
    else:
        cursor.close()
        return False, []
            
    #return records

def createUser(name:string, email:string, passw:string, allergens:List):
    cursor = conn.cursor()
    selectquery = "SELECT email FROM user WHERE email = " + email

    cursor.execute(selectquery)
    
    if cursor.rowcount > 0:
        records = cursor.fetchall()
        cursor.close()
        return "This email already has an account", records[0]
    
    createquery = "INSERT INTO user (name, email, password, isAdmin, allergens) VALUES (%s, %s, %s, %s, %s)"
    values = (name, email, passw, False, allergens)
    cursor.execute(createquery, values)
    records = cursor.fetchall()
    conn.commit()
    cursor.close()
    return "Account Created", records[0]
    

def updateUser(email:string, allergens:List):
    cursor = conn.cursor()
    updatequery = "UPDATE user SET allergens = %s WHERE email = %s"
    values = (email, allergens)

    cursor.execute(updatequery, values)
    conn.commit()
    cursor.close()


def deleteUser(email:string, passw:string):
    cursor = conn.cursor()
    deletequery = "DELETE FROM user WHERE email = " + email +" AND password = " + passw
    cursor.execute(deletequery)
    conn.commit()
    cursor.close()

def setUserRestRating(user_id:string, rest_id:string, rating:string):
    cursor = conn.cursor()
    selectquery = "SELECT user_id, restaurant_id FROM serves WHERE user_id = " + user_id + " AND restaurant_id = " + rest_id

    cursor.execute(selectquery)
    
    if cursor.rowcount > 0:
        updatequery = "UPDATE serves SET rating = %s WHERE user_id = %s AND restaurant_id = %s"
        values = (rating, user_id, rest_id)
        cursor.execute(updatequery, values)
        conn.commit()
    else:
        createquery = "INSERT INTO serves (restaurant_id, user_id, rating) VALUES (%s, %s, %s)"
        values = (rest_id, user_id, rating)
        cursor.execute(createquery, values)
        records = cursor.fetchall()
        conn.commit()

    cursor.close()
    #return "Account Created", records[0]

def updateRestaurantRating():
    cursor = conn.cursor()
    updatequery = "UPDATE restaurant r SET rating = (SELECT AVG (rating) FROM serves s WHERE s.rest_id = r.restaurant_id)"
    cursor.execute(updatequery)
    conn.commit()
    cursor.close()

conn.close()



