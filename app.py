import subprocess

username = input("Enter your username: ")

print(f"Welcome {username}")

command = input("Enter a command: ").split()

subprocess.run(command, check=True)
