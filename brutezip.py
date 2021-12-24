import zipfile
import sys



def crackPassword(file, wordlist):
    for word in wordlist:
        print(f"Senha usada: {word}")

        try:
            file.extractall(pwd=bytes(word, "utf-8"))

        except:
            continue 

        else:
            print(f"Senha Encontrada: {word}")
            return True
        
    return False


def main():
    file = zipfile.ZipFile(sys.argv[1])
    wordlist = open(sys.argv[2]).read().split("\n")

    result = crackPassword(file, wordlist)

    if(result == False):
        print("Senha não encontrada")
    
    else:
        exit(0)


main()