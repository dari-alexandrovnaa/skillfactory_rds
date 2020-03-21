import numpy as np
count = 0   
begin = 1
end = 100                         # счетчик попыток
number = np.random.randint(begin, end)    # загадали случайное число
predict = 0 # предполагаемое число
while begin < end:                        # бесконечный цикл
         
    count += 1    # плюсуем попытку
    predict = (begin + end) // 2
    if number == predict: 
      break    # выход из цикла, если угадали
    elif number > predict: 
      begin = predict
    elif number < predict:  
      end = predict
        
print (f"Вы угадали число {number} за {count} попыток.")