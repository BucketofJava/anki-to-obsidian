import urllib.parse
import re
f=open("Daily.txt", 'r', encoding='utf-8')
S=f.read()
S=S.split("\n")
f.close()
pairs=[]
#titles={}
titles={}
def string_to_md_name(str):
    return urllib.parse.quote(str)+".md"
def string_to_link(str):
    return "[{}]({})".format(str, string_to_md_name(str))
for line in S:
    if "{{c" in line or "[latex]" in line:
        continue; 
    pair=line.split("	")[:2] 
    if(len(pair[0].split(" "))>6 or "<img src" in pair[0]):
        continue; 
    pair[0]=pair[0].replace("/", "-").replace("\'", "").replace("\"", "").replace("\\", "").replace("&", "").replace(";", "")
    pair[0]=pair[0].replace("What is a ", "").replace("What is ", "").replace("An ", "").replace(" is", "").replace("A ", "").replace("?", "")
    pair[0]=pair[0].replace("<", "").replace(">", "").replace("|", "").replace("*", "")
    if(len(pair[0])<=2 or len(pair[1])<=2):
        continue;
    if(pair[0][0]==" "):
        pair[0]=pair[0][1:]
    if(pair[0][-1]==" "):
        pair[0]=pair[0][:-1]
    pairs.append(pair)
    titles[pair[0]]=string_to_link(pair[0])
notes_path="Notes/"
i=0
print(len(pairs))
for pair in pairs:
    cur_title=pair[0]
    body=pair[1]
    body_formatted=pair[1].replace(" ", "").lower()
    for title in list(titles.keys()):
        try:
            body=re.sub(title, titles[title], body, flags=re.IGNORECASE)
        except re.error:
            continue;
    f=open(notes_path+cur_title+".md", "w", encoding='utf-8')
    f.write(body)
    f.close()
    i+=1
    if(i%10==0):
        print(i)

