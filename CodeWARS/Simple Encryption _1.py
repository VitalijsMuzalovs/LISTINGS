"""
Implement a pseudo-encryption algorithm which given a string S and an integer N 
concatenates all the odd-indexed characters of S with all the even-indexed characters of S,
this process should be repeated N times.

Examples:

encrypt("012345", 1)  =>  "135024"
encrypt("012345", 2)  =>  "135024"  ->  "304152"
encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

encrypt("01234", 1)  =>  "13024"
encrypt("01234", 2)  =>  "13024"  ->  "32104"
encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
Together with the encryption function, you should also implement a decryption function which reverses the process.

If the string S is an empty value or the integer N is not positive, return the first argument without changes.
"""

def decrypt(encrypted_text, n):
    if encrypted_text is None or n<1: return encrypted_text
    lst = []
    for i in range(n):
        myStr= decr(encrypted_text)
        lst.append(myStr)
        encrypted_text = myStr
    # return print(' -> '.join(lst))
    return print(encrypted_text)


def encrypt(text, n):
    if text is None or n<1: return text
    lst = []
    for i in range(n):
        myStr= enc(text)
        lst.append(myStr)
        text = myStr
    # return print(' -> '.join(lst))
    return print(text)

def enc(text):
    even = ''.join(x for x in text[1:len(text):2])
    odd = ''.join(x for x in text[0:len(text):2])
    output =  ''.join([even,odd])
    return output 

def decr(text):
    even = ''.join((x for x in text[0:len(text)//2]))
    odd = ''.join((x for x in text[len(text)//2:]))
    if len(text)%2 != 0: 
        even = ' ' + even
        rez =  list(zip(odd,even))
        rez.reverse()
    else:
        rez =  list(zip(even,odd))
    output=''
    for i in rez:
        output += ''.join(i)
    return output

# encrypt("This is a test!", 1)
# decrypt("hskt svr neetn!Ti aai eyitrsig", 1)
decrypt("This is a test!", 4)

