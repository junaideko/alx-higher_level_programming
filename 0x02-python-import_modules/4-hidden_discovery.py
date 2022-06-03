#!/usr/bin/python3
if __name__ == "__main__":
    """print names defined by hidden_4 module by one nameper line"""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
