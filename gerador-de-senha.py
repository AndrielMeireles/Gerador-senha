import random #imprtação da biblioteca

#ites que serão usados para criar senha#
lower_case = "abcdefghijklmnopqrstuvwxyz"  #letras minúsculas
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  #lestras maiúscula
numbers = "0123456789"                     #números
symbols = "~!@#$%^&*+._:"                  #caracteres especiais

use_for = lower_case + upper_case + numbers + symbols

length_of_password = 20 #quantidade de caracteres 

password = "".join(random.sample(use_for, length_of_password)) #geração da senha

print("Sua senha gerada é", password) 
