import time

class CircuitBreaker:
    def __init__(self, http_client, error_threshold, time_window):
        self.http_client = http_client
        self.error_threshold = error_threshold
        self.time_window = time_window
        self.error_count = []

    def do_request(self, url):
        time_window_cutoff = time.time() - self.time_window
        errors_in_window = [x for x in error_count if x > time_window_cutoff]
        self.error_count = errors_in_window
        if len(errors_in_window) > self.error_threshold:
            raise CircuitOpenError
        try:
            self.http_client.request(url)
        except:
            self.error_count.append(time.time())

if __name__ == "__main__":
    breaker = CircuitBreaker(stub_client, x, y)