start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
# 1
# from math import sqrt
# for num in range(start+1, end + 1):
#     if num > 1:
#         for i in range(2, int(sqrt(num)+1)):
#             if num % i == 0:
#                 break
#         else:
#             print(num)
# 2
for num in range(start+1, end):
    if num > 1 and all(num % i != 0 for i in range(2, num)):
        print(num)
        