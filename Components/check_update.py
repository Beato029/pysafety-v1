
def check_update():
    import requests
    from get_version import get_version

    url = "https://raw.githubusercontent.com/Beato029/pysafety-v1/refs/heads/main/version.json"

    req = requests.get(url)
    req = req.json()

    new_version = req["version"]
    new_release = req["release"]
    new_compatibility = req["compatibility"]

    version, release = get_version()

    # print(version, release)
    
    if version == "beta" and new_version == "beta":
        if new_release > release:
            return f"New beta available {version} {release} -> {new_version} {new_release}\nI don't recommend installing beta versions because they may contain bugs"
    
    elif version == "beta" and new_version == "public":
        return f"New version available {version} {release} -> {new_version} {new_release}\nIt is recommended to update to fix bugs"
    
    elif version == "public" and new_version == "public":
        if new_release > release:
            return f"New version available {version} {release} -> {new_version} {new_release}\nIt is recommended to update to fix bugs"

    return "No updates available"