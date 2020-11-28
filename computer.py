##################################################################
##  Beings can:                                                 ##
##      Interact with each other (talk)                         ##
##      Positive interaction (+1 acquiantance level)            ##
##      Negative interaction (-1 acquiantance level)            ##
##      Become friends (if acquiantance level goes above 5)     ##
##      Become enemies (if acquiantance level goes below zero)  ##
##                                                              ##
##################################################################

class Being():

    def __init__(self, name):
        self.name = name
        self.connections = {}
        self.friends = {}
        self.enemies = {}

    def assessSurroundings(self):
        print("Assessing surroundings...")
        print("Nearby beings:")
        beings = state["beings"]
        for being in beings:
            print("\t- " + being.name)
        return state["beings"]

    def addConnection(self, being):
        self.connections[being] = {
            "relationship": "ACQUAINTANCE",
            "level": 0
        }

    def joinCommunity(self, community):
        state[community].append(self)


state = {
    "beings": []
}


def wake(name):
    print(name + " has woken")
    being = Being(name)
    state["beings"].append(being)
    return being


def establishCommunication(being0, being1):
    being0.addConnection(being1)
    being1.addConnection(being0)


def assessRelationship(being0, being1):
    level = being0.connections[being1]["level"]
    print(level)
    if level > 5:
        being0.connections[being1]["relationship"] = "FRIEND"
        being1.connections[being0]["relationship"] = "FRIEND"
    elif level < -2:
        being0.connections[being1]["relationship"] = "ENEMY"
        being1.connections[being0]["relationship"] = "ENEMY"
    else:
        being0.connections[being1]["relationship"] = "ACQUAINTANCE"
        being1.connections[being0]["relationship"] = "ACQUAINTANCE"
    print()


def positiveInteraction(being0, being1):
    being0.connections[being1]["level"] += 1
    being1.connections[being0]["level"] += 1
    assessRelationship(being0, being1)


def negativeInteraction(being0, being1):
    being0.connections[being1]["level"] -= 1
    being1.connections[being0]["level"] -= 1
    assessRelationship(being0, being1)


def formCommunity(communityName, beings):
    state[communityName] = beings


def main():
    dog = wake("Dash")
    phone = wake("Phone")
    computer = wake("Computer")

    computer.assessSurroundings()
    establishCommunication(computer, phone)

    fish = wake("Fish")

    establishCommunication(dog, fish)

    dogPlushDinosaur = wake("Dog Plush Dinosaur")

    establishCommunication(dog, dogPlushDinosaur)

    toyElephant = wake("Elephant")
    toyBear = wake("Bear")

    establishCommunication(toyElephant, dogPlushDinosaur)

    plant = wake("Plant")

    positiveInteraction(dog, fish)

    establishCommunication(toyBear, toyElephant)
    positiveInteraction(phone, computer)

    xbox = wake("Xbox")

    establishCommunication(xbox, computer)
    establishCommunication(xbox, phone)

    establishCommunication(toyBear, dogPlushDinosaur)

    negativeInteraction(phone, computer)
    positiveInteraction(computer, xbox)

    guitarHero5XboxGame = wake("Guitar Hero 5 Xbox Game")

    positiveInteraction(phone, xbox)
    positiveInteraction(computer, phone)

    cups = []
    dogMomMug = wake("Dog Mom Mug")
    cups.append(dogMomMug)
    
    positiveInteraction(dog, fish)

    establishCommunication(xbox, guitarHero5XboxGame)
    negativeInteraction(xbox, guitarHero5XboxGame)

    cableBox = wake("Cable Box")

    establishCommunication(cableBox, computer)
    establishCommunication(cableBox, phone)

    positiveInteraction(phone, computer)
    
    establishCommunication(cableBox, xbox)

    guitarHeroSmashHitsXboxGame = wake("Guitar Hero Smash Hits Xbox Game")

    toyTrain = wake("Toy Train")
    
    establishCommunication(guitarHeroSmashHitsXboxGame, xbox)

    toyBlanket = wake("Toy Blanket")

    establishCommunication(toyTrain, dogPlushDinosaur)

    wineGlass0 = wake("Wine Glass 0")
    cups.append(wineGlass0)

    establishCommunication(toyTrain, toyElephant)

    bentMetalStraw = wake("Bent Metal Straw")

    establishCommunication(toyTrain, toyBear)
    establishCommunication(toyBlanket, toyElephant)
    establishCommunication(toyBlanket, dogPlushDinosaur)
    establishCommunication(toyBear, toyBlanket)

    wineGlass1 = wake("Wine Glass 1")

    establishCommunication(wineGlass0, wineGlass1)
    establishCommunication(toyTrain, toyBlanket)

    cups.append(wineGlass1)
    UNDMug = wake("University of Notre Dame Mug")
    cups.append(UNDMug)
    justDance2014XboxGame = wake("Just Dance 2014 Xbox Game")
    minecraftXboxGame = wake("Minecraft Xbox Game")
    dogAlligatorToy = wake("Dog Alligator Toy")

    positiveInteraction(wineGlass0, wineGlass1)

    wineGlass2 = wake("Wine Glass 2")
    cups.append(wineGlass2)

    negativeInteraction(fish, dog)
    positiveInteraction(computer, phone)

    establishCommunication(dogPlushDinosaur, dogAlligatorToy)
    establishCommunication(toyTrain, dogAlligatorToy)
    establishCommunication(wineGlass0, wineGlass2)
    
    GTAVXboxGame = wake("GTA V Xbox Game")
    starWarsMug = wake("Star Wars Mug")
    cups.append(starWarsMug)
    xboxController0 = wake("Xbox Controller 0")
    wineGlass3 = wake("Wine Glass 3")
    cups.append(wineGlass3)
    
    establishCommunication(toyElephant, dogAlligatorToy)

    xboxController1 = wake("Xbox Controller 1")
    guitarHeroWorldTourXboxGame = wake("Guitar Hero World Tour Xbox Game")
    stemlessWineGlass0 = wake("Stemless Wine Glass 0")
    cups.append(stemlessWineGlass0)
    
    establishCommunication(toyBear, dogAlligatorToy)
    establishCommunication(wineGlass0, wineGlass3)
    
    tv = wake("TV")

    establishCommunication(toyBlanket, dogAlligatorToy)
    establishCommunication(tv, cableBox)

    dallasMug = wake("Dallas Mug")
    cups.append(dallasMug)
    
    callOfDutyMW3XboxGame = wake("Call of Duty MW3 Xbox Game")
    
    establishCommunication(tv, computer)
    
    dogPlushCarrot = wake("Dog Plush Carrot")

    establishCommunication(tv, phone)
    
    stemlessWineGlass1 = wake("Stemless Wine Glass")
    cups.append(stemlessWineGlass1)
    leechLakeMug = wake("Leech Lake Mug")
    cups.append(leechLakeMug)

    establishCommunication(toyElephant, dogPlushCarrot)
    establishCommunication(tv, xbox)
    establishCommunication(wineGlass0, stemlessWineGlass0)

    dogPlushMonkey = wake("Dog Plush Monkey")
    fallout4XboxGame = wake("Fallout 4 Xbox Game")

    establishCommunication(tv, xboxController0)
    establishCommunication(toyBear, dogPlushCarrot)
    establishCommunication(tv, xboxController1)
    establishCommunication(dogPlushDinosaur, dogPlushMonkey)

    positiveInteraction(dog, fish)

    electronicsCommunity = [computer, phone, xbox, cableBox, tv, xboxController0, xboxController1]
    formCommunity("Electronics", electronicsCommunity)

    establishCommunication(dogPlushDinosaur, dogPlushCarrot)
    establishCommunication(wineGlass0, stemlessWineGlass1)
    establishCommunication(dogPlushCarrot, dogPlushMonkey)

    house = wake("House")
    stemlessWineGlass2 = wake("Stemless Wine Glass 2")
    cups.append(stemlessWineGlass2)

    establishCommunication(toyTrain, dogPlushCarrot)
    
    keurig = wake("Keurig")
    
    establishCommunication(dogAlligatorToy, dogPlushCarrot)
    establishCommunication(toyElephant, dogPlushMonkey)

    dogBlanket = wake("Dog Blanket")

    establishCommunication(toyBlanket, dogBlanket)
    establishCommunication(dogAlligatorToy, dogPlushMonkey)
    
    xboxController2 = wake("Xbox Controller 2")

    establishCommunication(toyBear, dogPlushMonkey)
    establishCommunication(wineGlass0, stemlessWineGlass2)
    
    maddenXboxGame = wake("Madden Xbox Game")
    stemlessWineGlass3 = wake("Stemless Wine Glass 3")
    cups.append(stemlessWineGlass3)

    establishCommunication(toyBlanket, dogPlushCarrot)
    establishCommunication(dogAlligatorToy, dogBlanket)

    negativeInteraction(computer, phone)
    
    establishCommunication(toyTrain, dogPlushMonkey)
    establishCommunication(dogPlushCarrot, dogBlanket)

    dogDuraforce = wake("Duraforce")

    establishCommunication(dogPlushMonkey, dogBlanket)
    establishCommunication(wineGlass0, stemlessWineGlass3)
    
    halo5XboxGame = wake("Halo 5 Xbox Game")

    establishCommunication(toyBlanket, dogPlushMonkey)
    establishCommunication(dogPlushMonkey, dogDuraforce)
    
    tvRemote = wake("TV Remote")

    establishCommunication(toyElephant, dogBlanket)

    callOfDutyModernWarfare2XboxGame = wake("Call of Duty Modern Warfare 2 Xbox Game")
    xboxController3 = wake("Xbox Controller")
    seaofThievesXboxGame = wake("Sea of Thieves Xbox Game")

    establishCommunication(dogPlushDinosaur, dogBlanket)
    
    callOfDutyAdvancedWarfareXboxGame = wake("Call of Duty Advanced Warfare Xbox Game")
    pastaMaker = wake("Pasta Maker")

    establishCommunication(dogPlushDinosaur, dogDuraforce)
    
    legoStarWarsIIXboxGame = wake("Lego Star Wars II Xbox Game")
    dogKong = wake("Kong")

    establishCommunication(toyBear, dogBlanket)
    establishCommunication(toyTrain, dogDuraforce)
    
    loveseat = wake("Loveseat")
    iceCreamScoop = wake("Ice Cream Scoop")
    battlefield4XboxGame = wake("Battlefield 4 Xbox Game")
    
    establishCommunication(toyTrain, dogBlanket)
    establishCommunication(dogBlanket, dogDuraforce)

    dogRope = wake("Dog Rope")

    establishCommunication(toyElephant, dogDuraforce)
    establishCommunication(dogAlligatorToy, dogKong)
    
    couch = wake("Couch")

    establishCommunication(toyBear, dogDuraforce)
    establishCommunication(toyTrain, dogKong)
    
    bowls = []
    mediumMixingBowl = wake("Medium Mixing Bowl")
    bowls.append(mediumMixingBowl)

    establishCommunication(toyBlanket, dogKong)
    establishCommunication(dogPlushCarrot, dogRope)
    establishCommunication(dogAlligatorToy, dogDuraforce)
    
    throwPillow0 = wake("Throw Pillow 0")
    largeMixingBowl = wake("Large Mixing Bowl")
    bowls.append(largeMixingBowl)

    establishCommunication(dogPlushMonkey, dogKong)
    
    mediumPot0 = wake("Medium Pot 0")
    
    establishCommunication(toyBear, dogKong)
    establishCommunication(dogPlushDinosaur, dogRope)

    smallMixingBowl = wake("Small Mixing Bowl")
    bowls.append(smallMixingBowl)

    establishCommunication(dogPlushMonkey, dogRope)
    establishCommunication(dogBlanket, dogKong)
    establishCommunication(dogDuraforce, dogKong)
    
    whisk = wake("Whisk")
    microwave = wake("Microwave")

    establishCommunication(dogPlushDinosaur, dogKong)
    establishCommunication(toyElephant, dogRope)
    
    throwPillow1 = wake("Throw Pillow 1")
    ladle = wake("Ladle")
    fridge = wake("Fridge")

    establishCommunication(dogPlushCarrot, dogKong)
    establishCommunication(dogBlanket, dogRope)
    
    bottleOpener = wake("Bottle Opener")

    establishCommunication(toyElephant, dogKong)
    establishCommunication(toyBlanket, dogRope)
    
    crockpot = wake("Crockpot")

    positiveInteraction(dog, fish)

    establishCommunication(dogAlligatorToy, dogRope)

    spatula0 = wake("Spatula")

    positiveInteraction(phone, computer)

    establishCommunication(toyTrain, dogRope)

    oven = wake("Oven")
    mediumPot1 = wake("Medium Pot 1")
    christmasOvenMitt = wake("Christmas Oven Mitt")

    establishCommunication(toyBear, dogRope)
    
    spoons = []
    servingSpoon0 = wake("Serving Spoon 0")
    spoons.append(servingSpoon0)

    establishCommunication(dogKong, dogRope)

    throwPillow2 = wake("Throw Pillow 2")
    smallPot0 = wake("Small Pot 0")
    toaster = wake("Toaster")

    establishCommunication(dogDuraforce, dogRope)

    ovenMitt0 = wake("Oven Mitt 0")
    spatula1 = wake("Spatula 1")
    mediumPot2 = wake("Medium Pot 2")
    ovenMitt1 = wake("Oven Mitt 1")
    potholder1 = wake("Potholder 1")
    strainer = wake("Strainer")
    dishDryingTowel0 = wake("Dish Drying Towel 0")
    dishSoap = wake("Dish Soap")
    largePot0 = wake("Large Pot 0")
    throwPillow3 = wake("Throw Pillow 3")
    dryingRack = wake("Drying Rack")
    sponge = wake("Sponge")
    kitchenHandSoap = wake("Hand Soap")
    sink = wake("Sink")
    potholder0 = wake("Potholder 0")
    
    positiveInteraction(wineGlass1, wineGlass0)
    
    smallPot1 = wake("Small Pot 1")
    knives = []
    chefsKnife = wake("Chef's Knife")
    knives.append(chefsKnife)
    unicornWineStopper = wake("Unicorn Wine Stopper")
    pastaDryingRack = wake("Pasta Drying Rack")

    negativeInteraction(xbox, guitarHero5XboxGame)
    negativeInteraction(fish, dog)
    
    servingSpoon1 = wake("Serving Spoon 1")
    spoons.append(servingSpoon1)
    rug = wake("Rug")
    largePot1 = wake("Large Pot 1")
    dishDryingTowel1 = wake("Dish Drying Towel 1")
    oneCupMeasuringCup = wake("One Cup Measuring Cup")
    straightMetalStraw = wake("Straight Metal Straw")
    babyBlueWineStopper = wake("Baby Blue Wine Stopper")
    kitchenHandTowel0 = wake("Kitchen Hand Towel 0")
    cherryWineStopper = wake("Cherry Wine Stopper")
    serratedKnife = wake("Serrated Knife")
    knives.append(serratedKnife)
    navyWineStopper = wake("Navy Wine Stopper")

    negativeInteraction(computer, phone)

    blanket0 = wake("Blanket 0")
    tablespoon = wake("Tablespoon")
    blanket1 = wake("Blanket 1")
    coffeeTable = wake("Coffee Table")
    
    establishCommunication(plant, house)

    kitchenTable = wake("Kitchen Table")
    dishwasher = wake("Dishwasher")
    halfCupMeasuringCup = wake("Half Cup Measuring Cup")
    chair0 = wake("Chair 0")
    toyBasket = wake("Toy Basket")
    chair1 = wake("Chair 1")
    cloroxWipes = wake("Clorox Wipes")
    teaspoon = wake("Teaspoon")

    positiveInteraction(dog, fish)

    windex = wake("Windex")
    standingLamp = wake("Standing Lamp")
    entertainmentCenter = wake("Entertainment Center")
    slicingKnife = wake("Slicing Knife")
    knives.append(slicingKnife)
    kitchenHandTowel1 = wake("Kitchen Hand Towel")
    knifeBlock = wake("Knife Block")

    negativeInteraction(phone, computer)

    quarterCupMeasuringCup = wake("Quarter Cup Measuring Cup")
    rubberJarOpener = wake("Rubber Jar Opener")
    seasonalPlacemat0 = wake("Seasonal Placemat 0")
    lamp0 = wake("Lamp 0")
    throwPillow4 = wake("Throw Pillow 4")
    tinfoil = wake("Tinfoil")
    foodScale = wake("Food Scale")
    thirdCupMeasuringCup = wake("Third Cup Measuring Cup")
    seasonalPlacemat1 = wake("Seasonal Placemat 1")
    lamp1 = wake("Lamp 1")
    chair2 = wake("Chair 2")

    negativeInteraction(plant, house)
    
    gallonZiplockBags = wake("Gallon Ziplock Bags")
    
    positiveInteraction(wineGlass1, wineGlass0)
    
    saranWrap = wake("Saran Wrap")
    tomatoKnife = wake("Tomato Knife")
    knives.append(tomatoKnife)
    placemat0 = wake("Placemat 0")
    halfTeaspoon = wake("Half Teaspoon")
    bakingSheet0 = wake("Baking Sheet 0")
    sandwichZiplockBags = wake("Sandwich Ziplock Bags")
    kitchenTrashcan = wake("Kitchen Trashcan")
    seasonalPlacemat2 = wake("Seasonal Placemat 2")
    coffeePodBasket = wake("CoffeePodBasket")
    forks = []
    largeFork0 = wake("Large Fork 0")
    forks.append(largeFork0)
    steakKnife0 = wake("Steak Knife 0")
    knives.append(steakKnife0)
    dunkinDonutsCoffeePod0 = wake("Dunkin' Donuts Coffee Pod 0")
    smallCup0 = wake("Small Cup 0")
    cups.append(smallCup0)

    positiveInteraction(dog, fish)

    dunkinDonutsCoffeePod1 = wake("Dunkin' Donuts Coffee Pod 1")
    steakKnife1 = wake("Steak Knife 1")
    knives.append(steakKnife1)
    plates = []
    smallPlate0 = wake("Small Plate 0")
    plates.append(smallPlate0)
    sideTable1 = wake("Side Table 1")
    largeFork1 = wake("Large Fork 1")
    forks.append(largeFork1)
    knife0 = wake("Knife 0")
    knives.append(knife0)
    dunkinDonutsCoffeePod2 = wake("Dunkin' Donuts Coffee Pod 2")
    steakKnife2 = wake("Steak Knife 2")
    knives.append(steakKnife2)
    dunkinDonutsCoffeePod3 = wake("Dunkin' Donuts Coffee Pod 3")
    largeFork2 = wake("Large Fork 2")

    negativeInteraction(phone, computer)

    forks.append(largeFork2)
    tallCup1 = wake("Tall Cup 1")
    cups.append(tallCup1)
    smallPlate1 = wake("Small Plate 1")
    plates.append(smallPlate1)
    seasonalPlacemat3 = wake("Seasonal Placemat 3")
    largeFork3 = wake("Large Fork 3")
    forks.append(largeFork3)
    smallCup1 = wake("Small Cup 1")
    cups.append(smallCup1)
    dunkinDonutsCoffeePod4 = wake("Dunkin' Donuts Coffee Pod 4")
    quarterTeaspoon = wake("Quarter Teaspoon")
    dunkinDonutsCoffeePod5 = wake("Dunkin' Donuts Coffee Pod 5")
    largeFork4 = wake("Large Fork 4")
    forks.append(largeFork4)
    largeSpoon0 = wake("Large Spoon 0")
    spoons.append(largeSpoon0)
    smallFork0 = wake("Small Fork 0")
    forks.append(smallFork0)

    positiveInteraction(dog, fish)

    largePlate1 = wake("Large Plate 1")
    plates.append(largePlate1)
    steakKnife3 = wake("Steak Knife 3")
    knives.append(steakKnife3)
    dunkinDonutsCoffeePod6 = wake("Dunkin' Donuts Coffee Pod 6")
    largeFork5 = wake("Large Fork 5")
    placemat1 = wake("Placemat 1")
    bakingSheet1 = wake("Baking Sheet 1")
    forks.append(largeFork5)
    paringKnife = wake("Paring Knife")
    smallFork1 = wake("Small Fork 1")
    forks.append(smallFork1)
    knife1 = wake("Knife 1")
    knives.append(knife1)
    chair3 = wake("Chair 3")
    largeFork6 = wake("Large Fork 6")
    forks.append(largeFork6)

    positiveInteraction(phone, computer)
    utilityKnife = wake("Utility Knife")
    smallFork2 = wake("Small Fork 2")
    forks.append(smallFork2)
    dunkinDonutsCoffeePod7 = wake("Dunkin' Donuts Coffee Pod 7")
    largeFork7 = wake("Large Fork 7")
    forks.append(largeFork7)
    placemat2 = wake("Placemat 2")
    tallCup0 = wake("Tall Cup 0")
    cups.append(tallCup0)
    largeSpoon1 = wake("Large Spoon 1")
    spoons.append(largeSpoon1)
    dunkinDonutsCoffeePod8 = wake("Dunkin' Donuts Coffee Pod 8")
    
    negativeInteraction(xbox, guitarHero5XboxGame)
    
    largeFork8 = wake("Large Fork 8")
    placemat3 = wake("Placemat 3")
    forks.append(largeFork8)
    largeSpoon2 = wake("Large Spoon 2")
    spoons.append(largeSpoon2)
    dunkinDonutsCoffeePod9 = wake("Dunkin' Donuts Coffee Pod 9")
    steakKnife4 = wake("Steak Knife 4")
    knives.append(steakKnife4)
    bowl0 = wake("Bowl 0")
    bowls.append(bowl0)
    largeSpoon3 = wake("Large Spoon 3")
    spoons.append(largeSpoon3)
    largeFork9 = wake("Large Fork 9")
    forks.append(largeFork9)
    dunkinDonutsCoffeePod10 = wake("Dunkin' Donuts Coffee Pod 10")
    steakKnife5 = wake("Steak Knife 5")
    knives.append(steakKnife5)
    knife2 = wake("Knife 2")
    knives.append(knife2)
    
    negativeInteraction(wineGlass1, wineGlass0)
    
    canOpener = wake("Can Opener")
    steakKnife6 = wake("Steak Knife 6")
    knives.append(steakKnife6)
    strawBrush = wake("Straw Brush")
    dunkinDonutsCoffeePod11 = wake("Dunkin' Donuts Coffee Pod 11")
    smallSpoon1 = wake("Small Spoon 1")
    spoons.append(smallSpoon1)

    positiveInteraction(dog, fish)

    dunkinDonutsCoffeePod12 = wake("Dunkin' Donuts Coffee Pod 12")
    bowl2 = wake("Bowl 2")
    bowls.append(bowl2)
    steakKnife7 = wake("Steak Knife 7")
    knives.append(steakKnife7)
    smallFork3 = wake("Small Fork 3")
    forks.append(smallFork3)
    dunkinDonutsCoffeePod13 = wake("Dunkin' Donuts Coffee Pod 13")
    knife3 = wake("Knife 3")
    knives.append(knife3)
    
    positiveInteraction(wineGlass0, wineGlass1)
    
    smallFork4 = wake("Small Fork 4")
    forks.append(smallFork4)
    dunkinDonutsCoffeePod14 = wake("Dunkin' Donuts Coffee Pod 14")
    smallFork5 = wake("Small Fork 5")
    forks.append(smallFork5)
    bowl1 = wake("Bowl 1")
    bowls.append(bowl1)

    positiveInteraction(phone, computer)

    dunkinDonutsCoffeePod15 = wake("Dunkin' Donuts Coffee Pod 15")
    smallFork6 = wake("Small Fork 6")
    forks.append(smallFork6)
    sideTable0 = wake("Side Table 0")
    smallFork7 = wake("Small Fork 7")
    forks.append(smallFork7)
    smallFork8 = wake("Small Fork 8")
    forks.append(smallFork8)
    
    negativeInteraction(plant, house)
    
    dunkinDonutsCoffeePod16 = wake("Dunkin' Donuts Coffee Pod 16")
    smallFork9 = wake("Small Fork 9")
    forks.append(smallFork9)
    dunkinDonutsCoffeePod17 = wake("Dunkin' Donuts Coffee Pod 17")
    smallPlate2 = wake("Small Plate 2")
    
    negativeInteraction(xbox, guitarHero5XboxGame)
    
    plates.append(smallPlate2)
    knife4 = wake("Knife 4")
    knives.append(knife4)
    dunkinDonutsCoffeePod18 = wake("Dunkin' Donuts Coffee Pod 18")
    knife5 = wake("Knife 5")
    knives.append(knife5)
    knife6 = wake("Knife 6")
    knives.append(knife6)
    dunkinDonutsCoffeePod19 = wake("Dunkin' Donuts Coffee Pod 19")
    knife7 = wake("Knife 7")
    knives.append(knife7)
    knife8 = wake("Knife 8")
    knives.append(knife8)
    dunkinDonutsCoffeePod20 = wake("Dunkin' Donuts Coffee Pod 20")

    positiveInteraction(fish, dog)
    
    knife9 = wake("Knife 9")
    knives.append(knife9)
    dunkinDonutsCoffeePod21 = wake("Dunkin' Donuts Coffee Pod 21")
    dunkinDonutsCoffeePod22 = wake("Dunkin' Donuts Coffee Pod 22")
    dunkinDonutsCoffeePod23 = wake("Dunkin' Donuts Coffee Pod 23")
    largeSpoon4 = wake("Large Spoon 4")
    spoons.append(largeSpoon4)
    largeSpoon5 = wake("Large Spoon 5")
    spoons.append(largeSpoon5)
    largeSpoon6 = wake("Large Spoon 6")
    spoons.append(largeSpoon6)
    largeSpoon7 = wake("Large Spoon 7")
    spoons.append(largeSpoon7)
    largeSpoon8 = wake("Large Spoon 8")
    spoons.append(largeSpoon8)
    dunkinDonutsCoffeePod24 = wake("Dunkin' Donuts Coffee Pod 24")
    largeSpoon9 = wake("Large Spoon 9")
    spoons.append(largeSpoon9)
    dunkinDonutsCoffeePod25 = wake("Dunkin' Donuts Coffee Pod 25")
    smallSpoon0 = wake("Small Spoon 0")
    spoons.append(smallSpoon0)
    dunkinDonutsCoffeePod26 = wake("Dunkin' Donuts Coffee Pod 26")
    smallSpoon2 = wake("Small Spoon 2")
    spoons.append(smallSpoon2)
    dunkinDonutsCoffeePod27 = wake("Dunkin' Donuts Coffee Pod 27")
    dunkinDonutsCoffeePod28 = wake("Dunkin' Donuts Coffee Pod 28")
    smallSpoon3 = wake("Small Spoon 3")
    spoons.append(smallSpoon3)
    smallSpoon4 = wake("Small Spoon 4")
    spoons.append(smallSpoon4)
    dunkinDonutsCoffeePod29 = wake("Dunkin' Donuts Coffee Pod 29")
    
    positiveInteraction(dog, fish)
    
    smallSpoon5 = wake("Small Spoon 5")
    spoons.append(smallSpoon5)
    dunkinDonutsCoffeePod30 = wake("Dunkin' Donuts Coffee Pod 30")
    
    negativeInteraction(xbox, guitarHero5XboxGame)
    
    smallSpoon6 = wake("Small Spoon 6")
    spoons.append(smallSpoon6)
    smallSpoon7 = wake("Small Spoon 7")
    spoons.append(smallSpoon7)
    dunkinDonutsCoffeePod31 = wake("Dunkin' Donuts Coffee Pod 31")
    smallSpoon8 = wake("Small Spoon 8")
    spoons.append(smallSpoon8)

    positiveInteraction(computer, phone)

    dunkinDonutsCoffeePod32 = wake("Dunkin' Donuts Coffee Pod 32")
    smallSpoon9 = wake("Small Spoon 9")
    spoons.append(smallSpoon9)
    dunkinDonutsCoffeePod33 = wake("Dunkin' Donuts Coffee Pod 33")
    smallCup2 = wake("Small Cup 2")
    cups.append(smallCup2)
    smallCup3 = wake("Small Cup 3")
    cups.append(smallCup3)
    
    negativeInteraction(plant, house)
    
    dunkinDonutsCoffeePod34 = wake("Dunkin' Donuts Coffee Pod 34")
    tallCup2 = wake("Tall Cup 2")
    
    negativeInteraction(wineGlass1, wineGlass0)
    
    cups.append(tallCup2)
    tallCup3 = wake("Tall Cup 2")
    cups.append(tallCup3)
    dunkinDonutsCoffeePod35 = wake("Dunkin' Donuts Coffee Pod 35")
    smallPlate3 = wake("Small Plate 3")
    plates.append(smallPlate3)
    smallPlate4 = wake("Small Plate 4")
    plates.append(smallPlate4)
    dunkinDonutsCoffeePod37 = wake("Dunkin' Donuts Coffee Pod 37")
    largePlate0 = wake("Large Plate 0")
    plates.append(largePlate0)
    largePlate2 = wake("Large Plate 2")
    plates.append(largePlate2)
    
    positiveInteraction(fish, dog)
    
    positiveInteraction(dog, fish)
    dunkinDonutsCoffeePod38 = wake("Dunkin' Donuts Coffee Pod 38")
    largePlate3 = wake("Large Plate 3")
    plates.append(largePlate3)

    positiveInteraction(dog, fish)
    positiveInteraction(computer, phone)

    dunkinDonutsCoffeePod39 = wake("Dunkin' Donuts Coffee Pod 39")
    largePlate4 = wake("Large Plate 4")
    
    positiveInteraction(wineGlass1, wineGlass0)

    plates.append(largePlate4)
    bowl3 = wake("Bowl 3")
    
    negativeInteraction(xbox, guitarHero5XboxGame)
    
    bowls.append(bowl3)
    bowl4 = wake("Bowl 4")
    bowls.append(bowl4)
    positiveInteraction(fish, dog)
    dunkinDonutsCoffeePod40 = wake("Dunkin' Donuts Coffee Pod 40")

    ## REST OF HOUSE ##
    
    washingMachine = wake("Washing Machine")
    dryer = wake("Dryer")
    laundryDetergent = wake("Laundry Detergent")
    dryerSheets = wake("Dryer Sheets")
    bucket = wake("Bucket")
    broom = wake("Broom")
    vacuum = wake("Vacuum")
    bathTowel0 = wake("Bath Towel 0")
    bathTowel1 = wake("Bath Towel 1")
    bathTowel2 = wake("Bath Towel 2")
    bathTowel3 = wake("Bath Towel 3")
    bathRug0 = wake("Bath Rug 0")
    bathRug1 = wake("Bath Rug 1")
    bathRug2 = wake("Bath Rug 2")
    bathRug3 = wake("Bath Rug 3")
    handSoap0 = wake("Hand Soap 0")
    handSoap1 = wake("Hand Soap 1")
    handSoap2 = wake("Hand Soap 2")
    toilet0 = wake("Toilet 0")
    toilet1 = wake("Toilet 1")
    toilet1 = wake("Toilet 2")
    shower0 = wake("Shower 0")
    shower1 = wake("Shower 1")
    showerCurtain0 = wake("Shower Curtain 0")
    showerCurtain1 = wake("Shower Curtain 1")
    greyToothbrush = wake("Grey Toothbrush")
    blueToothbrush = wake("Blue Toothbrush")
    toothbrushHolder = wake("Toothbrush Holder")
    crest3DWhiteToothpaste = wake("Crest 3D White Toothpaste")
    hairbrush0 = wake("Hairbrush 0")
    hairbrush1 = wake("Hairbrush 1")
    bathroomTrashcan0 = wake("Bathroom Trashcan 0")
    bathroomTrashcan1 = wake("Bathroom Trashcan 1")
    bathroomTrashcan2 = wake("Bathroom Trashcan 2")
    razor0 = wake("Razor 0")
    razor1 = wake("Razor 1")
    extraRazorHeads = wake("Extra Razor Heads")
    hairtie0 = wake("Hairtie 0")
    hairtie1 = wake("Hairtie 1")
    hairtie2 = wake("Hairtie 2")
    hairtie3 = wake("Hairtie 3")
    hairtie4 = wake("Hairtie 4")
    hairtie5 = wake("Hairtie 5")
    hairtie6 = wake("Hairtie 6")
    hairtie7 = wake("Hairtie 7")
    hairtie8 = wake("Hairtie 8")
    hairtie9 = wake("Hairtie 9")
    hairtie10 = wake("Hairtie 10")
    hairtie11 = wake("Hairtie 11")
    hairtie12 = wake("Hairtie 12")
    hairtie13 = wake("Hairtie 13")
    hairtie14 = wake("Hairtie 14")
    hairtie15 = wake("Hairtie 15")
    hairtie16 = wake("Hairtie 16")
    hairtie17 = wake("Hairtie 17")
    hairtie18 = wake("Hairtie 18")
    hairtie19 = wake("Hairtie 19")
    hairtie20 = wake("Hairtie 20")
    hairtie21 = wake("Hairtie 21")
    hairtie22 = wake("Hairtie 22")
    hairtie23 = wake("Hairtie 23")
    hairtie24 = wake("Hairtie 24")
    hairtie25 = wake("Hairtie 25")
    hairtie26 = wake("Hairtie 26")
    hairtie27 = wake("Hairtie 27")
    hairtie28 = wake("Hairtie 28")
    hairtie29 = wake("Hairtie 29")
    hairtie30 = wake("Hairtie 30")
    hairtie31 = wake("Hairtie 31")
    hairtie32 = wake("Hairtie 32")
    hairtie33 = wake("Hairtie 33")
    hairtie34 = wake("Hairtie 34")
    hairtie35 = wake("Hairtie 35")
    hairtie36 = wake("Hairtie 36")
    hairtie37 = wake("Hairtie 37")
    hairtie38 = wake("Hairtie 38")
    hairtie39 = wake("Hairtie 39")
    plaidScrunchie = wake("Plaid Scrunchie")
    whiteFloralScrunchie = wake("White Floral Scrunchie")
    blackFloralScrunchie = wake("Black Floral Scrunchie")
    ginghamScrunchie = wake("Gingham Scrunchie")
    dottedScrunchie = wake("Dotted Scrunchie")
    stripedScrunchie = wake("Striped Scrunchie")
    listerineMouthWash = wake("Listerine Mouth Wash")
    ceraVeDailyMoisturizingLotion = wake("CeraVe Daily Moisturizing Lotion")
    ceraVeRenewingSACleanser = wake("CeraVe Renewing SA Cleanser")
    ceraVeFoamingFacialCleanser = wake("CeraVe Foaming Facial Cleanser")
    niveaVanillaCaramelFoamingSilkMousseBodyWash = wake("Nivea Vanilla Caramel Foaming Silk Mousse Body Wash")
    herbalEssencesShampoo = wake("Herbal Essences Shampoo")
    herbalEssencesConditioner = wake("Herbal Essences Conditioner")
    suave3in1ShampooConditionerBody = wake("Suave 3-in-1 Shampoo Conditioner Body")

    print("\n\nRELATIONSHIPS:")
    for being in state["beings"]:
        if being.connections == {}:
            continue
        print(being.name + "'s connections: ")
        for connection in being.connections:
            relationship = being.connections[connection]["relationship"]
            if relationship == "FRIEND" or relationship == "ENEMY":
                relationship += "\t"        # for alignment purposes
            print("\t" + relationship + "\t" + str(being.connections[connection]["level"]) + "\t" + connection.name)

    print("\n\nCOMMUNITIES:")
    if len(state) > 1:
        for community in state:
            if community == "beings":
                continue
            print(community + "'s members:")
            for being in state[community]:
                print("\t" + being.name)

if __name__ == '__main__':
    main()