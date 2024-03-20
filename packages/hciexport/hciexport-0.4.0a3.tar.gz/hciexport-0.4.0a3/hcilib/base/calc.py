# This file is closed source.
# Use without written allowance is prohibited.
#
# Copyright (c) 2017-2024 Thorsten Simons (sw@snomis.eu)

def calcbytesize(nbytes, kb=False, mb=False, formLang=False, nozero=False):
    '''
    Return a given no. of Bytes in a human-readable format.
    '''
    if nozero and not nbytes:
        return('')

    sz = ["B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB"]
    szl = ["Byte", "Kibibyte", "Mebibyte", "Gibibyte", "Tebibyte",
           "Pebibyte", "Exbibyte", "Zebibyte", "Yobibyte"]
    i = 0
    neg = False
    if kb:
        nbytes *= 1024  # we got kibibytes!
    if mb:
        nbytes *= 1024*1024  # we got mibibytes!

    if nbytes < 0:
        neg = True
        nbytes *= -1

    while nbytes > 1023:
                    nbytes = nbytes / 1024
                    i = i + 1
    if neg:
        nbytes *= -1

    if formLang:
        if szl[i] == 'Byte':
            return("{0:.0f} {1:}".format(nbytes, szl[i]))
        else:
            return ("{0:.2f} {1:}".format(nbytes, szl[i]))
    else:
        if sz[i] == 'B':
            return("{0:.0f} {1:}".format(nbytes, sz[i]))
        else:
            return("{0:.2f} {1:}".format(nbytes, sz[i]))

