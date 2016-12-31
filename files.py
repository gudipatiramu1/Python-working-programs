myobj=open("test.doc","w")
myobj.write("""This is cool!
Now I can create file using python!""")
myobj.close()
myobj=open("test.doc","a")
myobj.write("""Let's see where this text goes""")
myobj.close()
