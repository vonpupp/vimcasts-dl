vimcast-dl.py - download videos from vimcasts.org

THIS PROJECT IS NOT MAINTAINED ANYMORE. Feel free to send PRs

# SYNOPSIS
**vimcasts-dl.py** [JSON-FILE]


# INSTALLATION

To install it right away for all UNIX users (Linux, OS X, etc.), type:

    sudo curl https://yt-dl.org/latest/youtube-dl -o /usr/local/bin/youtube-dl
    sudo chmod a+x /usr/local/bin/youtube-dl

If you do not have curl, you can alternatively use a recent wget:

    wget --no-check-certificate https://raw.githubusercontent.com/vonpupp/vimcasts-dl/master/vimcasts-dl.py -O vimcasts-dl.py
    chmod a+x vimcasts-dl.py

# DESCRIPTION
**vimcasts-dl.py** is a small command-line program to download videos from
vimcasts.org. It requires the Python interpreter, version
2.6, 2.7, or 3+, and it is not platform specific. It should work on
your Unix box or on Mac OS X. It is released to the public domain,
which means you can modify it, redistribute it or use it however you like.

## REQUIREMENTS
 - aria2 must be installed on your system

# VIDEO SELECTION

Videos can be filtered by their upload date using the options `--date`, `--datebefore` or `--dateafter`, they accept dates in two formats:

 - Absolute dates: Dates in the format `YYYYMMDD`.
 - Relative dates: Dates in the format `(now|today)[+-][0-9](day|week|month|year)(s)?`

Examples:

```bash
# To install the base packages run:
wget --no-check-certificate https://raw.githubusercontent.com/vonpupp/vimcasts-dl/master/vimcasts-dl.py
```
# Download only the videos uploaded in the last 6 months
$ youtube-dl --dateafter now-6months

# Download only the videos uploaded on January 1, 1970
$ youtube-dl --date 19700101

$ # will only download the videos uploaded in the 200x decade
$ youtube-dl --dateafter 20000101 --datebefore 20091231
```

# COPYRIGHT

vimcasts-dl.py is released into the public domain by @vonpupp
