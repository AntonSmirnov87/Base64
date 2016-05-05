def main():
    print("This will convert a string of text to Base64.")
    inpStr = input("Enter the string to be converted: ")
    isHex = askYesOrNo("Is input in hexidecimal format? ")
    if(isHex):
        inpStr = convert16ToStr(inpStr)
    outStr = str(convertStrTo64(inpStr))
    print("\nThe resulting Base64 string is: \n")
    print(outStr)
    print("\n\n\n")
    main()

def convertStrTo64(inpStr):
    inpBin = ""
    for char in inpStr:
        inpBin += format(ord(char), 'b').zfill(8)
    padLen = (24 - len(inpBin))%24
    for i in range(0, padLen):
        inpBin += "0"
    digitTable = []
    for i in range(0, len(inpBin), 6):
        digitTable.append(int(inpBin[i: i + 6], 2))
    base64String = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    outStr = ""
    for i in digitTable:
        outStr += base64String[i]
    return outStr

def convert16ToStr(inputStr):
    outStr = ""
    startChar = 0
    endChar = 2
    inpLen = len(inputStr)
    while endChar <= inpLen:
        outStr += chr(int(inputStr[startChar:endChar], 16))
        startChar += 2
        endChar += 2
    return outStr   

def askYesOrNo(question):
	while(True):
		answer = input(question).lower().strip()[0]
		if(answer == "y"):
			return(True)
		elif(answer == "n"):
			return(False)
		else:
			print("Please type ""Yes"" or ""No""")

if __name__ == "__main__":
    main()
    exit()
