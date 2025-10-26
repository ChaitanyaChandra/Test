#!/usr/bin/env python3
import sys


def fix_text(text_input):
    # Step 1: Remove all newlines
    text = text.replace("\n", " ")

    # Step 2: Add newline after each period
    text = text.replace(". ", ".\n")

    # Clean up spaces/newlines
    text = text.strip()
    return text


if __name__ == "__main__":
    # Read text from stdin or command-line argument
    if len(sys.argv) > 1:
        raw_text = sys.argv
    else:
        raw_text = sys.stdin.read()

    cleaned = fix_text(raw_text)

    # Save to output file
    output_path = "/tmp/fixed_text_output.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(cleaned)

    # Print the path for the shell script to use
    print(output_path)
