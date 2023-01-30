#!/usr/bin/env python3
"""
ReleaseHound script entrypoint
"""

from release_hound import config

if __name__ == "__main__":
    log = config.setup_logging()
