def hanoi(n, f, to, via):
    if n == 1:
        print("move disk 1 from",f, "to",to)
    else:
        hanoi(n-1, f, via, to)
        print("move disk",n,"from",f,"to",to)
        hanoi(n-1, via, to, f)

n=3
f='a'
to='b'
via='c'
hanoi(n, f, via, to)

