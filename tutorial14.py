# str function
# non str to str

num = 42
str_num = str(num)
print(str_num)  # Output: "42"
print(type(str_num))

message = "HeLLo, WoRLD!"
print(message.lower())  # Output: "hello, world!"
print(message.upper())  # Output: "HELLO, WORLD!"


text = "   This is a sentence.   "
print(text.strip())  # Output: "This is a sentence."



sentence = "Hello, how are you?"
words = sentence.split()
print(words)  # Output: ['Hello,', 'how', 'are', 'you?']
