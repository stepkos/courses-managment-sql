with open("v2_parts/missing.sql") as f:
    inserts = []
    insert_number = 1
    for line in f:
        if line.startswith("INSERT"):
            if inserts:
                inserts[-1] = inserts[-1][:-2] 
                inserts[-1] += " ON CONFLICT DO NOTHING;\n"
            if len(inserts) == 400:
                with open(f"v2_parts/missing_{insert_number}.sql", "w") as f:
                    insert_number += 1
                    f.writelines(inserts)
                    inserts = []
            inserts.append(line)
        else:
            inserts[-1] += line
    if inserts:
        inserts[-1] = inserts[-1][:-2] 
        inserts[-1] += " ON CONFLICT DO NOTHING;\n"
        with open(f"v2_parts/missing_{insert_number}.sql", "w") as f:
            f.writelines(inserts)