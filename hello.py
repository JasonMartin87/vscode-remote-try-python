#a = 5
#b = 10

#if (a + b == 15):
    #print("15 is what we are looking for")
#elif (a + b < 15 or a + b > 15):
    #print("Not what we are looking for")

#Definition of the Hashes
Hash1 = "Hash1"
Hash2 = "Hash2"
Hash3 = "Hash3"
Hash4 = "Hash4"
Hash5 = "Hash5"
Hash6 = "Hash6"
Hash7 = "Hash7"

#List will be updated based on newly discovered hashes.

MaliciousHashList = [Hash1, Hash5, Hash3, Hash4, Hash6, Hash7]

IncomingHashList = [Hash1, Hash2, Hash5, Hash6, Hash7, Hash3, Hash4, Hash3, Hash1, Hash2, Hash3, Hash4, Hash3, Hash5, Hash6, Hash7]

#x = Incoming Hashes
#Summary: The following script will categorize malicious attacks based on hashes found from emails. 
#Step 1: Malicious Hash will be defined by x.
#Step 2: The Hash will be cross-analyzed from MaliciousHashList.
#Step 3: The end result of the script will define what kind of attack that incoming hash is.

for IncomingHash in IncomingHashList:
    IsIncomingHashSafe = True
    for MaliciousHash in MaliciousHashList:
        #1 == 1 = False
        #1 == 5 = False
        #1 == 3 = False
        #1 == 4 = False
        #2 == 1 = True
        #2 == 5 = True
        #2 == 3 = True
        #2 == 4 = True
        #3 == 1 = True
        #3 == 5 = True
        #3 == 3 = False
        #3 == 4 = False
        if (IncomingHash == MaliciousHash):
            IsIncomingHashSafe = False
    if (IsIncomingHashSafe == False):
        print(IncomingHash, "This is a malicious hash.")
    else:
        print(IncomingHash, "This hash is safe.")