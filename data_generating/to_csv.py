
def line_to_csv(line):
    if line.startswith("INSERT"):
        return line.split()[3]
    else:
        return line

with open ("output20x.txt") as f:
    lines = []
    table = None
    while line := f.readline():
        if line.startswith("INSERT"):
            if table is None:
                table = line.split()[2]
            elif table != line.split()[2]:
                with open(f"output20x_{table}.csv", "a") as f:
                    f.write("".join(lines))
                lines = [line]
                table = line.split()[2]
            else:
                lines.append(line)
        else:
            lines.append(line)