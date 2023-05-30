from pprint import pprint

with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for recipe in file:
        ingr_count = int(file.readline())
        ingr_list = []
        for i in range(ingr_count):
            ingr_name, quantity, measure = file.readline().strip().split(' | ')
            ingr_list.append({'ingredient_name': ingr_name, 'quantity': quantity, 'measure': measure})
        file.readline()
        cook_book[recipe.strip()] = ingr_list
# pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    ingredients = {}
    for dish in dishes:
        for in_name in cook_book[dish]:
            if ingredients.get(in_name['ingredient_name']):
                ingredients[in_name['ingredient_name']]['quantity'] += int(in_name['quantity']) * person_count
            else:
                ingredients[in_name['ingredient_name']] = {'measure': in_name['measure'],
                                                           'quantity': int(in_name['quantity']) * person_count}
    return ingredients


pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))

texts = ['1.txt', '2.txt', '3.txt']
text4 = []
for text in texts:
    with open(text, encoding='utf-8') as file:
        res = file.readlines()
        res.insert(0, text)
        text4.append(res)
text4.sort(key=len)

with open('4.txt', 'w', encoding='utf-8') as f4:
    for text in text4:
        f4.write(text[0])
        f4.write('\n')
        f4.write(str(len(text[1:])))
        f4.write('\n')
        f4.writelines(text[1:])
