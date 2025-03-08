input = input()
vowels = "aeiouAEIOU"

count = 0

for char in input:
    if char in vowels:
        count += 1
        
if count == 0:
    print("No vowels were found.")
else:
    print("Total number of vowels:", count)
