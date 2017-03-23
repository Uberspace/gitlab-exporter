from BaseHTTPServer import BaseHTTPRequestHandler
from StringIO import StringIO
import json

SECRET='iamsosecretplscheckme'

class GitlabWebhookHandler(BaseHTTPRequestHandler):

    def _authorize(self):
        token = self.headers.get('X-Gitlab-Token', '')
        return self._check_token(token)

    def _check_token(self, token=''):
        if token == SECRET:
            self.send_response(200)
            return True
        else:
            self.send_error(401, 'Unauthorized: secret token invalid')
            return False

    def do_POST(self):
        if not self._authorize():
            return
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        output = StringIO()
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_json = json.loads(post_body)
        return output
