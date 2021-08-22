import hashlib
import os
import random
fileHash = ['fea5f2bf1d0365d548676d62ba873f71e99a2c1e','10ff780d2fe67206204d9704f825cfce95180dbb','2ff3b4e23503ee68c39d15dccaaa3bd6f721a4f3'] #input own hashes here if u want
hashesFound = []
hashResults = []
hashesFoundList = open("SHA256 Hashes Found.txt", "w+")
hashesFoundList1 = open("MD5 Hashes Found.txt", "w+")
hashesFoundList2 = open("SHA1 Hashes Found.txt", "w+")

# made by aliomarz0
def sha256hash_file(file):

    a = hashlib.sha256()

    with open(file,'rb') as File:
        chunk = 0
        while chunk != b'':
            chunk = File.read(1024)
            a.update(chunk)

    return a.hexdigest()

def md5hash_file(file):

    a = hashlib.md5()

    with open(file,'rb') as File:
        chunk = 0
        while chunk != b'':
            chunk = File.read(1024)
            a.update(chunk)

    return a.hexdigest()


def sha1hash_file(file):

    a = hashlib.sha1()

    with open(file,'rb') as File:
        chunk = 0
        while chunk != b'':
            chunk = File.read(1024)
            a.update(chunk)

    return a.hexdigest()


def check_file(directory):
    i = 0
    for filename in os.scandir(directory):
       if filename.is_file():
           for hash in fileHash:


               if md5hash_file(filename) == hash:
                       print(f'Match found. {filename} is equal to MD5 {hash}')
                       hashResults.append(f'{filename} - {hash}\n')



               elif sha1hash_file(filename) == hash:
                       print(f'Match found. {filename} is equal to SHA1 {hash}')
                       hashResults.append(f'{filename} - {hash}\n')



               elif sha256hash_file(filename) == hash:
                       print(f'Match found. {filename} is equal to SHA256 {hash}')
                       hashResults.append(f'{filename} - {hash}\n')



    while True:
        answer1 = input("Do you want to save these results in a textfile? 1 for yes, 0 for no")
        if answer1 == '1':
            results = open(f"Hash Result.txt", "w+")
            for hashResult in hashResults:
                results.write(hashResult)
            break
        elif answer1 == '0':
            print("Thank you for using this program")
            break
        else:
            i += 1
            if i > 3:
                print("Program Terminated.")
                break
            print("Input not understood. Please enter 1 or 0.")


hashFile = input("Do you want to hash files or check for file hashes?\n1.Check for file hashes\n2. Hash Files")
if hashFile == '1':
    directory = input("Enter the name of the directory you want to scan")
    hashLocation = input("Enter the directory of the .txt file of the hashlist you made e.g C:/Downloads/hashlist.txt\n")
    hashRead = open(hashLocation,"r")
    hashSplit = hashRead.read().split()
    fileHash.append(hashSplit)
    print(fileHash)
    hashCheck = input("The program will check for the following hashes.\nMD5\nSHA1\nSHA256\n Are you ready? Press any key to continue")
    check_file(directory)
elif hashFile == '2':
    directory = input("Enter the name of the directory you want to hash")
    hashChoice = input("What hashing algorithm?\n1.SHA1\n2.SHA256\n3.MD5")
    if hashChoice == '1':
        for filename in os.scandir(directory): #sha1
            if filename.is_file():
                sha1ed = sha1hash_file(filename)

                hashesFoundList2.write(f"SHA1 {sha1ed}\n")

    elif hashChoice == '2':
        for filename in os.scandir(directory):
            if filename.is_file():
                sha256ed = sha256hash_file(filename)
                hashesFoundList.write(f"SHA256 {sha256ed}\n")

    elif hashChoice == '3':
        for filename in os.scandir(directory):
            if filename.is_file():
                md5ed = md5hash_file(filename)
               
                hashesFoundList1.write(f"MD5 {md5ed}\n")
                
    else:
        print("WRONG INPUT")





