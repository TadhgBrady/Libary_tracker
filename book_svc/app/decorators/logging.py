import functools
import time
import logging

logger = logging.getLogger("book_svc")
logging.basicConfig(level=logging.INFO)

def log_execution(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()

        logger.info(f"START: {func.__name__}")
        logger.info(f"ARGS: {args[1:]}, KWARGS {kwargs}")

        try:
            result = func(*args,**kwargs)

            logger.info(f"SUCCESS: {func.__name__}")
            return result
        
        except Exception as e:
            logger.error(f"ERROR in {func.__name__}: {str(e)}")
            raise
        
        finally:
            end = time.time()
            logger.info(f"END: {func.__name__}: took {end - start:.4f}s")
        
    return wrapper