import sys


def combine(hashinfo, trackers):
    if hashinfo.isalnum():
        trackinfo = '&tr=' + '&tr='.join(trackers)
        result = 'magnet:?xt=urn:btih:' + hashinfo + trackinfo
    else:
        sys.exit('ERROR: Bad hashinfo')

    return result


if __name__ == '__main__':
    hashinfo = '204a1789dd04e4d8f5a4e098e8f777794888f4ad'
    trackers = (
            'udp://tracker.coppersurfer.tk:6969/announce',
            'http://68.64.165.106:2710/announce',
            'http://p4p.arenabg.ch:1337/announce',
            'http://tracker.internetwarriors.net:1337/announce',
            'udp://tracker.vanitycore.co:6969/announce',
            'udp://tracker.leechers-paradise.org:6969/announce',
            'udp://p4p.arenabg.ch:1337/announce',
            )

    print(combine(hashinfo, trackers))
