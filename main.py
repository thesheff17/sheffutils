#!/usr/bin/env python3

import sheffutils


if __name__ == "__main__":
    sheffutils.terminal_clear()
    print ("main.py started...")
    sheffutils.hello_world()
    output = sheffutils.ollama_list_read(file1="test/test_ollama_list.txt")
    print (output)

    # example of using checkboxes for tools
    options = ["Option 1", "Option 2", "Option 3", "Option 4"]
    selected_options = sheffutils.create_checkboxes(options)

    print("\nSelected options:")
    for option, checked in selected_options.items():
        if checked:
            print(f"- {option}")

    print ("main.py completed.")
