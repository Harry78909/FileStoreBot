__all__ = ["logging"]

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

#def LOGGER(name: str) -> logging.Logger:
   # return logging.getLogger(name)
