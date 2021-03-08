def generate_diff(file1, file2):
    result = ''
    keys_file1 = file1.keys()
    keys_file2 = file2.keys()
    keys_file3 = list(set(keys_file1) | set(keys_file2))
    keys_file3.sort()
    for key in keys_file3:
        if key in keys_file1 and key in keys_file2:
            if file1[key] != file2[key]:
                result += f'  - {key}: {file1[key]}\n'
                result += f'  + {key}: {file2[key]}\n'
            else:
                result += f'    {key}: {file1[key]}\n'
        elif key not in keys_file2:
            result += f'  - {key}: {file1[key]}\n'
        else:
            result += f'  + {key}: {file2[key]}\n'
    template = f"{{\n{result}}}"
    return template
