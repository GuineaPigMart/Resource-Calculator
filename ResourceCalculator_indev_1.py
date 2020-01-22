#version indev_1

print("version: indev_1")
print("Note: for this to work you need the reactor .json in the same map as this program.")
print("Select a reactor by typing in the exact name:")


reactor = input()
reactorFile = open(reactor, "r")


reactorFileArray =  []

for line in reactorFile:
    reactorFileArray.append(line.rstrip("\n"))

reactorFileLen = len(reactorFileArray)

foundInLine = -1

for i in range(reactorFileLen):
    if (reactorFileArray[i].find("InteriorDimensions")) > 0:
        foundInLine = i

dimensions = reactorFileArray[foundInLine]
dimensions = dimensions.strip()
dimensions = list(dimensions)
dimensions.pop()
dimensionsNew = []

for i in range(len(dimensions)):
    string = dimensions[i]
    if string.isdigit():
        dimensionsNew.append(string)
    if string.endswith(","):
        dimensionsNew.append(string)

dimensions = ""

for i in range(len(dimensionsNew)):
    dimensions = dimensions + dimensionsNew[i]

dimensioneNew = []

dimensionsNew = dimensions.split(",")

x = int(dimensionsNew[0])
y = int(dimensionsNew[1])
z = int(dimensionsNew[2])

casings = (x*y*2) + (x*z*2) + (z*y*2)

casingsComp = casings // 4

if casingsComp*4 < casings:
    casingsComp = casingsComp + 1


#coolerCalcs

insideReactorNames = ["FuelCell","Water","Redstone","Quartz","Gold","Glowstone",
                      "Lapis","Diamond","Helium","Enderium","Cryotheum","Iron",
                      "Emerald","Copper","Tin","Magnesium","Graphite","Beryllium"]
insideReactor = []

coolerName = []
coolerValue = []

for name in insideReactorNames:
    for i in range(reactorFileLen):
        if (reactorFileArray[i].find(name)) > 0:
           coolerName.append(name)
           coolerValue.append(i)

for i in range(len(coolerValue)):
    for ii in range(len(coolerValue)-i-1):
        if coolerValue[ii] > coolerValue[ii+1]:
            coolerValue[ii], coolerValue[ii+1] = coolerValue[ii+1], coolerValue[ii]
            coolerName[ii], coolerName[ii+1] = coolerName[ii+1], coolerName[ii]

for i in range(len(coolerName)):
    insideReactor.append(coolerName[i])
    insideReactor.append(coolerValue[i])

insideReactor.append("InteriorDimensions")
insideReactor.append(foundInLine)



amounts = {"FuelCell": 0,"Water": 0,"Redstone": 0,"Quartz": 0,"Gold": 0,"Glowstone": 0,
                "Lapis": 0,"Diamond": 0,"Helium": 0,"Enderium": 0,"Cryotheum": 0,"Iron": 0,
                "Emerald": 0,"Copper": 0,"Tin": 0,"Magnesium": 0,"Graphite": 0,"Beryllium": 0}

countFloat = len(insideReactor)-2
count = int(countFloat)

for i in range(count):
    string = str(insideReactor[i])
    if string.isdigit() == False:
        amount = insideReactor[i+3] - insideReactor[i+1] - 4
        amounts[string] = amount


emptyCooler = 0

for elements in amounts:
    emptyCooler = emptyCooler + amounts[elements]
emptyCooler = emptyCooler - amounts["FuelCell"] - amounts["Graphite"] - amounts["Beryllium"]



fuelCell = amounts["FuelCell"]
waterBucket = amounts["Water"]
redstoneDust = amounts["Redstone"]*2
redstoneBlock = amounts["Redstone"]*2
quartzBlock = amounts["Quartz"]*2
quartzDust = amounts["Quartz"]*6
goldIngot = amounts["Gold"]*8
glowstoneDust = amounts["Glowstone"]*6
glowstoneBlock = amounts["Glowstone"]*2
lapisBlock = amounts["Lapis"]*2
diamonds = amounts["Diamond"]*8
heliumBucket = amounts["Helium"]*1
enderiumIngot = amounts["Enderium"]*8
cryotheumDust = amounts["Cryotheum"]*8
ironIngot= amounts["Iron"]*8
emeralds= amounts["Emerald"]*6
copperIngot = amounts["Copper"]*8
tinIngot = amounts["Tin"]*8
magnesiumIngot = amounts["Magnesium"]*8
graphiteBlock = amounts["Graphite"]
berylliumBlock = amounts["Beryllium"]

totalGlowstoneDust = glowstoneDust + (glowstoneBlock*4)
totalRedstoneDust = redstoneDust + (redstoneBlock*9)
totalLapis = lapisBlock*9
totalQuartz = quartzDust = (quartzBlock*4)
graphiteIngot = graphiteBlock*9
berylliumIngot = berylliumBlock*9

toughAlloy = 0
plating = 0

toughAlloy += (casings/4)

toughAlloy += (emptyCooler/2)

toughAlloy += (fuelCell*4)

if int(toughAlloy/4) < toughAlloy/4:
    toughAlloy = (int(toughAlloy/4))*4+4
else:
    toughAlloy = int(toughAlloy)

boron = toughAlloy/4
lithium = toughAlloy/2
steel = toughAlloy/4

glass = fuelCell*4

lead = casingsComp*2
graphiteDust = casingsComp*2

plating = lead


print("Everything you need for this reactor desing:")
print("Water buckets:", waterBucket)
print("Redstone dust:", redstoneDust,"Redstone blocks", redstoneBlock)
print("The total amount of redstone dust:", totalRedstoneDust)
print("Quartz blocks:", quartzBlock, "Quartz dust:", quartzDust)
print("The total amount of quartz:", totalQuartz)
print("Gold ingots:",goldIngot)
print("Glowstone dust:", glowstoneDust,"Glowstone blocks:", glowstoneBlock)
print("Lapis blocks:", lapisBlock,"The total amount of lapis:",totalLapis)
print("Diamonds:",diamonds)
print("Helium buckets:",heliumBucket)
print("Enderium ingots:", enderiumIngot)
print("Cryotheum dust:", cryotheumDust)
print("Iron ingots:", ironIngot)
print("Emeralds:",emeralds)
print("Copper ingots:", copperIngot)
print("Tin ingots:", tinIngot)
print("Magnesium ingots:", magnesiumIngot)
print("Graphite block:",graphiteBlock,"The tota; amount of graphite ingots:",graphiteIngot)
print("Berrylium blocks:",berylliumBlock,"The total amount of beryllium ingots:",berylliumIngot)
print("")
print("The total amount of:")
print("tough alloy:",toughAlloy,"That is made with: Boron:",boron,"Steel:",steel,"Lithium:",lithium)
print("The casings:",casings,"The plating:",plating,"Lead ingots:",lead,"graphite dust:",graphiteDust)


Wait = input()
