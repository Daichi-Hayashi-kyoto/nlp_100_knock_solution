sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
word_list = list(map(str, sentence.split()))
word_list = [word_list[i][:-1] if (word_list[i] in ".") or (word_list[i] in ",") else word_list[i] for i in range(len(word_list))] # 単語リスト

num_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
summary = {}
for i in range(1, len(word_list) + 1):
    if i in num_list:
        summary[word_list[i - 1][0]] = i
    else:
        summary[word_list[i - 1][:2]] = i

print(summary)