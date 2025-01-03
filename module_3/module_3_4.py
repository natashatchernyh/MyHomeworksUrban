
def single_root_words(root_word, *other_words):
    same_words = []
    root_word_upper = root_word.upper()

    for w in other_words:
        w_upper = w.upper()
        if w_upper in root_word_upper or root_word_upper in w_upper:
            same_words.append(w)

    return(same_words)

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)

# Вывод на консоль:
# ['richiest', 'orichalcum', 'richies']
# ['Able', 'Disable']
