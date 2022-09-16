def find_missing_letter(chars):
    for count, i in enumerate(chars):
        if ord(chars[count+1]) - ord(i) > 1:
            print(chr(ord(i) + 1))
            break

find_missing_letter('abdef')
