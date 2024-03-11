original_list = [item for item in input().split()]
result_list = []
for i in range(len(original_list)):
    if len(original_list[i]) <= 3:
        result_list.append(original_list[i])
print(result_list)
