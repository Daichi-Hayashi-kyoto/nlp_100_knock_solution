sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
word_list = list(map(str, sentence.split()))
#print(word_list)

word_list = [word_list[i][:-1] if ("." in word_list[i]) or ("," in word_list[i]) else word_list[i] for i in range(len(word_list))]
#print(word_list)
word_count_list = [len(word_list[i]) for i in range(len(word_list))]
print(word_count_list)