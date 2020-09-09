# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 16:22:05 2020

@author: Lenovo
"""


#https://csacademy.com/contest/interview-archive/task/pokemon-evolution/statement/ -- Alexis Galvan Cardenas


def pokemon_evolution():
    pokemons = input().split()
    pokemons = [int(i) for i in pokemons]
    total = (pokemons[0] * pokemons[3]) + pokemons[1]
    if pokemons[2] > total:
        return 0
    elif pokemons[2] == total:
        return 1
    elif int(pokemons[1]/pokemons[2]) >= pokemons[0]:
        return pokemons[0]
    else:
        L = 1
        R = pokemons[0]
        
        ans = 0
        while L <= R:
            mid = int(L + (int(R-L)/2))
            left = pokemons[0] - mid
            temp = pokemons[1] + (pokemons[3]*left)
            if int(temp/pokemons[2]) == mid:
                return mid
            elif int(temp/pokemons[2]) > mid:
                if mid > ans:
                    ans = mid
                L = mid + 1
            else:
                if (int(temp/pokemons[2])) > left:
                    if left > ans:
                        ans = left
                R = mid - 1
        
        return ans
            
            
    
output = pokemon_evolution()
print(output)

    

