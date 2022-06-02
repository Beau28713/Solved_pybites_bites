import os


def count_dirs_and_files(directory= '.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    file_count = 0
    dir_count = 0

    for dirpath, dirnames, files in os.walk(directory):
       """after i finaly figured out these was list and i could use len() this was easy"""
       dir_count += len(dirnames)
       file_count += len(files)
    

    return (dir_count, file_count)