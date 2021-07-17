#modules
from genericpath import isfile
import webbrowser,datetime,random,os,sys,requests,json,smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
#functions
def date():
    print(datetime.datetime.now())

def search():  
    icog = input()
    if(icog.lower() == 'incognito'):
        search = input("What do you want to search for ? ")
        if(search != ''):
            url = 'https://www.google.com/search?q=' + search
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
            webbrowser.get(chrome_path).open_new(url)
        else:
            print('no input given...not searching')
    else:
        search = input("What do you want to search for ? ")
        if(search != ''):
            url = 'https://www.google.com/search?q=' + search
            webbrowser.get().open(url)
        else:
            print('no input given...not searching')

def play():
    path = "C:\\Users\\HP\\Desktop\\music"
    files = os.listdir(path)
    d = random.choice(files)
    os.startfile('C:\\Users\\HP\\Desktop\\music\\' + d)

def video():
    try:
        search = input("What do you want to search for ? ")
        if(search != ''):
            url = 'https://www.youtube.com/results?search_query=' + search
            webbrowser.get().open(url)
    except:
        print('no input given...not searching')

def shut():
    c = input('1.press s for Shutdown \n 2.press r for Restart \n 3.else press any other button to abort. \n')
    if(c.lower() == 's'):
        os.system("shutdown /s /t 0")
    if(c.lower() == 'r'):
        os.system("shutdown /r /t 0")
    else:
        print('task abborted')

def weather():
    try:
        f_data = list()
        api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
        city = input('City Name : ')
        url = api_address + city
        json_data = requests.get(url).json()
        print("Weather desc and temp in celsius")
        f1 = json_data['weather'][0]['main']
        ftemp = json_data['main']['temp']
        f2 = int(ftemp)-273
        f_data.append(f1)
        f_data.append(f2)
        for data in f_data:
            print(data)
    except:
        print("city does not exist.")

def new_f():
    print("All folders will be created on the desktop.")
    nf = input('Enter name of directory: ')
    directory = nf
    parent_dir = "C:/Users/HP/Desktop/"
    checkdir = parent_dir+directory
    try:
        isfile = os.path.isfile(checkdir)
        path = os.path.join(parent_dir,directory)
        os.mkdir(path)
        print('folder created')
    except:
        print("folder already exists.")
    
def duckduckgo():
    print('What image/Wallpaper you want to look for ? ')
    img = input()
    if(img != ''):
        url = 'https://duckduckgo.com/?q=' + img + '+wallpaper&t=h_&iar=images&iax=images&ia=images'
        webbrowser.get().open(url)
    else:
        print('no input')
        

def photos():
    path = "D:\\PHOTOS\\"
    files = os.listdir(path)
    try:
        print('which file do you want to open ?')
        for name in files:
            print(name)
        fname = input()
        os.startfile("D:\\PHOTOS\\" + fname)
    except:
        print('incorrect file')
    
while(True):
    #Greeting   
    if(int(datetime.datetime.now().time().hour) >=5 and int(datetime.datetime.now().time().hour) < 12):
        print('Good Morning')
    elif(int(datetime.datetime.now().time().hour) >= 12 and int(datetime.datetime.now().time().hour) < 16):
        print('Good Afternoon')
    elif(int(datetime.datetime.now().time().hour) >= 16 and int(datetime.datetime.now().time().hour) < 19):
        print('Good Evening')
    elif(int((datetime.datetime.now().time().hour) >= 19 and int(datetime.datetime.now().time().hour) < 24) or ((datetime.datetime.now().time().hour) >= 24 and int(datetime.datetime.now().time().hour) < 5)):
        print('It\'s late')
    else:
        print('incorrect timezone')
    #assistance
    try:
        a = input('How can I assist you ?  ')
        assist = a.lower()
        if('date' in assist or 'time' in assist):
            date()
        if('search' in assist or 'find' in assist):
            search()
        if('music' in assist or 'songs' in assist):
            play()
        if('youtube' in assist or 'video' in assist):
            video()
        if('shutdown' in assist or 'restart' in assist):
            shut()
        if('weather' in assist or 'climate' in assist):
            weather()
        if('new folder' in assist):
            new_f()
        if('wallpaper' in assist or 'images' in assist):
            duckduckgo()
        if('photos' in assist):
            photos()
        if('exit' in assist):
            break
    except:
        print("wrong command, please try again.")
        