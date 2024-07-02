import time
import requests

class RateLimitManager:
    """
    Class to manage rate limits for API requests.
    """

    interval = 60  # 1-minute interval
    max_requests = 5  # Maximum number of requests per interval
    requests = 0
    last_check = time.time()

    @classmethod
    def check_rate_limit(cls):
        current_time = time.time()
        if current_time - cls.last_check > cls.interval:
            cls.requests = 0
            cls.last_check = current_time

    @classmethod
    def make_request(cls, url, method, headers=None, data=None, files=None):
        cls.check_rate_limit()
        if cls.requests >= cls.max_requests:
            wait_time = cls.interval - (time.time() - cls.last_check)
            print(f"Waiting {wait_time:.1f} seconds to avoid rate limit exceedance...")
            time.sleep(wait_time)
            cls.check_rate_limit()

        response = requests.request(method, url, headers=headers, data=data, files=files)
        cls.requests += 1
        return response
