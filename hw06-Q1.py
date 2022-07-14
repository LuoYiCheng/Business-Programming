# 將加密演算法定義為函數
def caesar_cipher(plain_text: str, key: int):
    '''凱薩加密
    param text: 欲加密文字(明文)
    param key: 字母偏移的數量
    ----------------------------
    return: 加密後文字(密文)
    '''
    punctuation = ' .-():,;?!\'"'
    digits = '1234567890'
    cipher_text = list(range(len(plain_text)))
    for i, character in enumerate(plain_text):
        if (character not in punctuation) and (character not in digits):
            # ASCII code
            ordinal_chr = ord(character) + key
            # 如果該字元為大寫
            if character.isupper() == True:
                if ordinal_chr <= 90:
                    cipher_text[i] = chr(ordinal_chr)
                else:
                    while ordinal_chr > 90:
                        ordinal_chr -= 26
                    cipher_text[i] = chr(ordinal_chr)
            # 如果該字元為小寫
            else:
                if ordinal_chr <= 122:
                    cipher_text[i] = chr(ordinal_chr)
                else:
                    while ordinal_chr > 122:
                        ordinal_chr -= 26
                    cipher_text[i] = chr(ordinal_chr)
        else:
            cipher_text[i] = character
    cipher_text = ''.join(cipher_text)
    return cipher_text

# Import variable
key = int(input())
plain_text = input()

# Apply the function
cipher_text = caesar_cipher(plain_text, key)

# Print out
print(cipher_text)