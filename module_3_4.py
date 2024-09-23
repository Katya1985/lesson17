def single_root_words(root_word, *other_words):
    same_words = []

    other_words = []
    return root_word.lower() in other_words.lower() or other_words.lower() in root_word.lower()

    # for word in  other_words:
    #     if root_word in word:
    #     same_words.append(word)
    #     return same_words
    # for word in other_words:
    #     print(word.lower())
    #     if root_word.lower() in other_words.lower() or other_words.lower() in root_word.lower():
    same_words.append(root_word)
    same_words.append(other_words)
    return same_words.append(other_words)



result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
