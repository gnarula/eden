from gluon import current

from s3.s3utils import S3CustomController

THEME = 'setup'

class index(S3CustomController):
    """ Custom Index for Remote Deployment """

    def __call__(self):

        response = current.response
        output = {}

        self._view(THEME, 'index.html')

        return output
