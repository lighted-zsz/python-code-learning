import os
if os.path.exists('./到无心'):
    a=os.listdir('./到无心/')
    # print(a)
    for i_f in a:
        i = 74
        with open(r'./到无心/'+i_f, 'r', encoding='utf-8') as p:
            b = p.read()
            # print(b)
            # print(b[:8]+'\n'+b[8:i])
            # print(b[8:i])

        line_word = b[:8] + '\n' + b[8:i]
        for i in range(74, len(b), 66):
            line_word = line_word + '\n' + b[i:i + 66]
        with open(r'./到无心/'+i_f, 'w', encoding='utf-8') as bp:
            bp.truncate(0)
            bp.write(line_word)
            print(i_f+'文本处理成功')
