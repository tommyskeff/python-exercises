NUMBER_ERROR = "That isn't a valid number!"
UNIT_ERROR = "That isn't a valid unit!"
UNITS = [
    ["b", "B", "kB", "MB", "GB", "TB", "KiB", "MiB", "GiB", "TiB"],
    [1, 8, 8000, 8000000, 8000000000, 8000000000000, 8192, 8388608, 8589934592, 8796093022208]
]

def get_unit(type):
    unit = ""
    valid = False
    while not valid:
        unit = input(f"What is the {type} unit? ({', '.join(UNITS[0])}) ")
        if unit in UNITS[0]:
            valid = True
        else:
            print(UNIT_ERROR)

    return unit;


def get_number(unit):
    number = ""
    valid = False
    while not valid:
        number = input(f"Enter {unit}: ")
        try:
            number = float(number)
            valid = True
        except:
            print(NUMBER_ERROR)
            
    return number

def get_bytes(unit):
    return UNITS[1][UNITS[0].index(unit)]

input_unit = get_unit("input");
input_number = get_number(input_unit)
output_unit = get_unit("output")
output_number = input_number / get_bytes(output_unit) * get_bytes(input_unit)

print(f"{input_number} {input_unit} = {output_number} {output_unit}")
