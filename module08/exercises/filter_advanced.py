numbers = [1, None, 2, None, 3, 0, False, 4, "", 5]

clean = list(filter(None, numbers))
print(clean)

only_ints = list(filter(lambda x: isinstance(x, int), numbers))
print(only_ints)

words = ["hello", "world", "python", "hi", "code"]

long_words_with_o = list(filter(lambda w: len(w) > 3 and "o" in w, words))
print(long_words_with_o)

emails = ["alice@mail.com", "not-an-email", "bob@mail.com", "broken@", "carol@mail.com"]

valid_emails = list(filter(lambda e: "@" in e and "." in e.split("@")[-1], emails))
print(valid_emails)
