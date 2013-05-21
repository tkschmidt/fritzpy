import md5
import requests
import xml.dom.minidom as dom
telephone_number = "XXX" #number you want to call
dialport ="**610" #port of the phone you want to use 
pwd = "" #passiwrd
username="" #user
t = requests.get('http://fritz.box/login_sid.lua')
g = dom.parseString(t.text)
def get_challenge(dom_parsed_string):
        g = dom.parseString(t.text)
        here = g.getElementsByTagName('SessionInfo')
        for a in here:
                x =  a.getElementsByTagName('Challenge')
                for b in x:
                        return b.firstChild.data.strip()

challenge=get_challenge(g)
def calculate(pwd,challenge):
        p = challenge+"-"+pwd
        return md5.new(p.encode("utf-16-le")).hexdigest()

response=challenge+"-"+calculate(pwd,challenge)

payload ={'response':response,'username':username}

r = requests.post("http://fritz.box/login_sid.lua", data=payload)

g=dom.parseString(r.text)
test=g.getElementsByTagName("SessionInfo")
for a in test:
        x = a.getElementsByTagName("SID")
        for b in x:
                sid = b.firstChild.data

payload ={"sid":sid, "telcfg:settings/UseClickToDial":1, "getpage":"../html/de/menus/menu2.html","telcfg:command/Dial":telephone_number, "telcfg:settings/DialPort":dialport}

r = requests.post("http://fritz.box/cgi-bin/webcm", data=payload)
