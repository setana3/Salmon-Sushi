import sys

def xor (argv):
        
    charList = argv
    XOR_base = int(input("The value for Base : "))
    string_box = []

    i = 0

    while i < len(charList):
            
        ans = bin(charList[i] ^ XOR_base)[2::] # XOR base is 9
        bin_ans = int(ans,2)

        print("bit-wise operation XOR >>> %s(%d) ^ %s(9)" % (bin(charList[i])[2::],charList[i], bin(XOR_base)[2::]))
        print("result = %s(%d) = %s" % (ans,bin_ans, chr(bin_ans)))
        string_box.append(chr(bin_ans))
        print("string: %s" % ''.join(string_box))

        i+= 1


args = sys.argv[1::]
args = [int(i) for i in args]

xor(args)