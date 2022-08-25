import os.path


def populate_file(filename):
    values_to_write = ["line1", "line2", "line3", "line4"]
    with open(filename, "w") as out:
        for values_to_write in values_to_write:
            out.write(values_to_write)
            out.write("\n")

def read_file(filename):
    data = []
    with open(filename, "r") as in_file:
        for line in in_file:
            yield line

def read_if_exists(filename):
    if os.path.isfile(filename):
        yield from read_file(filename)
    return []


filename = "sample_file.txt"

populate_file(filename)

file_contents = read_if_exists(filename)

print(file_contents)

line = next(file_contents)
print(line)

another_line = next(file_contents)
print(another_line)
