import re

def cleanUrl(url):

    #removes protocol
    urlCleaned = re.sub("^(http(s)?:\/\/)", "", url)

    return urlCleaned