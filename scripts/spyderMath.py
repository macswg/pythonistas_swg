#! python3
# spyderMath.py

"""A script for calculating keyframe position in Christie Spyder (1 indexed). 
This script is built for pythonista on iPhone, which runs python 3.6."""


""" Spyder numbers key:
0 = center
1 = moves to the right (left edge at center of pixelspace)
-1 = moves to the left (right edge at center of pixelspace)
"""


def keyFrel1(keyFwidth, pSpaceWidth):
    kM = keyFwidth / 2
    pM = pSpaceWidth / 2
    lft = int(pM - kM)
    return lft


def spyXfinder(keyFwidth, pSpaceWidth, absX):
    # wDiff = pSpaceWidth - keyFwidth 
    wDiff = keyFwidth - pSpaceWidth
    spyX = (wDiff + (absX * 2)) / pSpaceWidth
    # spyX = (kM - pM) / pM
    return round(spyX, 6)


def cropFinder(keyFwidth, cropFactor):
    croppedWidth = int(keyFwidth) * (1 - float(cropFactor))
    return croppedWidth


def cropFactor(keyFwidth, croppedWidth):
    cF = 1 - (int(croppedWidth) / float(keyFwidth))
    return cF


# Function to validate resolution input
def int_input_validation(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print('You need to enter an non-negative integer (a whole number) ')
            # better try again ... return to the start of the loop
            continue
        else:
            # input successfully parsed!
            # we're ready to exit the loop.
            break
    return value

# option selector
print('\nWhat do you want to do?')
print('\tOption 1 - calculate the keyframe position.')
print('\tOption 2 - calculate the cropped width.')
print('\tOption 3 - calculate the crop factor.')


while True:
    optionSelector = input('Type only the number of your option. ')
    if optionSelector == '1':
        pSpaceWidth = int_input_validation('What is the width of the pixelspace in Spyder? ')
        keyFwidth = int_input_validation('What is the width of the keyframe? ')

        lft = keyFrel1(keyFwidth, pSpaceWidth)

        print(f'Spyder Absolute X if keyframe centered (Left edge of frame) = {lft}')

        absX = round(int_input_validation('What is your desired absolute X position? '))
        spyX = spyXfinder(keyFwidth, pSpaceWidth, absX)
        print(f'The Spyder X position value you desire is: {spyX}')
        break
    elif optionSelector == '2':
        keyFwidth = int_input_validation('What is the width of the keyframe? ')
        cropFactor = input('What is the crop factor? ')
        croppedWidth = cropFinder(keyFwidth, cropFactor)
        print(croppedWidth)
        break
    elif optionSelector == '3':
        keyFwidth = int_input_validation('What is the width of the keyframe? ')
        croppedWidth = input('What is the cropped width? ')
        cropFactorCalculated = cropFactor(keyFwidth, croppedWidth)
        print(round(cropFactorCalculated, 3))
        break
    else:
        print('Enter a valid choice')
