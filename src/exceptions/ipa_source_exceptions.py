class IPASourceException(Exception):
    """Base exception for IPA source exceptions"""

    message = "An unknown IPA source exception occurred"

    def __str__(self) -> str:
        return self.message


class LinkIsNotHTTPS(IPASourceException):
    message = "This link should start with https://"
    pass

class LinkIsNotFileNorHTTPS(IPASourceException):
    message = "This link should start with either https:// or file://"
    pass

class LinkIsNotIPA(IPASourceException):
    message = "This link should end with .ipa"
    pass
