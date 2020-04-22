def n_gram(text, n):
    n = int(n)
    word_list = list(map(str, text.split())) 
    word_list = [word_list[i][:-1] if ("." in word_list[i]) or ("," in word_list[i]) else word_list[i] for i in range(len(word_list))] # 単語リスト
    moji_list = "".join(word_list)

    #print(len(moji_list))
    moji_gram = [moji_list[i:i+n] for i in range(len(moji_list) - n + 1)]

    return moji_gram

X = n_gram("paraparaparadise", 2)
Y = n_gram("paragraph", 2)

union = X.copy() 
intersection = X.copy()   

for word in Y:
    if not word in X:
        union.append(word)
    else:
        intersection.append(word)  # 積集合

diff_set = [x_word for x_word in X if x_word in Y] 


union = set(union)
print("和集合は", set(union))
print("積集合は", set(intersection))
print("差集合は", set(diff_set))