import os
import time
import multiprocessing
from PIL import Image, ImageFilter
os.chdir("C:")


# def converter(filename, size=(750, 750), catalog = "New_Image"):
#     img = Image.open(filename)
#     img = img.filter(ImageFilter.GaussianBlur())
#     img.thumbnail(size)
#     img.save(f"{catalog}/{os.path.basename(filename)}")
#     print(f"{filename} size changed")

# if __name__=="__main__":
#     Images = ["Picture/1.png"]

#     process = []
#     for x in Images:
#         process.append(multiprocessing.Process(target = converter, args=[x]))
#     for x in process:
#         x.start()
#     for x in process:
#         x.join()




# def bubbleSort(ls = []):
#     ls = list()
#     for i in range(10000):
#         ls.append(r(1, 10000))
#     for i in range(len(ls)):
#         check = False
#         for j in range(len(ls) - i - 1):
#             if ls[j] > ls[j+1]:
#                 ls[j], ls[j+1] = ls[j+1], ls[j]
#                 check = True

#         if check == False:
#             break
#     return ls

# def selectionSort(ls = []):
#     ls = list()
#     for i in range(10000):
#         ls.append(r(1, 10000))
#     for i in range(len(ls)):
#         minI = i
#         for j in range(i+1, len(ls)):
#             if ls[minI] < ls[j]:
#                 minI = j
#         if minI != i:
#             ls[minI], ls[i] = ls[i], ls[minI]
#     return ls

# if __name__ == "__main__":
#     file = open("th.txt", "at")
#     file.write("Bubble Sort\n")
#     for x in range(5):
#         # pro1 = multiprocessing.Process(target = bubbleSort)
#         # pro2 = multiprocessing.Process(target = selectionSort)
#         start = time.perf_counter()
#         bubbleSort()
#         finish = time.perf_counter()
#         print(f"{x+1} marta ishladi")
#         file.write(f"{x+1}. Ketgan vaqt: {finish-start:.3f}\n")

#     file.write("Selection Sort\n")
#     for x in range(5):
#         start = time.perf_counter()
#         selectionSort()
#         finish = time.perf_counter()
#         print(f"{x+1} marta ishladi")
#         file.write(f"{x+1}. Ketgan vaqt: {finish-start:.3f}\n")
#         # pro1.start()
#         # pro2.start()
#         # pro1.join()
#         # pro2.join()
#     file.close()



