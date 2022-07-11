text = input('enter a word: ')



while text[0] != '0' :
    if text[0] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'  and text[1] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' and text[2] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' and text[3] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
        ic = text[0:4]
        print((ic), (text[4:]))
    elif text[0] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' and text[1] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' and text[2] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
        ic = text[0:3]
        print((ic), (text[3:]))
    elif text[0] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' and text[1] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
        ic = text[0:2]
        print((ic), text[2:])
    elif text[0] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
        ic = text[0]
        print(ic, text[1:])











    text = input('Type another word, type a zero to quit: ')
    

