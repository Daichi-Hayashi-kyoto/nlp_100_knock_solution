def cipher(text):
    """
    require: text is English language. 
    """
    word_list = list(map(str, text.split()))
    word_list = [word_list[i][:-1] if ("." in word_list[i]) or ("," in word_list[i]) else word_list[i] for i in range(len(word_list))] # 単語リスト
    

