"""
Observe the process with the array given below and the tracking of the sums of each corresponding array.

[5, 3, 6, 10, 5, 2, 2, 1] (34) ----> [5, 3, 6, 10, 2, 1] ----> (27) ------> [10, 6, 5, 3, 2, 1]  ----> [4, 1, 2, 1, 1] (9) -----> [4, 1, 2] (7)
The tracked sums are : [34, 27, 9, 7]. We do not register one of the sums. It is not difficult to see why.

We need the function track_sum ( or trackSum ) that receives an array ( or list ) and outputs a tuple ( or array ) with the following results in the order given below:

array with the tracked sums obtained in the process
final array
So for our example given above, the result will be:

track_sum([5, 3, 6, 10, 5, 2, 2, 1]) == [[34, 27, 9, 7], [4, 1, 2]]
"""

def track_sum(arr):
    sum_arr=[]
    arr_2 = list(dict.fromkeys(arr))
    sum_1 = sum(arr)
    sum_arr.append(sum_1)
    sum_arr.append(sum(arr_2))

    arr_3 = sorted(arr_2,reverse=True)


    arr_4=[]
    for i in arr_3:
        if arr_3.index(i) != len(arr_3)-1: arr_4.append(i-arr_3[arr_3.index(i)+1])
    sum_arr.append(sum(arr_4))
    

    final_arr = list(dict.fromkeys(arr_4))
    final_arr_sum = sum(final_arr)
    sum_arr.append(final_arr_sum)

    print(arr,sum(arr),"->",arr_2,sum(arr_2),"->",arr_3,"->",arr_4,sum(arr_4),"->",final_arr,sum(final_arr))
    return [sum_arr,final_arr]

print(track_sum([5, 3, 6, 10, 5, 2, 2, 1]))

# def dotest(arr, expected):
#     test.assert_equals(track_sum(arr[:]), expected, f"Test failed with arr = {arr}")
    
# @test.describe("Tests")
# def test_group():
#     @test.it("Sample tests")
#     def test_case():
#         for arr, expected in [
#             ([5, 3, 6, 10, 5, 2, 2, 1], [[34, 27, 9, 7], [4, 1, 2]]),
#             ([-3, -5, 8, -11, 22, 16, -11, 22, -8, 8], [[38, 19, 33, 30], [6, 8, 11, 2, 3]]),
#             ([2, 3, 4, 1, 3, 2, -5, 4, 2, 3, 1, -5], [[15, 5, 9, 7], [1, 6]]),
#             ([4, 4, 4, 4, 4, 4, 4, 1],[[29, 5, 3, 3], [3]])
#             ]:
#             dotest(arr, expected)
