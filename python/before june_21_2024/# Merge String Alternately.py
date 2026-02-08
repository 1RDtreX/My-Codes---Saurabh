word1 = input("Enter 1st word : ").lower()
word2 = input("Enter 2nd word : ").lower()
merged = ""

if len(word1) > len(word2):
    word1, word2 = word2, word1

# main logic
j = 0
for i in word1:
    merged += word1[j] + word2[j]
    j += 1

if len(word2) >= len(word1):
    for i in range(len(word2)):
        if i >= len(word1):
            merged += word2[i]

print("final :", merged)
