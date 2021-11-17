import hashlib
puzzle = 'iwrupvqb'
targets = ['00000','000000']
for target in targets:
    do_another = True
    c=0
    while do_another:
        c=c+1
        inp = puzzle+str(c)
        hsh = hashlib.md5(inp.encode('utf-8')).hexdigest()[:len(target)]
        if hsh == target:
            print('Hash   : '+hsh)
            do_another = False
    print('Answer : ' +str(c))