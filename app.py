import subprocess

username = input("Enter your username: ")

print("Welcome", username)

command = input("Enter a command: ")

subprocess.call(command, shell=True)
