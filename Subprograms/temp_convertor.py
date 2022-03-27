def convert_temp(temp, char="f"):
    if (char.lower() == "f"):
        return (temp - 32) * 5 / 9
    elif (char.lower() == "c"):
        return temp * 9 / 5 + 32
    else:
        raise ValueError("Conversion must be C or F")


print(f"212F to C: {convert_temp(212, 'F')}")
print(f"100C to F: {convert_temp(100, 'C')}")
print(f"212 ambiguous: {convert_temp(212)}")
print(f"212 to invalid value: {convert_temp(100, 'invalid value')}")
