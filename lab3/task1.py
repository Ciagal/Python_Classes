#!/usr/bin/env python3

from pathlib import Path

def main():
    
    # words to be cut
    cut = {"and", "to", "why", "never", "i", "the"}
    
    print("Choose input mode:")
    print("1) direct text input")
    print("2) read from file")
    mode = input("Enter 1 or 2: ").strip()

    # 1: direct 
    if mode == "1":
        print("Input text. Finish with CTRL+D (mac/linux) or CTRL+Z + Enter (windows):")
        txt = ""

        try:
            while True:
                line = input()      
                txt += line + " "  
        except EOFError:
            pass

    # 2: read from file
    elif mode == "2":
        file_path = input("Enter full path or filename in current folder: ").strip()
        p = Path(file_path)

        # if file does not exist -> end script
        if not p.is_file():
            print("ERROR: file does not exist")
            exit(1)

        # open file
        with open(p, "r", encoding="utf-8") as f:
            txt = f.read()

    # error: wrong mode ex. "3"
    else:
        print("Error: Wrong Mode")
        exit(1)

    # filtering
    words = txt.split()         
    filtered = []               

    for w in words:
        if w.lower() not in cut:
            filtered.append(w)

    # joining
    out = " ".join(filtered)

    print("\n--- RESULT ---")
    print(out)


if __name__ == '__main__':
    main()
