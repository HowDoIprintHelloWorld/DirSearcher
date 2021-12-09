import requests, pyfiglet, sys, time

wordlist = ""

# Produces Banner 
def startup():
  pyfiglet.print_figlet("DirSearcher", "slant")
  print("Like gobuster, but just a little slower")

# Parses arguments
def getargs():
  timeinterval = 0.1
  
  # Gets necessary wordlist and url
  if "-w" in sys.argv and "-u" in sys.argv:
    wordlist = sys.argv[sys.argv.index("-w") + 1]
    url = sys.argv[sys.argv.index("-u") + 1]
  else:
    print("Please supply url (-u) and wordlist (-w)")
    sys.exit()
    
  # Gets optional arguments
  if "-t" in sys.argv:
    timeinterval = int(sys.argv[sys.argv.index("-t") + 1])
  return wordlist, url, timeinterval
  

def wrdlist(wordlist):
  l = []
  
  # Tries to get words from wordlist supplied
  try: 
    with open(wordlist, "r") as file:
      for line in file:
        l.append(line.rstrip())
  except FileNotFoundError:
    print("Error loading file. Please try again.")
    return None, False
    
  if len(wordlist) > 0: 
    print("Wordlist loaded: " + wordlist)
    
  return l, True


# Brains of the operation. Sends requests and analyses response
def request(l, url, tint):
  worked = []
  for i in l:
    try:
      rqst = requests.get(f"{url}/{i}")
      if rqst.status_code < 400:
        print(f"[ + ]     {url}/{i}\n[{rqst.status_code}]\n")
    except:
      print(f"{url}/{i} doesn't exist")
    time.sleep(tint)

# Heart of the operation. Starts all the functions
if __name__ == "__main__":
  worked = False
  startup()
  wordl, url, timeinterval = getargs()
  while not worked: 
    list, worked = wrdlist(wordl)
  request(list, url, timeinterval)
  
  
  
