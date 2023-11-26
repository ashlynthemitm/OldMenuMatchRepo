
import string
from typing import Dict, List, Tuple
import mysql.connector


def getAllMenus():
    conn = mysql.connector.connect(host="localhost", user="oonyemaobi1", password="#oonyemaobi1*", database="menumatchdb")
    cursor = conn.cursor()
    selectquery = "SELECT * FROM menu m INNER JOIN restaurant r ON m.restaurant_id = r.restaurant_id GROUP BY r.name"

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
    conn.close()
    return records


def getAllRestaurants():
    conn = mysql.connector.connect(host="localhost", user="oonyemaobi1", password="#oonyemaobi1*", database="menumatchdb")
    cursor = conn.cursor()
    selectquery = "SELECT * FROM restaurant"

    cursor.execute(selectquery)
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return records
  


def filterRestaurantBasedOn(name:string, distance:string, type:string, price:string):
    conn = mysql.connector.connect(host="localhost", user="oonyemaobi1", password="#oonyemaobi1*", database="menumatchdb")
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
    cursor.close()
    conn.close()
    return records

#filterRestaurantBasedOn("", "", "Foood", "")

    
def filterMenusBasedOn(menu_item:string, allergies:List, wait:string, type:string): #takes a list of allergens
    conn = mysql.connector.connect(host="localhost", user="oonyemaobi1", password="#oonyemaobi1*", database="menumatchdb")
    cursor = conn.cursor()
    filterquery = "SELECT m.menu_item FROM menu m INNER JOIN restaurant r ON m.restaurant_id = r.restaurant_id WHERE"
    if(menu_item != ""):
        filterquery = filterquery + " m.menu_item = " + menu_item
    else:
        if(len(allergies) > 0):
            algs = '('
            i = 0
            while(i < len(allergies)):
                algs = algs + "\""+ allergies[i] + "\","
                i+=1
            algs = algs[0:-1] + ')'
            print(algs)

            filterquery = filterquery + " m.allergens NOT IN " + algs
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
    conn.close()
    return records

def getUserPassCombo(email:string, passw:string):
    conn = mysql.connector.connect(host="localhost", user="oonyemaobi1", password="#oonyemaobi1*", database="menumatchdb")
    cursor = conn.cursor()
    selectquery = "SELECT email, password FROM user WHERE email = \'" + email +"\' AND password = \'" + passw + "\'"
    print(selectquery)
    cursor.execute(selectquery)
    
    records = cursor.fetchall()

    if cursor.rowcount > 0:
        cursor.close()
        conn.close()
        return True, records[0]
    
    else:
        cursor.close()
        conn.close()
        return False, []
            
    #return records

def checkUserCreated(email:string):
    conn = mysql.connector.connect(host="localhost", user="oonyemaobi1", password="#oonyemaobi1*", database="menumatchdb")
    cursor = conn.cursor()
    selectquery = "SELECT email FROM user WHERE email = \'" + email + "\'"

    num = cursor.execute(selectquery)
    
    if cursor.rowcount > 0:
        records = cursor.fetchall()
        cursor.close()
        conn.close()
        print("This email already has an account")
        return True
    return False
    

def createUser(name:string, email:string, passw:string, allergens:string):
    conn = mysql.connector.connect(host="localhost", user="oonyemaobi1", password="#oonyemaobi1*", database="menumatchdb")
    cursor = conn.cursor()
    if(checkUserCreated(email)):
        return "This email has an account", ""
    
    createquery = "INSERT INTO user (name, email, password, isAdmin, allergens) VALUES (%s, %s, %s, %s, %s)"
    values = (name, email, passw, False, allergens)
    cursor.execute(createquery, values)
    conn.commit()
    num = cursor.execute("select * from user where email = \'" + email + "\'")
    records = cursor.fetchall()
    num = cursor.rowcount
    cursor.close()
    conn.close()

    if(num > 0):
        return "User created", num
    else:
        return "User not created", "empty"
    

def updateUser(email:string, allergens:List):
    conn = mysql.connector.connect(host="localhost", user="oonyemaobi1", password="#oonyemaobi1*", database="menumatchdb")
    cursor = conn.cursor()
    updatequery = "UPDATE user SET allergens = %s WHERE email = %s"
    values = (allergens, email)

    num = cursor.execute(updatequery, values)
    records = cursor.fetchall()
    num = cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()

    if(num > 0):
        return "User updated"
    else:
        return "User not updated"


def deleteUser(email:string, passw:string):
    conn = mysql.connector.connect(host="localhost", user="oonyemaobi1", password="#oonyemaobi1*", database="menumatchdb")
    cursor = conn.cursor()
    deletequery = "DELETE FROM user WHERE email = \'" + email +"\' AND password = \'" + passw + "\'"
    num = cursor.execute(deletequery)
    num = cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()

    if(num > 0):
        return "User deleted"
    else:
        return "User not deleted"

def setUserRestRating(user_id:string, rest_id:string, rating:string):
    conn = mysql.connector.connect(host="localhost", user="oonyemaobi1", password="#oonyemaobi1*", database="menumatchdb")
    cursor = conn.cursor()
    selectquery = "SELECT user_id, restaurant_id FROM serves WHERE user_id = " + user_id + " AND restaurant_id = " + rest_id

    num = cursor.execute(selectquery)
    records = cursor.fetchall()
    
    if cursor.rowcount > 0:
        updatequery = "UPDATE serves SET rating = %s WHERE user_id = %s AND restaurant_id = %s"
        values = (rating, user_id, rest_id)
        num = cursor.execute(updatequery, values)
        records = cursor.fetchall()
        num = cursor.rowcount
        conn.commit()
    else:
        createquery = "INSERT INTO serves (restaurant_id, user_id, rating) VALUES (%s, %s, %s)"
        values = (rest_id, user_id, rating)
        num = cursor.execute(createquery, values)
        records = cursor.fetchall()
        num = cursor.rowcount
        conn.commit()

    cursor.close()
    conn.close()

    if(num > 0):
        return "rating set"
    else:
        return "rating not set"
    #return "Account Created", records[0]

def updateRestaurantRating():
    conn = mysql.connector.connect(host="localhost", user="oonyemaobi1", password="#oonyemaobi1*", database="menumatchdb")
    cursor = conn.cursor()
    updatequery = "UPDATE restaurant r SET rating = (SELECT AVG (rating) FROM serves s WHERE s.restaurant_id = r.restaurant_id)"
    num = cursor.execute(updatequery)
    records = cursor.fetchall()
    num = cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()

    if(num > 0):
        return "rating updated"
    else:
        return "rating not updated"



