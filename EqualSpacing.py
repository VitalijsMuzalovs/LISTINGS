import numpy as np

hill_min=2
hill_max=30
hill_step=0.1
groove_min=6
groove_max=20
groove_step=0.1
panel_1=1280
panel_2=1180



def sides(whole_len,hill,groove):
    count = int((whole_len-hill)/(hill+groove)*2+1)
    if count%2!=0:
        odd_count=count
        check_sim = (odd_count-5)%4
        if check_sim==0:
            sides_leftover = whole_len-(odd_count-1)/2*(hill+groove)-hill
            sides=(sides_leftover)/2
            # print(f'Groove: {round(groove,2)} \t Hill: {round(hill,2)} \t Sides:{round(sides,2)} \t {whole_len}')
            return sides



# def sides(panel_len,step):
#     count = int(panel_len//step)
#     if count%2!=0:
#         odd_count=count
#         check_sim = (odd_count-5)%4
#         if check_sim==0:
#             sides_leftover = step*odd_count
#             sides=(panel_len-sides_leftover)/2
#             print(f'Groove_width: {round(step,2)} \t Sides:{round(sides,2)} \t {panel_len}')
#             return sides

for i in np.arange(groove_min,groove_max,groove_step):
    for k in np.arange(hill_min,hill_max,hill_step):

        side_1=sides(panel_1,i,k)
        side_2=sides(panel_2,i,k)
        # print(f'Step:{round(i,2)}: {side_1} and {side_2}')
        if not(side_1 is None) and not(side_2 is None) and abs(side_1-side_2)<=0.5 and side_1>i/2:
            print(f'##### Groove width {round(i)}  hill width {round(k,2)} fits!##### Side is {round(side_1,2)}/{round(side_2,2)}')
