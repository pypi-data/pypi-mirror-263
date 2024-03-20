import json

from .exceptions import *

from flask import request
from functools import wraps

__all__ = ["DefaultRateLimitHandler"]

class DefaultRateLimitHandler:
    def __init__(self, db) -> None:
        """
        Represents a IP Rate Limit Handler. It helps prevent spam requests and blocks them according to their IPs.
        If an IP passes the specified request limit per specified `time duration`, the IP is blocked for the specified `block duration`.
        If the IP gets blocked more than the specified `block limit`, it is blacklisted. Most of the work is done by the specified `DB` handler.

        ## Parameters
            `db`: `DBHandler`
                The database to use.

        ## Returns
            `None`

        ## More features to add (Importance ↓)
            Async functions
                Implement async functions to prevent blocking the main thread.

            Improved logging
                As of now, only INFO logs are made.

            Window status
                Indicating whether a request window is `active` or `inactive`. Should be useful if `max_window_duration == 'FOREVER'` so that infrequent users are not unnecessarily rate-limited.
        
            Adaptive blocking
                Increase the window/block duration by multiplying, exponential backoff, adding a specified value, etc. based on the severity level.

            Cache layer
                Implement a feature to add cache layers (Memory, Redis, etc.) to prevent unnecessary reads to the DB which might be time-consuming.

            Database connections
                Implement a feature to add backup databases and automatically handle DB fail-overs.

            Request targeting
                Rate-limit / Block specific requests if suspected to be a bot or from a specific geo-location or from a suspected malicious IP.

            Grace Period
                A grace period for new or infrequent IPs slightly exceeding the rate-limit for the first time.
        """
        self.db = db

    def rate_limited_route(self):
        """
        It wraps a `Flask` route and rate-limits the IPs.

        ## Usage
            ```
            from HTTPE.server.rate_limit import RamHandler, RateLimitHandler

            rlhandler = RateLimitHandler(
                db=RamHandler(
                    amount=30,
                    time_window=timedelta(minutes=1),
                    block_limit=5,
                    block_exceed_duration='FOREVER' # block_exceed_duration can also be specified as any `timedelta` object.
                ) 
            )

            # Initialization of the `Flask` app and other essentials.

            @app.route("/rate-limited")
            @rate_limited_route()
            def rate_limited():
                ...                
        """
        def wrapper(func):
            @wraps(func)
            def inner(*args, **kwargs):
                ip = request.remote_addr

                if self.db.rdc and (self.db.rdc() is True):
                    self.db.log_info(f"Bypassed IP rate-limit check for IP - '{ip}'.")
                    return func(**args, **kwargs)
                
                try:
                    self.db.update_ip(ip)
                except (IPRateLimitExceeded, IPBlackListed) as e:
                    return json.dumps({"error": str(e)}), 429
                except Exception as e:
                    if self.db.logger:
                        self.db.logger.error(f"Unexpected internal error.", exc_info=e)
 
                return func(*args, **kwargs)
            
            return inner
        return wrapper

