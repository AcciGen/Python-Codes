#1
# lst = [(10,20,30),(40,50,60),(70,80,90)]

# for i in range(len(lst)):

#     t = list(lst[i])
#     t[-1] = 100
#     t = tuple(t)
#     lst[i] = t

# print(lst)


#2
# lst = [(),(),('',),(),('a','b'),('a','b','c'),('d')]
# t = ()
# l = []

# for i in range(len(lst)):

#     if lst[i] != t:
#         l.append(lst[i])

# print(l)


#3
# lst = [('item1',12.20),('item2',15.10),('item3',24.5)]
# nw_lst = []
# xv = []

# for i in range(len(lst)):

#     t = list(lst[i])
#     nw_lst.append(t)

# nw_lst.sort(reverse = True)

# for i in range(len(lst)):

#     t = nw_lst[i]
#     xv.append(tuple(t))

# print(xv)


#4
# tpl = (('333','33'),('1416','55'))
# nw = []
# tpl_1 = ()

# for i in range(len(tpl)):

#     t = list(tpl[i])
#     nw.append(t)

# for i in range(len(nw)):
#     for j in range(len(nw[i])):

#         nw[i][j]=int(nw[i][j])

#     nw[i] = tuple(nw[i])

# tpl_1 = tuple(nw)
# print(tpl_1)


#Birja
# n = int(input())
# lst = list(map(int, input().strip().split()))[:n]
# Max=-1

# for i in range (len(lst)):
#     for j in range (i, len(lst)):

#         if lst[j] - lst[i] > Max:
#             Max = lst[j] - lst[i]
# print(Max)


#5
# def gsd(num):
#     sum=0
#     while num != 0:
#         sum += num%10
#         num /= 10
#     return sum

# lts=[23,2,9,34,8,9,10,74]

# for i in range(len(lts)-1):
#     for j in range(i+1,len(lts)):

#         if(gsd(lts[i])>gsd(lts[j])):
#             temp=lts[i]
#             lts[i]=lts[j]
#             lts[j]=temp

# print(lts)


#6
# ls=['100','102.1','101.1']

# for i in range(len(ls)):
#     ls[i]=float(ls[i])

# print(max(ls))


#7
# text = "W3resourse Python, Exercises."
# text2 = ""

# for i in text:
#     if i != ",":
#         text2 += i

# txt1 = text2.split(" ")
# txt2 = []

# for i in range(len(text)):

#     if text[i-1] != "," and text[i] == " ":
#         txt2.append(text[i])

#     if text[i] == "," and text[i+1]==" ":
#         txt2.append(text[i]+text[i+1])

# lst = []
# lst.append(txt1)
# lst.append(txt2)  
# print(lst)
