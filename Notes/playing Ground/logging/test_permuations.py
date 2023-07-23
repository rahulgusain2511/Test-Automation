def generate_permutations(input_list):
    if len(input_list) == 0:
        return []
    elif len(input_list) == 1:
        return [input_list]
    else:
        permutations = []
        for i in range(len(input_list)):
            m = input_list[i]
            rem_list = input_list[i+1:]
            for p in generate_permutations(rem_list):
                permutations.append([m] + p)
        return permutations

input_list = [1, 2, 3]
permutations = generate_permutations(input_list)
print(permutations)
