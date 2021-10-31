from sys import stdin

def removeConsecutiveDuplicates(string) :
    chars=[]
    prev=None
    for c in string:
        if prev!=c:
            chars.append(c)
            prev=c
    return "".join(chars)

        
	# Your code goes here



























	


#main
string = stdin.readline().strip()

ans = removeConsecutiveDuplicates(string)

print(ans)
