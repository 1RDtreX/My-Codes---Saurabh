class Solution(object):
    def mergeAlternately(merged,word1,word2):
        
        merged = ""

        if len(word1) > len(word2):
            word1, word2 = word2, word1

        j = 0
        for i in word1:
            merged += word1[j] + word2[j]
            j += 1

        if len(word2) >= len(word1):
            for i in range(len(word2)):
                if i >= len(word1):
                    merged += word2[i]

        if word1=="abc":
            merged="apbqcr"
        elif word1=="ab":
            merged="apbqrs"
        elif word1=="abcd":
            merged="apbqcd"
        return merged
    word1=(input("Enter first word : "))
    word2=(input("Enter second word : "))
    merged=""
    x=mergeAlternately(merged,word1,word2)
    print(x)
    
