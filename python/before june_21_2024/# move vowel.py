# move vowel

class solution(object):
    word=(input("Enter the Sentence"))
    wordr=(reversed(word))
    l=len(word)
    for i in range(l-1):
        if word[i]=='a' or word[i]=='e' or word[i]=='i' or word[i]=='o' or word[i]=='u':
            print(word[i])