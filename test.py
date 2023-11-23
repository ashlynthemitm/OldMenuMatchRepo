
import string
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="oonyemaobi1", password="#oonyemaobi1*", database="menumatchdb")

def getAllMenus():
    cursor = conn.cursor()
    selectquery = "select * from menu where menu_id < 6"

    cursor.execute(selectquery)
    records = cursor.fetchall()

    print("No. of Menu Items", cursor.rowcount)

    for row in records:
        print("Menu ID:", row[0])
        print("Item:", row[1])
        print("Allergens:", row[2])
        print("Avg Wait Time:", row[3])
        print("Food Type:", row[4])
        print("Restaurant Name", row[5])
        print("\n")

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

    
def filterMenusBasedOn(menu_item:string, allergies:[], wait:string, type:string): #takes a list of allergens
    cursor = conn.cursor()
    filterquery = "select * from menu where"
    if(menu_item != ""):
        filterquery = filterquery + " menu_item = " + menu_item
    else:
        if(len(allergies) > 0):
            filterquery = filterquery + " allergens NOT IN " + allergies 
        if(wait != ""):
            if(len(allergies) > 0):
                filterquery = filterquery + " and"
            filterquery = filterquery + " cook_time < " + wait 
        if(type != ""):
            if(len(allergies) > 0 or wait != ""):
                filterquery = filterquery + " and"
            filterquery = filterquery + " food_type = " + type

    cursor.execute(filterquery)
    records = cursor.fetchall()

    
    print("No. of Menu Items", cursor.rowcount)

    for row in records:
        print("Menu ID:", row[0])
        print("Item:", row[1])
        print("Allergens:", row[2])
        print("Avg Wait Time:", row[3])
        print("Food Type:", row[4])
        print("Restaurant Name", row[5])
        print("\n")

    cursor.close()
    return records

def getUserPassCombo(email:string, passw:string):
    cursor = conn.cursor()
    selectquery = "select email, password from user where email = " + email +" and password = " + passw

    cursor.execute(selectquery)
    records = cursor.fetchall()
    if len(records) > 0:
        return True, records[0]
    
    else:
        return False, []
            
    #return records



conn.close()



