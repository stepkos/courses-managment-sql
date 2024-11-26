with open("v2_parts/output_v2_20x_9.sql") as f:
    inserts = []
    insert_number = 1
    new_inserts = []
    for line in f:
        new_line = line[:-2] + " ON CONFLICT DO NOTHING;\n"
        new_inserts.append(new_line)
    
    with open(f"v2_parts/output_v2_20x_9_conflicts.sql", "w") as f:
        f.writelines(new_inserts)