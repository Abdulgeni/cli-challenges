#!/usr/bin/env python3
"""Organize files in a directory by their file extension.

Usage:
    python file_organizer.py /path/to/folder
"""

import os
import sys
import shutil


def organize_by_extension(directory: str) -> dict:
    """
    Move files into subdirectories based on their file extension.

    Args:
        directory: Path to the directory to organize.

    Returns:
        A dict mapping each extension to the number of files moved.
    """
    if not os.path.isdir(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")

    moved = {}

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if os.path.isdir(filepath) or filename.startswith('.'):
            continue

        _, ext = os.path.splitext(filename)
        ext = ext.lstrip('.').lower() or 'no_extension'

        target_dir = os.path.join(directory, ext)
        os.makedirs(target_dir, exist_ok=True)

        shutil.move(filepath, os.path.join(target_dir, filename))
        moved[ext] = moved.get(ext, 0) + 1

    return moved


def main():
    if len(sys.argv) != 2:
        print("Usage: python file_organizer.py <directory>")
        sys.exit(1)

    try:
        result = organize_by_extension(sys.argv[1])
        if result:
            print("Files organized:")
            for ext, count in sorted(result.items()):
                print(f"  {ext}: {count} file(s)")
        else:
            print("No files to organize.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()