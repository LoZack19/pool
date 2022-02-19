import json


def init_config(filename: str) -> dict:
    config = {}

    with open(filename, 'r', encoding='utf-8') as infile:
        config = json.load(infile)
    
    return config


CONFIG_FILE = "config.json"
CONFIG = init_config(CONFIG_FILE)

(pool, author_pseudonyms, nation_pseudonyms, months, patches, fixed_links, help_screen) = (
    CONFIG["pool"],
    CONFIG["author_pseudonyms"],
    CONFIG["nation_pseudonyms"],
    CONFIG["months"],
    CONFIG["patches"],
    CONFIG["fixed_links"],
    CONFIG["help_screen"]
)