# I'm kinda rewriting the directions on this one
# Ask user for name of file
# Ask user what to put in file
# Output info to .txt file

if __name__ == "__main__":
    name = input("What would you like your file to be named?\n")
    text = input("What would you like written in your file?\n")

    with open(name + ".txt", "w") as openfile: #create very localized scope in below block (super cool!)
        openfile.write(text)
    

#"w" = write only, "r" = read only, "r+" = read and write!