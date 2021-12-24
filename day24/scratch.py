from alu import Alu

def read_rows(**kwargs):
    with open('data.txt', newline='') as csv_file:
        # return list(csv.reader(csv_file, **kwargs))
        # return csv_file.read().strip()
        return csv_file.read().splitlines()

rows = read_rows()

alu = Alu()
alu.parse(rows)

print(alu.z.expression)