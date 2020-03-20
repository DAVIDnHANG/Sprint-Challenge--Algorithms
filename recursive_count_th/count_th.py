'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    lengthOfWord = len(word)
    lengthOfSubString = len('th')
    # base case is when i am looking at an empty string
    if(lengthOfWord==0 or lengthOfWord<lengthOfSubString):
        return 0;
    #now start putting the word together. as we put the word together if we find word by lengthofSubstring-1 = "str2",
    #we +1 every time we find matching word to keep counter
    if(word[0:lengthOfSubString] == "th"):
        return count_th(word[lengthOfSubString-1:])+1;
    #otherword recursively put the word together.
    return count_th(word[lengthOfSubString-1:])

