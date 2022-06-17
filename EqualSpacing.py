"""
This module calculates grooving width,distance between groovings and length of side's grooving (leftovers).
Conditions: 
- 2 panels with different length with mirrored (symmetric from panel center) groovings on them.
- panel's ends up with equal groovings (within tolerance 'side_tolerance')

"""
from typing import Type
import numpy as np

def sides(whole_len,groove,hill):
    count = int((whole_len-hill)/(hill+groove)*2+1)
    if count%2!=0:
        odd_count=count
        check_sim = (odd_count-5)%4
        if check_sim==0:
            sides_leftover = whole_len-(odd_count-1)/2*(hill+groove)-hill
            sides=(sides_leftover)/2
            # print(f'Groove: {round(groove,2)} \t Hill: {round(hill,2)} \t Sides:{round(sides,2)} \t {whole_len}')
            return sides

def leftover(whole_len,groove,hill):
    odd_count = int((whole_len-hill)/(hill+groove)*2+1)
    sides_leftover = (whole_len-(odd_count-1)/2*(hill+groove)-hill)/2
    return odd_count

hill_min=2
hill_max=30
hill_step=0.1
groove_min=6
groove_max=25
groove_step=0.1
panel_1=340
panel_2=500

side_tolerance=2

print('-'*40)
print(f'Панели: {panel_1} ; {panel_2}')
print(f'Диапазон длины канавок: {groove_min} - {groove_max}')
print(f'Диапазон расстояний между канавок: {hill_min} - {hill_max}')
print(f'Допуск на длину крайних канавок: {side_tolerance}')
print('-'*80)
print(f'Канавка \t  Между канавок  \t  Крайние канавки  \t  Кол-во')
print('-'*80)


count = 0 
for i in np.arange(groove_min,groove_max,groove_step):
    for k in np.arange(hill_min,hill_max,hill_step):

        side_1=sides(panel_1,i,k)
        side_2=sides(panel_2,i,k)

        if not(side_1 is None) and not(side_2 is None) and abs(side_1-side_2)<=side_tolerance and (side_1>i/2 or side_2>i/2):
            print(f'{round(i,2)}  \t\t {round(k,2)} \t\t\t {round(side_1,2)} / {round(side_2,2)} \t\t {leftover(panel_1,i,k)}')
            count+=1

print(f'Всего: {count}')
