
def is_unique(string):
    string_set = set()
    for s in string:
        if s not in string_set and s != " ":
            string_set.add(s)
            print(f"adding \"{s}\" to set")
        elif s in string_set:
            print(f"\"{s}\" is already in the set")
            return False
    return True


string = "this is a string"
print(is_unique(string))