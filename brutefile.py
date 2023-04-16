
import zipfile

zip_file_name = input("Enter the name of the zip file: ")
wordlist_file_name = input("Enter the name of the wordlist file: ")

with open(wordlist_file_name, "r") as wordlist_file:
    for line in wordlist_file:
        password = line.strip()
        try:
            with zipfile.ZipFile(zip_file_name, "r", password=password) as zip_file:
                zip_file.extractall()
                print("The zip file was successfully unzipped.")
                break
        except:
            continue

    if not zip_file.extractall():
        print("The zip file could not be unzipped.")
