def read_ascii_file(filename):
    with open(filename, 'r', encoding='ascii') as file:
        for line in file:
            print(line.strip())

# Example usage
read_ascii_file('example.txt')