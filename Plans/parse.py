import json
import yaml
import os
import string
import shutil
import requests
import textwrap
import re

## This can be set to True to force use of tccr.io repo instead of normal
genTCCR = True

invalid = '<>:"/\|?*$ ()+'
invalidtext = '_<>:"/\|*$+'
blacklistedenvs = ["UID", "GID", "PUID", "PGID", "TZ"]
puidcheck = ["UID", "GID", "PUID", "PGID"]
puidflag = False


my_dir = './apps'

print("test: ")

with open("./blacklist.txt", "r") as f:
    blacklist = f.readlines()
for b in range(len(blacklist)):
    blacklist[b] = blacklist[b].strip("\n").lower()
    print(blacklist[b])
    
with open("./reqblocked.txt", "r") as f:
    reqblocked = f.readlines()
for r in range(len(reqblocked)):
    reqblocked[r] = reqblocked[r].strip("\n").lower()

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
os.mkdir("./export/app")
os.mkdir("./export/images")
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

paths1 = os.listdir("./website-charts/stable")
paths2 = os.listdir("./website-charts/incubator")
paths3 = os.listdir("./website-charts/dev")
paths4 = os.listdir("./website-charts/dependency")

paths = paths1 + paths2 + paths3 + paths4
for p in range(len(paths)):
    paths[p] = paths[p].lower()

print("Splitting and sanitising json input...")
for n in afList:
  if "Name" in n.keys() and ("Blacklist" not in n.keys() or not n["Blacklist"] ) and ("Deprecated" not in n.keys() or not n["Deprecated"] ) and ( "Plugin" not in n.keys() or not n["Plugin"] ) and ( "LanguagePack" not in n.keys() or not n["LanguagePack"] ):
    tmp = n["Name"].lower()
    for char in invalid:
      tmp = tmp.replace(char, '')
    tmp = tmp.replace('.', '-')
    tmp = tmp.replace('_', '-')
    tmp = tmp.replace('binhex-', '')
    tmp = tmp.replace('jbreed-', '')
    tmp = tmp.replace('bitnami-', '')
    tmp = tmp.encode("utf-8").decode("utf-8")
    if tmp in n.keys():
      tmp = tmp+"-duplicate-1"
    if tmp in n.keys():
      tmp = tmp+"-duplicate-2"
    if tmp in n.keys():
      tmp = tmp+"-duplicate-3"
    tmp = tmp.lower()
    print(tmp)
    n["Name"] = tmp
    testtmp = tmp.replace("-", '')
    if ( tmp not in paths ) and ( tmp.rstrip(string.digits) not in paths )  and ( testtmp not in paths ) and ( tmp not in blacklist )  and ( tmp.rstrip(string.digits) not in blacklist )  and ( testtmp not in blacklist ):
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
      n.pop("topPerforming", "")
      n.pop("topTrending", "")
      n.pop("TemplateURL", "")
      n.pop("ChangeLogPresent", "")
      n.pop("BindTime", "")
      n.pop("Beta", "")
      n.pop("RecommendedDate", "")
      n.pop("RecommendedRaw", "")
      n.pop("RecommendedReason", "")
      
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
    
      if not "CategoryList" in n.keys():
        n["CategoryList"] = ["Other"]
        
      if not "Overview" in n.keys():
        n["Overview"] = "This App does not have a description yet..."
        
      n["Sources"] = []
      if "Project" in n.keys() and n["Project"]:
        n["Sources"].append(n["Project"])
        
      if "Registry" in n.keys() and n["Registry"]:
        n["Sources"].append(n["Registry"])
        
      if "Github" in n.keys() and n["Github"]:
        n["Sources"].append(n["Github"])
        
      if "ReadMe" in n.keys() and n["ReadMe"]:
        n["Sources"].append(n["ReadMe"])
        
      n.pop("Project", "")
      n.pop("Github", "")
      n.pop("GitHub", "")
      n.pop("ReadMe", "")
        
      n["Keywords"] = []
      n["Keywords"].append(tmp)
      n["Keywords"] = n["Keywords"]+n["CategoryList"]
      
      if not "Requires" in n.keys():
        n["Requires"] = ""
    
        
      if "influxdb" in tmp:
        n["Requires"] = n["Requires"]+" Influxdb (autoadd)"
        
      if "exporter" in tmp:
        n["Requires"] = n["Requires"]+" exporter app (autoadd)"
        
      if "-duplicate-" in tmp:
        n["Requires"] = n["Requires"]+" duplicate app (autoadd)"
        
      if "vpn" in tmp:
        n["Requires"] = n["Requires"]+" VPN related app (autoadd)"
        
      if "Network" in n.keys() and n["Network"] == "host":
        n["Requires"] = n["Requires"]+" App uses hostnetworking (autoadd)"
      n.pop("Network", "")
        
      if "Networking" in n.keys() and n["Networking"] and "Mode" in n["Networking"].keys() and n["Networking"]["Mode"] and n["Networking"]["Mode"] == "host":
        n["Requires"] = n["Requires"]+" App uses hostnetworking (autoadd)"
        
      if (tmp in reqblocked) or (tmp.rstrip(string.digits) in reqblocked) or (testtmp in reqblocked) :
        n["Requires"] = n["Requires"]+" as was manually flagged as having requirements (autoadd)"
        
      dockersplit = n["Repository"].split(":", 1)
      n["Repository"] = dockersplit[0]
      if len(dockersplit) == 2:
        n["Tag"] = dockersplit[1]
      else:
        n["Tag"] = "latest"

      if not "Config" in n.keys() or not n["Config"]:
        n["Config"] = {}
      
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
      elif "@attributes" in n["Config"].keys() and not n["Config"]["@attributes"]:
          name = n["Config"]["@attributes"]["Name"]
          type = n["Config"]["@attributes"]["Type"]
          n["Config"].update(n["Config"]["@attributes"])
          n["Config"].pop("@attributes", "")
          hold[type][name] = n["Config"]
      n.pop("Config", "")
      n["Config"] = hold
        
      if ( "Environment" in n.keys() and n["Environment"] ) and isinstance(n["Environment"], dict) and ( "Variable" in n["Environment"].keys() and n["Environment"]["Variable"] ):
        if isinstance(n["Environment"]["Variable"], list):
          for var in n["Environment"]["Variable"]:
            if var["Name"] and var["Name"] in puidcheck:
              puidflag = True
            if var["Name"] and not var["Name"] in blacklistedenvs :
              n["Config"]["Variable"][var["Name"]] = {}
              n["Config"]["Variable"][var["Name"]]["Name"] = var["Name"]
              n["Config"]["Variable"][var["Name"]]["Target"] = var["Name"]
              n["Config"]["Variable"][var["Name"]]["value"] = var["Value"]
        elif isinstance(n["Environment"]["Variable"], dict) and not "Name" in n["Environment"]["Variable"] and not "Value" in n["Environment"]["Variable"]:
          for name, value in n["Environment"]["Variable"].items():
            if name and name in puidcheck:
              puidflag = True
            if name and not name in blacklistedenvs:
              n["Config"]["Variable"][name] = {}
              n["Config"]["Variable"][name]["Name"] = name
              n["Config"]["Variable"][name]["Target"] = value["name"]
              n["Config"]["Variable"][name]["value"] = value["Value"]
              
      n.pop("Environment", "")
      
      varstore = {}
      for name, value in n["Config"]["Variable"].items():
        store = value

        name = name.lower()
        for char in invalid:
          name = name.replace(char, '')
        name = name.replace('.', '-')
        varstore[name] = value
        
      n["Config"].pop("Variable", "")
      n["Config"]["Variable"] = varstore
              
      if ( "Data" in n.keys() and n["Data"] ) and isinstance(n["Data"], dict) and ( "Volume" in n["Data"].keys() and n["Data"]["Volume"] ):
        if isinstance(n["Data"]["Volume"], dict):
          store = n["Data"]["Volume"]
          n["Data"].pop("Volume", "")
          n["Data"]["Volume"] = [store]
        if isinstance(n["Data"]["Volume"], list):
          for var in n["Data"]["Volume"]:
            if not "Name" in var.keys():
              var["Name"] = os.path.basename(os.path.normpath(var["ContainerDir"]))
            label = n["Name"].lower()
            for char in invalid:
              label = label.replace(char, '')
            label = label.replace('.', '-')
            n["Config"]["Path"][label] = {}
            n["Config"]["Path"][label]["Name"] = var["Name"]
            
            if "HostDir" in var.keys() and var["HostDir"]:
              n["Config"]["Path"][label]["value"] = var["HostDir"]
            n["Config"]["Path"][label]["Target"] = var["ContainerDir"]
            if "Mode" in var.keys() and var["Mode"]:
              n["Config"]["Path"][label]["Mode"] = var["Mode"]

      n.pop("Data", "")
      
      pathstore = {}
      for name, value in n["Config"]["Path"].items():
        store = value
        basename = os.path.basename(os.path.normpath(value["Target"]))
        name = name.lower()
        name = re.sub(tmp+'-', '', name)
        for char in invalid:
          name = name.replace(char, '')
        
        if basename == "config" and not "config" in pathstore.keys():
          name = "config"
        if basename == "data" and not "data" in pathstore.keys():
          name = "data"

        name = name.lower()
        for char in invalid:
          name = name.replace(char, '')
        name = name.replace('.', '-')
        pathstore[name] = value
        
      n["Config"].pop("Path", "")
      n["Config"]["Path"] = pathstore
      


      if ( "Networking" in n.keys() and n["Networking"] ) and isinstance(n["Networking"], dict) and ( "Publish" in n["Networking"].keys() and n["Networking"]["Publish"] and isinstance(n["Networking"]["Publish"], dict) ) and ( "Port" in n["Networking"]["Publish"].keys() and n["Networking"]["Publish"]["Port"] ):
        if isinstance(n["Networking"]["Publish"]["Port"], dict):
          store = n["Networking"]["Publish"]["Port"]
          n["Networking"]["Publish"].pop("Port", "")
          n["Networking"]["Publish"]["Port"] = [store]
        if isinstance(n["Networking"]["Publish"]["Port"], list):
          for index, var in enumerate(n["Networking"]["Publish"]["Port"]):
            if "Mode" in var.keys() and var["Mode"]:
              var["Mode"] = var["Mode"]
            elif "Protocol" in var.keys() and var["Protocol"]:
              var["Mode"] = var["Protocol"]
            else:
              var["Mode"] = "tcp"
            if not "Name" in var.keys():
              var["Name"] = var["Mode"]+"-port-"+str(index)
            label = var["Name"].lower()
            for char in invalid:
              label = label.replace(char, '')
            label = label.replace('.', '-')
            n["Config"]["Port"][label] = {}
            n["Config"]["Port"][label] = var
            if "ContainerPort" in n["Config"]["Port"][label].keys() and n["Config"]["Port"][label]["ContainerPort"]:
              n["Config"]["Port"][label]["Target"] = n["Config"]["Port"][label]["ContainerPort"]
            if "HostPort" in n["Config"]["Port"][label].keys() and n["Config"]["Port"][label]["HostPort"]:
              n["Config"]["Port"][label]["value"] = n["Config"]["Port"][label]["HostPort"]

      
      n.pop("Networking", "")
      
      cleanedPorts = {}
      for name, value in n["Config"]["Port"].items():
        goodTarget = False
        goodvalue = False
        
        name = name.lower()
        for char in invalid:
          name = name.replace(char, '')
        
        name = re.sub('udp[\d]-', '', name)
        name = re.sub('tcp[\d]-', '', name)
        name = re.sub(tmp+'-', '', name)
        name = textwrap.shorten(name, 14, placeholder='')
        
        if "value" in value.keys() and value["value"]:
          cleanTarget0 = value["value"].split("-")[0]
          try:
            value["value"] = int(cleanTarget0)
            goodvalue = True
          except:
            value.pop("value", "")
            goodvalue = False
        
        if "value" not in value.keys() or not value["value"]:
          if "Default" in value.keys() and not value["Default"]:
            try:
              value["value"] = int(value["Default"])
            except:
              continue
            
          elif "Target" in value.keys() and value["Target"]:
            try:
              value["value"] = int(value["Target"])
            except:
              continue
        
        if "Target" in value.keys() and value["Target"]:
          cleanTarget2 = value["Target"].split("-")[0]
          try:
            value["Target"] = int(cleanTarget2)
            goodTarget = True
          except:
            value.pop("Target", "")
            goodTarget = False

            
        if goodTarget or goodvalue:
          cleanedPorts[name] = value
          

      n["Config"]["Port"] = cleanedPorts

      
      portstore = {}
      ## TODO flag expected main container
      mainport = ""
      if "WebUI" in n.keys() and n["WebUI"] and "[PORT:"  in n["WebUI"]:
        stripped = n["WebUI"].split("[PORT:", 1)[1]
        stripped = stripped.split("]/", 1)[0]
        for char in invalid:
          mainport = stripped.replace(char, '')
        mainport = ''.join(filter(str.isdigit, mainport))
        mainport = int(mainport)
      for name, value in n["Config"]["Port"].items():
        store = value
        mainset = False
        
        if len(n["Config"]["Port"]) == 1:
          name = "main"
        elif mainport and "Target" in value.keys() and value["Target"] == mainport:     
          name = "main"
          value["Mode"] = 'HTTP'

        name = name.lower()
        name = name.replace('.', '')
        name = name.replace('-', '')
        for char in invalid:
          name = name.replace(char, '')
        name = re.sub(tmp+'-', '', name)
        name = name.replace('.', '')
        name = name.replace('-', '')
        portstore[name] = value
      n["Config"].pop("Port", "")
      n["Config"]["Port"] = portstore
      
      globals()['%s' % tmp] = n
      
      combined[tmp] = n
      if "Requires" in n.keys() and n["Requires"]:
        print:("")
        ## Can be enabled when we actually need this data
        combinedreq[tmp] = n
        # jsonString = json.dumps(n)
        # jsonFile = open("apps/"+"req/"+"json/"+tmp+".json", "w")
        # jsonFile.write(jsonString)
        # jsonFile.close()
        # 
        # yamlString = yaml.dump(n)
        # yamlFile = open("apps/"+"req/"+"yaml/"+tmp+".yaml", "w")
        # yamlFile.write(yamlString)
        # yamlFile.close()
      else:
        ## Can be enabled when we actually need this data
        combinedfree[tmp] = n
        # jsonString = json.dumps(n)
        # jsonFile = open("apps/"+"json/"+tmp+".json", "w")
        # jsonFile.write(jsonString)
        # jsonFile.close()
        
        yamlString = yaml.dump(n)
        yamlFile = open("apps/"+"yaml/"+tmp+".yaml", "w")
        yamlFile.write(yamlString)
        yamlFile.close()
    
print("Writhing combined json and yaml output...")

## Can be enabled when we actually need this data
# jsonString2 = json.dumps(combinedfree)
# jsonFile2 = open("apps-free.json", "w")
# jsonFile2.write(jsonString2)
# jsonFile2.close()

yamlString2 = yaml.dump(combinedfree)
yamlFile2 = open("apps-free.yaml", "w")
yamlFile2.write(yamlString2)
yamlFile2.close()

## Can be enabled when we actually need this data
# jsonString3 = json.dumps(combinedreq)
# jsonFile3 = open("apps-req.json", "w")
# jsonFile3.write(jsonString3)
# jsonFile3.close()
# 
# yamlString3 = yaml.dump(combinedreq)
# yamlFile3 = open("apps-req.yaml", "w")
# yamlFile3.write(yamlString3)
# yamlFile3.close()

## Can be enabled when we actually need this data
# jsonString4 = json.dumps(combined)
# jsonFile4 = open("apps.json", "w")
# jsonFile4.write(jsonString4)
# jsonFile4.close()
# 
# yamlString4 = yaml.dump(combined)
# yamlFile4 = open("apps.yaml", "w")
# yamlFile4.write(yamlString4)
# yamlFile4.close()

print("Loading Helm Chart Defaults...")

chartsyaml = {}
questionsyaml = {}
valuesyaml = {}

fileObject = open("example/Chart.json", "r")
jsonContent = fileObject.read()
chartsyaml = json.loads(jsonContent)

fileObject = open("example/values.json", "r")
jsonContent = fileObject.read()
valuesyaml = json.loads(jsonContent)

chartsyaml["annotations"].pop("truecharts.org/catagories", "")
chartsyaml["annotations"]["truecharts.org/catagories"] = []

print("building Helm Charts...")
for name, app in combinedfree.items():
  appchartyaml = chartsyaml
  tmpname = app["Name"]
  
  for char in invalid:
    tmpname = tmpname.replace(char, '')
    
  print(tmpname)

  os.mkdir("./export/"+"app/"+tmpname)
  os.mkdir("./export/"+"images/"+tmpname)

  # Handle Image Mirror
  
  shutil.copyfile('./example/Dockerfile', "./export/"+"images/"+tmpname+"/Dockerfile")
  shutil.copyfile('./example/PLATFORM', "./export/"+"images/"+tmpname+"/PLATFORM")
  
  with open("./export/"+"images/"+tmpname+"/Dockerfile", "r") as f:
      lines = f.readlines()
  with open("./export/"+"images/"+tmpname+"/Dockerfile", "w") as f:
      for line in lines:
          if "example" in line:
            line = "FROM "+app["Repository"]+":"+app["Tag"]
            f.write(line+"\n")
          else:
            f.write(line)
  
  # Handle icon
  
  try:
    url = app["Icon"]
    r = requests.get(url, allow_redirects=True)

    open("./export/"+"app/"+tmpname+"/icon.png", 'wb').write(r.content)
  except:
    continue
    
  # readme.md
  
  open("./export/"+"app/"+tmpname+"/readme.md", mode='a').close()
  
  # Handle helmingore
  
  shutil.copyfile('./example/.helmignore', "./export/"+"app/"+tmpname+"/.helmignore")
  
  # Handle common template
  
  os.mkdir("./export/"+"app/"+tmpname+"/templates")
  shutil.copyfile('./example/common.yaml', "./export/"+"app/"+tmpname+"/templates/common.yaml")
  
  # Handle Chart.yaml
  
  appchartyaml["name"] = tmpname
  appchartyaml["annotations"]["truecharts.org/catagories"] = app["CategoryList"]
  appchartyaml["description"] = app["Overview"]
  appchartyaml["sources"] = app["Sources"]
  appchartyaml["keywords"] = app["Keywords"]
  appchartyaml["home"] = "https://github.com/truecharts/apps/tree/master/charts/stable/"+tmpname
  appchartyaml["icon"] = "https://truecharts.org/img/chart-icons/"+tmpname+".png"
  

  appyamlString = yaml.dump(appchartyaml)
  appyamlFile = open("./export/"+"app/"+tmpname+"/Chart.yaml", "w")
  appyamlFile.write(appyamlString)
  appyamlFile.close()
  
  with open("./export/"+"app/"+tmpname+"/Chart.yaml", "r") as f:
      lines2 = f.readlines()
  with open("./export/"+"app/"+tmpname+"/Chart.yaml", "w") as f:
      for line in lines2:
          if line.strip("\n") == "  truecharts.org/catagories:":
            f.write("  truecharts.org/catagories: |\n")
          elif "  - " in line:
            f.write("  "+line)
          else:
              f.write(line)
  
  # Handle values.yaml
  
  appvaluesyaml = valuesyaml
  if genTCCR:
    appvaluesyaml["image"]["repository"] = "tccr.io/truecharts/"+name
  else:
    appvaluesyaml["image"]["repository"] = app["Repository"]

  repoList = app["Repository"].split("/")
  if genTCCR and len(repoList) == 2 and repoList[1]  == "steamcmd":
    appvaluesyaml["image"]["tag"] = "latest"
  else:
    appvaluesyaml["image"]["tag"] = app["Tag"]
  
  appvaluesyaml["env"] = {}
  
  for name, value in app["Config"]["Variable"].items():
    if name and name in puidcheck:
      puidflag = True
    if value["Target"] in puidcheck:
      puidflag = True
    if not name in blacklistedenvs and not value["Target"] in blacklistedenvs:
      appvaluesyaml["env"][value["Target"]] = value["value"]

  appvaluesyaml["securityContext"] = {}
  appvaluesyaml["podSecurityContext"] = {}
  if puidflag:
    appvaluesyaml["securityContext"]["readOnlyRootFilesystem"] = False
    appvaluesyaml["securityContext"]["runAsNonRoot"] = False
    appvaluesyaml["podSecurityContext"]["runAsUser"] = 0
    appvaluesyaml["podSecurityContext"]["runAsGroup"] = 0

  privflag = False
  if "Privileged" in app["Config"].keys() and app["Config"]["Privileged"] and ( app["Config"]["Privileged"] == 'true' or app["Config"]["Privileged"] == 'True' or app["Config"]["Privileged"] == True ):
    appvaluesyaml["securityContext"]["privileged"] = True
    privflag = True
    
  if "PostArgs" in app["Config"].keys() and app["Config"]["PostArgs"]:
    appvaluesyaml["args"] = [app["Config"]["PostArgs"]]

  appvaluesyaml["persistence"] = {}
  for name, value in app["Config"]["Path"].items():
    appvaluesyaml["persistence"][name] = {}
    appvaluesyaml["persistence"][name]["mountPath"] = value["Target"]
    appvaluesyaml["persistence"][name]["enabled"] = True
    if "Mode" in value.keys() and value["Mode"] and value["Mode"] == "ro":
      appvaluesyaml["persistence"][name]["readOnly"] = True
      
  appvaluesyaml["service"] = {}
  
  if len(app["Config"]["Port"]) == 0:
    appvaluesyaml["service"]["main"] = {}
    appvaluesyaml["service"]["main"]["enabled"] = False
    appvaluesyaml["service"]["main"]["ports"] = {}
    appvaluesyaml["service"]["main"]["ports"]["main"] = {}
    appvaluesyaml["service"]["main"]["ports"]["main"]["enabled"] = False
    
  else:
    for name, value in app["Config"]["Port"].items():
      appvaluesyaml["service"][name] = {}
      appvaluesyaml["service"][name]["enabled"] = True
    
      appvaluesyaml["service"][name]["ports"] = {}
      appvaluesyaml["service"][name]["ports"][name] = {}
      appvaluesyaml["service"][name]["ports"][name]["enabled"] = True
      appvaluesyaml["service"][name]["ports"][name]["protocol"] = value["Mode"].upper()
      if "value" in value.keys() and value["value"]:
        appvaluesyaml["service"][name]["ports"][name]["port"] = value["value"]
      else:
        appvaluesyaml["service"][name]["ports"][name]["port"] = value["Target"]
      if "Target" in value.keys() and value["Target"]:
        appvaluesyaml["service"][name]["ports"][name]["targetPort"] = value["Target"]
      else: 
        appvaluesyaml["service"][name]["ports"][name]["targetPort"] = value["value"]
        
  if "main" not in  appvaluesyaml["service"].keys() or not appvaluesyaml["service"]["main" ]:
      placeholder = next(iter(appvaluesyaml["service"]))
      appvaluesyaml["service"]["main"] = appvaluesyaml["service"][placeholder]
      appvaluesyaml["service"]["main"]["ports"]["main"] = appvaluesyaml["service"][placeholder]["ports"][placeholder]
      appvaluesyaml["service"]["main"]["ports"].pop(placeholder, "")
      appvaluesyaml["service"].pop(placeholder, "")
      
        
  if  "main" not in  appvaluesyaml["service"].keys() or not appvaluesyaml["service"]["main" ]:
    raise Exception("App does not have a main port set: "+app["Name"] )

  setcustom = ""
  if appvaluesyaml["service"]["main"]["enabled"] is False:
    appvaluesyaml["probes"] = {}
    appvaluesyaml["probes"]["liveness"] = {}
    appvaluesyaml["probes"]["readiness"] = {}
    appvaluesyaml["probes"]["startup"] = {}
    appvaluesyaml["probes"]["liveness"]["enabled"] = False
    appvaluesyaml["probes"]["readiness"]["enabled"] = False
    appvaluesyaml["probes"]["startup"]["enabled"] = False
  elif "protocol" in  appvaluesyaml["service"]["main"]["ports"]["main"].keys() and appvaluesyaml["service"]["main"]["ports"]["main"]["protocol"] == "UDP":
    appvaluesyaml["probes"] = {}
    appvaluesyaml["probes"]["liveness"] = {}
    appvaluesyaml["probes"]["readiness"] = {}
    appvaluesyaml["probes"]["startup"] = {}
    appvaluesyaml["probes"]["liveness"]["enabled"] = False
    appvaluesyaml["probes"]["readiness"]["enabled"] = False
    appvaluesyaml["probes"]["startup"]["enabled"] = False
    for name, value in appvaluesyaml["service"].items():
      if "protocol" in  appvaluesyaml["service"][name]["ports"][name].keys():
        if not appvaluesyaml["service"][name]["ports"][name]["protocol"] == "UDP":
          setcustom = name
          break
      else:
        setcustom = name
        break
        
  else:
    appvaluesyaml.pop("probes", "")


  if setcustom:
    appvaluesyaml.pop("probes", "")
    appvaluesyaml["probes"] = {}
    appvaluesyaml["probes"]["liveness"] = {}
    appvaluesyaml["probes"]["readiness"] = {}
    appvaluesyaml["probes"]["startup"] = {}
    appvaluesyaml["probes"]["liveness"]["port"] = '{{ .Values.service.'+setcustom+'.ports.'+setcustom+'.targetPort }}'
    appvaluesyaml["probes"]["readiness"]["port"] = '{{ .Values.service.'+setcustom+'.ports.'+setcustom+'.targetPort }}'
    appvaluesyaml["probes"]["startup"]["port"] = '{{ .Values.service.'+setcustom+'.ports.'+setcustom+'.targetPort }}'

  appvaluesyamlString = yaml.dump(appvaluesyaml)
  appvaluesyamlFile = open("./export/"+"app/"+tmpname+"/values.yaml", "w")
  appvaluesyamlFile.write(appvaluesyamlString)
  appvaluesyamlFile.close()
  
  # Handle Questions.yaml
  
  
  with open("./example/questions1-no-portal.yaml", "r") as f:
      questions1noportal = f.readlines()
  with open("./example/questions1-portal.yaml", "r") as f:
      questions1portal = f.readlines()
  with open("./example/questions2.yaml", "r") as f:
      questions2 = f.readlines()
  with open("./example/questions2-service.yaml", "r") as f:
      questions2service = f.readlines()
  with open("./example/questions3.yaml", "r") as f:
      questions3 = f.readlines()
  with open("./example/questions4.yaml", "r") as f:
      questions4 = f.readlines()
  with open("./example/questions4-persistence.yaml", "r") as f:
      questions4persistence = f.readlines()
  with open("./example/questions5.yaml", "r") as f:
      questions5 = f.readlines()
  with open("./example/questions6.yaml", "r") as f:
      questions6 = f.readlines()
  with open("./example/questions7.yaml", "r") as f:
      questions7 = f.readlines()
  with open("./example/questions-env.yaml", "r") as f:
      questionsenv = f.readlines()
  with open("./example/questions-env-fixed.yaml", "r") as f:
      questionsenvfixed = f.readlines()
  with open("./export/"+"app/"+tmpname+"/questions.yaml", "w") as f:
      if not appvaluesyaml["service"]["main"]["enabled"]:
        for line in questions1noportal:
          f.write(line)
      else:
        for line in questions1portal:
          f.write(line)
      f.write("\n")
      if len(valuesyaml["env"]) != 0:
        for line in questionsenvfixed:
          f.write(line)
        f.write("\n")
        for name, value in appvaluesyaml["env"].items():
          for line in questionsenv:
            if "PLACEHOLDERNAME" in line:
              f.write("        - variable: "+name+"\n")
            elif "PLACEHOLDERLABEL" in line:
              f.write("          label: '"+name+"'\n")
            elif "PLACEHOLDERDESCRIPTION" in line:
              for name2, value2  in app["Config"]["Variable"].items():
                if value2["Target"] == name and "Description" in  value2.keys() and value2["Description"]:
                  try:
                    desc = value2["Description"]
                    desc = desc.replace("\r\n", '')
                    desc = desc.replace("\n", '')
                    desc = desc.replace("'", '')
                    for char in invalidtext:
                      desc = desc.replace(char, '')
                    desc = desc.encode("utf-8").decode("utf-8")
                    f.write('          description: "'+desc+'"\n')
                  except:
                    pass
                  break
            elif "PLACEHOLDERVALUE" in line:
              f.write('            default: "'+value+'"\n')
            else:
              f.write(line)
      f.write("\n")
      if appvaluesyaml["service"]["main"]["enabled"]:
        for line in questions2:
          if "PLACEHOLDERPORTPORT" in line:
            f.write("                              default: "+str(valuesyaml["service"]["main"]["ports"]["main"]["port"])+"\n")
          elif "PLACEHOLDERPORTMODE" in line:
            f.write("                                    default: "+str(valuesyaml["service"]["main"]["ports"]["main"]["protocol"])+"\n")
          elif "PLACEHOLDERPORTTARGET" in line:
            f.write("                                    default: "+str(valuesyaml["service"]["main"]["ports"]["main"]["targetPort"])+"\n")
          else:
            f.write(line)
        f.write("\n")
        for name, value in appvaluesyaml["service"].items():
          if name != "main":
            for line in questions2service:
              if "PLACEHOLDERSVCNAME" in line:
                f.write("        - variable: "+name+"\n")
              elif "PLACEHOLDERSVCLABEL" in line:
                f.write("          label: '"+name+" service'\n")
              elif "PLACEHOLDERDESCRIPTION" in line:
                for name2, value2  in app["Config"]["Port"].items():
                  if name2 == name and "Description" in  value2.keys() and value2["Description"]:
                    try:
                      desc = value2["Description"]
                      desc = desc.replace("\r\n", '')
                      desc = desc.replace("\n", '')
                      for char in invalidtext:
                        desc = desc.replace(char, '')
                      desc = desc.replace("'", '')
                      desc = desc.encode("utf-8").decode("utf-8")
                      f.write('          description: "'+desc+'"\n')
                    except:
                      pass
                    break
              elif "PLACEHOLDERPORTNAME" in line:
                f.write("                    - variable: "+name+"\n")
              elif "PLACEHOLDERPORTLABEL" in line:
                f.write('                      label: "'+name+' Service Port Configuration"\n')
              elif "PLACEHOLDERPORTPORT" in line:
                f.write("                              default: "+str(valuesyaml["service"][name]["ports"][name]["port"])+"\n")
              elif "PLACEHOLDERPORTMODE" in line:
                f.write("                                    default: "+str(valuesyaml["service"][name]["ports"][name]["protocol"])+"\n")
              elif "PLACEHOLDERPORTTARGET" in line:
                f.write("                                    default: "+str(valuesyaml["service"][name]["ports"][name]["targetPort"])+"\n")
              else:
                f.write(line)
        f.write("\n")
      f.write("\n")
      for line in questions3:
        f.write(line)
      f.write("\n")
      if len(valuesyaml["persistence"]) != 0:
        for line in questions4:
          f.write(line)
        f.write("\n")
        for name, value in appvaluesyaml["persistence"].items():
          for line in questions4persistence:
            if "PLACEHOLDERDESCRIPTION" in line:
              for name2, value2  in app["Config"]["Path"].items():
                    if name2 == name and "Description" in  value2.keys() and value2["Description"]:
                      try:
                        desc = value2["Description"]
                        desc = desc.replace("\r\n", '')
                        desc = desc.replace("\n", '')
                        for char in invalidtext:
                          desc = desc.replace(char, '')
                        desc = desc.replace("'", '')
                        desc = desc.encode("utf-8").decode("utf-8")
                        f.write('          description: "'+desc+'"\n')
                      except:
                        pass
                      break
            elif "PLACEHOLDERVAR" in line:
              f.write("        - variable: "+name+"\n")
            elif "PLACEHOLDERLABEL" in line:
              f.write('          label: "'+name+' Storage"\n')
            else:
              f.write(line)
        f.write("\n")
      f.write("\n")
      for line in questions5:
        f.write(line)
      f.write("\n")
      if appvaluesyaml["service"]["main"]["enabled"]:
        for line in questions6:
          f.write(line)
      f.write("\n")
      for line in questions7:
        if puidflag and "runAsGroupExample" in line:
          f.write("            default: 0\n")
        elif puidflag and  "runAsUserExample" in line:
          f.write("            default: 0\n")
        elif privflag and  "privilegedExample" in line:
          f.write("                  default: true\n")
        elif puidflag and  "runAsNonRootExample" in line:
          f.write("                  default: false\n")
        elif puidflag and  "readOnlyRootFilesystemExample" in line:
          f.write("                  default: false\n")
        elif "runAsGroupExample" in line:
          f.write("            default: 568\n")
        elif "runAsUserExample" in line:
          f.write("            default: 568\n")
        elif "privilegedExample" in line:
          f.write("                  default: false\n")
        elif "runAsNonRootExample" in line:
          f.write("                  default: true\n")
        elif "readOnlyRootFilesystemExample" in line:
          f.write("                  default: true\n")
        else:
          f.write(line)
      f.write("\n")
  appvaluesyaml = {}
  