from itertools import combinations

S , K = input().upper().split()

k = int(K)

result = []
for i in range(1 ,k + 1):
    result.extend(combinations(sorted(S) , i))

for j in result:
    print(''.join(j)) # А теперь разбирай, почему это работает, а предыдущий вариант не работал


#     from itertools import combinations

# if __name__ == "__main__":
#     given_string = input()
#     given_number = int(given_string[-1:])
    
#     for i in range(given_number):
#         iterlist = (list(combinations(given_string[:-2], i+1)))
#         for j in range(len(iterlist)):
#             print(iterlist[j]) # предыдущий вариант


# i have yet to understand how iterators work, will do it properly during that week