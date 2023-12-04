from winpwn import *

context.newline = "\n"

p = remote("chal.tuctf.com", 30012)

p.recvuntil("KEY:")
p.sendline("111111111111111111111111111111111111111111111111")
p.recvuntil("Select an Option:")

def option1():
    p.sendline("1")
    p.recvuntil("Select an Option:")

def option2():
    p.sendline("2")
    p.recvuntil("Study the Map to Be Able to Complete the Missions.\n")
    p.recvline()

    maps = {}

    while True:
        p.recvline()
        current = p.recvline().split(":")[1].strip()
        desc = p.recvline().strip()
        options = p.recvline().split("Options:  ")[1].strip().split("  ")

        if not current in maps:
            maps[current] = (desc, options)
        p.recvuntil("Next Location to Investigate:")
        p.sendline(input())
    
        print(maps)

def option3():
    p.sendline("3")
    p.recvuntil("Next Best Path to Take:")
    path = ["Charity", "Emell", "Iyona", "Kepliker", "Osiros", "Rhenora", "Shariot"]
    # Send each path, send 'done' at last

def option4():
    p.sendline("4")
    p.recvuntil("Input the Key:")
    p.sendline("good_job_agent1089")
    p.recvuntil(">")
    context.log_level = "debug"
    # Decode bytes with UTF-8
    p.recvuntil("our flag")
    context.log_level = ""

def option5():
    p.sendline("5")
    p.recvuntil("TYPE IN THE FLAG:")
    p.sendline("TUCTFISAMAZINGIWILLCOMEBACKAGAIN")
    p.recvuntil("Blessings Be Upon You. Good Bye!!")