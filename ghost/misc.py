import os

def ghost_path():
    import ghost
    return os.path.join(os.path.dirname(ghost.__file__), '..')
