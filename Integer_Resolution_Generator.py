print("Integer Resolution Generator")
print("By Thomas Seeds")
print("How to use: Input your targeted dimensions, Input the desired operation, Input the amount of values you want returned.\nMost numbers work better when rounded down. ")
x = input("xres\n")
y = input("yres\n")
operation = input("* or /\n")
times = input("amount\n")
times = (int(times))
x = (int(x))
y = (int(y))
increment = 1
while(increment) <= (times) and (operation) == ("*"):
    print((x) * (increment),(y) * (increment))
    increment = (increment) + (1)
while(increment) <= (times) and (operation) == ("/"):
    print((x) / (increment),(y) / (increment))
    increment = (increment) + (1)
exitinput = input("Type 'exit' to exit.")
if(exitinput) == ("exit"):
    exit
