

# in the file there are things like <bound method Provider.boolean of <faker.providers.misc.en_US.Provider object at 0x7f9030b9c800>>
# they should be randomly replaced with True or False


import random

with open("v2_parts/output_v2_20x_8.sql", "r") as f:
    with open("v2_parts/output_v2_20x_8_fixed.sql", "a") as f_fix:
        for line in f:
            f_fix.write(line.replace("<bound method Provider.boolean of <faker.providers.misc.en_US.Provider object at 0x7f9030b9c800>>", str(random.choice([True, False]))))
            # the number of object can be whatever
            f_fix.write(line.write)
