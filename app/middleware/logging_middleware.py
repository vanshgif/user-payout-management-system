import logging
import time

from fastapi import Request


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger("payout-system")


async def log_requests(request: Request, call_next):
    start_time = time.time()

    logger.info(
        f"Incoming Request -> {request.method} {request.url.path}"
    )

    response = await call_next(request)

    process_time = round((time.time() - start_time) * 1000, 2)

    logger.info(
        f"Completed -> {response.status_code} | "
        f"{request.method} {request.url.path} | "
        f"{process_time} ms"
    )

    return response