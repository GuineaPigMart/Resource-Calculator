import json

print("version: indev_2")
print("Note: for this to work you need the reactor .json in the same map as this program.")
print("Select a reactor by typing in the exact name:")

file = input()

with open(file) as json_file:
    data = json.load(json_file)
    data.pop("SaveVersion")
    data.pop("UsedFuel")

#casings    
interiorDimensions =  data["InteriorDimensions"]
x = interiorDimensions["X"]
y = interiorDimensions["Y"]
z = interiorDimensions["Z"]

casing = (x*y*2)+(x*z*2)+(z*y*2)

#coolers
compressedReactorRaw = data["CompressedReactor"]
compressedReactor = {}

for elements in compressedReactorRaw:
    compressedReactor[elements] = len(compressedReactorRaw[elements])

def Surrounded(name):
    for elements in compressedReactor:
        if elements == name:
            amount = compressedReactor[name]*8
            return amount

def TwoBlocks(name):
    for elements in compressedReactor:
        if elements == name:
            amount = compressedReactor[name]*2
            return amount

def Dust(name):
    for elements in compressedReactor:
        if elements == name:
            amount = {}
            amount["Dust"] = compressedReactor[name]*8
            amount["Block"] = compressedReactor[name]*2
            amount["Total"] = compressedReactor[name]*10
            return amount

def Fluid(name):
    for elements in compressedReactor:
        if elements == name:    
            amount = compressedReactor[name]
            return amount

def Moderator(name):
    for elements in compressedReactor:
        if elements == name:
            amount = {}
            amount["Ingot"] = compressedReactor[name]*9
            amount["Block"] = compressedReactor[name]
            return amount
        
def TwoBlockTwoDust(name):
    for elements in compressedReactor:
        if elements == name:
            amount = {}
            amount["Block"] = compressedReactor[name]*2
            amount["Dust"] = compressedReactor[name]*2
            amount["Total"] = compressedReactor[name]*20
            return amount

#ingots 
copperIngot = Surrounded("Copper")
ironIngot = Surrounded("Iron")
goldIngot = Surrounded("Gold")
enderiumIngot = Surrounded("Enderium")
tinIngot = Surrounded("Tin")
magnesiumIngot = Surrounded("Magnesium")

#gems
diamond = Surrounded("Diamond")
emerald = Surrounded("Emerald")

#dusts
lapis = TwoBlocks("Lapis")
glowstone = Dust("Glowstone")
quartz = Dust("Quartz")
redstone = TwoBlockTwoDust("Redstone")

#moderator
graphite = Moderator("Graphite")
beryllium = Moderator("Beryllium")

#fluid
helium = Fluid("Helium")
water = Fluid("Water")

#empty cooler count
emptyCooler = 0

for elements in compressedReactor:
    emptyCooler += compressedReactor[elements]

emptyCooler -= compressedReactor["FuelCell"] - compressedReactor["Graphite"] - compressedReactor["Beryllium"]

#other resources
toughAlloy = compressedReactor["FuelCell"]*4
graphiteDust = 0
leadIngot = 0

if casing//4 < casing/4:
    leadIngot = (casing//4+1)*4
    graphiteDust = (casing//4+1)*4
    toughAlloy += casing//4+1
else:
    leadIngot = casing//4*4
    graphiteDust = casing//4*4
    toughAlloy += casing//4


glass = compressedReactor["FuelCell"]*4
boron = toughAlloy/4
lithium = toughAlloy/2
steel = toughAlloy/4

if emptyCooler//2 == emptyCooler/2:
    steel += (emptyCooler/2)
    toughAlloy += (emptyCooler/2)
else:
    steel += ((emptyCooler+1)/2)
    toughAlloy += ((emptyCooler+1)/2)
#Display information
print("This is a list of what you need")
print("Copper ingots:",copperIngot)
print("Iron ingots:",ironIngot)
print("Gold ingots:",goldIngot)
print("Enderium ingots:",enderiumIngot)
print("Tin Ingots:",tinIngot)
print("Magnesium ingots:",magnesiumIngot)
print("Diamonds:",diamond)
print("Emeralds:",emerald)
print("Lapis blocks",lapis)
try:
    print("Glowstone dust:",glowstone["Dust"],"Glowstone Blocks",glowstone["Block"],"Total amount of glowstone dust:",glowstone["Total"])
except:
    print("Glowstone: None")
try:
    print("Quartz dust:",quartz["Dust"],"Quartz blocks",quartz["Block"],"Total amount of quartz:",quartz["Total"])
except:
    print("Quartz: None")
try:
    print("Redstone dust:",redstone["Dust"],"Redstone blocks:",redstone["Block"],"Total amount of redstone dust:",redstone["Total"])
except:
    print("Redstone: None")
print("Water buckets:",water)
print("Helium buckets:",helium)
try:
    print("Graphite blocks:",graphite["Block"],"That is",graphite["Ingot"],"ingots")
except:
    print("Graphite: None")
try:
    print("Beryllium blocks:",beryllium["Block"],"That is",beryllium["Ingot"],"ingots")
except:
    print("Beryllium: None")

print("Steel:",steel)
print("Boron:",boron)
print("Lithium:",lithium)
print("Tough alloy:",toughAlloy)
print("Glass:",glass)
print("Lead ingots:",leadIngot)
print("Graphite dust:",graphiteDust)

wait = input()
