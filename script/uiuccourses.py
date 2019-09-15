import re
# Contains: functions to help parse text-based UIUC course data

# return a list of the course codes (ie "AAS 100") contained in a string
def containsCourseCodes(st):
    codes = re.findall(r'[A-Z]{2,4}\s\d{3}', st)
    return [c.replace('\xa0', ' ') for c in codes]


# return a course code (ie "AAS 100") when the input string includes "See [Course]," return None otherwise
def seeCode(st):
    code = re.search(r'See\s([A-Z]{2,4}\s\d{3})\.', st)

    if code:
        return code.groups(1)[0].replace('\xa0', ' ') # the docs say .groups(1) should be a string but it's a tuple so whatever
    else:
        return None
