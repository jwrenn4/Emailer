import smtplib
import os
import ssl
import pathlib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(from_address, password, to_addresses, subject, body, attachment_file = None, smtp_address = 'smtp.gmail.com', port = 465, verbose = False):

    '''Send an email to a set of addresses, with the option of adding an attachment

    Parameters
    ----------
    from_address : str
        The email address to send from
    password : str
        The password to the email address to send from
    to_addresses : str or list of strings
        Email addresses to send the mail to
    subject : str
        The subject of the email
    body : str
        The text body of the message
    attachment_file : pathlib.Path object, str, list of previous, or None (default None)
        The path to the attachment, if desired
    smtp_address : str (default smtp.gmail.com)
        The url to identify the smtp server to use.  By default, assumes gmail
    port : int (default 465)
        The port to connect the smtp server to.  Default settings will work with gmail servers
    verbose : bool (default False)
        If True, will print out a message to console when the email is sent
    '''

    #instantiate the message and the sending address
    message = MIMEMultipart()
    message['From'] = from_address


    #take care of instances where the to receiving addresses are given in a list or a string
    if isinstance(to_addresses, list):
        message['To'] = ', '.join(to_addresses)
    else:
        message['To'] = to_addresses

    #set the message subject
    message['Subject'] = subject

    #attach the body of the email as plain text
    message.attach(MIMEText(body, 'plain'))
    #create the attachment if present
    if attachment_file:
        if isinstance(attachment_file, (pathlib.Path, str)):
            with open(attachment_file, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
            encoders.encode_base64(part)
            try:
                part.add_header('Content-Disposition', f'attachment; filename= {attachment_file.name}')
            except:
                part.add_header('Content-Disposition', f'attachment; filename= {os.path.basename(attachment_file)}')
            message.attach(part)
        elif isinstance(attachment_file, list):
            for f in attachment_file:
                with open(f, 'rb') as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                encoders.encode_base64(part)
                try:
                    part.add_header('Content-Disposition', f'attachment; filename= {f.name}')
                except:
                    part.add_header('Content-Disposition', f'attachment; filename= {os.path.basename(f)}')
                message.attach(part)
        else:
            raise ValueError('attachment_file must be pathlib.Path, str, or None')

    #stringify the message
    text = message.as_string()

    #create the default SSL context, connect to the server, and send the message
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_address, port, context = context) as server:
        server.login(from_address, password)
        server.sendmail(from_address, to_addresses, text)

    #if verbose, print that it was sent.  Else return
    if verbose:
        print('Email Sent')
    return
