#!/usr/bin/env python
import imaplib

class Pat(object):
    """Base connection class."""

    def __init__(self, options, *args, **kargs):
        self.options = options
        self.args = args
        self.kargs = kargs


    def connect(self):
        """Creat IMAP connection"""

        self.connection = imaplib.IMAP(self.kargs['host'], self.kargs['porrt'])


    def list_folders(self):
        """
        :return: list of folders
        """

    def list_email(self):
        """
        :return: list of emails
        """