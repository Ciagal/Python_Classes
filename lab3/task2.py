#!/usr/bin/env python3

from pathlib import Path

def main():

    #dictionery 
    mapping = {
        "i": "oraz",
        "oraz": "i",
        "nigdy": "prawie nigdy",
        "dlaczego": "czemu"
    }

    print("Choose input mode:")
    print("1) direct text input")
    print("2) read from file")
    mode = input("Enter 1 or 2: ").strip()

    #1 direct input
    if mode == "1":
        print("Paste text below. Finish with CTRL+D (mac/linux) or CTRL+Z + Enter (windows):")
        txt = ""

        try:
            while True:
                line = input()
                txt += line + " "
        except EOFError:
            pass

    #2 red from file
    elif mode == "2":
        file_path = input("Enter full path or filename in current folder: ").strip()
        p = Path(file_path)

        if not p.is_file():
            print("ERROR: file does not exist")
            exit(1)

        with open(p, "r", encoding="utf-8") as f:
            txt = f.read()

    else:
        print("Wrong mode")
        exit(1)

    # conversion
    words = txt.split()
    result_words = []

    for w in words:
        if w in mapping:
            result_words.append(mapping[w])
        else:
            result_words.append(w)

    out = " ".join(result_words)

    print("\n--- RESULT ---")
    print(out)


if __name__ == '__main__':
    main()