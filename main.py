import os


from pprint import pprint
file_path = os.path.join(os.getcwd(), 'recipes.txt')
with open(file_path, 'rt', encoding='utf-8') as file:

    cook_book = []
    cook = []

    for line in file:
        cook_name = line.strip()
        ingredient_count = int(file.readline())
        ingredients = list()
        for _ in range(ingredient_count):
            ingr = {}
            ingr = file.readline().strip().split(' | ')
            ingredient_name, quantity, measure = ingr

            quantity = int(quantity)
            ingredients.append({'ingredient_name': ingredient_name,
                            'quantity': quantity,
                            'measure': measure})
        cook_book = {cook_name: ingredients}
        file.readline()
        cook.append(cook_book)
    pprint(cook)


    def get_shop_list_by_dishes(dishes, person_count):

        shop_list = {}
        for dish in dishes:
            for cooks in cook:
                if dish in cooks:
                    for meal in cooks[dish]:
                        shop_list_meal = dict()
                        if meal['ingredient_name'] not in shop_list:
                            shop_list_meal['measure'] = meal['measure']
                            shop_list_meal['quantity'] = meal['quantity'] * person_count
                            shop_list[meal['ingredient_name']] = shop_list_meal

                        else:
                            shop_list[meal['ingredient_name']]['quantity'] += meal['quantity'] * person_count

        else:
            print(f'\n"Блюда нет"\n')
        pprint(shop_list)
        return shop_list



    get_shop_list_by_dishes(['Утка по-пекински', 'Фахитос', 'jh'], 2)



list1 = []
list2 = []
list3 = []
res = []
file_path1 = os.path.join(os.getcwd(), '1.txt')
with open(file_path1, 'rt', encoding='utf-8') as f1:
    res1 = f1.readlines()
    list1.append(len(res1))
    list1.append(os.path.basename(r'C:\Users\shoro\1.txt'))
    list1.append(res1)
    res.append(list1)
file_path2 = os.path.join(os.getcwd(), '2.txt')
with open(file_path2, 'r', encoding='utf-8') as f2:
    res2 = f2.readlines()
    list2.append(len(res2))
    list2.append(os.path.basename(r'C:\Users\shoro\2.txt'))
    list2.append(res2)
    res.append(list2)
file_path3 = os.path.join(os.getcwd(), '3.txt')
with open(file_path3, 'r', encoding='utf-8') as f3:
    res3 = f3.readlines()
    list3.append(len(res3))
    list3.append(os.path.basename(r'C:\Users\shoro\1.txt'))
    list3.append(res3)
    res.append(list3)
    res.sort()

    file_path4 = os.path.join(os.getcwd(), 'append_file.txt')
    open(file_path4, 'w').close()
    for r in res:
        with open(file_path4, 'a+', encoding='utf-8') as f_app:
            f_app.writelines(str(r[0]))
            f_app.writelines('\n')
            f_app.writelines(str(r[1]))
            f_app.writelines('\n')
        for k in r[2]:

            with open(file_path4, 'a+', encoding='utf-8') as f_app:
                f_app.writelines(str(k))
                f_app.writelines('\n')


