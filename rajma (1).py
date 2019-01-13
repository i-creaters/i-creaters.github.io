import gspread
import subprocess
from oauth2client.service_account import ServiceAccountCredentials
import schedule
import time
from bs4 import BeautifulSoup
import os

# page = open('index.html')
# soup = BeautifulSoup(page, 'html.parser')
# findId = soup.find(id='asmit12321')
# findId.contents[0].replace_with('Ujjwal singh')

# with open("index.html", "w") as outf:
#     outf.write(str(soup))


i = 0


def f():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'rajma-chawal-2854bb2a3f55.json', scope)
    gc = gspread.authorize(credentials)
    wks1 = gc.open('adminrajma').sheet1
    records = wks1.get_all_records()
    global i
    if(len(records)) > i:
        template = records[i]['Chose one of the templates']
        about_you = records[i]['About you?']
        title = records[i]['Enter title for your website?']
        linkedin = records[i]['Enter your Linkdin Id link?']
        github = records[i]['Enter your github link?']
        facebook = records[i]['Enter your facebook link?']
        email = records[i]['Enter your E-mail Address?']
        institute = records[i]['Institute you are studying in?']
        profession=records[i]['Enter something about your profession?']
        #image = records[i]['Enter the link of your image?']
        something_bussiness = records[i]['Enter Something about your business']
        print("flag paras")
        i += 1

        if (template == "Portfolio"):
            page = open('Portfolio/index.html')
            soup = BeautifulSoup(page, 'html.parser')
            findId = soup.find(id='asmit12321')
            findId.contents[0].replace_with(title)
            findId = soup.find(id='asmit1232')
            findId.contents[0].replace_with(title)
            findId = soup.find(id='facebook')
            findId['href']=facebook
            findId = soup.find(id='linkedin')
            findId['href']=linkedin
            findId = soup.find(id="mail")
            findId['href']=email
            
            with open("Portfolio/index.html", "w") as outf:
                outf.write(str(soup))
            #subprocess.call(['cd Portfolio'])
            os.chdir(r"/home/parasmehan123/Desktop/Rajma_Chawal/Portfolio")
            #print('SH FILE RUN BHOOTEKE')
            
            subprocess.call(['./g.sh'])

            
            
        elif (template == "Restaurants"):
            page = open('Restaurant/index.html',encoding = "ISO-8859-1")
            soup = BeautifulSoup(page, 'html.parser')
            findId = soup.find(id='nameof')
            findId.contents[0].replace_with(title)
            findId = soup.find(id='nameof1')
            findId.contents[0].replace_with(title)
            findId = soup.find(id='aboutus')
            findId.contents[0].replace_with(about_you)
            with open("Restaurant/index.html", "w") as outf:
                outf.write(str(soup))

            os.chdir(r"/home/parasmehan123/Desktop/Rajma_Chawal/Restaurant")
            subprocess.call(['./g.sh'])
            

        elif (template == "Business"):

            page = open('Business/index.html',encoding = "ISO-8859-1")
            soup = BeautifulSoup(page, 'html.parser')
            findId = soup.find(id='paras')
            findId.contents[0].replace_with(title)
            findId = soup.find(id='paras1')
            findId.contents[0].replace_with(title)
            findId = soup.find(id='info')
            findId.contents[0].replace_with(about_you)
            findId = soup.find(id='facebook')
            findId['href']=facebook
            findId = soup.find(id='linkedin') 
            findId['href']=linkedin
            # findId = soup.find(id="mail")
            # findId['href']=email
            # findId.contents[0].replace_with(email)
            with open("Business/index.html", "w") as outf:
                outf.write(str(soup))

            os.chdir(r"/home/parasmehan123/Desktop/Rajma_Chawal/Business")
            subprocess.call(['./g.sh'])


        elif (template == "Designer"):
            print("fee")
            page=open('Designer/index.html')
            soup = BeautifulSoup(page, 'html.parser')
            findId = soup.find(id='name')
            findId.contents[0].replace_with(title)
            findId = soup.find(id='name1')
            findId.contents[0].replace_with(title)
            findId = soup.find(id='name2')
            findId.contents[0].replace_with(title)
            findId = soup.find(id='name3')
            findId.contents[0].replace_with(title)
            findId = soup.find(id='name4')
            findId.contents[0].replace_with(title)
            findId = soup.find(id='name5')
            findId.contents[0].replace_with(title)
            findId = soup.find(id='name6')
            findId.contents[0].replace_with(title)
            findId = soup.find(id='about1')
            findId.contents[0].replace_with(about_you)
            findId = soup.find(id='facebook')
            findId['href']=facebook
            findId = soup.find(id='pinterest') 
            findId['href']=linkedin
            # findId = soup.find(id="mail")
            # findId['href']=email
            # findId.contents[0].replace_with(email)
            with open("Designer/index.html", "w") as outf:
                outf.write(str(soup))

            #subprocess.call(['cd Designer'])
            
            os.chdir(r"/home/parasmehan123/Desktop/Rajma_Chawal/Designer")
            subprocess.call(['./g.sh'])

        os.chdir(r"/home/parasmehan123/Desktop/Rajma_Chawal/")
            
        #subprocess.call(['pwd'])




                 





# with open("index.html", "w") as outf:
#     outf.write(str(soup))

#subprocess.call(['pwd'])


schedule.every(5).seconds.do(f)
# schedule.every(1).minutes.do(r)
while 1:
    schedule.run_pending()
    # time.sleep(0.5)
