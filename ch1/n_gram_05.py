def n_gram(text, n):
    n = int(n)
    word_list = list(map(str, text.split())) 
    word_list = [word_list[i][:-1] if ("." in word_list[i]) or ("," in word_list[i]) else word_list[i] for i in range(len(word_list))] # 単語リスト
    moji_list = "".join(word_list)

    n_gram = []
    for i in range(len(word_list) - n + 1):
        add_word_list = word_list[i:i+n]
        n_gram.append(add_word_list)

    #print(len(moji_list))
    moji_gram = [moji_list[i:i+n] for i in range(len(moji_list) - n + 1)]

    print(n_gram)
    print(moji_gram)



import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('function_name',
                        type=str,
                        help='set fuction name in this file')
    parser.add_argument('-i', '--func_args',
                        nargs='*',
                        help='args in function',
                        default=[])
    args = parser.parse_args()

    # このファイル内の関数を取得
    func_dict = {k: v for k, v in locals().items() if callable(v)}
    # 引数のうち，数値として解釈できる要素はfloatにcastする
    func_args = [float(x) if x.isnumeric() else x for x in args.func_args]
    # 関数実行
    ret = func_dict[args.function_name](*func_args)