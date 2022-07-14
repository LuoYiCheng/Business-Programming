# Full-form Chinese punctuation marks
ff_ch_pm = '。，、；：「」『』（）？！《》〈〉～'

# Half-shaped English punctuation marks
hs_en_pm = '.-():,;?!\'\"/'


# 定義一個判定半形英文字的函數
def isenalpha(enalpha):
    '''A-Z,a-z'''
    if 65 <= ord(enalpha) <= 90 or 97 <= ord(enalpha) <= 122:
        answer = True
    else:
        answer = False
    return answer


# 定義一個判定中文字的函數
# 假設ASCII code > 10000，且不在全形清單就是中文字
def ischinese(char):
    '''羅'''
    if ord(char) > 19967 and char not in ff_ch_pm:
        answer = True
    else:
        answer = False
    return answer


# 定義一個「全形字元之間，不空格」的函數
def no_space_between_ff(sentence_list):
    '''移除全形字元間的空白鍵'''
    new_sentence = ''
    for i in range(len(sentence_list)):
        # 如果該字元為空白，直接跳過
        if sentence_list[i] == ' ':
            continue
        # 假設ASCII code > 10000，且不在全形清單就是中文字
        elif ischinese(sentence_list[i]) or sentence_list[i] in ff_ch_pm:
            # 檢查下一個字元是否為半形空白，直到找到不為空白的字元才停止
            next = 1
            try:
                while sentence_list[i + next] == ' ':
                    next += 1
                    if sentence_list[i + next] != ' ':
                        break
                # 如果下一個非空白位元為全形字元
                if ord(sentence_list[i + next]) > 10000 or\
                        sentence_list[i + next] in ff_ch_pm:
                    new_sentence += sentence_list[i]
                else:
                    new_sentence += sentence_list[i]
                    new_sentence += ' ' * (next - 1)
            except IndexError:  # 最後一個字元
                new_sentence += sentence_list[i]
        else:  # 全形字元以外
            next = 1
            try:
                while sentence_list[i + next] == ' ':
                    next += 1
                    if sentence_list[i + next] != ' ':
                        break
                new_sentence += sentence_list[i]
                new_sentence += ' ' * (next - 1)
            except IndexError:
                new_sentence += sentence_list[i]
                new_sentence += ' ' * (next - 1)
    return new_sentence


# 定義一個「全形標點符號與半形字元之間，不空格」的函數
def no_space_between_alnum_ff(sentence_list):
    new_sentence = ''
    for i in range(len(sentence_list)):
        if sentence_list[i] == ' ':
            continue
        elif sentence_list[i] in ff_ch_pm:
            next = 1
            try:
                while sentence_list[i + next] == ' ':
                    next += 1
                    if sentence_list[i + next] != ' ':
                        break
                if sentence_list[i + next].isdigit() or \
                        isenalpha(sentence_list[i + next])\
                        or sentence_list[i + next] in hs_en_pm:
                    new_sentence += sentence_list[i]
                else:
                    new_sentence += sentence_list[i]
                    new_sentence += ' ' * (next - 1)
            except IndexError:
                new_sentence += sentence_list[i]
        elif sentence_list[i].isdigit() or isenalpha(sentence_list[i])\
                or sentence_list[i] in hs_en_pm:
            next = 1
            try:
                while sentence_list[i + next] == ' ':
                    next += 1
                    if sentence_list[i + next] != ' ':
                        break
                if sentence_list[i + next] in ff_ch_pm:
                    new_sentence += sentence_list[i]
                else:
                    new_sentence += sentence_list[i]
                    new_sentence += ' ' * (next - 1)
            except IndexError:
                new_sentence += sentence_list[i]
        else:
            new_sentence += sentence_list[i]
    return new_sentence


# 定義一個「全形中文字與半形字元之間，要一個空格」的函數
def one_space_between_ff_alnum(sentence_list):
    '''全形中文字與半形字元之間，要一個空格'''
    new_sentence = ''
    for i in range(len(sentence_list)):
        # 如果該字元為空白，直接跳過
        if sentence_list[i] == ' ':
            continue
        # 為了滿足中文後面與半形字元要隔一個space
        elif ischinese(sentence_list[i]):
            # 檢查下一個字元是否為半形空白，直到找到不為空白的字元才停止
            next = 1
            try:
                while sentence_list[i + next] == ' ':
                    next += 1
                    if sentence_list[i + next] != ' ':
                        break
                # 如果下一個非空白位元為半形字元
                if isenalpha(sentence_list[i + next]) or\
                        sentence_list[i + next].isdigit() or\
                        sentence_list[i + next] in hs_en_pm:
                    new_sentence += sentence_list[i]
                    new_sentence += ' '
                else:
                    new_sentence += sentence_list[i]
            except IndexError:  # 表示該字為最後一個
                new_sentence += sentence_list[i]
        # 為了滿足半形字元後面與中文字要隔一個space
        elif isenalpha(sentence_list[i]) or\
            sentence_list[i].isdigit() or\
                sentence_list[i] in hs_en_pm:
            # 檢查下一個字元是否為半形空白，直到找到不為空白的字元才停止
            next = 1
            try:
                while sentence_list[i + next] == ' ':
                    next += 1
                    if sentence_list[i + next] != ' ':
                        break
                # 如果下一個非空白位元為中文字
                if ischinese(sentence[i + next]):
                    new_sentence += sentence_list[i]
                    new_sentence += ' '
                # 如果下一位是半形字元，保持不變
                elif isenalpha(sentence_list[i + next]) or \
                        sentence_list[i + next].isdigit() or \
                        sentence_list[i + next] in hs_en_pm:
                    new_sentence += sentence_list[i]
                    new_sentence += ' ' * (next - 1)
                else:
                    new_sentence += sentence_list[i]
                    # new_sentence += ' ' * (next - 1)
            except IndexError:  # 表示該字為最後一個
                new_sentence += sentence_list[i]
        else:
            new_sentence += sentence_list[i]
    return new_sentence


# 讀入變數
n_row = int(input())
text_list = [input() for _ in range(n_row)]

# 處理文件檔案
new_text_list = []
for i, sentence in enumerate(text_list):
    # Step1:全形字元之間，不空格
    sentence = no_space_between_ff(sentence)
    # Step2:全形標點符號與半形字元之間，不空格。
    sentence = no_space_between_alnum_ff(sentence)
    # Step3:全形中文字與半形字元之間，要一個空格
    sentence = one_space_between_ff_alnum(sentence)
    # 最後一行的最後沒有換行字元
    if i != n_row-1:
        print(sentence)
    else:
        print(sentence, end='')
