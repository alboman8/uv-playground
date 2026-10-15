from joke_lib import tell_joke
from utils import get_logger

try:
    from joke_lib import tell_another_joke
except ImportError:
    tell_another_joke = None

try:
    from joke_lib import tell_yet_another_joke
except ImportError:
    tell_yet_another_joke = None

logger = get_logger(__name__)


def main() -> None:
    print(tell_joke())

    if tell_another_joke is not None:
        print(tell_another_joke())
    else:
        logger.error("tell_another_joke is not available, it only ships with the test/dev groups")

    if tell_yet_another_joke is not None:
        print(tell_yet_another_joke())
    else:
        logger.error("tell_yet_another_joke is not available, it only ships with the dev group")


if __name__ == "__main__":
    main()
