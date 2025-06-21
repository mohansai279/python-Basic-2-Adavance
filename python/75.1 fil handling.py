# Write to a file
with open("demo.txt", "w") as f:
    f.write("My name is Python.\n")
    f.write("I love file handling.\n")

# Append more text
with open("demo.txt", "a") as f:
    f.write("This line was appended.\n")

# Read it back
with open("demo.txt", "r") as f:
    print(f.read())
