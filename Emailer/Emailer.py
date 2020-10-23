from .core import send_email

class Emailer:
    '''Class used to simplify the process of sending emails programmatically using Python

    Parameters
    ----------
    from_address : str
        The email address to be sending emails from
    password : str
        The password to the from_address
    smtp_address : str (default 'smtp.gmail.com')
        The url of the smtp server to be connected to
    port : int (default 465)
        The port to connect to the smtp server through
    '''
    def __init__(
            self,
            from_address,
            password,
            smtp_address = 'smtp.gmail.com',
            port = 465
    ):
        self.from_address = from_address
        self.password = password
        self.smtp_address = smtp_address
        self.port = port

    @property
    def from_address(self):
        return self._from_address
    @from_address.setter
    def from_address(self, value):
        if not isinstance(value, str):
            raise TypeError('from_address must be a string')
        self._from_address = value

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError('password must be string')
        self._password = value

    @property
    def smtp_address(self):
        return self._smtp_address
    @smtp_address.setter
    def smtp_address(self, value):
        if not isinstance(value, str):
            raise TypeError('smtp_address must be a string')
        self._smtp_address = value

    @property
    def port(self):
        return self._port
    @port.setter
    def port(self, value):
        if not isinstance(value, int):
            raise TypeError('port must be integer-valued')
        self._port = value

    def send_email(
            self,
            to_addresses,
            subject,
            message,
            attachment_file = None,
            verbose = False
    ):
        '''Send an email

        Parameters
        ----------
        to_addresses : str or list of str
            The email addresses to send mail to
        subject : str
            The subject of the email
        message : str
            The message to include in the email
        attachment_file : pathlib.Path object, str, list of previous, or None (default None)
            If present, the path to a file to attach to the email
        verbose : bool (default False)
            If True, prints out to the console after the message was sent
        '''
        return send_email(
            self.from_address,
            self.password,
            to_addresses,
            subject,
            message,
            attachment_file,
            self.smtp_address,
            self.port,
            verbose
        )
