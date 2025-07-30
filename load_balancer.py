from http.server import BaseHTTPRequestHandler, HTTPServer
import http.client
import itertools

# Backend server configuration
backends = [("localhost", 9001), ("localhost", 9002), ("localhost", 9003)]
backend_cycle = itertools.cycle(backends)  # Round-robin cycling

class LoadBalancerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        backend_host, backend_port = next(backend_cycle)
        print(f"Forwarding to {backend_host}:{backend_port}")

        try:
            conn = http.client.HTTPConnection(backend_host, backend_port)
            conn.request("GET", self.path)
            resp = conn.getresponse()

            self.send_response(resp.status)
            for header, value in resp.getheaders():
                self.send_header(header, value)
            self.end_headers()
            self.wfile.write(resp.read())
            conn.close()
        except Exception as e:
            self.send_error(502, f"Bad Gateway: {e}")

def run_load_balancer(port=9000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, LoadBalancerHandler)
    print(f"Load balancer running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_load_balancer()
