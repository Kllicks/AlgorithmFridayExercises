# Our attempt:
# num_list = [9,7,8,1,3,6,5,2,4]
# for i in range(0, len(num_list)):
#    for i in range(0, len(num_list)):
#         a = i
#         b = i + 1
#         if num_list[a] < num_list[b]:
#             pass
#             # i+=1
#         elif num_list[b] < num_list[a]:
#             num_list[a], num_list[b] = num_list[b], num_list[a]
#             # i+=1
#         print(num_list)

# DIR solution:
# num_list = [9,7,8,1,3,6,5,2,4]
# def bubble_sort(num_list):
#     brakes = True
#     while(brakes):
#         brakes = False ##flutter the brakes
#         for i in range(len(num_list) - 1):
#             if num_list[i] > num_list[i + 1]:
#                 num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
#                 brakes = True
#     return num_list
# print(bubble_sort(num_list))

# Best solution I could find:
num_list = [9,7,8,1,3,6,5,2,4]

def bubbleSort(num_list):
    for listChange in range(len(num_list)-1,0,-1):
        for i in range(listChange):
            if num_list[i]>num_list[i+1]:
                temp = num_list[i]
                num_list[i] = num_list[i+1]
                num_list[i+1] = temp

bubbleSort(num_list)
print(num_list)