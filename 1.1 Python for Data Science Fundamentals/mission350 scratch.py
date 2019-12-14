def notEnglish (a_string):
    for char in a_string:
        if ord(char) > 127:
            return False
         
    return True

print (notEnglish ('Instagram'))
print (notEnglish('爱奇艺PPS -《欢乐颂2》电视剧热播'))