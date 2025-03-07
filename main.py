#!/usr/bin/env python3

import sheffutils


if __name__ == "__main__":
    sheffutils.terminal_clear()
    print ("main.py started...")
    sheffutils.hello_world()
    output = sheffutils.ollama_list_read(file1="test/test_ollama_list.txt")
    print (output)
    print ("main.py completed.")
