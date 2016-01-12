# encrypts each char using a corresponding char in the key and its position in the string
def enc(s,k) :
    fs = "";
    ka = 0;
    for i in range(0,len(s)) :
        fs += chr(int(ord(s[i])-10+(ord(k[ka])-35+(i%20-len(s)%20))))
        ka+=1;
        ka%=len(k);
    return fs;
def dec(s,k) :
    fs = "";
    ka = 0;
    for i in range(0,len(s)) :
        fs += chr(int(ord(s[i])+10-(ord(k[ka])-35+(i%20-len(s)%20))))
        ka+=1;
        ka%=len(k);
    return fs;
if __name__ == "__main__" :
    st = "<pyth0n>"
    key = "this is the best key in the world, you'll never guess it :D 4&#*%:J"
    pw = enc(st,key)
    print 'This is the password (encrypted): ', pw
    n = raw_input('Enter Password: ')
    if enc(n, key) == pw:
        print 'Correct'
    else:
        print 'Incorrect'

print 'test'
print 'on new line?'
