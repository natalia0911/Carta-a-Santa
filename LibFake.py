#Creado por Natalia Vargas
#Version 3.7.2
from faker import Faker
import random

fake = Faker()
todosPerfiles=[]

for i in range(10):
    perfiles=fake.simple_profile()
    for i in perfiles:
        if i =='name':
            perfil=perfiles[i].split(' ')
            perfil[1]+=' '+fake.last_name()
            todosPerfiles.append(perfil)
           
        if i =='sex':
            perfil.append(perfiles[i])
            perfil.append(random.randint(0,12))
            
print(todosPerfiles)

