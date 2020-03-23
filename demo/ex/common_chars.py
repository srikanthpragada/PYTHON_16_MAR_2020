
st1 = "This is fine"
st2 = "That is also good"

common = []

for ch in st1:
    if ch in st2:
        if ch not in common:
           common.append(ch)
           print(ch)

