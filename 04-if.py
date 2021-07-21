
text = 'gweukfhwukfhi2fbookref'
KEY = 'book'


# 1.1
b = KEY in text

# 1.2
b = text.count(KEY) > 0

# 1.3
b = not text.find(KEY) == -1


# 2.1
d = (len(KEY) >= 6 and len(KEY) <= 16)

# 2.2
d = (6 <= len(KEY) <= 16)
