from clients import postgres_client

with postgres_client() as conn:
    # load data ../output.txt lazily line by line
    with open("output20x.txt") as f:
        lines = []
        i = 0
        while line := f.readline():
            i += 1
            if line.startswith("INSERT"):
                print()
                conn.execute("".join(lines))
                lines = [line]
            else:
                lines.append(line)
        if lines:
            conn.execute("".join(lines))
        conn.commit()
        

     
            

