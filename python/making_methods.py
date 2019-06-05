# def recipe_list(ingredient):
#     print("Remember to buy " + ingredient)
#
# def when_dinner(day):
#     print('for ' + day)
#
# def weekly_menu(ingredient, day):
#     recipe_list(ingredient), when_dinner(day)
#
# ingredients = ['chicken', 'celery', 'onion', 'rice']
# days = ['mon', 'tues', 'wed', 'thurs']
#
# for ingredient in ingredients:
#     for day in days:
#         weekly_menu(ingredient, day)

#initially tried to print out a double indexed list of 1st ingredient + 1st day, etc. but using methods on lists didn't organize by index place. Using a dicitonary helped resolve that issue.

recipes = {'chicken': 'mon', 'celery': 'tues', 'onion': 'wed', 'rice': 'thurs'}

for ingredient, day in recipes.items():
        print('remember to buy ' + ingredient + ' for ' + day)
