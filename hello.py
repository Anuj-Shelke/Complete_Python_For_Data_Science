#Write a program to read from file poem.txt and find if twinkle word is present in the file 

with open("poem.txt") as f:
    content = f.read()
    if("Twinkle" in content):
        print(content)
    else:
        print("The file does not contain the word sorry")




    


