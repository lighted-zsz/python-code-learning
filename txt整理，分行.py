i = 74
with open(r'./马过江河/第8章8.争先.txt','r',encoding='utf-8') as p:
     b=p.read()
     # print(b)
     # print(b[:8]+'\n'+b[8:i])
     # print(b[8:i])

line_word=b[:8]+'\n'+b[8:i]
for i in range(74,len(b),66):
    line_word=line_word+'\n'+b[i:i+66]
with open(r'./马过江河/第8章8.争先.txt','w',encoding='utf-8') as bp:
    bp.truncate(0)
    bp.write(line_word)
    print('文本处理成功')