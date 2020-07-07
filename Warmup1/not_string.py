def not_string(str):
    if len(str)>=3 and str[:3]:
        return str
    else:
        return "not " + str

print(not_string("candy"))
print(not_string("bad"))
print(not_string("not bad"))
