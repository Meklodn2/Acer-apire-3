# def faktorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * faktorial(n-1)  #recursive

# print(faktorial())

def total(q):
    if q == 1:
        return 1
    else:
        return q + total(q-1) #recursive
print(total(4))