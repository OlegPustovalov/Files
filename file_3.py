name1 = 'files_3_1.txt'
name2 = 'files_3_2.txt'
name3 = 'superfile.txt'
list_file1 = []
list_file2 = []
list_file3 = []
list_file_sum = []

with open(name1,'r') as document:
    list_file1 = document.readlines()
n1 = len (list_file1)
str_n1 = str (n1)
list_file_1 = ['\n' + name1 + '\n',str_n1 + '\n']
list_file_1 = list_file_1+list_file1

with open(name2,'r') as document:
    list_file2 = document.readlines()
n2 = len (list_file2)
str_n2 = str (n2)
list_file_2 = ['\n' + name2 + '\n',str_n2 + '\n']
list_file_2 = list_file_2+list_file2

with open(name3,'r') as document:
    list_file3 = document.readlines()
n3 = len (list_file3)
str_n3 = str (n3)
list_file_3 = ['\n' + name3 + '\n',str_n3 + '\n']
list_file_3 = list_file_3+list_file3

if n1 <= n2 and n2 <= n3:
    list_file_sum = list_file_1 + list_file_2 + list_file_3
elif n1 <= n3 and n3 <= n2:
    list_file_sum = list_file_1 + list_file_3 + list_file_2
elif n2 <= n1 and n1 <= n3:
    list_file_sum = list_file_2 + list_file_1 + list_file_3
elif n2 <= n3 and n3 <= n1:
    list_file_sum = list_file_2 + list_file_3 + list_file_2
elif n3 <= n1 and n1 <= n2:
    list_file_sum = list_file_3 + list_file_1 + list_file_2
elif n3 <= n2 and n2 <= n1:
    list_file_sum = list_file_3 + list_file_2 + list_file_1
str_f = ''
with open('file_sum.txt','w') as document:
    for str_f in list_file_sum:
        document.write(str_f)

