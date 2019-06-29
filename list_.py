def change_to_list(s):
    while(1):
        if '\n' in s:
            i = s.index('\n')
            s = s[:i] + s[i+1:]
        else:
            break
    l = s.split(" ")
    c = l.count('')
    for i in range(c):
        l.remove('')

    l[0] = l[0][1:]
    if ']' in l:
        l = l[:len(l)-1]
    else:
        l[len(l)-1] = l[len(l)-1][:len(l[len(l)-1]) -1]
    l = list(map(float, l))
    return(l)

        
