def get_file_stats(Lab1py, filename):
    with open(Lab1py, 'r') as file:
        data = file.read()
    return f"Word count: {len(data.split())}"
content = get_file_stats('Lab1py', 'input.txt')
with open("summary.txt", 'w') as file:
    file.write(content)