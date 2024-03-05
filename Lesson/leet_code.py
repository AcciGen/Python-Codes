# Task-1470
# ls1=[]
# ls2=[]
# ls3=[]
# for i in range(n):
#     ls1.append(nums[i])
# for i in range(n,2*n):
#     ls2.append(nums[i])
# for i in range(n):
#     ls3.append(ls1[i])
#     ls3.append(ls2[i])
# return ls3

# ls = [1, 2]

# for i in ls:

#     if i != max(ls) and i != min(ls):
#         print(i)
#         exit(1)

# print(-1)

# def median(nums1, nums2):
#     nums1.extend(nums2)
#     if len(nums1) % 2 == 0:
#         return (sorted(nums1)[len(nums1) // 2] + sorted(nums1)[len(nums1) // 2 - 1]) / 2 

#     return sorted(nums1)[len(nums1)//2]

# lst = [1, 2]
# lst1 = [3, 4]
# pprint(median(lst, lst1))


a = 100
b = 5
res = 0
for i in range(1, a, 1):
    if b*i > a:
        res = res*10 + (i-1)
        break
print(res)