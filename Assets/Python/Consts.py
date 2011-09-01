# Rhye's and Fall of Civilization - Constants


# globals

from CvPythonExtensions import *
gc = CyGlobalContext()

l0Array =       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
l0ArrayActive = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
l0ArrayTotal =  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

lm1Array =      [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

# initialise player variables to player IDs from WBS
iEgypt = 0
iIndia = 1
iChina = 2
iBabylonia = 3
iGreece = 4
iPersia = 5
iCarthage = 6
iRome = 7
iJapan = 8
iEthiopia = 9
iKorea = 10
iMaya = 11
iByzantium = 12
iVikings = 13
iArabia = 14
iKhmer = 15
iIndonesia = 16
iSpain = 17
iFrance = 18
iEngland = 19
iGermany = 20
iRussia = 21
iNetherlands = 22
iHolland = 22
iMali = 23
iPortugal = 24
iInca = 25
iMongolia = 26
iAztecs = 27
iTurkey = 28
iAmerica = 29
iNumPlayers = 30
iNumMajorPlayers = 30
iNumActivePlayers = 30
iIndependent = 30
iIndependent2 = 31
iNative = 32
iCeltia = 33
iNumTotalPlayers = 34
iBarbarian = 34
iNumTotalPlayersB = 35

#for Congresses and Victory
lCivGroups = [[iGreece, iRome, iByzantium, iVikings, iSpain, iFrance, iEngland, iGermany, iRussia, iNetherlands, iPortugal],  #Euros
                [iIndia, iChina, iPersia, iJapan, iKorea, iByzantium, iKhmer, iIndonesia, iRussia, iMongolia], #Asian
                [iEgypt, iBabylonia, iPersia, iArabia, iTurkey, iCarthage], #MiddleEastern
                [iEgypt, iGreece, iCarthage, iRome, iByzantium], #Mediterranean
                [iEgypt, iCarthage, iEthiopia, iMali], #African
                [iMaya, iInca, iAztecs, iAmerica]] #American

lCivStabilityGroups = [[iVikings, iSpain, iFrance, iEngland, iGermany, iRussia, iNetherlands, iPortugal],  #Euros
                [iIndia, iChina, iJapan, iKorea, iKhmer, iIndonesia, iMongolia], #Asian
                [iBabylonia, iPersia, iArabia, iTurkey], #MiddleEastern
                [iEgypt, iGreece, iCarthage, iRome, iEthiopia, iByzantium, iMali], #Mediterranean
                [iMaya, iInca, iAztecs, iAmerica]] #American


lCivBioOldWorld = [iEgypt, iIndia, iChina, iBabylonia, iGreece, iPersia, iCarthage, iRome, iJapan, \
                   iEthiopia, iKorea, iByzantium, iVikings, iArabia, iKhmer, iIndonesia, iSpain, iFrance, iEngland, iGermany, iRussia, \
                   iNetherlands, iMali, iTurkey, iPortugal, iMongolia, iAmerica, \
                   iIndependent, iIndependent2, iCeltia, iBarbarian]
lCivBioNewWorld = [iMaya, iInca, iAztecs] #, iNative]


#for Victory and the handler
tAmericasTL = (3, 0)
tAmericasBR = (43, 63)


#for messages
iDuration = 14
iWhite = 0
iRed = 7
iGreen = 8
iBlue = 9
iLightBlue = 10
iYellow = 11
iDarkPink = 12
iLightRed = 20
iPurple = 25
iCyan = 44
iBrown = 55
iOrange = 88
iTan = 90
iLime = 100

#neighbours
lNeighbours = [
[iBabylonia, iGreece, iPersia, iCarthage, iRome, iEthiopia, iByzantium, iArabia, iTurkey], #Egypt
[iChina, iPersia, iKhmer, iMongolia], #India
[iIndia, iJapan, iKorea, iKhmer, iMongolia], #China
[iEgypt, iGreece, iPersia, iTurkey, iMongolia, iCarthage, iByzantium], #Babylonia
[iPersia, iCarthage, iRome, iByzantium, iGermany, iRussia, iTurkey], #Greece
[iIndia, iBabylonia, iGreece, iByzantium, iTurkey, iMongolia, iCarthage], #Persia
[iEgypt, iGreece, iRome, iSpain, iMali, iPortugal, iBabylonia, iPersia, iArabia, iTurkey], #Carthage
[iEgypt, iBabylonia, iGreece, iCarthage, iSpain, iFrance, iGermany, iPortugal], #Rome
[iChina, iKorea, iKhmer, iMongolia], #Japan
[iEgypt, iArabia, iMali], #Ethiopia
[iChina, iJapan, iMongolia], #Korea
[iSpain, iInca, iAztecs, iAmerica], #Maya
[iEgypt, iBabylonia, iGreece, iPersia, iArabia, iRussia], #Byzantium
[iFrance, iEngland, iGermany, iRussia, iNetherlands], #Vikings
[iEgypt, iBabylonia, iPersia, iEthiopia, iByzantium, iTurkey, iCarthage], #Arabia
[iIndia, iChina, iJapan, iIndonesia], #Khmer
[iIndia, iJapan, iKhmer], #Indonesia
[iCarthage, iRome, iFrance, iEngland, iPortugal], #Spain
[iRome, iVikings, iSpain, iEngland, iGermany, iNetherlands, iPortugal], #France
[iRome, iVikings, iSpain, iFrance, iGermany, iNetherlands], #England
[iRome, iVikings, iFrance, iEngland, iRussia, iNetherlands], #Germany
[iPersia, iByzantium, iVikings, iGermany, iTurkey, iMongolia], #Russia
[iVikings, iFrance, iEngland, iGermany], #Netherlands
[iEgypt, iCarthage, iEthiopia], #Mali
[iCarthage, iRome, iSpain, iFrance], #Portugal
[iSpain, iAztecs, iAmerica], #Inca
[iIndia, iChina, iPersia, iJapan, iKorea, iRussia, iTurkey], #Mongolia
[iSpain, iInca, iAmerica], #Aztec
[iBabylonia, iGreece, iPersia, iByzantium, iRussia, iMongolia, iCarthage], #Turkey
[iJapan, iSpain, iFrance, iEngland, iRussia, iInca, iAztecs] #America
]

#for stability hit on spawn
lOlderNeighbours = [
[], #Egypt
[], #India
[], #China
[], #Babylonia
[iEgypt, iBabylonia], #Greece
[iEgypt, iBabylonia, iGreece], #Persia
[iEgypt, iBabylonia], #Carthage
[iEgypt, iGreece, iCarthage], #Rome
[], #Japan
[iEgypt], #Ethiopia
[iChina, iJapan], #Korea
[], #Maya
[iGreece], #Byzantium
[], #Vikings
[iEgypt, iPersia, iByzantium], #Arabia
[iIndia], #Khmer
[iKhmer], #Indonesia
[iCarthage, iRome], #Spain
[iRome], #France
[], #England
[iGreece, iRome, iVikings], #Germany
[iPersia, iGreece], #Russia
[iRome, iGermany], #Netherlands
[iCarthage, iEthiopia], #Mali
[iCarthage, iRome], #Portugal
[], #Inca
[iChina, iJapan, iKorea, iKhmer, iRussia], #Mongolia
[iMaya], #Aztec
[iBabylonia, iGreece, iPersia, iByzantium], #Turkey
[iSpain, iFrance, iEngland, iNetherlands, iPortugal, iAztecs, iMaya] #America
]

# civ birth dates

# converted to years - edead
tBirth = (
-3000, # 0, #3000BC
-3000, # 0, #3000BC
-3000, # 0, #3000BC
-3000, # 0, #3000BC
-1600, # 50, #1600BC
-850, # 84, #844BC
-1200, # 66, #814BC # Leoreth: 1200 BC
-753, # 90, #753BC
-660, # 97, #660BC
-300, # 121, #300BC
-50,
60, # 145, #60AD
330,
551, # 177, #551AD
620, # 183, #622AD
655, # 187, #657AD
700,
720, # 193, #718AD
750, # 196, #751AD
820, # 203, #829AD
840, # 205, #843AD
860, # 207, #860AD
1500, # 281, #922AD # Leoreth: 1500 AD
989, # 220, #989AD
1130, # 234, #1128AD
1150, # 236, #1150AD
1190, # 240, #1190AD
1200, # 241, #1195AD
1280, # 249, #1280AD (1071AD)
1775, # 346, #1775AD #332 for 1733AD
-3000, # 0,
-3000, # 0,
-3000, # 0,
-3000, # 0,
-3000, # 0)
)

# Leoreth: stability penalty from this date on
tFall = (
-343,
1206,
1271,
-539,
-146,
651,
-146,
476,
2020,
960,
1255, #Mongol invasion
900,
1204, #fourth crusade
1300,
1258,
1431, # Angkor razed by the Thais
2020,
2020,
2020,
2020,
2020, # Germany was 1648, but is kept alive until Prussia is added
2020,
2020,
1600,
2020,
1533,
1368,
1521,
2020,
2020)

# Leoreth: date-triggered respawn for certain civs
tRebirth = (
-1,
-1,
#1674,	# Maratha Empire
-1,
-1,
-1,	# Byzantium
1501,	# Safavid Persia
-1,
1167,	# Italy
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1)

# Leoreth: ID of the civilization a player is turned into on rebirth
tRebirthCiv = (
-1,
-1,
-1,
-1,
4,	# Byzantium
-1,
-1,
18,	# Italy
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1)

tRebirthPlot = (
-1,
(88,36),	# Marathas - Raigad/Mumbai
-1,
-1,
(69,44),
(81,41),	# Safavids - Esfahan
-1,
(59,46),	# Italy - Florence
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1)

tRebirthArea = (
-1,
((87,28),(94,37)),	# Maratha - Deccan
-1,
-1,
((64,45),(74,42)),	# Byzantium - Balkans, Greece, Anatolia, Levant
((78,38),(86,43)),	# Safavids - Azerbaijan, Iran, Afghanistan (no Merv, no Baghdad)
-1,
((57,45),(62,47)),	# Italy - Lombardy and Tuscany without Rome
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1)

tResurrectionIntervals = (
[(900, 1300), (1800, 2020)], #Egypt
[(1600, 1800), (1900, 2020)], #India
[(1360, 1640), (1930, 2020)], #China
[(-700, -500)], #Babylonia
[(1820, 2020)], #Greece
[(220, 650), (1500, 2020)], #Persia
[], #Carthage
[], #Rome
[(1800, 2020)], #Japan
[(1850, 2020)], #Ethiopia
[(1800, 2020)], #Korea
[], #Maya
[], #Byzantium
[(1520, 2020)], #Vikings
[(1900, 2020)], #Arabia
[(1950, 2020)], #Khmer
[(1900, 2020)], #Indonesia
[(1700, 2020)], #Spain
[(1700, 2020)], #France
[(1700, 2020)], #England
[(1870, 2020)], #Germany
[(1280, 1550), (1700, 2020)], #Russia
[(1700, 2020)], #Netherlands
[(1340, 1590)], #Mali
[(1700, 2020)], #Portugal
[], #Inca
[(1910, 2020)], #Mongolia
[], #Aztec
[(1700, 2020)], #Turkey
[(1770, 2020)] #America
)

tYear = (
("3000 ", "TXT_KEY_BC"),
("3000 ", "TXT_KEY_BC"),
("3000 ", "TXT_KEY_BC"),
("3000 ", "TXT_KEY_BC"),
("1600 ", "TXT_KEY_BC"),
("850 ", "TXT_KEY_BC"),
("1200 ", "TXT_KEY_BC"),
("760 ", "TXT_KEY_BC"),
("655 ", "TXT_KEY_BC"),
("295 ", "TXT_KEY_BC"),
("50 ", "TXT_KEY_BC"),
("65 ", "TXT_KEY_AD"),
("330 ", "TXT_KEY_AD"),
("545 ", "TXT_KEY_AD"),
("620 ", "TXT_KEY_AD"),
("660 ", "TXT_KEY_AD"),
("700 ", "TXT_KEY_AD"),
("720 ", "TXT_KEY_AD"),
("750 ", "TXT_KEY_AD"),
("820 ", "TXT_KEY_AD"),
("840 ", "TXT_KEY_AD"),
("860 ", "TXT_KEY_AD"),
("1500 ", "TXT_KEY_AD"),
("980 ", "TXT_KEY_AD"),
("1130 ", "TXT_KEY_AD"),
("1150 ", "TXT_KEY_AD"),
("1190 ", "TXT_KEY_AD"),
("1200 ", "TXT_KEY_AD"),
("1280 ", "TXT_KEY_AD"),
("1775 ", "TXT_KEY_AD"))

# edead: tGoals[iGameSpeed][iCiv][iGoal]
# Leoreth: tGoals[reborn][iGameSpeed][iCiv][iGoal]
tGoals1 = (
( # Marathon
("TXT_KEY_UHV_EGY1_MARATHON", "TXT_KEY_UHV_EGY2_MARATHON", "TXT_KEY_UHV_EGY3_MARATHON"),
("TXT_KEY_UHV_IND1", "TXT_KEY_UHV_IND2", "TXT_KEY_UHV_IND3"),
("TXT_KEY_UHV_CHI1", "TXT_KEY_UHV_CHI2", "TXT_KEY_UHV_CHI3"),
("TXT_KEY_UHV_BAB1", "TXT_KEY_UHV_BAB2_NOTURN", "TXT_KEY_UHV_BAB3_NOTURN"),
("TXT_KEY_UHV_GRE1", "TXT_KEY_UHV_GRE2_NOTURN", "TXT_KEY_UHV_GRE3"),
("TXT_KEY_UHV_PER1_NOTURN", "TXT_KEY_UHV_PER2_NOTURN", "TXT_KEY_UHV_PER3_NOTURN"),
("TXT_KEY_UHV_CAR1_NOTURN", "TXT_KEY_UHV_CAR2_NOTURN", "TXT_KEY_UHV_CAR3"),
("TXT_KEY_UHV_ROM1_NOTURN", "TXT_KEY_UHV_ROM2_NOTURN", "TXT_KEY_UHV_ROM3"),
("TXT_KEY_UHV_JAP1", "TXT_KEY_UHV_JAP2", "TXT_KEY_UHV_JAP3"),
("TXT_KEY_UHV_ETH1", "TXT_KEY_UHV_ETH2", "TXT_KEY_UHV_ETH3"),
("TXT_KEY_UHV_KOR1", "TXT_KEY_UHV_KOR2", "TXT_KEY_UHV_KOR3"),
("TXT_KEY_UHV_MAY1_NOTURN", "TXT_KEY_UHV_MAY2", "TXT_KEY_UHV_MAY3"),
("TXT_KEY_UHV_BYZ1", "TXT_KEY_UHV_BYZ2", "TXT_KEY_UHV_BYZ3"),
("TXT_KEY_UHV_VIK1_MARATHON", "TXT_KEY_UHV_VIK2", "TXT_KEY_UHV_VIK3"),
("TXT_KEY_UHV_ARA1", "TXT_KEY_UHV_ARA2", "TXT_KEY_UHV_ARA3"),
("TXT_KEY_UHV_KHM1_MARATHON", "TXT_KEY_UHV_KHM2", "TXT_KEY_UHV_KHM3"),
("TXT_KEY_UHV_INO1", "TXT_KEY_UHV_INO2", "TXT_KEY_UHV_INO3"),
("TXT_KEY_UHV_SPA1", "TXT_KEY_UHV_SPA2", "TXT_KEY_UHV_SPA3"),
("TXT_KEY_UHV_FRA1", "TXT_KEY_UHV_FRA2", "TXT_KEY_UHV_FRA3"),
("TXT_KEY_UHV_ENG1", "TXT_KEY_UHV_ENG2", "TXT_KEY_UHV_ENG3"),
("TXT_KEY_UHV_GER1", "TXT_KEY_UHV_GER2", "TXT_KEY_UHV_GER3"),
("TXT_KEY_UHV_RUS1", "TXT_KEY_UHV_RUS2", "TXT_KEY_UHV_RUS3"),
("TXT_KEY_UHV_HOL1", "TXT_KEY_UHV_HOL2", "TXT_KEY_UHV_HOL3"),
("TXT_KEY_UHV_MAL1", "TXT_KEY_UHV_MAL2_MARATHON", "TXT_KEY_UHV_MAL3_MARATHON"),
("TXT_KEY_UHV_POR1", "TXT_KEY_UHV_POR2", "TXT_KEY_UHV_POR3"),
("TXT_KEY_UHV_INC1", "TXT_KEY_UHV_INC2_MARATHON", "TXT_KEY_UHV_INC3"),
("TXT_KEY_UHV_MON1", "TXT_KEY_UHV_MON2", "TXT_KEY_UHV_MON3"),
("TXT_KEY_UHV_AZT1", "TXT_KEY_UHV_AZT2", "TXT_KEY_UHV_AZT3"),
("TXT_KEY_UHV_TUR1", "TXT_KEY_UHV_TUR2", "TXT_KEY_UHV_TUR3"),
("TXT_KEY_UHV_AME1", "TXT_KEY_UHV_AME2", "TXT_KEY_UHV_AME3")
),
( # Epic
("TXT_KEY_UHV_EGY1_EPIC", "TXT_KEY_UHV_EGY2_EPIC", "TXT_KEY_UHV_EGY3_EPIC"),
("TXT_KEY_UHV_IND1", "TXT_KEY_UHV_IND2", "TXT_KEY_UHV_IND3"),
("TXT_KEY_UHV_CHI1", "TXT_KEY_UHV_CHI2", "TXT_KEY_UHV_CHI3"),
("TXT_KEY_UHV_BAB1", "TXT_KEY_UHV_BAB2_NOTURN", "TXT_KEY_UHV_BAB3_NOTURN"),
("TXT_KEY_UHV_GRE1", "TXT_KEY_UHV_GRE2_NOTURN", "TXT_KEY_UHV_GRE3"),
("TXT_KEY_UHV_PER1_NOTURN", "TXT_KEY_UHV_PER2_NOTURN", "TXT_KEY_UHV_PER3_NOTURN"),
("TXT_KEY_UHV_CAR1_NOTURN", "TXT_KEY_UHV_CAR2_NOTURN", "TXT_KEY_UHV_CAR3"),
("TXT_KEY_UHV_ROM1_NOTURN", "TXT_KEY_UHV_ROM2_NOTURN", "TXT_KEY_UHV_ROM3"),
("TXT_KEY_UHV_JAP1", "TXT_KEY_UHV_JAP2", "TXT_KEY_UHV_JAP3"),
("TXT_KEY_UHV_ETH1", "TXT_KEY_UHV_ETH2", "TXT_KEY_UHV_ETH3"),
("TXT_KEY_UHV_KOR1", "TXT_KEY_UHV_KOR2", "TXT_KEY_UHV_KOR3"),
("TXT_KEY_UHV_MAY1", "TXT_KEY_UHV_MAY2", "TXT_KEY_UHV_MAY3"),
("TXT_KEY_UHV_BYZ1", "TXT_KEY_UHV_BYZ2", "TXT_KEY_UHV_BYZ3"),
("TXT_KEY_UHV_VIK1_EPIC", "TXT_KEY_UHV_VIK2", "TXT_KEY_UHV_VIK3"),
("TXT_KEY_UHV_ARA1", "TXT_KEY_UHV_ARA2", "TXT_KEY_UHV_ARA3"),
("TXT_KEY_UHV_KHM1_EPIC", "TXT_KEY_UHV_KHM2", "TXT_KEY_UHV_KHM3"),
("TXT_KEY_UHV_INO1", "TXT_KEY_UHV_INO2", "TXT_KEY_UHV_INO3"),
("TXT_KEY_UHV_SPA1", "TXT_KEY_UHV_SPA2", "TXT_KEY_UHV_SPA3"),
("TXT_KEY_UHV_FRA1", "TXT_KEY_UHV_FRA2", "TXT_KEY_UHV_FRA3"),
("TXT_KEY_UHV_ENG1", "TXT_KEY_UHV_ENG2", "TXT_KEY_UHV_ENG3"),
("TXT_KEY_UHV_GER1", "TXT_KEY_UHV_GER2", "TXT_KEY_UHV_GER3"),
("TXT_KEY_UHV_RUS1", "TXT_KEY_UHV_RUS2", "TXT_KEY_UHV_RUS3"),
("TXT_KEY_UHV_HOL1", "TXT_KEY_UHV_HOL2", "TXT_KEY_UHV_HOL3"),
("TXT_KEY_UHV_MAL1", "TXT_KEY_UHV_MAL2_EPIC", "TXT_KEY_UHV_MAL3_EPIC"),
("TXT_KEY_UHV_POR1", "TXT_KEY_UHV_POR2", "TXT_KEY_UHV_POR3"),
("TXT_KEY_UHV_INC1", "TXT_KEY_UHV_INC2_EPIC", "TXT_KEY_UHV_INC3"),
("TXT_KEY_UHV_MON1", "TXT_KEY_UHV_MON2", "TXT_KEY_UHV_MON3"),
("TXT_KEY_UHV_AZT1", "TXT_KEY_UHV_AZT2", "TXT_KEY_UHV_AZT3"),
("TXT_KEY_UHV_TUR1", "TXT_KEY_UHV_TUR2", "TXT_KEY_UHV_TUR3"),
("TXT_KEY_UHV_AME1", "TXT_KEY_UHV_AME2", "TXT_KEY_UHV_AME3")
),
( # Normal
("TXT_KEY_UHV_EGY1", "TXT_KEY_UHV_EGY2", "TXT_KEY_UHV_EGY3"),
("TXT_KEY_UHV_IND1", "TXT_KEY_UHV_IND2", "TXT_KEY_UHV_IND3"),
("TXT_KEY_UHV_CHI1", "TXT_KEY_UHV_CHI2", "TXT_KEY_UHV_CHI3"),
("TXT_KEY_UHV_BAB1", "TXT_KEY_UHV_BAB2", "TXT_KEY_UHV_BAB3"),
("TXT_KEY_UHV_GRE1", "TXT_KEY_UHV_GRE2", "TXT_KEY_UHV_GRE3"),
("TXT_KEY_UHV_PER1", "TXT_KEY_UHV_PER2", "TXT_KEY_UHV_PER3"),
("TXT_KEY_UHV_CAR1", "TXT_KEY_UHV_CAR2", "TXT_KEY_UHV_CAR3"),
("TXT_KEY_UHV_ROM1", "TXT_KEY_UHV_ROM2", "TXT_KEY_UHV_ROM3"),
("TXT_KEY_UHV_JAP1", "TXT_KEY_UHV_JAP2", "TXT_KEY_UHV_JAP3"),
("TXT_KEY_UHV_ETH1", "TXT_KEY_UHV_ETH2", "TXT_KEY_UHV_ETH3"),
("TXT_KEY_UHV_KOR1", "TXT_KEY_UHV_KOR2", "TXT_KEY_UHV_KOR3"),
("TXT_KEY_UHV_MAY1", "TXT_KEY_UHV_MAY2", "TXT_KEY_UHV_MAY3"),
("TXT_KEY_UHV_BYZ1", "TXT_KEY_UHV_BYZ2", "TXT_KEY_UHV_BYZ3"),
("TXT_KEY_UHV_VIK1", "TXT_KEY_UHV_VIK2", "TXT_KEY_UHV_VIK3"),
("TXT_KEY_UHV_ARA1", "TXT_KEY_UHV_ARA2", "TXT_KEY_UHV_ARA3"),
("TXT_KEY_UHV_KHM1", "TXT_KEY_UHV_KHM2", "TXT_KEY_UHV_KHM3"),
("TXT_KEY_UHV_INO1", "TXT_KEY_UHV_INO2", "TXT_KEY_UHV_INO3"),
("TXT_KEY_UHV_SPA1", "TXT_KEY_UHV_SPA2", "TXT_KEY_UHV_SPA3"),
("TXT_KEY_UHV_FRA1", "TXT_KEY_UHV_FRA2", "TXT_KEY_UHV_FRA3"),
("TXT_KEY_UHV_ENG1", "TXT_KEY_UHV_ENG2", "TXT_KEY_UHV_ENG3"),
("TXT_KEY_UHV_GER1", "TXT_KEY_UHV_GER2", "TXT_KEY_UHV_GER3"),
("TXT_KEY_UHV_RUS1", "TXT_KEY_UHV_RUS2", "TXT_KEY_UHV_RUS3"),
("TXT_KEY_UHV_HOL1", "TXT_KEY_UHV_HOL2", "TXT_KEY_UHV_HOL3"),
("TXT_KEY_UHV_MAL1", "TXT_KEY_UHV_MAL2", "TXT_KEY_UHV_MAL3"),
("TXT_KEY_UHV_POR1", "TXT_KEY_UHV_POR2", "TXT_KEY_UHV_POR3"),
("TXT_KEY_UHV_INC1", "TXT_KEY_UHV_INC2", "TXT_KEY_UHV_INC3"),
("TXT_KEY_UHV_MON1", "TXT_KEY_UHV_MON2", "TXT_KEY_UHV_MON3"),
("TXT_KEY_UHV_AZT1", "TXT_KEY_UHV_AZT2", "TXT_KEY_UHV_AZT3"),
("TXT_KEY_UHV_TUR1", "TXT_KEY_UHV_TUR2", "TXT_KEY_UHV_TUR3"),
("TXT_KEY_UHV_AME1", "TXT_KEY_UHV_AME2", "TXT_KEY_UHV_AME3")
)
)

tGoals2 = (
( # Marathon
("TXT_KEY_UHV_EGY1_MARATHON", "TXT_KEY_UHV_EGY2_MARATHON", "TXT_KEY_UHV_EGY3_MARATHON"),
("TXT_KEY_UHV_IND1", "TXT_KEY_UHV_IND2", "TXT_KEY_UHV_IND3"),
("TXT_KEY_UHV_CHI1", "TXT_KEY_UHV_CHI2", "TXT_KEY_UHV_CHI3"),
("TXT_KEY_UHV_BAB1", "TXT_KEY_UHV_BAB2_NOTURN", "TXT_KEY_UHV_BAB3_NOTURN"),
("TXT_KEY_UHV_GRE1", "TXT_KEY_UHV_GRE2_NOTURN", "TXT_KEY_UHV_GRE3"),
("TXT_KEY_UHV_PER1_NOTURN", "TXT_KEY_UHV_PER2_NOTURN", "TXT_KEY_UHV_PER3_NOTURN"),
("TXT_KEY_UHV_CAR1_NOTURN", "TXT_KEY_UHV_CAR2_NOTURN", "TXT_KEY_UHV_CAR3"),
("TXT_KEY_UHV_ITA1", "TXT_KEY_UHV_ITA2", "TXT_KEY_UHV_ITA3"),
("TXT_KEY_UHV_JAP1", "TXT_KEY_UHV_JAP2", "TXT_KEY_UHV_JAP3"),
("TXT_KEY_UHV_ETH1", "TXT_KEY_UHV_ETH2", "TXT_KEY_UHV_ETH3"),
("TXT_KEY_UHV_KOR1", "TXT_KEY_UHV_KOR2", "TXT_KEY_UHV_KOR3"),
("TXT_KEY_UHV_MAY1_NOTURN", "TXT_KEY_UHV_MAY2", "TXT_KEY_UHV_MAY3"),
("TXT_KEY_UHV_BYZ1", "TXT_KEY_UHV_BYZ2", "TXT_KEY_UHV_BYZ3"),
("TXT_KEY_UHV_VIK1_MARATHON", "TXT_KEY_UHV_VIK2", "TXT_KEY_UHV_VIK3"),
("TXT_KEY_UHV_ARA1", "TXT_KEY_UHV_ARA2", "TXT_KEY_UHV_ARA3"),
("TXT_KEY_UHV_KHM1_MARATHON", "TXT_KEY_UHV_KHM2", "TXT_KEY_UHV_KHM3"),
("TXT_KEY_UHV_INO1", "TXT_KEY_UHV_INO2", "TXT_KEY_UHV_INO3"),
("TXT_KEY_UHV_SPA1", "TXT_KEY_UHV_SPA2", "TXT_KEY_UHV_SPA3"),
("TXT_KEY_UHV_FRA1", "TXT_KEY_UHV_FRA2", "TXT_KEY_UHV_FRA3"),
("TXT_KEY_UHV_ENG1", "TXT_KEY_UHV_ENG2", "TXT_KEY_UHV_ENG3"),
("TXT_KEY_UHV_GER1", "TXT_KEY_UHV_GER2", "TXT_KEY_UHV_GER3"),
("TXT_KEY_UHV_RUS1", "TXT_KEY_UHV_RUS2", "TXT_KEY_UHV_RUS3"),
("TXT_KEY_UHV_HOL1", "TXT_KEY_UHV_HOL2", "TXT_KEY_UHV_HOL3"),
("TXT_KEY_UHV_MAL1", "TXT_KEY_UHV_MAL2_MARATHON", "TXT_KEY_UHV_MAL3_MARATHON"),
("TXT_KEY_UHV_POR1", "TXT_KEY_UHV_POR2", "TXT_KEY_UHV_POR3"),
("TXT_KEY_UHV_INC1", "TXT_KEY_UHV_INC2_MARATHON", "TXT_KEY_UHV_INC3"),
("TXT_KEY_UHV_MON1", "TXT_KEY_UHV_MON2", "TXT_KEY_UHV_MON3"),
("TXT_KEY_UHV_AZT1", "TXT_KEY_UHV_AZT2", "TXT_KEY_UHV_AZT3"),
("TXT_KEY_UHV_TUR1", "TXT_KEY_UHV_TUR2", "TXT_KEY_UHV_TUR3"),
("TXT_KEY_UHV_AME1", "TXT_KEY_UHV_AME2", "TXT_KEY_UHV_AME3")
),
( # Epic
("TXT_KEY_UHV_EGY1_EPIC", "TXT_KEY_UHV_EGY2_EPIC", "TXT_KEY_UHV_EGY3_EPIC"),
("TXT_KEY_UHV_IND1", "TXT_KEY_UHV_IND2", "TXT_KEY_UHV_IND3"),
("TXT_KEY_UHV_CHI1", "TXT_KEY_UHV_CHI2", "TXT_KEY_UHV_CHI3"),
("TXT_KEY_UHV_BAB1", "TXT_KEY_UHV_BAB2_NOTURN", "TXT_KEY_UHV_BAB3_NOTURN"),
("TXT_KEY_UHV_GRE1", "TXT_KEY_UHV_GRE2_NOTURN", "TXT_KEY_UHV_GRE3"),
("TXT_KEY_UHV_PER1_NOTURN", "TXT_KEY_UHV_PER2_NOTURN", "TXT_KEY_UHV_PER3_NOTURN"),
("TXT_KEY_UHV_CAR1_NOTURN", "TXT_KEY_UHV_CAR2_NOTURN", "TXT_KEY_UHV_CAR3"),
("TXT_KEY_UHV_ITA1", "TXT_KEY_UHV_ITA2", "TXT_KEY_UHV_ITA3"),
("TXT_KEY_UHV_JAP1", "TXT_KEY_UHV_JAP2", "TXT_KEY_UHV_JAP3"),
("TXT_KEY_UHV_ETH1", "TXT_KEY_UHV_ETH2", "TXT_KEY_UHV_ETH3"),
("TXT_KEY_UHV_KOR1", "TXT_KEY_UHV_KOR2", "TXT_KEY_UHV_KOR3"),
("TXT_KEY_UHV_MAY1", "TXT_KEY_UHV_MAY2", "TXT_KEY_UHV_MAY3"),
("TXT_KEY_UHV_BYZ1", "TXT_KEY_UHV_BYZ2", "TXT_KEY_UHV_BYZ3"),
("TXT_KEY_UHV_VIK1_EPIC", "TXT_KEY_UHV_VIK2", "TXT_KEY_UHV_VIK3"),
("TXT_KEY_UHV_ARA1", "TXT_KEY_UHV_ARA2", "TXT_KEY_UHV_ARA3"),
("TXT_KEY_UHV_KHM1_EPIC", "TXT_KEY_UHV_KHM2", "TXT_KEY_UHV_KHM3"),
("TXT_KEY_UHV_INO1", "TXT_KEY_UHV_INO2", "TXT_KEY_UHV_INO3"),
("TXT_KEY_UHV_SPA1", "TXT_KEY_UHV_SPA2", "TXT_KEY_UHV_SPA3"),
("TXT_KEY_UHV_FRA1", "TXT_KEY_UHV_FRA2", "TXT_KEY_UHV_FRA3"),
("TXT_KEY_UHV_ENG1", "TXT_KEY_UHV_ENG2", "TXT_KEY_UHV_ENG3"),
("TXT_KEY_UHV_GER1", "TXT_KEY_UHV_GER2", "TXT_KEY_UHV_GER3"),
("TXT_KEY_UHV_RUS1", "TXT_KEY_UHV_RUS2", "TXT_KEY_UHV_RUS3"),
("TXT_KEY_UHV_HOL1", "TXT_KEY_UHV_HOL2", "TXT_KEY_UHV_HOL3"),
("TXT_KEY_UHV_MAL1", "TXT_KEY_UHV_MAL2_EPIC", "TXT_KEY_UHV_MAL3_EPIC"),
("TXT_KEY_UHV_POR1", "TXT_KEY_UHV_POR2", "TXT_KEY_UHV_POR3"),
("TXT_KEY_UHV_INC1", "TXT_KEY_UHV_INC2_EPIC", "TXT_KEY_UHV_INC3"),
("TXT_KEY_UHV_MON1", "TXT_KEY_UHV_MON2", "TXT_KEY_UHV_MON3"),
("TXT_KEY_UHV_AZT1", "TXT_KEY_UHV_AZT2", "TXT_KEY_UHV_AZT3"),
("TXT_KEY_UHV_TUR1", "TXT_KEY_UHV_TUR2", "TXT_KEY_UHV_TUR3"),
("TXT_KEY_UHV_AME1", "TXT_KEY_UHV_AME2", "TXT_KEY_UHV_AME3")
),
( # Normal
("TXT_KEY_UHV_EGY1", "TXT_KEY_UHV_EGY2", "TXT_KEY_UHV_EGY3"),
("TXT_KEY_UHV_IND1", "TXT_KEY_UHV_IND2", "TXT_KEY_UHV_IND3"),
("TXT_KEY_UHV_CHI1", "TXT_KEY_UHV_CHI2", "TXT_KEY_UHV_CHI3"),
("TXT_KEY_UHV_BAB1", "TXT_KEY_UHV_BAB2", "TXT_KEY_UHV_BAB3"),
("TXT_KEY_UHV_GRE1", "TXT_KEY_UHV_GRE2", "TXT_KEY_UHV_GRE3"),
("TXT_KEY_UHV_PER1", "TXT_KEY_UHV_PER2", "TXT_KEY_UHV_PER3"),
("TXT_KEY_UHV_CAR1", "TXT_KEY_UHV_CAR2", "TXT_KEY_UHV_CAR3"),
("TXT_KEY_UHV_ITA1", "TXT_KEY_UHV_ITA2", "TXT_KEY_UHV_ITA3"),
("TXT_KEY_UHV_JAP1", "TXT_KEY_UHV_JAP2", "TXT_KEY_UHV_JAP3"),
("TXT_KEY_UHV_ETH1", "TXT_KEY_UHV_ETH2", "TXT_KEY_UHV_ETH3"),
("TXT_KEY_UHV_KOR1", "TXT_KEY_UHV_KOR2", "TXT_KEY_UHV_KOR3"),
("TXT_KEY_UHV_MAY1", "TXT_KEY_UHV_MAY2", "TXT_KEY_UHV_MAY3"),
("TXT_KEY_UHV_BYZ1", "TXT_KEY_UHV_BYZ2", "TXT_KEY_UHV_BYZ3"),
("TXT_KEY_UHV_VIK1", "TXT_KEY_UHV_VIK2", "TXT_KEY_UHV_VIK3"),
("TXT_KEY_UHV_ARA1", "TXT_KEY_UHV_ARA2", "TXT_KEY_UHV_ARA3"),
("TXT_KEY_UHV_KHM1", "TXT_KEY_UHV_KHM2", "TXT_KEY_UHV_KHM3"),
("TXT_KEY_UHV_INO1", "TXT_KEY_UHV_INO2", "TXT_KEY_UHV_INO3"),
("TXT_KEY_UHV_SPA1", "TXT_KEY_UHV_SPA2", "TXT_KEY_UHV_SPA3"),
("TXT_KEY_UHV_FRA1", "TXT_KEY_UHV_FRA2", "TXT_KEY_UHV_FRA3"),
("TXT_KEY_UHV_ENG1", "TXT_KEY_UHV_ENG2", "TXT_KEY_UHV_ENG3"),
("TXT_KEY_UHV_GER1", "TXT_KEY_UHV_GER2", "TXT_KEY_UHV_GER3"),
("TXT_KEY_UHV_RUS1", "TXT_KEY_UHV_RUS2", "TXT_KEY_UHV_RUS3"),
("TXT_KEY_UHV_HOL1", "TXT_KEY_UHV_HOL2", "TXT_KEY_UHV_HOL3"),
("TXT_KEY_UHV_MAL1", "TXT_KEY_UHV_MAL2", "TXT_KEY_UHV_MAL3"),
("TXT_KEY_UHV_POR1", "TXT_KEY_UHV_POR2", "TXT_KEY_UHV_POR3"),
("TXT_KEY_UHV_INC1", "TXT_KEY_UHV_INC2", "TXT_KEY_UHV_INC3"),
("TXT_KEY_UHV_MON1", "TXT_KEY_UHV_MON2", "TXT_KEY_UHV_MON3"),
("TXT_KEY_UHV_AZT1", "TXT_KEY_UHV_AZT2", "TXT_KEY_UHV_AZT3"),
("TXT_KEY_UHV_TUR1", "TXT_KEY_UHV_TUR2", "TXT_KEY_UHV_TUR3"),
("TXT_KEY_UHV_AME1", "TXT_KEY_UHV_AME2", "TXT_KEY_UHV_AME3")
)
)

tGoals = (tGoals1, tGoals2)


# date waypoints - now obsolete-edead

# i3000BC = 0
# i2250BC = 25
# i2085BC = 31
# i2000BC = 34
# i1800BC = 42
# i1600BC = 50
# i1000BC = 74
# i850BC = 84
# i700BC = 94
# i650BC = 97
# i600BC = 101
# i483BC = 108
# i479BC = 109
# i400BC = 114 #new timeline
# i350BC = 117
# i250BC = 124 #new timeline
# i210BC = 127
# i110BC = 133
# i100BC = 134 #new timeline
# i10BC = 140
# i33AD = 143
# i50AD = 144
# i140AD = 150 #new timeline
# i170AD = 152
# i190AD = 153
# i200AD = 154 #new timeline
# i250AD = 157
# i300AD = 161
# i350AD = 164
# i450AD = 171
# i470AD = 172 #new timeline
# i476AD = 172
# i500AD = 174 #new timeline
# i550AD = 177
# i600AD = 181
# i622AD = 183
# i690AD = 190
# i700AD = 191
# i860AD = 207
# i900AD = 211
# i920AD = 213
# i1000AD = 221
# i1100AD = 231
# i1140AD = 235
# i1190AD = 240
# i1200AD = 241
# i1250AD = 246
# i1300AD = 251
# i1350AD = 256
# i1400AD = 261
# i1450AD = 271
# i1500AD = 281
# i1600AD = 301
# i1607AD = 302
# i1650AD = 311
# i1700AD = 321
# i1715AD = 326
# i1730AD = 331
# i1745AD = 336
# i1760AD = 341
# i1775AD = 346
# i1800AD = 355
# i1820AD = 361
# i1850AD = 372
# i1860AD = 377
# i1870AD = 382
# i1880AD = 387
# i1900AD = 397
# i1910AD = 402
# i1918AD = 406
# i1930AD = 412
# i1940AD = 420
# i1950AD = 430
# i2000AD = 480

iEurope = gc.getMap().plot(55, 50).getArea()
iAfrica = gc.getMap().plot(72, 29).getArea()
iAsia = gc.getMap().plot(102, 47).getArea()

lMiddleEast = []
lEastIndies = []
lNorthAfrica = []
lConstantinople = []

# North Africa
for i in range(48,65+1):
	for j in range(35,39+1):
		lNorthAfrica.append((i,j))

for i in range(66,71+1):
	for j in range(29,37+1):
		lNorthAfrica.append((i,j))

for i in range(72,73+1):
	for j in range(29,32+1):
		lNorthAfrica.append((i,j))

# Middle East
for i in range(72,86+1):
	for j in range(34,46+1):
		lMiddleEast.append((i,j))

for i in range(69,71+1):
	for j in range(40,45+1):
		lMiddleEast.append((i,j))

for i in range(78,86+1):
	for j in range(47,49+1):
		lMiddleEast.append((i,j))
		

# starting locations coordinates
tCapitals = (
((69, 33), #tThebes
(90, 40), #tDelhi
(102, 47), #tBeijing
(76, 40), #tBabylon
(67, 41), #tAthens
(82, 39), #tPersepolis
#(58, 39), #tCarthage
(73, 40), #tSur
(60, 44), #tRome
(113, 45), #tKyoto
(72, 29), #tAksum
(109, 46), #tSeoul
(22, 35), #tTikal
(68, 45), #tConstantinople
#(61, 62), #tNidaros
(60, 59), #tOslo
(75, 33), #tMecca
#(102, 34), #tAngkor
(102, 33), #tAngkor
(100, 26), #Palembang
(52, 43), #tMadrid
(55, 50), #tParis
(53, 54), #tLondon
#(62, 52), #tBerlin
(63, 49), #tVienna
(73, 54), #tMoskow
(57, 53), #tAmsterdam
(53, 31), #tTimbuktu
(49, 43), #tLisboa
(28, 22), #tCuzco
(99, 51), #tKarakorum
(18, 37), #tTenochtitlan
(70, 43), #tSogut ((72, 43), #tKonya  #71?)
(27, 46) #tWashington
),
((69, 33), #tThebes
(90, 40), #tDelhi
(102, 47), #tBeijing
(76, 40), #tBabylon
(67, 41), #tAthens
(81, 41), #Esfahan
#(58, 39), #tCarthage
(73, 40), #tSur
(60, 44), #tRome
(113, 45), #tKyoto
(72, 29), #tAksum
(109, 46), #tSeoul
(22, 35), #tTikal
(68, 45), #tConstantinople
#(61, 62), #tNidaros
(60, 59), #tOslo
(75, 33), #tMecca
#(102, 34), #tAngkor
(102, 33), #tAngkor
(100, 26), #Palembang
(52, 43), #tMadrid
(55, 50), #tParis
(53, 54), #tLondon
#(62, 52), #tBerlin
(63, 49), #tVienna
(73, 54), #tMoskow
(57, 53), #tAmsterdam
(53, 31), #tTimbuktu
(49, 43), #tLisboa
(28, 22), #tCuzco
(99, 51), #tKarakorum
(18, 37), #tTenochtitlan
(70, 43), #tSogut ((72, 43), #tKonya  #71?)
(27, 46) #tWashington
)) 

#for minor civs
tReserveCapitals = (
(), 
(), 
(), 
(), 
(), 
(), 
(), 
(), 
(),
(), 
(),
(), 
(), 
(), 
(), 
(), 
(), 
(),
(), 
(), 
(), 
(), 
(), #((57, 52), (56, 52), (58, 53)), #tAmsterdam
(), 
(), #((49, 42), (49, 44)) #tLisboa
(),
(),
(),
(),
(), 
)

#core areas (for RiseAndFall and Victory)

tCoreAreasTL = (
((66, 30), #Egypt
(87, 33), #India
(99, 43), #China 
(75, 38), #Babylonia
(65, 39), #Greece
(79, 37), #Persia
(71, 39), #Carthage
(59, 41), #Rome
(111, 41), #Japan
(69, 27), #Ethiopia
(108, 45), #Korea
(20, 35), #Maya
(64, 38), #Byzantium
(57, 57), #Vikings
(73, 30), #Arabia
(100, 32), #Khmer
(98, 24), #Indonesia
(49, 40), #Spain
(54, 47), #France
(50, 53), #England
(59, 48), #Germany
(67, 50), #Russia
(56, 52), #Holland
(49, 26), #Mali
(44, 42), #Portugal
(24, 18), #Inca
(87, 46), #Mongolia
(15, 36), #Aztecs
(69, 41), #Turkey
(26, 42) #America
),
((66, 30), #Egypt
(87, 33), #India
(99, 43), #China 
(75, 38), #Babylonia
(65, 39), #Greece
(79, 37), #Persia
(71, 39), #Carthage
(58, 45), #Rome		# ITALY (now doesn't include southern italy because that apparently causes a crash with Byzantine or independent Naples?)
(111, 41), #Japan
(69, 27), #Ethiopia
(108, 45), #Korea
(20, 35), #Maya
(64, 41), #Byzantium
(57, 57), #Vikings
(73, 30), #Arabia
(100, 32), #Khmer
(98, 24), #Indonesia
(49, 40), #Spain
(54, 47), #France
(50, 53), #England
(59, 48), #Germany
(67, 50), #Russia
(56, 52), #Holland
(49, 26), #Mali
(44, 42), #Portugal
(24, 18), #Inca
(87, 46), #Mongolia
(15, 36), #Aztecs
(69, 41), #Turkey
(26, 42) #America
)) 

tCoreAreasBR = (
((70, 36), #Egypt
(94, 40), #India
(107, 47), #China
(77, 42), #Babylonia
(70, 44), #Greece
(85, 44), #Persia
(74, 41), #Carthage
(63, 47), #Rome
(116, 49), #Japan
(73, 30), #Ethiopia
(110, 49), #Korea
(23, 37), #Maya
(74, 45), #Byzantium
(70, 65), #Vikings
(81, 39), #Arabia
(103, 36), #Khmer
(107, 31), #Indonesia
(55, 46), #Spain
(57, 52), #France
(54, 60), #England   57 without Scotland
(66, 54), #Germany
(74, 57), #Russia
(58, 53), #Holland
(57, 31), #Mali
(50, 44), #Portugal
(29, 24), #Inca
(105, 58), #Mongolia
(20, 41), #Aztecs
(78, 48), #Turkey
(31, 48) #America
),
((70, 36), #Egypt
(94, 40), #India
(107, 47), #China
(77, 42), #Babylonia
(70, 44), #Greece
(85, 44), #Persia
(74, 41), #Carthage
(63, 47), #Rome
(116, 49), #Japan
(73, 30), #Ethiopia
(110, 49), #Korea
(23, 37), #Maya
(74, 45), #Byzantium
(70, 65), #Vikings
(81, 39), #Arabia
(103, 36), #Khmer
(107, 31), #Indonesia
(55, 46), #Spain
(57, 52), #France
(54, 60), #England   57 without Scotland
(66, 54), #Germany
(74, 57), #Russia
(58, 53), #Holland
(57, 31), #Mali
(50, 44), #Portugal
(29, 24), #Inca
(105, 58), #Mongolia
(20, 41), #Aztecs
(78, 48), #Turkey
(31, 48) #America
))


tExceptions = (  #for RiseAndFall
((), #Egypt
(), #India
(), #China
((78, 41), (78, 42)), #Babylonia
(), #Greece
(), #Persia
(),#(73, 40), (73, 41)), #Carthage
(), #Rome
(), #Japan
(), #Ethiopia
(), #Korea
(), #Maya
((65,40), (66,40)), #Byzantium
((59, 55), (60, 55), (62, 55), (59, 56), (62, 56), (63, 56)), #Vikings
((82, 34), (73, 40), (74, 40), (75, 40), (71, 36), (72, 37)),  #Arabia
(), #Khmer
(), #Indonesia (should probably exclude Borneo)
(), #Spain
((51, 50), (52, 49), (52, 50), (53, 47), (53, 48), (53, 49), (53, 50), (53, 51), (55, 46), (56, 46), (57, 46), (56, 45), (57, 45), (58, 48), (58, 49), (58, 50)), #France
(), #England
((62, 47), (63, 47), (64, 47), (58, 51), (58, 52), (58, 53), (57, 53), (65, 55), (66, 55), (66, 56)),  #Germany
((68, 58), (69, 58), (70, 58), (65, 55), (66, 55), (66, 56)), #Russia
((57, 51), (58, 51)), #Holland
(), #Mali
(), #Portugal
(), #Inca
((90, 47), (91, 47), (92, 47), (93, 47), (94, 47), (95, 47), (96, 47), (97, 47), (98, 47), (99, 47), (100, 47), (101, 47), (102, 47), (103, 47), (99, 46), (100, 46), (101, 46), (102, 46), (103, 46), (104, 46), (99, 45), (100, 45), (101, 45), (102, 45), (103, 45), (104, 45), (105, 45), (106, 45)), #Mongolia
(), #Aztecs
((68, 48), (68, 49), (73, 40), (73, 41), (73, 42), (71, 42), (70, 42), (74, 42), (75, 42), (80, 47), (80, 48), (80, 49), (67, 42), (67, 41)), #Turkey
((29, 49), (30, 49), (31, 49), (31, 50), (32, 50), (24, 44), (25, 44), (24, 43), (25, 43), (26, 48)) #America
),
((), #Egypt
(), #India
(), #China
((78, 41), (78, 42)), #Babylonia
(), #Greece
(), #Persia
(),#(73, 40), (73, 41)), #Carthage
((63,47), (63,46)), #Rome		# ITALY
(), #Japan
(), #Ethiopia
(), #Maya
(), #Byzantium
((59, 55), (60, 55), (62, 55), (59, 56), (62, 56), (63, 56)), #Vikings
((82, 34), (73, 40), (74, 40), (75, 40), (71, 36), (72, 37)),  #Arabia
(), #Khmer
(), #Indonesia (should probably exclude Borneo)
(), #Spain
((51, 50), (52, 49), (52, 50), (53, 47), (53, 48), (53, 49), (53, 50), (53, 51), (55, 46), (56, 46), (57, 46), (56, 45), (57, 45), (58, 48), (58, 49), (58, 50)), #France
(), #England
((62, 47), (63, 47), (64, 47), (58, 51), (58, 52), (58, 53), (57, 53), (65, 55), (66, 55), (66, 56)),  #Germany
((68, 58), (69, 58), (70, 58), (65, 55), (66, 55), (66, 56)), #Russia
((57, 51), (58, 51)), #Holland
(), #Mali
(), #Portugal
(), #Inca
((90, 47), (91, 47), (92, 47), (93, 47), (94, 47), (95, 47), (96, 47), (97, 47), (98, 47), (99, 47), (100, 47), (101, 47), (102, 47), (103, 47), (99, 46), (100, 46), (101, 46), (102, 46), (103, 46), (104, 46), (99, 45), (100, 45), (101, 45), (102, 45), (103, 45), (104, 45), (105, 45), (106, 45)), #Mongolia
(), #Aztecs
((68, 48), (68, 49), (73, 40), (73, 41), (73, 42), (71, 42), (70, 42), (74, 42), (75, 42), (80, 47), (80, 48), (80, 49)), #Turkey
((29, 49), (30, 49), (31, 49), (31, 50), (32, 50), (24, 44), (25, 44), (24, 43), (25, 43), (26, 48)) #America
))



#normal areas (for Victory and resurrection)

tNormalAreasTL = (
((65, 30), #Egypt
(86, 29), #India
(99, 39), #China
(74, 38), #Babylonia
(64, 39), #Greece
(79, 37), #Persia
(72, 39), #Carthage
(57, 40), #Rome
(111, 41), #Japan
(68, 25), #Ethiopia
(108, 45), #Korea
(20, 32), #Maya
(64, 38), #Byzantium
(57, 55), #Vikings
(72, 30), #Arabia
(98, 26), #Khmer
(98, 24), #Indonesia
(49, 40), #Spain
(51, 46), #France
(50, 53), #England
(59, 48), #Germany
(68, 49), #Russia
(56, 51), #Holland
(48, 26), #Mali
(44, 41), #Portugal
(24, 14), #Inca
(92, 48), #Mongolia
(15, 35), #Aztecs
(68, 42), #Turkey
(11, 43) #America
),
((65, 30), #Egypt
(86, 29), #India
(99, 39), #China
(74, 38), #Babylonia
(64, 39), #Greece
(79, 37), #Persia
(72, 39), #Carthage
(57, 40), #Rome
(111, 41), #Japan
(68, 25), #Ethiopia
(108, 45), #Korea
(20, 32), #Maya
(64, 38), #Byzantium
(57, 55), #Vikings
(73, 30), #Arabia
(98, 26), #Khmer
(98, 24), #Indonesia
(49, 40), #Spain
(51, 46), #France
(50, 53), #England
(59, 48), #Germany
(68, 49), #Russia
(56, 51), #Holland
(48, 26), #Mali
(44, 41), #Portugal
(24, 14), #Inca
(92, 48), #Mongolia
(15, 35), #Aztecs
(68, 42), #Turkey
(11, 43) #America
))

tNormalAreasBR = (
((72, 37), #Egypt
(97, 42), #India
(108, 50), #China
(79, 44), #Babylonia
(68, 44), #Greece
(86, 46), #Persia
(74, 41), #Carthage
(63, 47), #Rome
(116, 52), #Japan
(77, 30), #Ethiopia
(110, 49), #Korea
(23, 37), #Maya
(74, 45), #Byzantium
(67, 65), #Vikings
(82, 38), #Arabia
(103, 37), #Khmer
(113, 31), #Indonesia
(55, 46), #Spain
(58, 52), #France
(54, 60), #England
(66, 54), #Germany
(83, 62), #Russia
(58, 53), #Holland
(60, 33), #Mali
(50, 44), #Portugal
(30, 29), #Inca
(104, 54), #Mongolia
(20, 40), #Aztecs
(78, 49), #Turkey
(31, 49) #America
),
((72, 37), #Egypt
(97, 42), #India
(108, 50), #China
(79, 44), #Babylonia
(68, 44), #Greece
(86, 46), #Persia
(74, 41), #Carthage
(63, 47), #Rome
(116, 52), #Japan
(77, 30), #Ethiopia
(110, 49), #Korea
(23, 37), #Maya
(74, 45), #Byzantium
(67, 65), #Vikings
(82, 38), #Arabia
(103, 37), #Khmer
(113, 31), #Indonesia
(55, 46), #Spain
(58, 52), #France
(54, 60), #England
(66, 54), #Germany
(83, 62), #Russia
(58, 53), #Holland
(60, 33), #Mali
(50, 44), #Portugal
(30, 29), #Inca
(104, 54), #Mongolia
(20, 40), #Aztecs
(78, 49), #Turkey
(31, 49) #America
))


tNormalAreasSubtract = (  #for resurrection and stability
(((72, 37), (70, 30), (71, 30), (72, 30)), #Egypt
((93, 42), (94, 42), (95, 42), (96, 42)), #India
((99, 49), (100, 49), (101, 49), (99, 50), (100, 50), (101, 50), (102, 50)), #China
(), #Babylonia
(), #Greece
((86, 39), (86, 38), (86, 37)), #Persia
(), #Carthage
((62, 47), (63, 47), (63, 46)), #Rome
((111, 52), (112, 52), (111, 51)), #Japan
((76, 30), (77, 30)), #Ethiopia
(), #Korea
(), #Maya
(), #Byzantium
((65, 55), (66, 55), (67, 55), (66, 56), (67, 56)), #Vikings
((81, 38), (82, 38), (82, 37)),  #Arabia
(), #Khmer
(), #Indonesia
((49, 44), (49, 43), (49, 42), (49, 41)), #Spain #bts only
((51, 46), (52, 46), (53, 46), (58, 47), (58, 46), (58, 51), (58, 52), (57, 52)), #France #changed in BTS
(), #England
(),  #Germany
((80, 49), (68, 62), (68, 61), (68, 60), (68, 59)), #Russia
(), #Holland
(), #Mali
(), #Portugal
(), #Inca
((92, 52), (92, 53), (92, 54), (93, 54), (94, 54), (100, 48), (101, 48), (102, 48), (103, 48), (104, 48)), #Mongolia
((20, 35)), #Aztecs #bts only
(), #Turkey
() #America
),
(((72, 37), (70, 30), (71, 30), (72, 30)), #Egypt
((93, 42), (94, 42), (95, 42), (96, 42)), #India
((99, 49), (100, 49), (101, 49), (99, 50), (100, 50), (101, 50), (102, 50)), #China
(), #Babylonia
(), #Greece
((86, 39), (86, 38), (86, 37)), #Persia
(), #Carthage
((62, 47), (63, 47), (63, 46)), #Rome
((111, 52), (112, 52), (111, 51)), #Japan
((76, 30), (77, 30)), #Ethiopia
(), #Maya
(), #Byzantium
((65, 55), (66, 55), (67, 55), (66, 56), (67, 56)), #Vikings
((81, 38), (82, 38), (82, 37)),  #Arabia
(), #Khmer
(), #Indonesia
((49, 44), (49, 43), (49, 42), (49, 41)), #Spain #bts only
((51, 46), (52, 46), (53, 46), (58, 47), (58, 46), (58, 51), (58, 52), (57, 52)), #France #changed in BTS
(), #England
(),  #Germany
((80, 49), (68, 62), (68, 61), (68, 60), (68, 59)), #Russia
(), #Holland
(), #Mali
(), #Portugal
(), #Inca
((92, 52), (92, 53), (92, 54), (93, 54), (94, 54), (100, 48), (101, 48), (102, 48), (103, 48), (104, 48)), #Mongolia
((20, 35)), #Aztecs #bts only
(), #Turkey
() #America
))

# broader areas coordinates (top left and bottom right) (for RiseAndFall)

tBroaderAreasTL = (
((60, 26), #Egypt
(85, 28), #India
(95, 38), #China
(72, 37), #Babylonia
(62, 39), #Greece
(70, 37), #Persia
(71, 39), #Carthage
(49, 35), #Rome
(110, 40), #Japan
(67, 21), #Ethiopia
(106, 45), #Korea
(19, 30), #Maya
(58, 34), #Byzantium
(57, 55), #Vikings
(64, 30), #Arabia
(97, 25), #Khmer
(98, 24), #Indonesia
(49, 38), #Spain
(49, 44), #France
(48, 53), #England
(55, 46), #Germany
(65, 48), #Russia
(56, 51), #Holland
(48, 21), #Mali
(49, 40), #Portugal
(24, 14), #Inca
(82, 44), #Mongolia
(14, 32), #Aztecs
(68, 42), #Turkey
(10, 42) #America
),
((60, 26), #Egypt
(85, 28), #India
(95, 38), #China
(72, 37), #Babylonia
(62, 39), #Greece
(70, 37), #Persia
(71, 39), #Carthage
(57, 47), #Rome		# ITALY
(110, 40), #Japan
(67, 21), #Ethiopia
(106, 45), #Korea
(19, 30), #Maya
(64, 38), #Byzantium
(57, 55), #Vikings
(64, 30), #Arabia
(97, 25), #Khmer
(98, 24), #Indonesia
(49, 38), #Spain
(49, 44), #France
(48, 53), #England
(55, 46), #Germany
(65, 48), #Russia
(56, 51), #Holland
(48, 21), #Mali
(49, 40), #Portugal
(24, 14), #Inca
(82, 44), #Mongolia
(14, 32), #Aztecs
(68, 42), #Turkey
(10, 42) #America
))

tBroaderAreasBR = (
((74, 38), #Egypt
(99, 43), #India
(108, 50), #China
(78, 44), #Babylonia
(77, 47), #Greece
(87, 49), #Persia
(74, 41), #Carthage
(73, 50), #Rome
(116, 56), #Japan
(77, 30), #Ethiopia
(110, 52), #Korea
(26, 37), #Maya
(74, 45), #Byzantium
(71, 65), #Vikings
(85, 44), #Arabia
(105, 39), #Khmer
(113, 31), #Indonesia
(55, 46), #Spain
(61, 52), #France
(54, 60), #England
(67, 56), #Germany
(92, 59), #Russia
(58, 53), #Holland
(67, 32), #Mali
(51, 45), #Portugal
(30, 27), #Inca
(110, 62), #Mongolia
(24, 43), #Aztecs
(86, 49), #Turkey
(37, 56) #America
),
((74, 38), #Egypt
(99, 43), #India
(108, 50), #China
(78, 44), #Babylonia
(77, 47), #Greece
(87, 49), #Persia
(74, 41), #Carthage
(65, 47), #Rome		# ITALY
(116, 56), #Japan
(77, 30), #Ethiopia
(110, 52), #Korea
(26, 37), #Maya
(74, 45), #Byzantium
(71, 65), #Vikings
(85, 44), #Arabia
(105, 39), #Khmer
(113, 31), #Indonesia
(55, 46), #Spain
(61, 52), #France
(54, 60), #England
(67, 56), #Germany
(92, 59), #Russia
(58, 53), #Holland
(67, 32), #Mali
(51, 45), #Portugal
(30, 27), #Inca
(110, 62), #Mongolia
(24, 43), #Aztecs
(86, 49), #Turkey
(37, 56) #America
))

#Mercenaries. Higher number = less likely to hire
tHire = (
10, #Egypt
30, #India
30, #China
30, #Babylonia
50, #Greece
20, #Persia
10, #Carthage
30, #Rome
60, #Japan
30, #Ethiopia
60, #Korea
30, #Maya
10, #Byzantium
60, #Viking
50, #Arabia
30, #Khmer
60, #Indonesia
50, #Spain
50, #France
50, #England
60, #Germany
60, #Russia
10, #Holland
30, #Mali
60, #Portugal
30, #Inca
70, #Mongolia
30, #Aztec
50, #Turkey
50, #America
100,
100,
100,
100,
100) #Barbs



#rnf. Some civs have a double entry, for a higher chance
lEnemyCivsOnSpawn = [
[], #Egypt
[], #India
[iIndependent,iIndependent2,iIndependent2], #China
[iIndependent,iIndependent2], #Babylonia
[iIndependent,iIndependent2,iBabylonia], #Greece
[iBabylonia,iBabylonia,iGreece,iCarthage,iCarthage,iIndia,iIndia], #Persia
[], #Carthage
#[iEgypt,iGreece,iGreece,iCarthage,iCarthage], #Rome
[], # rome for testing
[], #Japan
[], #Ethiopia
[], #Korea
[], #Maya
[iGreece, iPersia], #Byzantium
[iRome,iArabia,iSpain,iEngland,iEngland,iFrance,iFrance,iGermany,iGermany,iCeltia,iIndependent,iIndependent2], #Vikings
[iEgypt,iEgypt,iEgypt,iBabylonia,iBabylonia,iGreece,iPersia,iCarthage,iRome,iByzantium,iByzantium,iSpain,iFrance,iCeltia,iCeltia,iIndependent,iIndependent2], #Arabia
[], #Khmer
[], #Indonesia
[iArabia], #Spain
[iArabia], #France
[], #England
[iRome], #Germany
[], #Russia
[], #Netherlands
[], #Mali
[], #Portugal
[], #Inca
[iChina,iChina,iIndependent,iIndependent,iIndependent2,iIndependent2], #Mongolia
[iMaya], #Aztec
[iEgypt,iBabylonia,iGreece,iGreece,iArabia,iArabia,iArabia], #Turkey
[iIndependent,iIndependent2] #America
]

# Leoreth
lTotalWarOnSpawn = [
[], #Egypt
[], #India
[], #China
[], #Babylonia
[], #Greece
[iBabylonia, iCarthage], #Persia
[], #Phoenicia
[iGreece], #Rome
[], #Japan
[], #Ethiopia
[], #Korea
[], #Maya
[iGreece], #Byzantium
[], #Vikings
[iEgypt, iBabylonia, iCarthage, iPersia], #Arabia
[], #Khmer
[], #Indonesia
[], #Spain
[], #France
[], #England
[iRome], #Germany
[], #Russia
[], #Netherlands
[], #Mali
[], #Portugal
[], #Inca
[iChina], #Mongolia
[iMaya], #Aztec
[iArabia], #Turkey
[], #America
]


#AIWars
tAggressionLevel = (
0, #Egypt
0, #India
1, #China
1, #Babylonia
2, #Greece
3, #Persia
0, #Carthage
3, #Rome
1, #Japan
0, #Ethiopia
0, #Korea
1, #Maya
1, #Byzantium
2, #Viking
2, #Arabia
1, #Khmer
1, #Indonesia
2, #Spain
1, #France
1, #England
2, #Germany
1, #Russia
0, #Holland
0, #Mali
0, #Portugal
1, #Inca
2, #Mongolia
1, #Aztec
2, #Turkey
2, #America
0) #Barbs


#war during rise of new civs
tAIStopBirthThreshold = (
    80, #Egypt
    80, #India
    60, #China
    50, #Babylonia
    50, #Greece #would be 80 but with Turks must be lower
    70, #Persia
    80, #Carthage
    80, #Rome
    80, #Japan
    80, #Ethiopia
    80, #Korea
    80, #Maya
    80, #Byzantium
    80, #Viking
    80, #Arabia
    80, #Khmer
	80, #Indonesia
    80, #Spain  #60 in vanilla and Warlords
    80, #France #60 in vanilla and Warlords
    50, #England
    80, #Germany #70 in vanilla and Warlords
    50, #Russia
    80, #Holland
    70, #Mali
    60, #Portugal
    70, #Inca
    70, #Mongolia
    50, #Aztec
    70, #Turkey
    50, #America
    100,
    100,
    100,
    100,
    100)


#RiseAndFall
tResurrectionProb = (
80, #Egypt
100, #India
100, #China
30, #Babylonia
60, #Greece
60, #Persia
30, #Carthage
65, #Rome
100, #Japan
80, #Ethopia
80, #Korea
30, #Maya
65, #Byzantium
60, #Viking
100, #Arabia
60, #Khmer
80, #Indonesia
100, #Spain
100, #France
100, #England
100, #Germany
100, #Russia
100, #Holland
30, #Mali
100, #Portugal
70, #Inca
80, #Mongolia
70, #Aztec
100, #Turkey
100, #America
#    100, #Holland
#    100, #Portugal
100) #Barbs 


#Congresses.
tPatienceThreshold = (
30, #Egypt
50, #India
30, #China
30, #Babylonia
35, #Greece
30, #Persia
35, #Carthage
25, #Rome
25, #Japan
20, #Ethopia
25, #Korea
35, #Maya
25, #Byzantium
30, #Viking
30, #Arabia
30, #Khmer
30, #Indonesia
20, #Spain
20, #France
20, #England
20, #Germany
30, #Russia
30, #Holland
35, #Mali
30, #Portugal
35, #Inca
20, #Mongolia
30, #Aztec
35, #Turkey
30, #America
100) #Barbs


#RnF Colonists
tMaxColonists = (
0, #Egypt
0, #India
0, #China
0, #Babylonia
0, #Greece
0, #Persia
0, #Carthage
0, #Rome
0, #Japan
0, #Ethopia
0, #Korea
0, #Maya
0, #Byzantium
1, #Viking
0, #Arabia
0, #Khmer
0, #Indonesia
6, #Spain
6, #France
6, #England
1, #Germany
0, #Russia
6, #Holland
0, #Mali
6, #Portugal
0, #Inca
0, #Mongolia
0, #Aztec
0, #Turkey
0) #America


# initialise religion variables to religion indices from XML
iJudaism = 0
iChristianity = 1
iIslam = 2
iHinduism = 3
iBuddhism = 4
iConfucianism = 5
iTaoism = 6
iZoroastrianism = 7
iNumReligions = 8


# initialise tech variables to unit indices from XML

iMysticism = 0
iMeditation = 1
iPolytheism = 2
iPriesthood = 3
iMonotheism = 4
iMonarchy = 5
iLiterature = 6
iCodeOfLaws = 7
iDrama = 8
iFeudalism = 9
iTheology = 10
iMusic = 11
iCivilService = 12
iGuilds = 13
iDivineRight = 14
iNationalism = 15
iMilitaryTradition = 16
iConstitution = 17
iLiberalism = 18
iDemocracy = 19
iCorporation = 20
iFascism = 21
iUtopia = 22
iCommunism = 22 #
iMassMedia = 23
iEcology = 24

iFishing = 25
iTheWheel = 26
iAgriculture = 27
iPottery = 28
iAesthetics = 29
iSailing = 30
iWriting = 31
iMathematics = 32
iAlphabet = 33
iCalendar = 34
iCurrency = 35
iPhilosophy = 36
iPaper = 37
iBanking = 38
iEducation = 39
iPrintingPress = 40
iEconomics = 41
iAstronomy = 42
iChemistry = 43
iScientificMethod = 44
iPhysics = 45
iBiology = 46
iMedicine = 47
iElectricity = 48
iCombustion = 49
iFission = 50
iFlight = 51
iAdvancedFlight = 52
iPlastics = 53
iComposites = 54
iStealth = 55
iGenetics = 56
iFiberOptics = 57
iFusion = 58

iHunting = 59
iMining = 60
iArchery = 61
iMasonry = 62
iAnimalHusbandry = 63
iBronzeWorking = 64
iHorsebackRiding = 65
iIronWorking = 66
iMetalCasting = 67
iCompass = 68
iConstruction = 69
iMachinery = 70
iEngineering = 71
iOptics = 72
iGunpowder = 73
iReplaceableParts = 74
iMilitaryScience = 75
iRifling = 76
iSteamPower = 77
iSteel = 78
iAssemblyLine = 79
iRailroad = 80
iArtillery = 81
iIndustrialism = 82
iRadio = 83
iRefrigeration = 84
iSuperconductors = 85
iComputers = 86
iLaser = 87
iRocketry = 88
iSatellites = 89
iRobotics = 90

iNumTechs = 91
iFutureTech = 91

iNumTechsFuture = 92


# initialise unit variables to unit indices from XML

iLion = 0
iBear = 1
iPanther = 2
iWolf = 3
iSettler = 4
iWorker = 5
iIndianFastWorker = 6
iScout = 7
iExplorer = 8
iSpy = 9
iJewishMissionary = 10
iChristianMissionary = 11
iIslamicMissionary = 12
iHinduMissionary = 13
iBuddhistMissionary = 14
iConfucianMissionary = 15
iTaoistMissionary = 16
iZoroastrianMissionary = 17
iWarrior = 18
iIncanQuechua = 19
iSwordsman = 20
iAztecJaguar = 21
iCelticGallicWarrior = 22
iRomePraetorian = 23
iAxeman = 24
iGreekPhalanx = 25
iSumerianVulture = 26
iNativeAmericaDogSoldier = 27
iMaceman = 28
iJapanSamurai = 29
iVikingBeserker = 30
iSpearman = 31
iZuluImpi = 32
iMayaHolkan = 33
iPikeman = 34
iHolyRomanLandsknecht = 35
iIndonesianPencuSilat = 36
iMusketman = 37
iFrenchMusketeer = 38
iOttomanJanissary = 39
iEthiopianOromoWarrior = 40
iRifleman = 41
iEnglishRedcoat = 42
iGrenadier = 43
iAtInfantry = 44
iInfantry = 45
iSamInfantry = 46
iMobileSam = 47
iMarine = 48
iAmericanNavySeal = 49
iParatrooper = 50
iMechanizedInfantry = 51
iArcher = 52
iMaliSkirmisher = 53
iBabylonBowman = 54
iLongbowman = 55
iCrossbowman = 56
iChinaChokonu = 57
iChariot = 58
iEgyptWarchariot = 59
iPersiaImmortal = 60
iHorseArcher = 61
iCarthageNumidianCavalry = 62
iMongolKeshik = 63
iKnight = 64
iArabiaCamelarcher = 65
iCamelArcher = 65 #
iByzantineCataphract = 66
iSpanishConquistador = 67
iConquistador = 67 #
iCuirassier = 68
iCavalry = 69
iRussiaCossack = 70
iWarElephant = 71
iKhmerBallistaElephant = 72
iTank = 73
iGermanPanzer = 74
iModernArmor = 75
iGunship = 76
iCatapult = 77
iKoreanHwacha = 78
iTrebuchet = 79
iCannon = 80
iMachineGun = 81
iArtillery = 82
iMobileArtillery = 83
iWorkboat = 84
iWorkBoat = 84 #
iGalley = 85
iTrireme = 86
iCaravel = 87
iPortugalCarrack = 88
iGalleon = 89
iNetherlandsOostindievaarder = 90
iPrivateer = 91
iFrigate = 92
iShipOfTheLine = 93
iIronclad = 94
iTransport = 95
iDestroyer = 96
iBattleship = 97
iMissileCruiser = 98
iStealthDestroyer = 99
iSubmarine = 100
iAttackSubmarine = 101
iCarrier = 102
iAirship = 103
iFighter = 104
iJetFighter = 105
iBomber = 106
iStealthBomber = 107
iGuidedMissile = 108
iTacticalNuke = 109
iIcbm = 110
iProphet = 111
iArtist = 112
iScientist = 113
iMerchant = 114
iEngineer = 115
iGreatGeneral = 116
iGreatSpy = 117
iCulverine = 118
iBireme = 119
iBersagliere = 120
iLevy = 121


# initialise bonuses variables to bonuses IDs from WBS
iAluminium = 0
iCoal = 1
iCopper = 2
iHorse = 3
iIron = 4
iMarble = 5
iOil = 6 
iStone = 7
iUranium = 8
iBanana = 9
iClam = 10
iCorn = 11
iCow = 12
iCrab = 13
iDeer = 14
iFish = 15
iPig = 16
iRice = 17
iSheep = 18
iWheat = 19
iDye = 20
iFur = 21
iGems = 22
iGold = 23
iIncense = 24
iIvory = 25
iSilk = 26
iSilver = 27
iSpices = 28
iSugar = 29
iWine = 30
iWhales = 31
iCotton = 35


#Buildings (update Persian UHV every time this is changed)
iTemple = 78 #generic
iCathedral = 79 #generic
iMonastery = 80 #generic
iShrine = 81 #generic


iPalace = 0
iGreatPalace = 1
iSummerPalace = 1 #
iVersailles = 2
iForbiddenPalace = 2 #
iWalls = 3
iCelticDun = 4
iCastle = 5
iSpanishCitadel = 6
iBarracks = 7
iZuluIkhanda = 8
iStable = 9
iMongolGer = 10
iBunker = 11
iBombShelter = 12
iGranary = 13
iIncanTerrace = 14
iAqueduct = 15
iOttomanHammam = 16
iKhmerBaray = 17
iHospital = 18
iRecyclingCenter = 19
iLighthouse = 20
iVikingTradingPost = 21
iHarbor = 22
iCarthageCothon = 23
iCustomHouse = 24
iPortugalFeitoria = 25
iDrydock = 26
iAirport = 27
iForge = 28
iMaliMint = 29
iFactory = 30
iGermanAssemblyPlant = 31
iCoalPlant = 32
iJapaneseShalePlant = 33
iHydroPlant = 34
iNuclearPlant = 35
iIndustrialPark = 36
iObelisk = 37
iEgyptianObelisk = 38
iEthiopianStele = 39
iNativeAmericaTotem = 40
iPublicTransportation = 41
iAcademy = 42
iLibrary = 43
iArabianMadrassa = 44
iUniversity = 45
iKoreanSeowon = 46
iObservatory = 47
iLaboratory = 48
iRussianResearchInstitute = 49
iTheatre = 50
iFrenchSalon = 51
iByzantineHippodrome = 52
iChinesePavillion = 53
iIndonesianCandi = 54
iColosseum = 55
iGreekOdeon = 56
iMayaBallCourt = 57
iBabylonGarden = 58
iBroadcastTower = 59
iMarket = 60
iRomanForum = 61
iPersianApothecary = 62
iGrocer = 63
iBank = 64
iEnglishStockExchange = 65
iSupermarket = 66
iAmericanMall = 67
iCourthouse = 68
iAztecSacrificialAltar = 69
iHolyRomanRathaus = 70
iSumerianZiggurat = 71
iJail = 72
iIndianMausoleum = 73
iLevee = 74
iNetherlandsDike = 75
iIntelligenceAgency = 76
iNationalSecurity = 77
iJewishTemple = 78
iJewishCathedral = 79
iJewishMonastery = 80
iJewishShrine = 81
iChristianTemple = 82
iChristianCathedral = 83
iChristianMonastery = 84
iChristianShrine = 85
iIslamicTemple = 86
iIslamicCathedral = 87
iIslamicMonastery = 88
iIslamicShrine = 89
iHinduTemple = 90
iHinduCathedral = 91
iHinduMonastery = 92
iHinduShrine = 93
iBuddhistTemple = 94
iBuddhistCathedral = 95
iBuddhistMonastery = 96
iBuddhistShrine = 97
iConfucianTemple = 98
iConfucianCathedral = 99
iConfucianMonastery = 100
iConfucianShrine = 101
iTaoistTemple = 102
iTaoistCathedral = 103
iTaoistMonastery = 104
iTaoistShrine = 105
iZoroastrianTemple = 106
iZoroastrianCathedral = 107
iZoroastrianMonastery = 108
iZoroastrianShrine = 109
iHeroicEpic = 110 #
iFlavianAmphitheatre = 110
iNationalEpic = 111
iTriumphalArch = 111 #
iGlobeTheatre = 112
iNationalPark = 113
iHermitage = 114
iNationalGallery = 114 #
iChannelTunnel = 115
iWallStreet = 116
iIronWorks = 117
iTradingCompany = 118
iMtRushmore = 119
iRedCross = 120
iScotlandYard = 121
iInterpol = 121 #
iPyramid = 122
iStonehenge = 123
iGreatLibrary = 124
iGreatLighthouse = 125
iHangingGarden = 126
iColossus = 127
iOracle = 128
iParthenon = 129
iAngkorWat = 130
iHagiaSophia = 131
iChichenItza = 132
iTempleOfKukulkan = 132 #
iSistineChapel = 133
iSpiralMinaret = 134
iNotreDame = 135
iTajMahal = 136
iKremlin = 137
iEiffelTower = 138
iStatueOfLiberty = 139
iBroadway = 140
iWembley = 140 #
iRocknroll = 141
iGraceland = 141 #
iHollywood = 142
iGreatDam = 143
iPentagon = 144
iUnitedNations = 145
iSpaceElevator = 146
iMilitaryAcademy = 147
iArtemis = 148
iSankore = 149
iGreatWall = 150
iStatueOfZeus = 151
iMausoleumOfMaussollos = 152
iCristoRedentor = 153
iShwedagonPaya = 154
iMoaiStatues = 155
iApostolicPalace = 156
iLeaningTower = 157
iOlympicPark = 158
iTempleOfSalomon = 159
iIshtarGate = 160
iTheodosianWalls = 161
iTerracottaArmy = 162
iMezquita = 163
iDomeOfTheRock = 164
iTopkapiPalace = 165
iBrandenburgGate = 166
iSanMarcoBasilica = 167
iWestminster = 168
iItalianArtStudio = 169
iBorobudur = 170
iKhajuraho = 171
iHimejiCastle = 172
iPorcelainTower = 173
iHarmandirSahib = 174
iGreatBath = 175


iNumBuildings = 176
iPlague = 176
iNumBuildingsPlague = 177

iEgyEmbassy = 177
iIndEmbassy = 178
iChiEmbassy = 179
iBabEmbassy = 180
iGreEmbassy = 181
iPerEmbassy = 182
iCarEmbassy = 183
iRomEmbassy = 184
iJapEmbassy = 185
iEthEmbassy = 186
iKorEmbassy = 187
iMayEmbassy = 188
iByzEmbassy = 189
iVikEmbassy = 190
iAraEmbassy = 191
iKhmEmbassy = 192
iInoEmbassy = 193
iSpaEmbassy = 194
iFraEmbassy = 195
iEngEmbassy = 196
iGerEmbassy = 197
iRusEmbassy = 198
iHolEmbassy = 199
iMalEmbassy = 200
iPorEmbassy = 201
iIncEmbassy = 202
iMonEmbassy = 203
iAztEmbassy = 204
iTurEmbassy = 205
iAmeEmbassy = 206

iNumBuildingsEmbassy = 207


#Projects

iManhattanProject = 0
iTheInternet = 1
iSDI = 2
iApolloProgram = 3
iSSCasing = 4
iSSThrusters = 5
iSSEngine = 6
iSSDockingBay = 7
iSSCockpit = 8
iSSLifeSupport = 9
iSSStasisChamber = 10


#Eras

iAncient = 0
iClassical = 1
iMedieval = 2
iRenaissance = 3
iIndustrial = 4
iModern = 5
iFuture = 6


#Improvements

iHut = 3
iCottage = 19
iHamlet = 20
iVillage = 21
iTown = 22

#feature & terrain

iSeaIce = 0
iJungle = 1
iOasis = 2
iFloodPlains = 3
iForest = 4
iFallout = 5
iMud = 6

iGrass = 0
iPlains = 1
iDesert = 2
iTundra = 3
iSnow = 4
iCoast = 5
iOcean = 6
iTerrainPeak = 7
iTerrainHills = 8
iMarsh = 9

iSwamp = 36 #bonus


#Stability Parameters

iParCities3 = 0
iParCitiesE = 1
iParCivics3 = 2
iParCivics1 = 3
iParCivicsE = 4
iParDiplomacy3 = 5
iParDiplomacyE = 6
iParEconomy3 = 7
iParEconomy1 = 8
iParEconomyE = 9
iParExpansion3 = 10
iParExpansion1 = 11
iParExpansionE = 12
iNumStabilityParameters = 13

#Plague
iImmunity = 20


#leaders
iLeaderBarbarian = 0
iAlexander = 1
iAsoka = 2
iAugustus = 3
iBismarck = 4
iBoudica = 5
iBrennus = 6
iAlfred = 6
iCatherine = 7
iCharlemagne = 8
iOttoI = 8
iChurchill = 9
iCyrus = 10
iDarius = 11
iDe_Gaulle = 12
iElizabeth = 13
iFrederick = 14
iGandhi = 15
iGenghis_Khan = 16
iGilgamesh = 17
iHammurabi = 18
iHannibal = 19
iHatshepsut = 20
iHuayna_Capac = 21
iIsabella = 22
iJoao = 23
iJulius_Caesar = 24
iJustinian = 25
iKublai_Khan = 26
iLincoln = 27
iLouis_Xiv = 28
iMansa_Musa = 29
iMao = 30
iMehmed = 31
iMontezuma = 32
iNapoleon = 33
iPacal = 34
iPericles = 35
iPeter = 36
iQin_Shi_Huang = 37
iRamesses = 38
iRagnar = 39
iFranklin_Roosevelt = 40
iSaladin = 41
iShaka = 42
iSitting_Bull = 43
iStalin = 44
iSuleiman = 45
iSuryavarman = 46
iTokugawa = 47
iVictoria = 48
iWangkon = 49
iMing_Tai_Zu = 49
iWashington = 50
iWillem_Van_Oranje = 51
iZara_Yaqob = 52
iJimmu = 53
iMeiji = 54
iAkbar = 55
iHiram = 56
iHaile_Selassie = 57
iGustav = 58
iAbu_Bakr = 59
iMongkut = 60
iElishat = 61
iPhilip = 62
iBarbarossa = 63
iCharles = 64
iFrancis = 65
iYaroslav = 66
iAfonso = 67
iAtaturk = 68
iMaria = 69
iHitler = 70
iFranco = 71
iNicholas = 72
iCixi = 73
iChiang_Kaishek = 74
iCavour = 75
iAbbas = 76
iKhomeini = 77
iTaizong = 78
iYongle = 79
iDharmasetu = 80
iHayamWuruk = 81
iSuharto = 82
iShivaji = 83


tLeaders = (
(iRamesses, iHatshepsut),
(iAsoka, iShivaji, iGandhi),
(iQin_Shi_Huang, iTaizong, iYongle, iCixi),
(iHammurabi, iGilgamesh),
(iPericles, iAlexander,),
(iCyrus, iDarius),
(iHannibal, iHiram),
(iAugustus, iJulius_Caesar),	#Justinian now Byzantine, find new
(iTokugawa, iJimmu, iMeiji),
(iZara_Yaqob, iHaile_Selassie),
(iWangkon,),
(iPacal,),
(iJustinian,),
(iRagnar, iGustav),
(iSaladin, iAbu_Bakr),
(iSuryavarman,),
(iHayamWuruk, iDharmasetu, iSuharto),
(iIsabella, iPhilip),
(iLouis_Xiv, iCharlemagne, iNapoleon, iDe_Gaulle),
(iVictoria, iBrennus, iElizabeth, iChurchill),
(iBismarck, iCharles, iFrederick),
(iStalin, iYaroslav, iPeter, iCatherine),
(iWillem_Van_Oranje,),
(iMansa_Musa,),
(iJoao, iAfonso, iMaria),
(iHuayna_Capac,),
(iGenghis_Khan, iKublai_Khan),
(iMontezuma,),
(iMehmed, iSuleiman, iAtaturk),
(iFranklin_Roosevelt, iWashington, iLincoln))

tEarlyLeaders = (
(iRamesses), 
(iAsoka),
(iQin_Shi_Huang),
(iGilgamesh),
(iPericles),
(iCyrus),
(iHiram),
(iJulius_Caesar),
(iJimmu),
(iZara_Yaqob),
(iWangkon),
(iPacal),
(iJustinian),
(iRagnar),
(iAbu_Bakr),
(iSuryavarman),
(iDharmasetu),
(iIsabella),
(iCharlemagne),
(iAlfred),
(iCharles),
(iYaroslav),
(iWillem_Van_Oranje),
(iMansa_Musa),
(iAfonso),
(iHuayna_Capac),
(iGenghis_Khan),
(iMontezuma),
(iMehmed),
(iWashington))

# converted to years - edead

#Leoreth: no longer needed because Justinian is now Byzantine
#if (gc.getPlayer(0).isPlayable()): #late start condition
        #tRomanLateLeaders = (iAugustus, 50, 5, 2, iJustinian, 1000, 10, 3)	
#else: 
        #tRomanLateLeaders = (iAugustus, 50, 5, 2)
tRomanLateLeaders = (iAugustus, 50, 5, 2)


tLateLeaders = ( #all up to 300 turns earlier because the switch is triggered after a few years
(iHatshepsut, -400, 5, 1), 
(iAkbar, 1400, 5, 3, iGandhi, 1900, 5, 4),
(iTaizong, 600, 10, 2, iYongle, 1400, 15, 3, iCixi, 1870, 10, 4),
(iHammurabi, -1600, 10, 1),
(iAlexander, -10, 5, 2),
(iDarius, -10, 5, 2),
(iHannibal, -400, 10, 1),
tRomanLateLeaders,
(iTokugawa, 1200, 10, 3, iMeiji, 1850, 10, 4),
(iHaile_Selassie, 1800, 10, 4),
(iWangkon,),
(iPacal,),
(iJustinian,),
(iGustav, 1600, 10, 3),
(iSaladin, 1000, 10, 2),
(iSuryavarman,),
(iHayamWuruk, 1300, 10, 2, iSuharto, 1940, 10, 5),
(iPhilip, 1400, 10, 3),
(iLouis_Xiv, 1600, 10, 3, iNapoleon, 1750, 10, 4, iDe_Gaulle, 1940, 10, 5),
(iElizabeth, 1500, 10, 3, iVictoria, 1750, 15, 3, iChurchill, 1930, 10, 5),
(iFrederick, 1700, 10, 4, iBismarck, 1850, 10, 4),
(iPeter, 1400, 15, 3, iCatherine, 1650, 15, 4, iNicholas, 1850, 15, 5),
(iWillem_Van_Oranje,),
(iMansa_Musa,),
(iJoao, 1400, 10, 2, iMaria, 1800, 10, 4),
(iHuayna_Capac,),
(iKublai_Khan, 1500, 10, 3),
(iMontezuma,),
(iSuleiman, 1500, 10, 3, iAtaturk, 1900, 10, 5),
(iLincoln, 1800, 15, 5, iFranklin_Roosevelt, 1930, 15, 5))

tRebirthLeaders = (
-1,
(iShivaji, 1900, iGandhi),
-1,
-1,
-1,
(iAbbas, 1900, iKhomeini),
-1,
(iCavour,),
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1)

tFascistLeaders = (
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
iFranco,
-1,
-1,
iHitler,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1)

tCommunistLeaders = (
-1,
-1,
iMao,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
iStalin,
-1,
-1,
-1,
-1,
-1,
-1,
-1,
-1)

tIsActiveOnLateStart = (
0, 
0,
1,
0,
0,
0,
0,
0,
1,
0,
1,
0,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1)
