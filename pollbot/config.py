"""Config values for pollbot."""
import logging
import os
import sys

import toml

default_config = {
    "telegram": {
        "bot_name": "volley_and_more_poll@vollpm_bot",
        "api_key": "8470755344:AAFFhjWFHBozjGaOheeFpEcBwZEeSROxeYY",
        "worker_count": 20,
        "admin": "KukuruzG",
        "allow_private_vote": False,
        "max_user_votes_per_day": 200,
        "max_inline_shares": 20,
        "max_polls_per_user": 200,
    },
    "database": {
        "sql_uri": "postgresql://pollbot:fer38@localhost:5432/pollbot",
        "connection_count": 20,
        "overflow_count": 10,
    },
    "logging": {
        "sentry_enabled": False,
        "sentry_token": "",
        "log_level": logging.INFO,
        "debug": False,
    },
    "webhook": {
        "enabled": False,
        "domain": "https://localhost",
        "token": "pollbot",
        "cert_path": "/path/to/cert.pem",
        "port": 7000,
    },
}

config_path = os.path.expanduser("~/.config/volley-poll-bot.toml")

if not os.path.exists(config_path):
    with open(config_path, "w") as file_descriptor:
        toml.dump(default_config, file_descriptor)
    print("Please adjust the configuration file at '~/.config/volley-poll-bot.toml'")
    sys.exit(1)
else:
    config = toml.load(config_path)

    # Set default values for any missing keys in the loaded config
    for key, category in default_config.items():
        for option, value in category.items():
            if option not in config[key]:
                config[key][option] = value
