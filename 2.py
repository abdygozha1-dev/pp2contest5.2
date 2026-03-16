#1
import re
s = input()
if re.match(r"Hello", s):
    print("Yes")
else:
    print("No")

#2
import re
s = input()
sub = input()
if re.search(sub, s):
    print("Yes")
else:
    print("No")

#3
import re
s = input()
pattern = input()
matches = re.findall(pattern, s)
print(len(matches))

#4
import re
s = input()
digits = re.findall(r"\d", s)
print(" ".join(digits))

#5
import re
s = input()
if re.match(r'^[A-Za-z].*[0-9]$', s):
    print("Yes")
else:
    print("No")

#6
import re
s = input()
match = re.search(r'\S+@\S+\.\S+', s)
if match:
    print(match.group())
else:
    print("No email")

#7
import re
s = input()
pattern = input()
replacement = input()
result = re.sub(pattern, replacement, s)
print(result)

#8
import re
s = input()
pattern = input()
parts = re.split(pattern, s)
print(",".join(parts))

#9
import re
s = input()
words = re.findall(r'\b\w{3}\b', s)
print(len(words))

#10
import re
s = input()
if re.search(r'cat|dog', s):
    print("Yes")
else:
    print("No")

#11
import re
s = input()
uppercase_letters = re.findall(r'[A-Z]', s)
print(len(uppercase_letters))

#12
import re
s = input()
matches = re.findall(r'\d{2,}', s)
print(" ".join(matches))

#13
import re
s = input()
words = re.findall(r'\w+', s)
print(len(words))

#14
import re
s = input()
pattern = re.compile(r'^\d+$')
if pattern.fullmatch(s):
    print("Match")
else:
    print("No match")

#15
import re
s = input()
def double_digit(match):
    return match.group() * 2
result = re.sub(r'\d', double_digit, s)
print(result)

#16
import re
s = input()
match = re.match(r'Name: (.+), Age: (.+)', s)
if match:
    name = match.group(1)
    age = match.group(2)
    print(name, age)
    
#17
import re
s = input()
dates = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', s)
print(len(dates))

#18
import re
s = input()
pattern = input()
escaped_pattern = re.escape(pattern)
matches = re.findall(escaped_pattern, s)
print(len(matches))

#19
import re
s = input()
pattern = re.compile(r'\b\w+\b')
words = pattern.findall(s)
print(len(words))
