def read_text_file(filename):
    groups = []
    current_group = []

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                current_group.append(int(line))
                print(current_group)
            else:
                if current_group:
                    groups.append(current_group)
                #    print(groups)
                current_group = []

        if current_group:
            groups.append(current_group)
    print(groups)
    return groups  #--we put all of the data inside a group

# Example usage
filename = 'amount.txt'  # Replace with the actual filename
groups = read_text_file(filename)

# Calculate the sum for each group
group_sums = [sum(group) for group in groups]

# Find the group with the highest sum
if group_sums:
    max_sum_index = group_sums.index(max(group_sums))
    max_sum_group = groups[max_sum_index]

    print("Group with the highest sum:")
    print("Sum of Values:", max(group_sums))
    print("Group:", max_sum_group)
else:
    print("No groups found.")

