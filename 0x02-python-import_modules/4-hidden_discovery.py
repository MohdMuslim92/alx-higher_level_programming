#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = [
            name
            for name in sorted(dir(hidden_4))
            if not name.startswith("__")
            ]
    if len(names) == 0:
        exit()
    else:
        print("\n".join(names))
