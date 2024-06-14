from Enigma.simple_replace import simple_replace, rotors


def main():
    r_word1 = ''
    r_word2 = ''
    r_word3 = ''
    with open(".\\Enigma\\replace_word1.txt", "r") as f:
        for line in f:
            r_word1 += line.strip()
        f.close()
    with open(".\\Enigma\\replace_word2.txt", "r") as f:
        for line in f:
            r_word2 += line.strip()
        f.close()
    with open(".\\Enigma\\replace_word3.txt", "r") as f:
        for line in f:
            r_word3 += line.strip()
        f.close()
    password = input("Enter password: ")
    cheatSheet = input("Enter CheatSheet: ")
    wordlist = list()
    for i in range(26):
        wordlist.append(chr(i + ord('A')))
    for rotor1 in wordlist:
        for rotor2 in wordlist:
            for rotor3 in wordlist:
                _rotor1 = ord(str(rotor1)) - ord('A')
                _rotor2 = ord(str(rotor2)) - ord('A')
                _rotor3 = ord(str(rotor3)) - ord('A')
                tmp_r1 = r_word1
                tmp_r2 = r_word2
                tmp_r3 = r_word3
                for i in range(_rotor1):
                    tmp_r1=rotors(tmp_r1)
                for i in range(_rotor2):
                    tmp_r2=rotors(tmp_r2)
                for i in range(_rotor3):
                    tmp_r3=rotors(tmp_r3)
                print('Trying: ' + chr(_rotor1 + ord('A')) + chr(_rotor2 + ord('A')) \
                      + chr(_rotor3+ord('A')) + ': ', end='')
                tmp = simple_replace(password, tmp_r1, tmp_r2, tmp_r3)
                if tmp ==cheatSheet:
                    print()
                    print("SUCCESS! THE ROTORS CODE IS "+ chr(_rotor1 + ord('A')) + chr(_rotor2 + ord('A')) \
                      + chr(_rotor3+ord('A')))
                    exit(0)
                else:
                    print("Failed")

if __name__ == '__main__':
    main()