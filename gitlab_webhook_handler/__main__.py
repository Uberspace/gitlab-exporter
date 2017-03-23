from gitlab_webhook_handler import GitlabWebhookHandler
import SocketServer

PORT = 8000

Handler = GitlabWebhookHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
