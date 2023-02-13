class CaptchaException(Exception):
    def __init__(self, content):
        self.content = content
