from socketserver import TCPServer, ThreadingMixIn


class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass
