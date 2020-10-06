global writera
writera = open("speedrunsimplified.txt", "a")
import requests
from datetime import datetime, timedelta
overallcounter = 0
global content
global setence
global aditionalcounter
global startercounter
global counter
global startercounter1
global aditionalcounter1
def ForceToWrite(staa):
  writera.write(staa)
def Runner():
  if content[counter - 7:counter] == '{"id":"':
   startercounter = counter
   aditionalcounter = counter
   while not content[aditionalcounter] == '"':
     aditionalcounter = aditionalcounter + 1
   setence = "Run ID: "
   ForceToWrite(setence + content[startercounter:aditionalcounter])
   SetCounter(aditionalcounter)
  if content[counter - 8:counter] == '"game":"':
    startercounter = counter
    aditionalcounter = PlusOneCounter
    while not content[aditionalcounter] == '"':
      aditionalcounter = aditionalcounter + 1
    setence = " Game ID: "
    ForceToWrite(setence + content[startercounter:aditionalcounter])
    SetCounter(aditionalcounter)
  if content[counter - 12:counter] == '"category":"':
    startercounter = counter
    aditionalcounter = PlusOneCounter
    while not content[aditionalcounter] == '"':
      aditionalcounter = aditionalcounter + 1
    setence = " Category ID: "
    ForceToWrite(setence + content[startercounter:aditionalcounter])
    SetCounter(aditionalcounter)
def TextOrUri():
  if bootler == "b":
    if content[aditionalcounter - 7:aditionalcounter] == '"uri":"':
      SetAditionalCounter(aditionalcounter - 1)
    while not content[aditionalcounter - 7:aditionalcounter] == '"uri":"': 
      SetAditionalCounter(aditionalcounter + 1)
      if content[aditionalcounter:aditionalcounter + 8] == '"text":"':
        startercounter1 = aditionalcounter
        aditionalcounter1 = aditionalcounter
        SetBoonala("a")
        while boonala == "a":
          aditionalcounter1 = aditionalcounter1 + 1
          if content[aditionalcounter1:aditionalcounter1 + 2] == '",':
            SetBoonala("b")
        setence = " Video Text: "
        ForceToWrite(setence + content[startercounter1 + 1:aditionalcounter1])
def StarterVideo():
  if content[counter] == '"':
    SetBootler("b")
def Simplify():
  if content[aditionalcounter] == '"':
    SetAditionalCounter(aditionalcounter + 1)
    SetBoonalraa("b")
def Runnerx():
  if content[counter - 9:counter] == '"videos":':
    aditionalcounter = counter
    SetBootler("a")
    StarterVideo()
    TextOrUri()
    SetAditionalCounter(aditionalcounter)
    Simplify()
    startercounter = aditionalcounter
    SetBoonala("a")
    while boonala == "a":
      aditionalcounter = aditionalcounter + 1
      if content[aditionalcounter] == '"':
        SetBoonala("b")
      if content[aditionalcounter:aditionalcounter + 2] == ',"':
        SetBoonala("b")
    if bootler == "b":
      setence = " Video URL: "
      ForceToWrite(setence + content[startercounter:aditionalcounter])
    else:
      setence = " No Video URL"
      ForceToWrite(setence)
    SetCounter(aditionalcounter)
  if content[counter - 10:counter] == '"comment":':
    aditionalcounter = PlusOneCounter
    SetBootler("a")
    if content[counter] == '"':
      aditionalcounter = aditionalcounter + 1
    startercounter = aditionalcounter
    while bootler == "a":
      aditionalcounter = aditionalcounter + 1
      if content[aditionalcounter:aditionalcounter + 2] == ',"':
        SetBootler("b")
      if content[aditionalcounter:aditionalcounter + 2] == '",':
        SetBootler("b")
    if not content[startercounter:aditionalcounter] == "null":
      setence = " Comment: "
      ForceToWrite(setence + content[startercounter:aditionalcounter] + " ")
    SetCounter(aditionalcounter)
  if content[counter - 20:counter] == '"status":{"status":"':
    startercounter = counter
    aditionalcounter = PlusOneCounter
    while not content[aditionalcounter] == '"':
      aditionalcounter = aditionalcounter + 1
    ForceToWrite(" " + content[startercounter:aditionalcounter])
    SetCounter(aditionalcounter)
def SetBoonala(star):
  global boonala
  boonala = star
def SetBootler(saa):
  global bootler
  bootler = saa
def OrientalRunner():
  if content[counter - 10:counter] == 'examiner":':
    aditionalcounter = PlusOneCounter
    SetBootler("a")
    if content[counter] == '"':
      aditionalcounter = aditionalcounter + 1
    startercounter = aditionalcounter
    while bootler == "a":
      aditionalcounter = aditionalcounter + 1
      if content[aditionalcounter] == ',':
        SetBootler("b")
      if content[aditionalcounter] == '"':
        SetBootler("b")
    if not content[startercounter:aditionalcounter] == "null":
     setence = " Eaxminer ID: "
     ForceToWrite(setence + content[startercounter:aditionalcounter])
     SetCounter(aditionalcounter)
    else:
     setence = " No Examiner"
     ForceToWrite(setence)
     SetCounter(aditionalcounter)
  if content[counter - 14:counter] == '"verify-date":':
    aditionalcounter = PlusOneCounter
    SetBootler("a")
    if content[counter] == '"':
      aditionalcounter = aditionalcounter + 1
    startercounter = aditionalcounter
    while bootler == "a":
      aditionalcounter = aditionalcounter + 1
      if content[aditionalcounter] == ',':
        SetBootler("b")
      if content[aditionalcounter] == '"':
        SetBootler("b")
    if not content[startercounter:aditionalcounter] == "null}":
     setence = " Verify Date: "
     ForceToWrite(setence + content[startercounter:aditionalcounter])
     SetCounter(aditionalcounter)
    else:
     setence = " No Verify Date"
     ForceToWrite(setence)
     SetCounter(aditionalcounter)
def Runnery():
  if content[counter - 10:counter] == '"players":':
    aditionalcounter = PlusOneCounter
    setence = " Players: "
    boonal = "a"
    SetBoonala("a")
    ForceToWrite(setence)
    while boonala == "a":
     if boonala == "a":
       boonal = "a"
     while boonal == "a":
       aditionalcounter = aditionalcounter + 1
       if content[aditionalcounter - 6:aditionalcounter] == '"id":"':
         boonal = "b"
       if content[aditionalcounter - 8:aditionalcounter] == '"name":"':
         boonal = "b"
       if content[aditionalcounter - 2:aditionalcounter] == "],":
         SetBoonala("b")
         boonal = "b"
     startercounter = aditionalcounter
     if boonala == "a":
      aditionalcounter = aditionalcounter + 1
      while not content[aditionalcounter] == '"':
        aditionalcounter = aditionalcounter + 1
      ForceToWrite(content[startercounter:aditionalcounter] + " ")
    SetCounter(aditionalcounter)
def WritePlatform():
  if not content[startercounter:aditionalcounter] == "null,":
    setence = " Platform: "
    ForceToWrite(setence + content[startercounter:aditionalcounter])
  else:
    setence = " No Platform"
    ForceToWrite(setence)
def SetAditionalCounter(zan):
   global aditionalcounter
   aditionalcounter = zan
def UpdateStarterCounter():
  SetStarterCounter(aditionalcounter)
def Defreshrate():
  if content[aditionalcounter] == '"':
    SetAditionalCounter(aditionalcounter + 1)
  UpdateStarterCounter()
  while not content[aditionalcounter] == '"':
    SetAditionalCounter(aditionalcounter + 1)
def Isitemulated():
  setence = ""
  if content[startercounter:aditionalcounter] == "false":
    setence = " Not Emulated"
  else:
    setence = " Emulated"
  ForceToWrite(setence)
def RegionCounter():
  SetStarterCounter(aditionalcounter)
  while not content[aditionalcounter] == '}':
    SetAditionalCounter(aditionalcounter + 1)
def LongestCode():
  if content[counter - 9:counter] == '"system":':
    global aditionalcounter
    global setence
    global startercounter
    aditionalcounter = PlusOneCounter
    while not content[aditionalcounter - 11:aditionalcounter] == '"platform":':
      aditionalcounter = aditionalcounter + 1
    Defreshrate()
    WritePlatform()
    while not content[aditionalcounter - 10:aditionalcounter] == 'emulated":':
      aditionalcounter = aditionalcounter + 1
    if content[aditionalcounter] == '"':
      aditionalcounter = aditionalcounter + 1
    startercounter = aditionalcounter
    while not content[aditionalcounter] == ',':
      aditionalcounter = aditionalcounter + 1
    Isitemulated()
    while not content[aditionalcounter - 8:aditionalcounter] == 'region":':
      SetAditionalCounter(aditionalcounter + 1)
    if not content[aditionalcounter] == '"':
      SetAditionalCounter(aditionalcounter)
    else:
      SetAditionalCounter(aditionalcounter + 1)        
    RegionCounter()
    if content[aditionalcounter - 1] == '"':
      aditionalcounter = aditionalcounter - 1
    if not content[startercounter:aditionalcounter] == "null":
      setence = " Region ID: "
      ForceToWrite(setence + content[startercounter:aditionalcounter])
    else:
      setence = " No Region"
      ForceToWrite(setence)
    while not content[aditionalcounter - 9:aditionalcounter] == '"splits":':
      aditionalcounter = aditionalcounter + 1
    if not content[aditionalcounter:aditionalcounter + 4] == "null":
      while not content[aditionalcounter - 7:aditionalcounter] == '"uri":"':
        aditionalcounter = aditionalcounter + 1
      startercounter = aditionalcounter
      while not content[aditionalcounter] == '"':
        aditionalcounter = aditionalcounter + 1
      setence = " Splits URL: "
      ForceToWrite(setence + content[startercounter:aditionalcounter])
    else:
      setence = " No Splits"
      ForceToWrite(setence)
      SetAditionalCounter(aditionalcounter + 4)
    SetCounter(aditionalcounter)
def Runnerz():
  if content[counter - 8:counter] == '"date":"':
    startercounter = counter
    aditionalcounter = PlusOneCounter
    while not content[aditionalcounter] == ',':
      aditionalcounter = aditionalcounter + 1
    if content[aditionalcounter - 1] == '"':
      aditionalcounter = aditionalcounter - 1
    if not content[startercounter:aditionalcounter] == "null,":
      setence = " Date: "
      ForceToWrite(setence + content[startercounter:aditionalcounter])
    else:
      setence = " No Date "
      ForceToWrite(setence)
    SetCounter(aditionalcounter)
  if content[counter - 12:counter] == '"primary_t":':
    startercounter = counter
    aditionalcounter = PlusOneCounter
    while not content[aditionalcounter] == ',':
      aditionalcounter = aditionalcounter + 1
    setence = " Time in Seconds: "
    ForceToWrite(setence + content[startercounter:aditionalcounter])
    SetCounter(aditionalcounter)
  LongestCode()
def SetBoonalraa(seter):
  global boonalraa
  boonalraa = seter
def Runnera():
  if content[counter - 8:counter] == 'values":':
    aditionalcounter = counter
    boonalr = "a"
    SetBoonalraa("a")
    setence = " Values ID: "
    if content[counter] == '{':
      SetAditionalCounter(aditionalcounter - 1)
    if not content[counter:counter + 4] == "null":
      ForceToWrite(setence)
    if content[counter] == '"':
      SetAditionalCounter(aditionalcounter - 1)
    if content[counter] == ':':
      SetAditionalCounter(aditionalcounter - 1)
    if not content[counter:counter + 4] == "null":
     while boonalraa == "a":
      boonalr = "a"
      while boonalr == "a":
       aditionalcounter = aditionalcounter + 1
       if content[aditionalcounter - 2:aditionalcounter] == '},':
          SetBoonalraa("b")
          boonalr = "b"
       if content[aditionalcounter] == '"':
          boonalr = "b"
      if boonalraa == "a":
        startercounter = aditionalcounter
        aditionalcounter = aditionalcounter + 1
        while not content[aditionalcounter] == '"':
          aditionalcounter = aditionalcounter + 1
        ForceToWrite(content[startercounter + 1:aditionalcounter] + " ")
    if content[counter:counter + 4] == "null":
      setence = " No Values"
      ForceToWrite(setence)
    SetCounter(aditionalcounter)
    ForceToWrite("\n")
def SetCounter(counters):
  global counter 
  counter = counters
def SetPlusOneCounter(PlusOneCounters):
  global PlusOneCounter
  PlusOneCounter = PlusOneCounters
def SetStarterCounter(startercounters):
  global startercounter
  startercounter = startercounters
SetCounter(-1)
SetPlusOneCounter(-1)
runcounter = 0
aditionalcounter = 0
maximumurlcounter = 500
calculatemaximumsize = 0
OverallStartTime = datetime.now()
urlcounter = 0
while urlcounter < maximumurlcounter:
 ReadStarttime = datetime.now()
 url = "https://www.speedrun.com/api/v1/runs?max=201&status=verified&offset=" + str(urlcounter)
 r = requests.get(url)
 content = r.text
 lengther = len(content)
 maximumsize = lengther + 1
 calculatemaximumsize = calculatemaximumsize + lengther
 while counter < maximumsize:
   SetPlusOneCounter(counter + 1)
   SetCounter(PlusOneCounter)
   Runner()
   Runnerx()
   OrientalRunner()
   Runnery()
   Runnerz()
   Runnera()
 percentagecounter = (urlcounter / maximumurlcounter) * 100
 FinishTimer1 = datetime.now() - ReadStarttime
 FinishTimer2 = datetime.now() - OverallStartTime
 timeremaininger = ""
 timeremaining = ""
 pt = datetime.strptime(str(FinishTimer1),'%H:%M:%S.%f')
 converttoseconds = pt.microsecond/1000000 + pt.second + pt.minute*60 + pt.hour*3600
 calculator = ((maximumurlcounter - urlcounter) / 200) * converttoseconds
 timeremaininger = timedelta(seconds=calculator)
 timeremaining = str(timeremaininger)
 print(str(FinishTimer1) + " " + str(FinishTimer2) + " " + str(counter) + " " + str(percentagecounter) + "%  Estimated Time Remaining: " + str(timeremaining) + " File Size: " + str(lengther) + " Total File Size: " + str(calculatemaximumsize) + " Current: " + str(urlcounter))
 urlcounter = urlcounter + 200
 writera.flush()
 SetCounter(-1)
writera.close()
print("Finished Simplifing in: " + str(FinishTimer2))