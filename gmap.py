import webbrowser, sys, pyperclip

sys.argv

# check if cli args passed
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.ca/maps/place/' + address)
