symbol =0                                                                      #инициализация для переменной
string_1=str(input("Введите  первую строку для проверки на анограмму : "))     #ввод с калвиатуры первой строки 
string_replace=string_1.replace(" ","")                                        #убрать все пробелы
len_string_1=len(string_replace)                                               #длина первой строки 
string_2=str(input("Введите вторую строку для проверки на анограмму : "))      #ввод второй строки 

 #перебор символов и сравнение строк
for i in string_2:
 if i in string_replace:      
  symbol +=1
if symbol==len_string_1:

#вывод результата
  print("Ваша строка анограмма")   
else:
  print("Ваша строка не анограмма")
