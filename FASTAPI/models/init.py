import logging

from .import init_db
from db.session import Session

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    db = Session()
    logger.info("Creating initial data")
    init_db(db)
    logger.info("Initial data created")


if __name__ == "__main__":
    init()
