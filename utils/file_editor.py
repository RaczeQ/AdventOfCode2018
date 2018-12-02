def read_input(file_name):
    with open(file_name, 'r') as f: 
        lines = [l.strip() for l in f.readlines()]
        return lines

def save_result(file_name, result):
    with open(file_name, 'w') as f: 
        f.write(str(result))