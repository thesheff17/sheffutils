#!/usr/bin/env python3

import os
import sys
from datetime import datetime
import subprocess as sb
from dataclasses import dataclass
from typing import List


# this block help manages 3rd party imports
# you can still use all the code that doesn't 
# depend on 3rd party modules but you can also
# build off requirements.txt to build a virtualenv
# to fix this message. I only want to manage 1 utils file.
try:
    import boto3
    import requests
    import flask
except ModuleNotFoundError as f:
    print ({f})
    print ("pip module(s) not found.  Exiting script.")
    print ("Please read README.md to create virtualenv.")
    sys.exit(1)
except Exception as e:
    print ("something else went wrong...")
    sys.exit(1)

######################################
#                                    #
# basic def to manage terminal stuff #
# namespace: terminal_               #
#                                    #
######################################
def terminal_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def terminal_create_checkboxes(options):
    """
    Creates a simple checkbox-like interface in the console, allowing ranges.

    Args:
        options: A list of strings representing the checkbox options.

    Returns:
        A dictionary where keys are the options and values are booleans
        representing whether the option is checked.
    """

    checkboxes = {option: False for option in options}

    while True:
        print("\nSelect options (press Enter to confirm):")
        for i, option in enumerate(options):
            checked = "[x]" if checkboxes[option] else "[ ]"
            print(f"{i + 1}. {checked} {option}")

        try:
            choice = input(
                "Enter option number(s) or ranges (e.g., 1 3 2-4), or press Enter to finish: "
            )
            if not choice:
                break  # User pressed Enter, finish selection

            parts = choice.split()
            selected_indices = []

            for part in parts:
                if "-" in part:
                    start, end = map(int, part.split("-"))
                    selected_indices.extend(range(start - 1, end))
                else:
                    selected_indices.append(int(part) - 1)

            for index in selected_indices:
                if 0 <= index < len(options):
                    options_list = list(options)
                    checkboxes[options_list[index]] = not checkboxes[options_list[index]]
                else:
                    print(f"Invalid option number: {index+1}")

        except ValueError:
            print("Invalid input. Please enter numbers or ranges.")

    return checkboxes


def run_command(command, output_file):
    """
    Run a terminal command and optionally write its output to a file.

    Args:
        command (str): The terminal command to be executed as a string.
        output_file (str): The filename to which the output should be written.

    Returns:
        str: The output of the command if successful, otherwise an error message.
    """
    try:
        # Execute the command using subprocess.run
        result = sb.run(command, shell=True, check=True, text=True, capture_output=True)
        
        with open(f"text/{output_file}", 'w+') as file:
            file.write(result.stdout.strip())
        
        return "Command executed successfully."
    except sb.CalledProcessError as e:
        # Return the error message if something goes wrong
        return f"Error: {e.stderr}"

######################################
#                                    #
# basic def to random things I need  #
#                                    #
######################################

def get_timestamp():
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d-%H-%M-%S-%f")
    return formatted_date

def hello_world():
    print ("hello world")
    print (f"timestamp: {get_timestamp()}")
    print (f"python version: {sys.version}")
    return "hello world"

######################################
#                                    #
# ollama stuff                       #
# namespace: ollama_                 #
#                                    #
######################################

@dataclass
class Ollamalist:
    name: str
    id: str
    size: str
    modified: str

def ollama_list_read(file1="text/ollama-list.txt"):
    f = open(file1, "r")
    text1 = f.readlines()
    
    data_entries = [] # store entries in a list

    # Loop through each line and create a DataEntry instance
    for line in text1[1:]:
        parts = line.split()
        name = parts[0]
        id = parts[1]
        size = ' '.join(parts[2:4])
        modified = ' '.join(parts[4:])
        
        # Create a new DataEntry instance and add it to the list
        entry = Ollamalist(name, id, size, modified)
        data_entries.append(entry)

    return data_entries

    # example of looping over the data
    # Print the parsed data entries
    # for entry in data_entries:
    #    print(entry)