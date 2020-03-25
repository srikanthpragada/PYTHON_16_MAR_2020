# Word Frequency

st = "How    do    you do is    how do you do today"

words = st.lower().split(" ")

freq = {}
for w in words:
    w = w.strip()
    if len(w) == 0:
        continue

    if w in freq:
        freq[w] += 1  # Increment count
    else:
        freq[w] = 1   # Insert new element

for w, c in sorted(freq.items()):
    print(f"{w:10} {c}")
