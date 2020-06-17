import re
Email_List = []
get_website_outerHTML = 'email mktgkal@gmail.com 32dsivbkjvbbbiubiusa'
Email_regex = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9_.+-]+\.[a-zA-Z]+)", get_website_outerHTML)
print('Email Regex Through Found Email: ', Email_regex)

for EMail in Email_regex:
    Extension = ['.jpeg', '.png','.io','.xls','xyz.com','.doc','.jpeg','.pdf','.gif','.jpg','example','facebook','test@','test','amazon','naukri','wikipedia','tenders','tender']
    if not any(x in EMail for x in Extension):
        if EMail not in Email_List:
            Email_List.append(EMail)