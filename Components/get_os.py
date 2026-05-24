
def get_os():
    import platform
    data = [platform.system(), platform.release()]
    return data