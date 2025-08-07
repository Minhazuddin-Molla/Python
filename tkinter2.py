# a=[]
# def lst(n,a,i):
#     if i<=n:
#         b,t=sum(i,[],n,0)
#         a.append(b)
#         if t:
#             return lst(n,a,i+1)
#         else:
#             return lst(n,a,i)
#     else:
#         return a
# def sum(c,a,n,s):
#     if s==n:
#         a.extend([s])
#         for i in range(2,c+1):
#             a=        
# # n=int(input("Enter any number:"))
# # print(lst(n,a,2))
# # import datetime as dt
# # import pickle as p
# # try:
# #     with open("Example.txt","w") as file:
# #         file.write(str(dt.datetime.now()))
# #         file.write()
# #     print("Work done!")
# # except IOError:
# #     print("Error found.")
def find_combinations(n, start, current_combination, result):
    if n == 0:
        result.append(current_combination)
        return result

    for i in range(start, n + 1):
        find_combinations(n - i, i, current_combination + [i], result)

    return result

num = int(input("Enter a number: "))

combinations = find_combinations(num,1,[],[])

print(combinations)