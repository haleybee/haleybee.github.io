#store your data
Words = ['color','color','colour','amok','amok','amuck','adviser','advisor','adviser','pepper']

canonical_spellings = ['color','amuck','adviser','pepper']

#make a dictionary?
pairings = {'colour': 'color', 'amok': 'amuck', 'advisor': 'adviser'}

#make an empty list
new_list = []
#compare the words in some way, i.e. stemming

#loop over the list of words
for word in Words:
    if word in pairings:
        #if a word is misspelled do something
        #correct the spelling using mappings dictionary
        corrected_word = pairings[word]
        #add that corrected_word
        new_list.append(corrected_word)
    else:
        #if a word is correct do something else
        new_list.append(word)

print(new_list)
