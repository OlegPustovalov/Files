#Функция преобразования строки инградиента в словарь
def get_shop_list_by_dishes(dishes, person_count):
    cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }
    dict_={}
    list_2 = []
    for name_dishes in dishes:
        for name,list_ingrad in cook_book.items():   
            if name == name_dishes: 
                list_2 = list_2 + list_ingrad         
    for dict_ in list_2:
        dict_['quantity'] = dict_['quantity'] * person_count 
    return list_2

list_zakaz = get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2)  
print (list_zakaz)
