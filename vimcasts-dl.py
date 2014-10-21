#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import urllib2
import subprocess

JSON_URL = 'http://media.vimcasts.org/videos/index.json'
config = {}


def load_json(filename=None):
    if filename is None:
        reader = urllib2.urlopen(JSON_URL)
    else:
        reader = open(filename)
    return json.load(reader)


def parse_args():
    global config
    if len(sys.argv) > 2:
        print('Usage:')
        print('  wget http://media.vimcasts.org/videos/index.json  #(optional)')
        print('  python {} [index.json]'.format(sys.argv[0]))
        sys.exit(0)
    config['filename'] = None
    if len(sys.argv) == 2:
        config['filename'] = sys.argv[1]


def get_url(dictionary, index):
    return dictionary[index]['ogg']['url']


def get_save_as_filename(video_url, index):
    filename = video_url.split('?')[0]
    filename = filename.split('/')[-1]
    return index.zfill(2) + '_' + filename


def download_file_as(video_url, filename):
    command = ['aria2c',
               '--continue=true',
               '--max-concurrent-downloads=1',
               '--user-agent="Mozilla/5.0 (X11; Linux x86_64; rv:7.0.1) \
                Gecko/20100101 Firefox/7.0.1"',
               '{}'.format(video_url),
               '-o videos/{}'.format(filename)]
    subprocess.Popen(command).communicate()


def run():
    try:
        global config
        parse_args()
        filename = config['filename']
        data = load_json(filename)
        for video in sorted(data):
            video_url = get_url(data, video)
            filename = get_save_as_filename(video_url, video)
            print("Getting: {}".format(video_url))
            print("Saving as: {}".format(filename))
            download_file_as(video_url, filename)
    except KeyboardInterrupt:
        print('Canceled by user')

if __name__ == "__main__":
    run()
