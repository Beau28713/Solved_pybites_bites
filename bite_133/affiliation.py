import re

def generate_affiliation_link(url):

    affil_link = 'http://www.amazon.com/{}/?tag=pyb0f-20'

    pattern = r'(dp\/\w*)'
    find_pattern = re.findall(pattern, url)
    if find_pattern:
        return affil_link.format(find_pattern[0])