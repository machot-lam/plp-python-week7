# Write three notes to a new file 
with open("my_notes.txt", "w") as f:
    f.write("Python is fun\n" )
# Write a second note
    f.write("I am learning python\n")
# Write a third note
    f.write("Programming is interesting\n")
# Write the fourth note
    line = f.write("I added this later\n")
    print(line, end="")

    # count the line
    with open("my_notes.txt", "r") as f:
        lines = f.readlines()
        print(" total lines:", len(lines))
        