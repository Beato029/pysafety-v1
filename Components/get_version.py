def get_version():
    import json
    from pathlib import Path

    path = Path(__file__).parent / "config.json"

    with open(path, "r") as f:
        data = json.load(f)

    return data["version"], data["release"]