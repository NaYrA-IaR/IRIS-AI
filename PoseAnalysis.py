def read_file(filename):
    file = open(filename, 'r')
    frame = []
    allAngles = []
    s = file.read()
    output = s.split(',')
    frame.append(int(output[0]))
    for i in range(1, len(output) - 1):
        if( i % 8 == 0):
            allAngles.append(frame)
            frame = []
        frame.append(int(output[i]))
    return allAngles

# Put the respective .txt files here.
idealAngles = read_file('1.txt')
testAngles = read_file('2.txt')

idealFrameCount = 0
testFrameCount = 0
idealDisplay = []
testDisplay = []

while idealFrameCount < len(idealAngles):
    idealVal = sum(idealAngles[idealFrameCount])
    frameToBeDisplayed = -1
    minSimilarity = 10000
    
    for temp in range(testFrameCount, min(len(testAngles), testFrameCount + 10)):
        testVal = sum(testAngles[temp])
        
        if abs(idealVal - testVal) < minSimilarity:
            minSimilarity = abs(idealVal - testVal)
            frameToBeDisplayed = temp
    
    if minSimilarity < 20:
        idealDisplay.append(idealFrameCount)
        testDisplay.append(frameToBeDisplayed)
        idealFrameCount += 1
        testFrameCount = frameToBeDisplayed + 1
    else:
        idealFrameCount += 1

file = open("idealDisplay.1.txt", 'w')
for frame in idealDisplay:
    file.write(str(frame) + ',')
file.close()

file = open("testDisplay.1.txt", 'w')
for frame in testDisplay:
    file.write(str(frame) + ',')
file.close()

print(len(idealAngles))
print(len(testAngles))
print(idealDisplay)
print(len(idealDisplay))
print(testDisplay)
print(len(testDisplay))