
import hashlib

def convertmd5(text):
    message = hashlib.md5()
    message.update(text)
    return message.hexdigest()


def main():
    userinput = raw_input()
    print convertmd5(userinput)


    
main()
