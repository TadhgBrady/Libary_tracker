import time
import logging
import uuid
from fastapi import Request

from app.core.request_context import set_request_id, get_request_id

logger = logging.getLogger("book_svc")
logging.basicConfig(level=logging.INFO)


async def log_requests(request: Request, call_next):
    request_id = str(uuid.uuid4())[:8]
    start_time = time.time()

    logger.info(f"[{request_id}] REQUEST START: {request.method} {request.url.path}")

    try:
        response = await call_next(request)
        duration = time.time() - start_time

        logger.info(
            f"[{request_id}] REQUEST END: {request.method} {request.url.path} "
            f"STATUS: {response.status_code} "
            f"DURATION: {duration:.4f}s"
        )

        response.headers["X-Request-ID"] = request_id
        return response

    except Exception as e:
        duration = time.time() - start_time
        logger.error(
            f"[{request_id}] REQUEST ERROR: {request.method} {request.url.path} "
            f"DURATION: {duration:.4f}s ERROR: {str(e)}"
        )
        raise