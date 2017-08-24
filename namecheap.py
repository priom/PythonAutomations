import webbrowser, sys

# sys.argv

# check if cli args passed
if len(sys.argv) < 2:
    print("Please enter your desired domain name!")
else:
    webbrowser.open('https://www.namecheap.com/domains/registration/results.aspx?domain=' + sys.argv[1])


