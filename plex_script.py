#!/Users/dona8756/CODE/scripts/python/test_scripts
# -*- coding: utf-8 -*- #

"""Rename plex movie files."""

import os

"""Function to rename multiple files."""
# replace directory with working directory of files
dir_loc = '/Users/dona8756/CODE/scripts/python/test_scripts/movie_files/'
list_files = []

print("The dir is: %s" % os.listdir(os.getcwd()))

for count, filename in enumerate(os.listdir(dir_loc)):
    list_files.append(filename)

for filename in list_files:

    if '.mkv' not in filename and '.mp4' not in filename:
        print('Skipping:', filename)
        list_files.remove(filename)

for filename in list_files:

    if 'mkv' in filename:
        # this strips the '.' out, then appends '.mkv'
        clean_file = filename.replace('.', ' ').replace(' mkv', '')
        dst = clean_file
        src = filename
        key_words = ['BluRay', '1080p', 'X264-AMIABLE']
        querywords = dst.split()
        resultwords = [wrd for wrd in querywords if wrd not in key_words]
        result = ' '.join(resultwords)
        file_type = '.mkv'
        clean_name = result
        dst = clean_name
        print('Old File', 'Name:', filename.replace('.mkv', ''))
        print('New File', 'Name:', dst)

        os.rename(src, dst)

    if 'mp4' in filename:
        # this strips the '.' out, then appends '.mkv'
        org_src = filename
        clean_file = filename.replace('.', ' ').replace(' mp4', '')

        dst = clean_file
        src = filename
        key_words = ['BluRay', '1080p', 'X264-AMIABLE']
        querywords = dst.split()
        resultwords = [wrd for wrd in querywords if wrd not in key_words]
        result = ' '.join(resultwords)
        file_type = '.mp4'
        clean_name = result
        dst = clean_name
        print('Old File', 'Name:', filename.replace('.mp4', ''))
        print('New File', 'Name:', dst)

        os.rename(src, dst)
