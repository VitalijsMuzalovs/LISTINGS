import math

def load_numbers(filename):
    global num_list
    num_list=[]

    with open(r"E:\TEHNIKUMS\Python\26.04.2022-File\dati.txt","r") as fails:
        for line in fails:
            num=line.strip()
            num_list+=num
            #num_list.append(num)
    return (num_list)

def main():
    load_numbers(r"E:\TEHNIKUMS\Python\26.04.2022-File\dati.txt")
    print(num_list)
    print(num_list[-1])

main()