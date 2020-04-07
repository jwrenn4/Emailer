# Emailer

This Python package abstracts away much of the intracacies of sending emails programmatically.  There is a single object in this package, the Emailer object.

## Setting Up

First, it is assumed that the user has git and Python installed (preferrably Python 3.6 or higher), along with pip to install Python packages.  Once those are installed, run the following commands to install this package (assuming Linux-like environment).

```bash
cd desired-directory
git clone https://github.com/jwrenn4/Emailer.git
cd Emailer
pip install .
```

Successful completion of those commands will install this package into your current Python virtual environment.  To check that intallation is completed, you can run the following command in Python:

```python
from Emailer import Emailer
```

If no error occurs, congratulations.  You've successfully installed this package.

## Usage

It is hoped that the Emailer object is quick and easy to use.  Simply start by instantiating the object with the parameters for your email address, then send an email with the `send_email` method.  Note that the Emailer object is preconfigured for Gmail addresses; to send using a different server, you will have to find the SMTP address and port number for that address and use them in the initialization of your object.

Quick example of usage:

```python
from Emailer import Emailer

emailer = Emailer("my.email@gmail.com", "my_password")
subject = "Test"
message = "This is a test."
to_addresses = ["example1@gmail.com", "example2@other_site.com"]
emailer.send_email(
    to_addresses,
    subject,
    message
)
```

## NOTE: Enable less-secure apps

With gmail, you may need to enable less-secure apps on your email address to actually send an email.