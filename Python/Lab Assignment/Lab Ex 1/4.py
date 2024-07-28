ListColour= [["Black", "Red", "Maroon", "Yellow"], ["000000", "FF0000",
"800000", "FFFF00"]]
print(ListColour)
DictColor={}

for i in range(len(ListColour[0])):
    DictColor[i]={"colorname": ListColour[0][i], "colorcode": ListColour[1][i]}

print(DictColor)