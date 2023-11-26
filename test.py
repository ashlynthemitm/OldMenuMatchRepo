import menu_match_crud_fun as mm
'''
all_menus = mm.getAllMenus()

print(all_menus)

all_rests = mm.getAllRestaurants()

for row in all_rests:
    print(row)

restaurants_one_mile = mm.filterRestaurantBasedOn("", "1", "", "")
for row in restaurants_one_mile:
    print(row)

menu_allergens = mm.filterMenusBasedOn("", ["Gluten", "Nuts"], "", "")
for row in menu_allergens:
    print(row)

bool, record = mm.getUserPassCombo("onyi@gmail.com", "onyi123")
print(bool)
print(record)

str, num = mm.createUser("Jim Ellis", "jim@gmail.com", "jim123", "Dairy")
print(str, num)

str = mm.updateUser("toni@gmail.com", "Dairy, Gluten, Nuts")
print(str)

str = mm.deleteUser("jim@gmail.com", "jim123")
print(str)
'''
str = mm.setUserRestRating("2", "146", "3.0")
print(str)


str = mm.updateRestaurantRating()
print(str)
