import functools
import time
import logging

from app.core.request_context import get_request_id

logger = logging.getLogger("book_svc")
logging.basicConfig(level=logging.INFO)

def log_execution(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()

        logger.info(f"[{get_request_id()}] START: {func.__name__}")
        logger.info(f"ARGS: {args[1:]}, KWARGS {kwargs}")

        try:
            result = func(*args,**kwargs)

            logger.info(f"[{get_request_id()}] SUCCESS: {func.__name__}")
            return result
        
        except Exception as e:
            logger.error(f"[{get_request_id()}] ERROR in {func.__name__}: {str(e)}")
            raise
        
        finally:
            end = time.time()
            logger.info(f"END: {func.__name__}: took {end - start:.4f}s")
        
    return wrapper