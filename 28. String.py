str1 = input("Enter a string: ")

print("Lowercase:", str1.lower())

print("Uppercase:", str1.upper())

print("Total characters:", len(str1))

count = 0
for ch in str1.lower():
    if ch in "aeiou":
        count += 1

print("Total vowels:", count)