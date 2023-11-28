
import string
from typing import Dict, List, Tuple
import mysql.connector

from flask import Flask, request
 
app = Flask(__name__) 

#make a function that calls all the other functions based on the JSON object sent from script
#in the js function add a variable that holds the method name you want to call, when you get to app.py
#in the main function you create, use if statements to choose which method to call
#send the json object to each function and use data.get('insert_var_name', default value)
#once you do final return it will go to success if you get a response or error if you have no response.
#so I would do repsonse.records to get the values.

@app.route('call-python-functions')
def callFunctions():
    data = request.json
    if(data.get('function', "") == 'get-all-menus'):
        return getAllMenus()
    elif(data.get('function', "") == 'get-all-restaurants'):
        return getAllRestaurants()
    



@app.route('/get-all-menus') 
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
    return {'records' : records}

@app.route('/get-all-restaurants') 
def getAllRestaurants():
    conn = mysql.connector.connect(host="localhost", user="oonyemaobi1", password="#oonyemaobi1*", database="menumatchdb")
    cursor = conn.cursor()
    selectquery = "SELECT * FROM restaurant"

    cursor.execute(selectquery)
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return {'records': records}
  

@app.route('/filter-restaurants') 
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
    return {'records': records}

#filterRestaurantBasedOn("", "", "Foood", "")
  
@app.route('/filter-menus') 
def filterMenusBasedOn(menu_item:string, allergies:List, wait:string, type:string): #takes a list of allergens
    conn = mysql.connector.connect(host="localhost", user="oonyemaobi1", password="#oonyemaobi1*", database="menumatchdb")
    cursor = conn.cursor()
    filterquery = "SELECT m.menu_item FROM menu m INNER JOIN restaurant r ON m.restaurant_id = r.restaurant_id WHERE"
    if(menu_item != ""):
        filterquery = filterquery + " m.menu_item = " + menu_item
    else:
        if(len(allergies) > 0):
            algs = "" #'\''
            i = 0
            while(i < len(allergies)):
                temp = " m.allergens NOT LIKE \'%" + allergies[i] + "%\'"
                algs = algs + temp
                i+=1
                if(i < len(allergies)):
                    algs = algs + " AND"
            #algs = algs[0:-1] + '\''
            print(algs)
            #" m.allergens NOT LIKE " +
            filterquery = filterquery + algs
        if(wait != ""):
            if(len(allergies) > 0):
                filterquery = filterquery + " AND"
            filterquery = filterquery + " m.cook_time < " + wait 
        if(type != ""):
            if(len(allergies) > 0 or wait != ""):
                filterquery = filterquery + " AND"
            filterquery = filterquery + " m.food_type = " + type

        print(filterquery)

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
    response = {'records' : records}
    return 

@app.route('/get-user-pass') 
def getUserPassCombo(email:string, passw:string):
    conn = mysql.connector.connect(host="localhost", user="oonyemaobi1", password="#oonyemaobi1*", database="menumatchdb")
    cursor = conn.cursor()
    selectquery = "SELECT name, email, password, allergens FROM user WHERE email = \'" + email +"\' AND password = \'" + passw + "\'"
    print(selectquery)
    cursor.execute(selectquery)
    
    records = cursor.fetchall()

    if cursor.rowcount > 0:
        cursor.close()
        conn.close()
        return {'success' : True, 'records' : records[0]}
    
    else:
        cursor.close()
        conn.close()
        return {'success' : False, 'records' : []}
            
    #return records

@app.route('/check-user-created')
def checkUserCreated(email:string):
    conn = mysql.connector.connect(host="localhost", user="oonyemaobi1", password="#oonyemaobi1*", database="menumatchdb")
    cursor = conn.cursor()
    selectquery = "SELECT * FROM user WHERE email = \'" + email + "\'"

    cursor.execute(selectquery)
    records = cursor.fetchall()
    num = cursor.rowcount
    
    if num > 0:
        cursor.close()
        conn.close()
        print("This email already has an account")
        return {'success' : True, 'records' :records}
    return {'success' : False, 'records' : ""}
    
@app.route('/create-user')
def createUser(name:string, email:string, passw:string, allergens:string):
    conn = mysql.connector.connect(host="localhost", user="oonyemaobi1", password="#oonyemaobi1*", database="menumatchdb")
    cursor = conn.cursor()
    tempBool, record = checkUserCreated(email)
    if(tempBool):
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
        return {'success' : True, 'records' : records}
    else:
        return {'success' : False, 'records' : []}
    
@app.route('/update-user')
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

    tempBool, record = checkUserCreated(email)
    #print(tempBool, record)

    if(num > 0):
        return {'success' : True, 'records': record}
    else:
        return {'success' : False, 'records': ""}

@app.route('/delete-user')
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
        return {'success' : True}
    else:
        return {'success' : False}

@app.route('/set-user-rest-rating')
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
        return {'success' : True}
    else:
        return {'success' : False}
    #return "Account Created", records[0]

@app.route('/update-restaurant-rating')
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
        return {'success' : True}
    else:
        return {'success' : False}



