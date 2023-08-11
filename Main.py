import pandas as pd
import time

# Storing the CSV file in a variable to make things easier 
File = "shows.csv"

Database = pd.read_csv(File, delimiter=";")

#Definning essential functions ==>

#  For Aesthetic Purposes only :
def seperator():
    print("----------------------")

# To Welcome the User :
def welcome():
    print("Hello User. I am a Show Recommender (^ _ ^).\n Would you like to Proceed?\n")
    global chosen_answer 
    chosen_answer = input ("My answer is :  ").upper()
    
# To Save the User's Chosen Genre into a Variable
def chosen_genre():
    print("==> Please choose a genre by typing it's corresponding letter :\n")
    global chosen_genre
    chosen_genre =  input("My chosen genre is :  ").upper()

# To Save the User's Chosen Type into a Variable
def chosen_type():
    print("==> Please choose a type by typing it's corresponding letter:\n")
    global chosen_type
    chosen_type = input("My answer is:  ").upper()

# To Match Said Variables with the Items in the Dictionaries (Genres,Types)

def Matching():
      global U_Genre,U_Type
      U_Genre = Genres.get(chosen_genre)
      U_Type = Types.get(chosen_type)

# To Search into the DataBase for the Shows that match the User's Input
    
def recommendation():
    global Show, Recommended_shows
    Show = Database[(Database['Genre'] == U_Genre) & (Database['Type'] == U_Type)]
    Recommended_shows = Show['Name']
    max_length = Recommended_shows.str.len().max()
    seperator()
    print(f"Here are the shows I recommend : \n")
    print(f"{Recommended_shows.str.ljust(max_length).to_string(index=False)}\n")



# Essential Variables

Genres = {
    'A':'Science Fiction',
    'B':'Comedy',
    'C':'Drama',
    'D':'Fantasy',
    'E':'Crime',
    'F':'Historical',
   
}

Types ={
    'A':'TV Show',
    'B':'Film'
}

# Start of the ACTUAL code 

welcome()
if chosen_answer == "YES":
  seperator()
# Print the Genres List ==>
  for key,value in Genres.items():
     print("{}: {}".format(key, value))
# Ask User for their chosen Genre ==>
  seperator()
  chosen_genre()
  seperator()
#Print the Types List ==>
  for key,value in Types.items():
      print("{}: {}".format(key,value))
# Ask User for their chosen Types ==>
  seperator()
  chosen_type()
# Processing Data ( Just to add mystery ;) !!! )
  seperator()
  print("\nProcessing your choices..\n")
  time.sleep(1.0)
  print("Still working on it...\n")
  time.sleep(0.6)
  print("Almost..\n")
  time.sleep(0.4)
  Matching()
  recommendation()
  exit = input("Press enter to exit")
        
elif chosen_answer == "NO":
    print("Fine...\nEnjoy looking for something to watch by yourself !! >:[")
    exit()
else :
    print("I'm not sure I understand...Try Again later ? \n")
    exit()