def tConv(temp, char="f"):
    if (char.lower() == "f"):
        return (temp - 32) * 5 / 9
    elif (char.lower() == "c"):
        return temp * 9 / 5 + 32
    else:
        raise ValueError("Conversion must be C or F")


print(f"212F to C: {tConv(212, 'F')}")
print(f"100C to F: {tConv(100, 'C')}")
print(f"212 ambiguous: {tConv(212)}")
print(f"212 to invalid value: {tConv(100, 'invalid value')}")
