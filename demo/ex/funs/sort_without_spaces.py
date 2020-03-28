def remove_spaces(st):
    return st.replace(' ', '')


strs = ["Abc xy", "Acbde", "  Abc", "   Xy   "]

for s in sorted(strs, key=remove_spaces):
    print(s)

for s in map(remove_spaces, strs):
    print(s)
