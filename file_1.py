#Функция преобразования строки инградиента в словарь
def func_ingred (str_ingred):
    dict_={}
    str1 = ''
    m = 0
    for sumbol in str_ingred:      
        if sumbol == '|' and m == 0:
            dict_['ingredient_named'] = str1
            m = 1
            str1 = ''
        elif sumbol == '|' and m == 1:
            str2 = str1.replace(' ','')
            str3 = str2.replace('|','')
            dict_['quantity'] = str3
            m = 2
            str1 = ''
        str1 = str1 + sumbol
        if m == 2:
            str2 = str1.replace('\n','')
            str3 = str2.replace('| ','')
            dict_['measure'] =str3
    return dict_
cook_book = {}
list_file = []
with open('cook_book.txt','r') as document:
    list_file = document.readlines()
n = len (list_file)
i = 0
dic_2 = {}
while n > 0:
#название блюда и количество инградиентов
    str1 = list_file [i]
    name_dishes = str1.replace('\n','')
    q_ingred = int(list_file [i+1])
#обработка строк с инградиентами    
    j = i+2
    list_ = []
    while j < q_ingred+i+2:
        dic_2 = func_ingred (list_file[j])
        list_.append (dic_2)
        j = j + 1
#корректировка индексов
    n = n - q_ingred-2-1
    i = i+1+q_ingred+1+1
    cook_book [name_dishes] = list_
print (cook_book)
    
