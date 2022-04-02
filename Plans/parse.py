import json
import yaml
import os
import string
import shutil

invalid = '<>:"/\|?*$ '

my_dir = './apps'
for root, dirs, files in os.walk(my_dir, topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))
        
my_dir = './export'
for root, dirs, files in os.walk(my_dir, topdown=False):
    for name in files:
        os.remove(os.path.join(root, name))
    for name in dirs:
        os.rmdir(os.path.join(root, name))

shutil.rmtree('./apps', ignore_errors=True)


shutil.rmtree('./export', ignore_errors=True)


os.mkdir("./apps")
os.mkdir("./export")
os.mkdir("./apps/yaml")
os.mkdir("./apps/json")
os.mkdir("./apps/req/")
os.mkdir("./apps/req/yaml")
os.mkdir("./apps/req/json")

fileObject = open("af.json", "r")
jsonContent = fileObject.read()
afList = json.loads(jsonContent)
combined = {}
combinedfree = {}
combinedreq = {}

paths1 = os.listdir("../website/apps/stable")
paths2 = os.listdir("../website/apps/incubator")
paths3 = os.listdir("../website/apps/core")
paths4 = os.listdir("../website/apps/games")

paths = paths1 + paths2 + paths3 + paths4
for p in range(len(paths)):
    paths[p] = paths[p].lower()

print("Splitting and sanitising json input...")
for n in afList:
  if "Name" in n.keys() and n["Name"].lower() not in paths and ("Blacklist" not in n.keys() or not n["Blacklist"] ) and ("Deprecated" not in n.keys() or not n["Deprecated"] ) :
    tmp = n["Name"].lower()
    for char in invalid:
      tmp = tmp.replace(char, '')
    if tmp in n.keys():
      tmp = tmp+"2"
    if tmp in n.keys():
      tmp = tmp+"3"
    if tmp in n.keys():
      tmp = tmp+"4"
    print(tmp.encode("utf-8"))
    
    
    n.pop("downloads", "")
    n.pop("downloadtrend", "")
    n.pop("stars", "")
    n.pop("trending", "")
    n.pop("trends", "")
    n.pop("trendsDate", "")
    n.pop("templatePath", "")
    n.pop("Shell", "")
    n.pop("CPUset", "")
    n.pop("DonateImg", "")
    n.pop("DonateLink", "")
    n.pop("DonateText", "")
    n.pop("Video", "")
    n.pop("Support", "")
    n.pop("FirstSeen", "")
    n.pop("LastUpdate", "")
    n.pop("LastUpdateScan", "")
    n.pop("Repo", "")
    
    if "Overview" in n.keys() and n["Overview"]:
      ovlist = n["Overview"].splitlines(keepends=True)
      try:
        while True:
          ovlist.remove("\r\n")
        while True:
          ovlist.remove("\n")
        while True:
          ovlist.remove("DESCRIPTION\r\n")
        while True:
          ovlist.remove("DESCRIPTION")
      except ValueError:
        pass
      n["Overview"] = ovlist[0]
    
    if "Config" in n.keys() and n["Config"]:
      hold = {}
      hold["Port"] = {}
      hold["Variable"] = {}
      hold["Path"] = {}
      hold["Device"] = {}
      hold["Label"] = {}
      if isinstance(n["Config"], list):
        for a in n["Config"]:
          name = a["@attributes"]["Name"]
          type = a["@attributes"]["Type"]
          a.update(a["@attributes"])
          a.pop("@attributes", "")
          hold[type][name] = a
      else:
          name = n["Config"]["@attributes"]["Name"]
          type = n["Config"]["@attributes"]["Type"]
          n["Config"].update(n["Config"]["@attributes"])
          n["Config"].pop("@attributes", "")
          hold[type][name] = n["Config"]
      n.pop("Config", "")
      n["Config"] = hold
      
    
    globals()['%s' % tmp] = n
    
    if "Plugin" in n.keys() and n["Plugin"]:
      print("skipping "+tmp+" is a unraid plugin...")
    else:
      combined[tmp] = n
      if ("Requires" in n.keys() and n["Requires"]) or ("Network" in n.keys() and n["Network"] == "host"):
        combinedreq[tmp] = n
        jsonString = json.dumps(n)
        jsonFile = open("apps/"+"req/"+"json/"+tmp+".json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        
        yamlString = yaml.dump(n)
        yamlFile = open("apps/"+"req/"+"yaml/"+tmp+".yaml", "w")
        yamlFile.write(yamlString)
        yamlFile.close()
      else:
        combinedfree[tmp] = n
        jsonString = json.dumps(n)
        jsonFile = open("apps/"+"json/"+tmp+".json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        
        yamlString = yaml.dump(n)
        yamlFile = open("apps/"+"yaml/"+tmp+".yaml", "w")
        yamlFile.write(yamlString)
        yamlFile.close()

print("Writhing combined json and yaml output...")

jsonString2 = json.dumps(combinedfree)
jsonFile2 = open("apps-free.json", "w")
jsonFile2.write(jsonString2)
jsonFile2.close()

yamlString2 = yaml.dump(combinedfree)
yamlFile2 = open("apps-free.yaml", "w")
yamlFile2.write(yamlString2)
yamlFile2.close()


jsonString3 = json.dumps(combinedreq)
jsonFile3 = open("apps-req.json", "w")
jsonFile3.write(jsonString3)
jsonFile3.close()

yamlString3 = yaml.dump(combinedreq)
yamlFile3 = open("apps-req.yaml", "w")
yamlFile3.write(yamlString3)
yamlFile3.close()

jsonString4 = json.dumps(combined)
jsonFile4 = open("apps.json", "w")
jsonFile4.write(jsonString4)
jsonFile4.close()

yamlString4 = yaml.dump(combined)
yamlFile4 = open("apps.yaml", "w")
yamlFile4.write(yamlString4)
yamlFile4.close()

chartsyaml = {}
questionsyaml = {}
valuesyaml = {}

fileObject = open("example/Chart.json", "r")
jsonContent = fileObject.read()
chartsyaml = json.loads(jsonContent)

fileObject = open("example/values.json", "r")
jsonContent = fileObject.read()
valuesyaml = json.loads(jsonContent)

fileObject = open("example/questions.json", "r")
jsonContent = fileObject.read()
questionsyaml = json.loads(jsonContent)

print("building Helm Charts...")
for name, app in combinedfree.items():
  appchartyaml = chartsyaml
  tmpname = app["Name"]
  
  for char in invalid:
    tmpname = tmpname.replace(char, '')
    
  print(tmpname.encode("utf-8"))
  appchartyaml["name"] = tmpname
  os.mkdir("./export/"+tmpname)
  appyamlString = yaml.dump(appchartyaml)
  appyamlFile = open("./export/"+tmpname+"/Chart.yaml", "w")
  appyamlFile.write(appyamlString)
  appyamlFile.close()