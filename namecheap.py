# search domain in namecheap
import webbrowser, sys


# check no. of args
if len(sys.argv) < 2:
    print("Please enter your desired domain name!")
else:
    webbrowser.open('https://www.namecheap.com/domains/registration/results.aspx?domain=' + sys.argv[1])


