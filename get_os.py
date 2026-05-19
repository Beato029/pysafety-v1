import platform

def get_os():
    data = [platform.system(), platform.release()]
    return data