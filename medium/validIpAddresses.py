def validIpAddresses(string):
    ipAddressesFound=[]
    for i in range(1,min(len(string),4)):
        currentIpAddressParts=['','','','','']
        currentIpAddressParts[0]=string[:i]
        if not isValidPart(currentIpAddressParts[0]):
            continue
        for j in range(i+1,i+min(len(string)-i,4)):
            currentIpAddressParts[1]=string[i:j]
            if not isValidPart(currentIpAddressParts[1]):
                continue
            for k in range(j+1,j+min(len(string)-j,4)):
                currentIpAddressParts[2]=string[j:k]
                currentIpAddressParts[3]=string[k:]
                if isValidPart(currentIpAddressParts[2]) and isValidPart(currentIpAddressParts[3]):
                    ipAddressesFound.append('.'.join(currentIpAddressParts))
    return ipAddressesFound
def isValidPart(string):
    stringAsInt=int(string)
    if stringAsInt>255:
        return False
    return len(string)==len(str(stringAsInt))# to check for leading zeros