import requests, pyfiglet, sys

wordlist = ""

def startup():
  pyfiglet.print_figlet("DirSearcher", "slant")
  print("Like gobuster, but just a little slower")

def wrdlist():
  l = []
  if "-w" in sys.argv:
    wordlist = sys.argv[sys.argv.index("-w") + 1]
  try: 
    with open(wordlist, "r") as file:
      for line in file:
        l.append(line.rstrip())
  except:
    print("Error loading file. Please try again.")
    return None, False
    
  if len(wordlist) > 0: 
    print("Wordlist loaded: " + wordlist)
    
  return l, True




if __name__ == "__main__":
  worked = False
  startup()
  while not worked: 
    list, worked = wrdlist()
  
  
