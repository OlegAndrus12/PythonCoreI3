# str.translate() + str.maketrans()
# translate() swaps/removes individual characters based on a mapping table

# --- basic swap ---
# maketrans(from_chars, to_chars) pairs each char at the same index
table = str.maketrans("aeiou", "AEIOU")
print("hello world".translate(table))   # hEllO wOrld

# --- ROT13 cipher ---
plain  = "abcdefghijklmnopqrstuvwxyz"
cipher = "nopqrstuvwxyzabcdefghijklm"
rot13 = str.maketrans(plain, cipher)
encoded = "hello".translate(rot13)
print(encoded)                           # uryyb
print(encoded.translate(rot13))          # hello  (decode = same table)

# --- remove characters (third arg maps char → None) ---
# maketrans("", "", chars_to_delete)
remove_punct = str.maketrans("", "", ".,!?;:")
dirty = "Hello, World! How are you?"
print(dirty.translate(remove_punct))     # Hello World How are you

# --- combine swap + delete in one table ---
table2 = str.maketrans("aeiou", "AEIOU", " ")
print("hello world".translate(table2))  # hEllOwOrld  (vowels uppercased, spaces removed)
