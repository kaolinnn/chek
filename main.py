

import csv
import random

f = open('students.csv', 'r', encoding='UTF-8')
reader = csv.DictReader
slv ='01234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
slv1 = '0123456789'
slv2 = 'qwertyuiopasdfghjklzxcvbnm'
slv3 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
file = open('students_password.csv', 'w', encoding='UTF-8')
writer = csv.writer(file)
writer.writerow(['id','Name','titleProject_id','class','score','login','password'])
for line in reader:
    name_mas = line['Name'].split()
    password = random.choice(slv)+random.choice(slv1)+random.choice(slv)+random.choice(slv)+random.choice(slv)+random.choice(slv2)+random.choice(slv)+random.choice(slv3)
    writer.writerow([line['id'],line['Name'],line['titleProject_id'],line['class'],line['score'],line['login'],name_mas[0]+'_'+name_mas[1][0]+name_mas[2][0],password])