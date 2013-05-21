import re, urllib2

# Here's some utilities from taking a uuid from uuidgenerator.net
# and (deterministically) turning it into a pronouncable baby name.
# Sadly, this baby name is no longer 100% unique, but whatever, neither
# is your actual baby's name.
# love, -- Brian "@bgawalt" Gawalt

consonants = "bcdfghjklmnpqrstvwxyz"
vowels = "aeiou"

combos = []
for con in consonants:
    for vow in vowels:
        combos.append(con+vow)

def popHexPair(s):
    if len(s) < 3:
        num = int(s, 16)
        rest = ""
    else:
        num = int(s[0:2], 16)
        rest = s[2:]
    return (num,rest)

WSP_REX = re.compile("\s+")
DASH_REX = re.compile("(\-\s)|(\s\-)|(\-\-)")

def cleanName(n):
    return n.replace("- ", '-').replace(" -", ' ').replace("--", '-').strip().strip("-")

def uuidToName(uuid):
    name = " "
    x = uuid.replace("-", '')
    while len(x) > 0:
        tup = popHexPair(x)
        n = tup[0]
        if n >= len(combos):
            if n %5 == 1:
                spacer = "-"
            else:
                spacer = " "
            if n%2 == 0 and name[-1] != " " and name[-1] != "-":
                syllable = consonants[n%len(consonants)]+spacer
            else:
                syllable = " "
        else:
            syllable = combos[n]
        name = name + syllable
        x = tup[1]
    sname = re.split(WSP_REX, name)
    capname = " ".join([n.capitalize() for n in sname])
    return cleanName(capname)


def getUUIDfromSite():
    http = urllib2.urlopen("http://www.uuidgenerator.net/version4")
    text = http.read()
    START_STR = '<p class="uuid">'
    start = text.find(START_STR)
    if start < 0:
        return "{NO UUID FOR YOU}"
    end = text.find('</p>', start+len(START_STR))
    if end < 0:
        return "{NO UUID FOR YOU}"
    return text[start+len(START_STR):end]
    
    

if __name__ == "__main__":
    uuid = getUUIDfromSite()
    if "UUID" in uuid:
        print uuid
    else:
        print uuid
        print uuidToName(uuid)
        
        
    
    
    
