key=13*"k"
encrypted="|\x15:GKj-?}?s(p>l-$:\x08>.w<ETwHf|\x15\x113?Ot^"
flaglen=len(encrypted)-15
flag=flaglen*"a"
message=flag + "|" + key
key=list(key)
message=list(message)
for i in range(13):
    x=(ord(encrypted[flaglen+1])-ord(message[flaglen])-ord(encrypted[flaglen]))%128
    first=(chr(x))
    key[flaglen%13]=first
    message[22+flaglen%13]=key[flaglen%13]
    flaglen=22+(flaglen)%13
key="".join(key)
for i in range(22):
    x=(ord(encrypted[i+1])-ord(key[i%13])-ord(encrypted[i]))%128
    first=(chr(x))
    message[i]=first
message="".join(message)
print(message)
print(message[0:21])


