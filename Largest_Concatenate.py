# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:28:37 2020

@author: Lenovo
"""

###regresar el numero maximo convinando strings, '1','231','3' = 32311

def largest_concat_number(numbers):
    if len(numbers) == 1:
        return numbers[0]
    output = []
    if int(numbers[0] + numbers[1]) >= int(numbers[1] + numbers[0]):
        output.append(numbers[0])
        output.append(numbers[1])
        numbers.pop(0)
        numbers.pop(0)
    else:
        output.append(numbers[1])
        output.append(numbers[0])
        numbers.pop(0)
        numbers.pop(0)
        
    for i in range(len(numbers)):
        j = 0
        while True:
            if int(numbers[i] + output[j]) >= int(output[j] + numbers[i]):
                output.insert(j, numbers[i])
                break
            else:
                j += 1
            
            if j == len(output):
                output.append(numbers[i])
                break

    output = ''.join([str(i) for i in output])
    if int(output) == 0:
        return 0
    return output
          


###
n = int(input())
numbers = []
for i in range(n):
    numbers.append(input())
answer = largest_concat_number(numbers)
print(answer)


