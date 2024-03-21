"""Get nice logging easily everywhere."""
import logging
import sys


def get_logger(log_stream=sys.stdout, log_file=None, log_level=logging.INFO, extra_handlers: list = None):
    """Set up nice logging, with the option of extra handlers."""
    if extra_handlers is None:
        extra_handlers = []

    handler_list = [logging.StreamHandler(log_stream)]
    handler_list.extend(extra_handlers)

    if log_file is not None:
        handler_list.append(logging.FileHandler(log_file))

    logging.basicConfig(
        level=log_level,
        format="%(asctime)s:%(msecs)03d [%(filename)s - %(levelname)s] \t\t %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=handler_list,
    )

    return logging.getLogger()
