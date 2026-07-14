import json


# Default Configuration
DEFAULT_CONFIG = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "mydb"
    },
    "api": {
        "timeout": 30,
        "retries": 3
    },
    "logging": {
        "level": "INFO",
        "file": "app.log"
    }
}


def configuration_manager():

    file_name = "config.json"

    try:

        print("Loading config.json...\n")

        with open(file_name, "r") as file:
            config = json.load(file)
        print("Configuration loaded successfully.")

    except FileNotFoundError:
        print("Config file not found.")
        print("Using default configuration.\n")
        config = DEFAULT_CONFIG

    except json.JSONDecodeError:
        print("Invalid JSON file.")
        print("Using default configuration.\n")
        config = DEFAULT_CONFIG

    except IOError:
        print("File Error.")
        return


    required_keys = [
        "database",
        "api",
        "logging"
    ]

    for key in required_keys:
        if key not in config:
            print(f"Missing Key: {key}")
            return

    print("\nCurrent Settings")

    print(f"-Database Host : {config['database']['host']}")
    print(f"-API Timeout   : {config['api']['timeout']} seconds")
    print(f"-Logging Level : {config['logging']['level']}")

    print("\nAdding new setting: cache.enabled = true")
    config["cache"] = {"enabled": True}
    print("New setting added.")

    print("\nUpdating API timeout to 60...")
    config["api"]["timeout"] = 60
    print("Configuration updated.")


    if "retries" in config["api"]:
        del config["api"]["retries"]
        print("\nRemoved API retries.")


    if not isinstance(config["api"]["timeout"], int):
        print("Timeout must be Integer.")
        return
    
    if not isinstance(config["database"]["port"], int):
        print("Database port must be an integer.")
        return

    if config["api"]["timeout"] < 1:
        print("Timeout must be Positive.")
        return


    try:
        with open(file_name, "w") as file:
            json.dump(config, file, indent=4)
        print("\nConfiguration Saved Successfully.")
        print(f"\nConfiguration saved to {file_name}")

    except IOError:
        print("Unable to Save Configuration.")


configuration_manager()