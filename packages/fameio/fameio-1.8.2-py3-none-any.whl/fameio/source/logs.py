# SPDX-FileCopyrightText: 2023 German Aerospace Center <fame@dlr.de>
#
# SPDX-License-Identifier: Apache-2.0

import logging as log
from pathlib import Path
from typing import NoReturn

LOG_LEVELS = {
    "critical": log.CRITICAL,
    "error": log.ERROR,
    "warn": log.WARNING,
    "warning": log.WARNING,
    "info": log.INFO,
    "debug": log.DEBUG,
}


def log_and_raise_critical(message: str) -> NoReturn:
    """Raises a critical error and logs with given `error_message`"""
    log.critical(message)
    raise Exception(message)


def log_error_and_raise(exception: Exception) -> NoReturn:
    """Raises the specified `exception` and logs an error with the same `message`"""
    log.error(str(exception))
    raise exception


def set_up_logger(level_name: str, file_name: Path) -> None:
    """Uses existing logger or sets up logger"""
    if not log.getLogger().hasHandlers():
        _set_up_new_logger(level_name, file_name)


def _set_up_new_logger(level_name: str, file_name: Path) -> None:
    """Sets up new logger which always writes to the console and if provided also to `file_name`"""
    level = LOG_LEVELS.get(level_name.lower())
    if level is log.DEBUG:
        formatter_string = (
            "%(asctime)s.%(msecs)03d — %(levelname)s — %(module)s:%(funcName)s:%(lineno)d — %(message)s"  # noqa
        )
    else:
        formatter_string = "%(asctime)s — %(levelname)s — %(message)s"  # noqa

    log_formatter = log.Formatter(formatter_string, "%H:%M:%S")

    root_logger = log.getLogger()
    root_logger.setLevel(level)

    if file_name:
        file_handler = log.FileHandler(file_name, mode="w")
        file_handler.setFormatter(log_formatter)
        root_logger.addHandler(file_handler)

    console_handler = log.StreamHandler()
    console_handler.setFormatter(log_formatter)
    root_logger.addHandler(console_handler)
