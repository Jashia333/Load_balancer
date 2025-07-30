import http.server
import socketserver
import sys
import os

def run_server(port, directory):
    os.chdir(directory)
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Serving at port {port} from {directory}")
        httpd.serve_forever()

if __name__ == "__main__":
    port = int(sys.argv[1])
    site_dir = sys.argv[2]
    run_server(port, site_dir)
