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

    toyBlanket = wake("Blanket")

    establishCommunication(toyTrain, dogPlushDinosaur)

    wineGlass0 = wake("Wine Glass")
    cups.append(wineGlass0)

    establishCommunication(toyTrain, toyElephant)

    bentMetalStraw = wake("Bent Metal Straw")

    establishCommunication(toyTrain, toyBear)
    establishCommunication(toyBlanket, toyElephant)

    establishCommunication(toyBlanket, dogPlushDinosaur)



    wineGlass1 = wake("Wine Glass")

    establishCommunication(wineGlass0, wineGlass1)

    cups.append(wineGlass1)
    UNDMug = wake("University of Notre Dame Mug")
    cups.append(UNDMug)
    justDance2014XboxGame = wake("Just Dance 2014 Xbox Game")
    minecraftXboxGame = wake("Minecraft Xbox Game")
    dogAlligatorToy = wake("Dog Alligator Toy")

    positiveInteraction(wineGlass0, wineGlass1)

    wineGlass2 = wake("Wine Glass")
    cups.append(wineGlass2)

    positiveInteraction(computer, phone)
    
    GTAVXboxGame = wake("GTA V Xbox Game")
    starWarsMug = wake("Star Wars Mug")
    cups.append(starWarsMug)
    xboxController0 = wake("Xbox Controller")
    wineGlass3 = wake("Wine Glass")
    cups.append(wineGlass3)
    xboxController1 = wake("Xbox Controller")
    guitarHeroWorldTourXboxGame = wake("Guitar Hero World Tour Xbox Game")
    stemlessWineGlass0 = wake("Stemless Wine Glass")
    cups.append(stemlessWineGlass0)
    
    tv = wake("TV")

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

    establishCommunication(tv, xbox)

    dogPlushMonkey = wake("Dog Plush Monkey")
    fallout4XboxGame = wake("Fallout 4 Xbox Game")

    establishCommunication(tv, xboxController0)
    establishCommunication(tv, xboxController1)

    electronicsCommunity = [computer, phone, xbox, cableBox, tv, xboxController0, xboxController1]

    stemlessWineGlass2 = wake("Stemless Wine Glass")
    cups.append(stemlessWineGlass2)
    keurig = wake("Keurig")
    dogBlanket = wake("Dog Blanket")
    xboxController2 = wake("Xbox Controller")
    maddenXboxGame = wake("Madden Xbox Game")
    stemlessWineGlass3 = wake("Stemless Wine Glass")
    cups.append(stemlessWineGlass3)

    negativeInteraction(computer, phone)
    
    dogDuraforce = wake("Duraforce")
    halo5XboxGame = wake("Halo 5 Xbox Game")
    tvRemote = wake("TV Remote")
    callOfDutyModernWarfare2XboxGame = wake("Call of Duty Modern Warfare 2 Xbox Game")
    xboxController3 = wake("Xbox Controller")
    seaofThievesXboxGame = wake("Sea of Thieves Xbox Game")
    callOfDutyAdvancedWarfareXboxGame = wake("Call of Duty Advanced Warfare Xbox Game")
    pastaMaker = wake("Pasta Maker")
    legoStarWarsIIXboxGame = wake("Lego Star Wars II Xbox Game")
    dogKong = wake("Kong")
    loveseat = wake("Loveseat")
    iceCreamScoop = wake("Ice Cream Scoop")
    battlefield4XboxGame = wake("Battlefield 4 Xbox Game")
    dogRope = wake("Dog Rope")
    couch = wake("Couch")
    bowls = []
    mediumMixingBowl = wake("Medium Mixing Bowl")
    bowls.append(mediumMixingBowl)
    throwPillow0 = wake("Throw Pillow")
    largeMixingBowl = wake("Large Mixing Bowl")
    bowls.append(largeMixingBowl)
    mediumPot0 = wake("Medium Pot")
    smallMixingBowl = wake("Small Mixing Bowl")
    bowls.append(smallMixingBowl)
    whisk = wake("Whisk")
    microwave = wake("Microwave")
    throwPillow1 = wake("Throw Pillow")
    ladle = wake("Ladle")
    fridge = wake("Fridge")
    bottleOpener = wake("Bottle Opener")
    crockpot = wake("Crockpot")
    spatula0 = wake("Spatula")

    positiveInteraction(phone, computer)

    oven = wake("Oven")
    mediumPot1 = wake("Medium Pot")
    christmasOvenMitt = wake("Christmas Oven Mitt")
    spoons = []
    servingSpoon0 = wake("Serving Spoon")
    spoons.append(servingSpoon0)
    throwPillow2 = wake("Throw Pillow")
    smallPot0 = wake("Small Pot")
    toaster = wake("Toaster")
    ovenMitt0 = wake("Oven Mitt")
    spatula1 = wake("Spatula")
    mediumPot2 = wake("Medium Pot")
    ovenMitt1 = wake("Oven Mitt")
    potholder1 = wake("Potholder")
    strainer = wake("Strainer")
    dishDryingTowel0 = wake("Dish Drying Towel")
    dishSoap = wake("Dish Soap")
    largePot0 = wake("Large Pot")
    throwPillow3 = wake("Throw Pillow")
    dryingRack = wake("Drying Rack")
    sponge = wake("Sponge")
    kitchenHandSoap = wake("Hand Soap")
    sink = wake("Sink")
    potholder0 = wake("Potholder")
    
    positiveInteraction(wineGlass1, wineGlass0)
    
    smallPot1 = wake("Small Pot")
    knives = []
    chefsKnife = wake("Chef's Knife")
    knives.append(chefsKnife)
    unicornWineStopper = wake("Unicorn Wine Stopper")
    pastaDryingRack = wake("Pasta Drying Rack")

    negativeInteraction(xbox, guitarHero5XboxGame)
    
    servingSpoon1 = wake("Serving Spoon")
    spoons.append(servingSpoon1)
    rug = wake("Rug")
    largePot1 = wake("Large Pot")
    dishDryingTowel1 = wake("Dish Drying Towel")
    oneCupMeasuringCup = wake("One Cup Measuring Cup")
    straightMetalStraw = wake("Straight Metal Straw")
    babyBlueWineStopper = wake("Baby Blue Wine Stopper")
    kitchenHandTowel0 = wake("Kitchen Hand Towel")
    cherryWineStopper = wake("Cherry Wine Stopper")
    serratedKnife = wake("Serrated Knife")
    knives.append(serratedKnife)
    navyWineStopper = wake("Navy Wine Stopper")

    negativeInteraction(computer, phone)

    blanket0 = wake("Blanket")
    tablespoon = wake("Tablespoon")
    blanket1 = wake("Blanket")
    coffeeTable = wake("Coffee Table")
    kitchenTable = wake("Kitchen Table")
    dishwasher = wake("Dishwasher")
    halfCupMeasuringCup = wake("Half Cup Measuring Cup")
    chair0 = wake("Chair")
    toyBasket = wake("Toy Basket")
    chair1 = wake("Chair")
    cloroxWipes = wake("Clorox Wipes")
    teaspoon = wake("Teaspoon")
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
    seasonalPlacemat0 = wake("Seasonal Placemat")
    lamp0 = wake("Lamp")
    throwPillow4 = wake("Throw Pillow")
    tinfoil = wake("Tinfoil")
    foodScale = wake("Food Scale")
    thirdCupMeasuringCup = wake("Third Cup Measuring Cup")
    seasonalPlacemat1 = wake("Seasonal Placemat")
    lamp1 = wake("Lamp")
    chair2 = wake("Chair")
    gallonZiplockBags = wake("Gallon Ziplock Bags")
    
    positiveInteraction(wineGlass1, wineGlass0)
    
    saranWrap = wake("Saran Wrap")
    tomatoKnife = wake("Tomato Knife")
    knives.append(tomatoKnife)
    placemat0 = wake("Placemat")
    halfTeaspoon = wake("Half Teaspoon")
    bakingSheet0 = wake("Baking Sheet")
    sandwichZiplockBags = wake("Sandwich Ziplock Bags")
    kitchenTrashcan = wake("Kitchen Trashcan")
    seasonalPlacemat2 = wake("Seasonal Placemat")
    coffeePodBasket = wake("CoffeePodBasket")
    house = wake("House")
    forks = []
    largeFork0 = wake("Large Fork")
    forks.append(largeFork0)
    steakKnife0 = wake("Steak Knife")
    knives.append(steakKnife0)
    dunkinDonutsCoffeePod0 = wake("Dunkin' Donuts Coffee Pod")
    smallCup0 = wake("Small Cup")
    cups.append(smallCup0)
    dunkinDonutsCoffeePod1 = wake("Dunkin' Donuts Coffee Pod")
    steakKnife1 = wake("Steak Knife")
    knives.append(steakKnife1)
    plates = []
    smallPlate0 = wake("Small Plate")
    plates.append(smallPlate0)
    sideTable1 = wake("Side Table")
    largeFork1 = wake("Large Fork")
    forks.append(largeFork1)
    knife0 = wake("Knife")
    knives.append(knife0)
    dunkinDonutsCoffeePod2 = wake("Dunkin' Donuts Coffee Pod")
    steakKnife2 = wake("Steak Knife")
    knives.append(steakKnife2)
    dunkinDonutsCoffeePod3 = wake("Dunkin' Donuts Coffee Pod")
    largeFork2 = wake("Large Fork")

    negativeInteraction(phone, computer)

    forks.append(largeFork2)
    tallCup1 = wake("Tall Cup")
    cups.append(tallCup1)
    smallPlate1 = wake("Small Plate")
    plates.append(smallPlate1)
    seasonalPlacemat3 = wake("Seasonal Placemat")
    largeFork3 = wake("Large Fork")
    forks.append(largeFork3)
    smallCup1 = wake("Small Cup")
    cups.append(smallCup1)
    dunkinDonutsCoffeePod4 = wake("Dunkin' Donuts Coffee Pod")
    quarterTeaspoon = wake("Quarter Teaspoon")
    dunkinDonutsCoffeePod5 = wake("Dunkin' Donuts Coffee Pod")
    largeFork4 = wake("Large Fork")
    forks.append(largeFork4)
    largeSpoon0 = wake("Large Spoon")
    spoons.append(largeSpoon0)
    smallFork0 = wake("Small Fork")
    forks.append(smallFork0)
    largePlate1 = wake("Large Plate")
    plates.append(largePlate1)
    steakKnife3 = wake("Steak Knife")
    knives.append(steakKnife3)
    dunkinDonutsCoffeePod6 = wake("Dunkin' Donuts Coffee Pod")
    largeFork5 = wake("Large Fork")
    placemat1 = wake("Placemat")
    bakingSheet1 = wake("Baking Sheet")
    forks.append(largeFork5)
    paringKnife = wake("Paring Knife")
    smallFork1 = wake("Small Fork")
    forks.append(smallFork1)
    knife1 = wake("Knife")
    knives.append(knife1)
    chair3 = wake("Chair")
    largeFork6 = wake("Large Fork")
    forks.append(largeFork6)

    positiveInteraction(phone, computer)
    utilityKnife = wake("Utility Knife")
    smallFork2 = wake("Small Fork")
    forks.append(smallFork2)
    dunkinDonutsCoffeePod7 = wake("Dunkin' Donuts Coffee Pod")
    largeFork7 = wake("Large Fork")
    forks.append(largeFork7)
    placemat2 = wake("Placemat")
    tallCup0 = wake("Tall Cup")
    cups.append(tallCup0)
    largeSpoon1 = wake("Large Spoon")
    spoons.append(largeSpoon1)
    dunkinDonutsCoffeePod8 = wake("Dunkin' Donuts Coffee Pod")
    
    negativeInteraction(xbox, guitarHero5XboxGame)
    
    largeFork8 = wake("Large Fork")
    placemat3 = wake("Placemat")
    forks.append(largeFork8)
    largeSpoon2 = wake("Large Spoon")
    spoons.append(largeSpoon2)
    dunkinDonutsCoffeePod9 = wake("Dunkin' Donuts Coffee Pod")
    steakKnife4 = wake("Steak Knife")
    knives.append(steakKnife4)
    bowl0 = wake("Bowl")
    bowls.append(bowl0)
    largeSpoon3 = wake("Large Spoon")
    spoons.append(largeSpoon3)
    largeFork9 = wake("Large Fork")
    forks.append(largeFork9)
    dunkinDonutsCoffeePod10 = wake("Dunkin' Donuts Coffee Pod")
    steakKnife5 = wake("Steak Knife")
    knives.append(steakKnife5)
    knife2 = wake("Knife")
    knives.append(knife2)
    
    negativeInteraction(wineGlass1, wineGlass0)
    
    canOpener = wake("Can Opener")
    steakKnife6 = wake("Steak Knife")
    knives.append(steakKnife6)
    strawBrush = wake("Straw Brush")
    dunkinDonutsCoffeePod12 = wake("Dunkin' Donuts Coffee Pod")
    smallSpoon1 = wake("Small Spoon")
    spoons.append(smallSpoon1)
    dunkinDonutsCoffeePod11 = wake("Dunkin' Donuts Coffee Pod")
    bowl2 = wake("Bowl")
    bowls.append(bowl2)
    steakKnife7 = wake("Steak Knife")
    knives.append(steakKnife7)
    smallFork3 = wake("Small Fork")
    forks.append(smallFork3)
    dunkinDonutsCoffeePod13 = wake("Dunkin' Donuts Coffee Pod")
    knife3 = wake("Knife")
    knives.append(knife3)
    
    positiveInteraction(wineGlass0, wineGlass1)
    
    smallFork4 = wake("Small Fork")
    forks.append(smallFork4)
    dunkinDonutsCoffeePod14 = wake("Dunkin' Donuts Coffee Pod")
    smallFork5 = wake("Small Fork")
    forks.append(smallFork5)
    bowl1 = wake("Bowl")

    positiveInteraction(phone, computer)

    bowls.append(bowl1)
    dunkinDonutsCoffeePod15 = wake("Dunkin' Donuts Coffee Pod")
    smallFork6 = wake("Small Fork")
    forks.append(smallFork6)
    sideTable0 = wake("Side Table")
    smallFork7 = wake("Small Fork")
    forks.append(smallFork7)
    smallFork8 = wake("Small Fork")
    forks.append(smallFork8)
    dunkinDonutsCoffeePod16 = wake("Dunkin' Donuts Coffee Pod")
    smallFork9 = wake("Small Fork")
    forks.append(smallFork9)
    dunkinDonutsCoffeePod17 = wake("Dunkin' Donuts Coffee Pod")
    smallPlate2 = wake("Small Plate")
    
    negativeInteraction(xbox, guitarHero5XboxGame)
    
    plates.append(smallPlate2)
    knife4 = wake("Knife")
    knives.append(knife4)
    dunkinDonutsCoffeePod18 = wake("Dunkin' Donuts Coffee Pod")
    knife5 = wake("Knife")
    knives.append(knife5)
    knife6 = wake("Knife")
    knives.append(knife6)
    dunkinDonutsCoffeePod19 = wake("Dunkin' Donuts Coffee Pod")
    knife7 = wake("Knife")
    knives.append(knife7)
    knife8 = wake("Knife")
    knives.append(knife8)
    dunkinDonutsCoffeePod20 = wake("Dunkin' Donuts Coffee Pod")
    knife9 = wake("Knife")
    knives.append(knife9)
    dunkinDonutsCoffeePod21 = wake("Dunkin' Donuts Coffee Pod")
    dunkinDonutsCoffeePod22 = wake("Dunkin' Donuts Coffee Pod")
    dunkinDonutsCoffeePod23 = wake("Dunkin' Donuts Coffee Pod")
    largeSpoon4 = wake("Large Spoon")
    spoons.append(largeSpoon4)
    largeSpoon5 = wake("Large Spoon")
    spoons.append(largeSpoon5)
    largeSpoon6 = wake("Large Spoon")
    spoons.append(largeSpoon6)
    largeSpoon7 = wake("Large Spoon")
    spoons.append(largeSpoon7)
    largeSpoon8 = wake("Large Spoon")
    spoons.append(largeSpoon8)
    dunkinDonutsCoffeePod24 = wake("Dunkin' Donuts Coffee Pod")
    largeSpoon9 = wake("Large Spoon")
    spoons.append(largeSpoon9)
    dunkinDonutsCoffeePod25 = wake("Dunkin' Donuts Coffee Pod")
    smallSpoon0 = wake("Small Spoon")
    spoons.append(smallSpoon0)
    dunkinDonutsCoffeePod26 = wake("Dunkin' Donuts Coffee Pod")
    smallSpoon2 = wake("Small Spoon")
    spoons.append(smallSpoon2)
    dunkinDonutsCoffeePod27 = wake("Dunkin' Donuts Coffee Pod")
    dunkinDonutsCoffeePod28 = wake("Dunkin' Donuts Coffee Pod")
    smallSpoon3 = wake("Small Spoon")
    spoons.append(smallSpoon3)
    smallSpoon4 = wake("Small Spoon")
    spoons.append(smallSpoon4)
    dunkinDonutsCoffeePod29 = wake("Dunkin' Donuts Coffee Pod")
    smallSpoon5 = wake("Small Spoon")
    spoons.append(smallSpoon5)
    dunkinDonutsCoffeePod30 = wake("Dunkin' Donuts Coffee Pod")
    
    negativeInteraction(xbox, guitarHero5XboxGame)
    
    smallSpoon6 = wake("Small Spoon")
    spoons.append(smallSpoon6)
    smallSpoon7 = wake("Small Spoon")
    spoons.append(smallSpoon7)
    dunkinDonutsCoffeePod31 = wake("Dunkin' Donuts Coffee Pod")
    smallSpoon8 = wake("Small Spoon")

    positiveInteraction(computer, phone)

    spoons.append(smallSpoon8)
    dunkinDonutsCoffeePod32 = wake("Dunkin' Donuts Coffee Pod")
    smallSpoon9 = wake("Small Spoon")
    spoons.append(smallSpoon9)
    dunkinDonutsCoffeePod33 = wake("Dunkin' Donuts Coffee Pod")
    smallCup2 = wake("Small Cup")
    cups.append(smallCup2)
    smallCup3 = wake("Small Cup")
    cups.append(smallCup3)
    dunkinDonutsCoffeePod34 = wake("Dunkin' Donuts Coffee Pod")
    tallCup2 = wake("Tall Cup")
    
    negativeInteraction(wineGlass1, wineGlass0)
    
    cups.append(tallCup2)
    tallCup3 = wake("Tall Cup")
    cups.append(tallCup3)
    dunkinDonutsCoffeePod35 = wake("Dunkin' Donuts Coffee Pod")
    smallPlate3 = wake("Small Plate")
    plates.append(smallPlate3)
    smallPlate4 = wake("Small Plate")
    plates.append(smallPlate4)
    dunkinDonutsCoffeePod37 = wake("Dunkin' Donuts Coffee Pod")
    largePlate0 = wake("Large Plate")
    plates.append(largePlate0)
    largePlate2 = wake("Large Plate")
    plates.append(largePlate2)
    dunkinDonutsCoffeePod38 = wake("Dunkin' Donuts Coffee Pod")
    largePlate3 = wake("Large Plate")

    positiveInteraction(computer, phone)

    plates.append(largePlate3)
    dunkinDonutsCoffeePod39 = wake("Dunkin' Donuts Coffee Pod")
    largePlate4 = wake("Large Plate")
    
    positiveInteraction(wineGlass1, wineGlass0)

    plates.append(largePlate4)
    bowl3 = wake("Bowl")
    
    negativeInteraction(xbox, guitarHero5XboxGame)
    
    bowls.append(bowl3)
    bowl4 = wake("Bowl")
    bowls.append(bowl4)
    dunkinDonutsCoffeePod40 = wake("Dunkin' Donuts Coffee Pod")

    ## REST OF HOUSE ##
    
    washingMachine = wake("Washing Machine")
    dryer = wake("Dryer")
    laundryDetergent = wake("Laundry Detergent")
    dryerSheets = wake("Dryer Sheets")
    bucket = wake("Bucket")
    broom = wake("Broom")
    vacuum = wake("Vacuum")
    bathTowel0 = wake("Bath Towel")
    bathTowel1 = wake("Bath Towel")
    bathTowel2 = wake("Bath Towel")
    bathTowel3 = wake("Bath Towel")
    bathRug0 = wake("Bath Rug")
    bathRug1 = wake("Bath Rug")
    bathRug2 = wake("Bath Rug")
    bathRug3 = wake("Bath Rug")
    handSoap0 = wake("Hand Soap")
    handSoap1 = wake("Hand Soap")
    handSoap2 = wake("Hand Soap")
    toilet0 = wake("Toilet")
    toilet1 = wake("Toilet")
    toilet1 = wake("Toilet")
    shower0 = wake("Shower")
    shower1 = wake("Shower")
    showerCurtain = wake("Shower Curtain")
    showerCurtain = wake("Shower Curtain")
    greyToothbrush = wake("Grey Toothbrush")
    blueToothbrush = wake("Blue Toothbrush")
    toothbrushHolder = wake("Toothbrush Holder")
    crest3DWhiteToothpaste = wake("Crest 3D White Toothpaste")
    hairbrush0 = wake("Hairbrush")
    hairbrush1 = wake("Hairbrush")
    bathroomTrashcan0 = wake("Bathroom Trashcan")
    bathroomTrashcan1 = wake("Bathroom Trashcan")
    bathroomTrashcan2 = wake("Bathroom Trashcan")
    razor = wake("Razor")
    razor = wake("Razor")
    extraRazorHeads = wake("Extra Razor Heads")
    hairtie0 = wake("Hairtie")
    hairtie1 = wake("Hairtie")
    hairtie2 = wake("Hairtie")
    hairtie3 = wake("Hairtie")
    hairtie4 = wake("Hairtie")
    hairtie5 = wake("Hairtie")
    hairtie6 = wake("Hairtie")
    hairtie7 = wake("Hairtie")
    hairtie8 = wake("Hairtie")
    hairtie9 = wake("Hairtie")
    hairtie10 = wake("Hairtie")
    hairtie11 = wake("Hairtie")
    hairtie12 = wake("Hairtie")
    hairtie13 = wake("Hairtie")
    hairtie14 = wake("Hairtie")
    hairtie15 = wake("Hairtie")
    hairtie16 = wake("Hairtie")
    hairtie17 = wake("Hairtie")
    hairtie18 = wake("Hairtie")
    hairtie19 = wake("Hairtie")
    hairtie20 = wake("Hairtie")
    hairtie21 = wake("Hairtie")
    hairtie22 = wake("Hairtie")
    hairtie23 = wake("Hairtie")
    hairtie24 = wake("Hairtie")
    hairtie25 = wake("Hairtie")
    hairtie26 = wake("Hairtie")
    hairtie27 = wake("Hairtie")
    hairtie28 = wake("Hairtie")
    hairtie29 = wake("Hairtie")
    hairtie30 = wake("Hairtie")
    hairtie31 = wake("Hairtie")
    hairtie32 = wake("Hairtie")
    hairtie33 = wake("Hairtie")
    hairtie34 = wake("Hairtie")
    hairtie35 = wake("Hairtie")
    hairtie36 = wake("Hairtie")
    hairtie37 = wake("Hairtie")
    hairtie38 = wake("Hairtie")
    hairtie39 = wake("Hairtie")
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
                print("\t" + being)

if __name__ == '__main__':
    main()