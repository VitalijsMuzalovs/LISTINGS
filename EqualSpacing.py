"""
This module calculates grooving width,distance between groovings and length of side's grooving (leftovers).
Conditions: 
- 2 panels with different length with mirrored (symmetric from panel center) groovings on them.
- panel's ends up with equal groovings (within tolerance 'side_tolerance')

"""
from typing import Type
import numpy as np

hill_min=2
hill_max=30
hill_step=0.1
groove_min=6
groove_max=25
groove_step=0.1
panel_1=1280
panel_2=1180

side_tolerance=1

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

for i in np.arange(groove_min,groove_max,groove_step):
    for k in np.arange(hill_min,hill_max,hill_step):

        side_1=sides(panel_1,i,k)
        side_2=sides(panel_2,i,k)

        if not(side_1 is None) and not(side_2 is None) and abs(side_1-side_2)<=side_tolerance and side_1>i/2:
            print(f'Канавка: {round(i)}  Между канавок: {round(k,2)} Остается по краям: {round(side_1,2)}/{round(side_2,2)} Кол-во: {leftover(panel_1,i,k)}')

