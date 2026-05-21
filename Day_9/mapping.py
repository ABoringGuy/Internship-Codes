"""For string:"""

def censored_word(word):
    list_of_censor=["fuck", "ass", "shit"]

    if word.lower() in list_of_censor:
        return "*" * len(word)
    return word

sentence="Why the fuck is this so complicated?"
word= sentence.split()

censored_sentence=map(censored_word,word)
result = " ".join(censored_sentence)

print(result)

"""For list:"""

def multiplier(x):
    return x*2

n_list=[1,2,3,4,5,6,7,8,9,10]

multiplied_list=map(multiplier, n_list)
print(list(multiplied_list))