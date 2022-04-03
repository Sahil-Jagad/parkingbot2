from flask import Flask, render_template, request 
from selenium import webdriver
from datetime import datetime
import time
import random
import pyautogui 
 

def bot(values):

    name_cars = {
    "Sahil": ["Toyota", "Highlander", "Silver", "6ZUP627"],
    "Matt": ["Lexus", "LS430", "Silver", "5KJK567"],
    "Tim": ["Honda", "CRV", "White", "7ECE482"],
    "Grace": ["Volkswagen", "Jetta", "Grey", "6ZIN828"],
    "Nica": ["Mazda", "3", "White", "8XSU346"],
    "Palak": ["Toyota", "Prius", "Dark Grey", ""],
    "Adrian": ["Hyundai", "Elantra", "Silver", "7BLT620"]
    }

    name_apartment = {
        1: ["Sahil Jagad",  1582],
        2: ["Adarsh Pachori", 1582],
        3: ["Matthew Prata",  1582],
        4 : ["Timothy Boshaw", 1582],
        5 : [ "Manasi Patel", 1328],
        6 : ["Ramya Mark" , 1328],
        7: ["Varshini Srikanth", 1328],
        8: ["Farhaan Rasool",  1506],
        9: ["Aashish Polineni",  1506],
    }

    option = webdriver.ChromeOptions()
    driver= webdriver.Chrome('/usr/local/bin/chromedriver',options = option)  

    driver.get("https://accounts.google.com/Login?continue=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSfS4YITfKS0UVVTUjO13E6rqPr4b744szTCZooaUH533vMISg%2Fviewform%3Ffbzx%3D-785423508921260424")

    gmail = driver.find_elements_by_class_name("whsOnd.zHQkBf")
    gmailSubmit = driver.find_elements_by_class_name("VfPpkd-vQzf8d")
    gmail[0].send_keys("mbprata19@damien-hs.edu")
    gmailSubmit[0].click()
    time.sleep(2)

    password = driver.find_elements_by_class_name("whsOnd.zHQkBf")
    passwordSubmit = driver.find_elements_by_class_name("VfPpkd-vQzf8d")
    password[0].send_keys("1FMlw1377")
    passwordSubmit[0].click()
    time.sleep(2)

    for name in values:

        driver.get("https://accounts.google.com/Login?continue=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSfS4YITfKS0UVVTUjO13E6rqPr4b744szTCZooaUH533vMISg%2Fviewform%3Ffbzx%3D-785423508921260424")

        textboxes = driver.find_elements_by_class_name("whsOnd.zHQkBf")
        CommunityButton = driver.find_element_by_class_name("e2CuFe.eU809d")
        submit = driver.find_element_by_class_name('NPEfkd.RveJvd.snByac')

        time.sleep(2)

        name_apt_list = name_apartment[random.randint(0,9)]
        textboxes[0].send_keys(name_apt_list[0]) #name
        textboxes[1].send_keys(name_apt_list[1]) #apartment
        textboxes[2].send_keys(name_cars[name][0]) #make
        textboxes[3].send_keys(name_cars[name][1]) #model
        textboxes[4].send_keys(name_cars[name][2]) #color
        textboxes[5].send_keys(name_cars[name][3]) #plate
        current_time = datetime.now()
        formatted_date = current_time.strftime("%m/%d/%Y")
        textboxes[6].send_keys(formatted_date) #date

        CommunityButton.click()
        time.sleep(1)
        for i in range(4):
            pyautogui.press('down')
        pyautogui.press('enter')
        time.sleep(3)
        submit.click()


    driver.close()

#initialise app
app = Flask(__name__)

#decorator for homepage 
@app.route('/' )
def index():
    return render_template('index.html',
                           PageTitle = "Landing page")

@app.route('/', methods = ["POST"] )
def call_bot():
        value = request.form.getlist('check') 
        bot(value)
        return render_template('index.html',
                           PageTitle = "Landing page")

if __name__ == '__main__':
    app.run(debug = True)
