def group_by_owners(original_dict):

    final_dict = {}

    for key, value in original_dict.items():
        if value in final_dict:
            final_dict[value].append(key)
        else:
            final_dict[value] = [key]
    return final_dict


sorted_dict={}
original_dict = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
sorted_dict = group_by_owners(original_dict)
print(sorted_dict)
