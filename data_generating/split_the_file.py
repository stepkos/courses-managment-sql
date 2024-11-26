# get a file and split it into 20 files

import os

# with open("output_v2_20x.txt") as f:
#     # split it into 20 files
#     lines = f.readlines()
#     num_lines = len(lines)
#     num_lines_per_file = num_lines // 20
#     for i in range(20):
#         print("Saving file", i)
#         with open(f"v2_parts/output_v2_20x_{i}.sql", "w") as f:
#             f.writelines(lines[i * num_lines_per_file : (i + 1) * num_lines_per_file])

with open("v2_parts/output_v2_20x_8_fixed.sql") as f:
    inserts = []
    insert_number = 1
    for line in f:
        if line.startswith("INSERT"):
            if len(inserts) == 400:
                with open(f"v2_parts/output_v2_20x_8_fixed_{insert_number}.sql", "w") as f:
                    insert_number += 1
                    f.writelines(inserts)
                    inserts = []
            inserts.append(line)
        else:
            inserts[-1] += line
        

        

