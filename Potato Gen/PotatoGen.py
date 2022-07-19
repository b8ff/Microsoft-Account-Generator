from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from random import randint, sample, choice
from win32api import GetSystemMetrics
from random_word import RandomWords
from string import ascii_letters
import undetected_chromedriver
from msvcrt import getch
from time import sleep
import ctypes
import sys
import os

def log(step):
    print(step)

def setup():
    ctypes.windll.kernel32.SetConsoleTitleW("PotatoGen v4.2")
    os.system("cls")
    os.system("color 03")
    print("""
     ______   ______    ______   ______    ______   ______    ______    ______    __   __    
    /\ === \ /\  __ \  /\__  _\ /\  __ \  /\__  _\ /\  __ \  /\  ___\  /\  ___\  /\ "-.\ \   
    \ \  _-/ \ \ \/\ \ \/_/\ \/ \ \  __ \ \/_/\ \/ \ \ \/\ \ \ \ \__ \ \ \  __\  \ \ \-.  \  
     \ \_\    \ \_____\   \ \_\  \ \_\ \_\   \ \_\  \ \_____\ \ \_____\ \ \_____\ \ \_\\\\"\_\ 
      \/_/     \/_____/    \/_/   \/_/\/_/    \/_/   \/_____/  \/_____/  \/_____/  \/_/ \/_/ 
      
       MAKE SURE TO USE A VPN OR A PROXY
""")

def delete(lines):
    while lines != 0:
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        lines -= 1

class PotatoGen:
    def __init__(self):
        super(PotatoGen, self).__init__()

        self.DRIVER = None
        self.DRIVERDIRECTORY = "chromedriver.exe"
        self.DRIVEROPTIONS = None
        self.DRIVERPREFERENCES = {"credentials_enable_service" : False, "profile.password_manager_enabled" : False}
        self.DRIVERTIMEOUT = 86400
        self.DRIVERVERSION = 103

        self.MICROSOFTSIGNUP = "https://signup.live.com/signup?wa=wsignin1.0&rpsnv=13&ct=1656322628&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d84195185-8c5b-4818-2f7d-dc10a1b164aa&id=292841&aadredir=1&whr=outlook.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&contextid=7CD0ACC3A36D208A&bk=1656322628&uiflavor=web&lic=1&mkt=EN-EN&lc=1040&uaid=304f33a463d341388d71ab5068be748c"

        self.CHARACTERS = f"{ascii_lowercase}{ascii_uppercase}{digits}{punctuation}"
        self.NOTLETTERS = f"{digits}{punctuation}"
        self.LETTERS = ascii_letters
        self.WORDS = RandomWords()

        self.NAME_INPUT = None
        self.LASTNAME_INPUT = None
        self.FULLNAME_INPUT = None
        self.PASSWORD_INPUT = None

        self.NAME_LENGTH = None
        self.LASTNAME_LENGTH = None

        self.COUNTRY_INPUT = None
        self.BIRTHMONTH_INPUT = None
        self.BIRTHDAY_INPUT = None
        self.BIRTHYEAR_INPUT = None

        self.STORAGE = [False, 0, True]

        self.start()

    def credentials(self, dictionary):
        if self.STORAGE[0]:
            log("\nGenerating new credentials...")
        else:
            delete(2)
            log("Generating credentials...")

        self.NAME_LENGTH = randint(5, 8)
        self.LASTNAME_LENGTH = randint(5, 8)

        if dictionary:
            try:
                self.NAME_INPUT = self.WORDS.get_random_word(hasDictionaryDef="true", minLength=self.NAME_LENGTH, maxLength=self.NAME_LENGTH)
                self.LASTNAME_INPUT = self.WORDS.get_random_word(hasDictionaryDef="true", minLength=self.LASTNAME_LENGTH, maxLength=self.LASTNAME_LENGTH)

                for CHARACTER in self.NOTLETTERS:
                    if CHARACTER in self.NAME_INPUT:
                        self.NAME_INPUT = self.NAME_INPUT.replace(CHARACTER, "")
                    if CHARACTER in self.LASTNAME_INPUT:
                        self.LASTNAME_INPUT = self.LASTNAME_INPUT.replace(CHARACTER, "")

                self.NAME_INPUT = self.NAME_INPUT.title()
                self.LASTNAME_INPUT = self.LASTNAME_INPUT.title()
            except (Exception,):
                log("\nPotatoGen could not generate credentials. This is probably caused by a failed connection to the dictionary website.\nPress any key to exit...")
                self.DRIVER.close()
                os.system("color 0C")
                getch()
                exit()
        else:
            self.NAME_INPUT = "".join(sample(self.LETTERS, self.NAME_LENGTH)).title()
            self.LASTNAME_INPUT = "".join(sample(self.LETTERS, self.LASTNAME_LENGTH)).title()

        self.FULLNAME_INPUT = f"{self.NAME_INPUT}{self.LASTNAME_INPUT}{randint(1000, 9999)}"
        self.PASSWORD_INPUT = "".join(sample(self.CHARACTERS, 15))

        self.COUNTRY_INPUT = choice(["United States", "United Kingdom", "Canada"])
        self.BIRTHMONTH_INPUT = choice(["May", "October", "January"])
        self.BIRTHDAY_INPUT = randint(1, 31)
        self.BIRTHYEAR_INPUT = randint(1989, 2003)

    def driver(self):
        self.DRIVEROPTIONS = undetected_chromedriver.ChromeOptions()
        self.DRIVEROPTIONS.add_argument("--log-level=3")
        self.DRIVEROPTIONS.add_experimental_option("prefs", self.DRIVERPREFERENCES)
        if not os.path.exists("chromedriver.exe"):
            undetected_chromedriver.install(executable_path="", target_version=self.DRIVERVERSION)
        log("\nStarting Chrome Driver...\n")
        self.DRIVER = undetected_chromedriver.Chrome(executable_path=self.DRIVERDIRECTORY, options=self.DRIVEROPTIONS)

        self.DRIVER.set_window_size(450, 600)
        self.DRIVER.set_window_position((round(GetSystemMetrics(0) / 2) - round(450 / 2)), (round(GetSystemMetrics(1) / 2) - round(600 / 2)))

    def generate(self):
        if self.STORAGE[0]:
            log("Reconnecting to signup page...")
        else:
            log("Connecting to signup page...")
        self.DRIVER.get(self.MICROSOFTSIGNUP)

        if self.STORAGE[0]:
            log("Generating another account...")
        else:
            log("Generating account...")
        WebDriverWait(self.DRIVER, self.DRIVERTIMEOUT).until(expected_conditions.visibility_of_element_located((By.ID, "MemberName"))).send_keys(self.FULLNAME_INPUT)
        WebDriverWait(self.DRIVER, self.DRIVERTIMEOUT).until(expected_conditions.visibility_of_element_located((By.ID, "iSignupAction"))).click()

        WebDriverWait(self.DRIVER, self.DRIVERTIMEOUT).until(expected_conditions.visibility_of_element_located((By.ID, "PasswordInput"))).send_keys(self.PASSWORD_INPUT)
        WebDriverWait(self.DRIVER, self.DRIVERTIMEOUT).until(expected_conditions.visibility_of_element_located((By.ID, "iOptinEmail"))).click()
        WebDriverWait(self.DRIVER, self.DRIVERTIMEOUT).until(expected_conditions.visibility_of_element_located((By.ID, "iSignupAction"))).click()

        WebDriverWait(self.DRIVER, self.DRIVERTIMEOUT).until(expected_conditions.visibility_of_element_located((By.ID, "FirstName"))).send_keys(self.NAME_INPUT)
        WebDriverWait(self.DRIVER, self.DRIVERTIMEOUT).until(expected_conditions.visibility_of_element_located((By.ID, "LastName"))).send_keys(self.LASTNAME_INPUT)
        WebDriverWait(self.DRIVER, self.DRIVERTIMEOUT).until(expected_conditions.visibility_of_element_located((By.ID, "iSignupAction"))).click()

        WebDriverWait(self.DRIVER, self.DRIVERTIMEOUT).until(expected_conditions.visibility_of_element_located((By.ID, "Country"))).send_keys(self.COUNTRY_INPUT)
        WebDriverWait(self.DRIVER, self.DRIVERTIMEOUT).until(expected_conditions.visibility_of_element_located((By.ID, "BirthMonth"))).send_keys(self.BIRTHMONTH_INPUT)
        WebDriverWait(self.DRIVER, self.DRIVERTIMEOUT).until(expected_conditions.visibility_of_element_located((By.ID, "BirthDay"))).send_keys(self.BIRTHDAY_INPUT)
        WebDriverWait(self.DRIVER, self.DRIVERTIMEOUT).until(expected_conditions.visibility_of_element_located((By.ID, "BirthYear"))).send_keys(self.BIRTHYEAR_INPUT)
        WebDriverWait(self.DRIVER, self.DRIVERTIMEOUT).until(expected_conditions.visibility_of_element_located((By.ID, "iSignupAction"))).click()

        WebDriverWait(self.DRIVER, self.DRIVERTIMEOUT).until(expected_conditions.visibility_of_element_located((By.ID, "enforcementFrame"))).click()
        log("Complete the bot verification to continue...")
        os.system("color 08")

        WebDriverWait(self.DRIVER, self.DRIVERTIMEOUT).until(expected_conditions.visibility_of_element_located((By.ID, "KmsiCheckboxField"))).is_displayed()
        os.system("color 03")
        WebDriverWait(self.DRIVER, self.DRIVERTIMEOUT).until(expected_conditions.visibility_of_element_located((By.ID, "KmsiCheckboxField"))).click()
        WebDriverWait(self.DRIVER, self.DRIVERTIMEOUT).until(expected_conditions.visibility_of_element_located((By.ID, "idBtn_Back"))).click()

        if os.path.exists("accounts.txt"):
            with open("accounts.txt", "r") as SAVEACCOUNTS:
                LASTACCOUNTS = SAVEACCOUNTS.read()
                SAVEACCOUNTS.close()
        else:
            LASTACCOUNTS = ""

        with open("accounts.txt", "w+") as ACCOUNT:
            if LASTACCOUNTS == "":
                ACCOUNT.write("Accounts Generated By PotatoGen\n\n")
            else:
                ACCOUNT.write(f"{LASTACCOUNTS}\n\n")
            ACCOUNT.write(f"Name: {self.NAME_INPUT}\n")
            ACCOUNT.write(f"Lastname: {self.LASTNAME_INPUT}\n")
            ACCOUNT.write(f"EMail: {self.FULLNAME_INPUT}@outlook.com\n")
            ACCOUNT.write(f"Password: {self.PASSWORD_INPUT}")
            ACCOUNT.close()

        log("Done!")

    def start(self):
        setup()

        if input("Do you want to generate a new Microsoft account? (y, n): ").lower() != "y":
            exit()

        try:
            self.STORAGE[1] = int(input("How many accounts do you want to generate? (max 3): "))

            if self.STORAGE[1] > 3:
                self.STORAGE[1] = 3
            elif self.STORAGE[1] < 1:
                self.STORAGE[1] = 1
        except (Exception,):
            self.STORAGE[1] = 1

        if input("Do you want to use a dictionary to generate credentials? (y, n): ").lower() != "y":
            self.STORAGE[2] = False

        log("\nIF THE PHONE VERIFICATION SCREEN APPEARS CHANGE IP AND RESTART POTATOGEN")

        self.driver()
        for _ in range(self.STORAGE[1]):
            self.credentials(self.STORAGE[2])
            self.generate()

            if not self.STORAGE[0]:
                self.STORAGE[0] = True
            sleep(1)
        self.DRIVER.close()

        os.system("color 0A")
        if self.STORAGE[1] == 1:
            log(f"\nSuccessfully generated {self.STORAGE[1]} Microsoft account!")
        else:
            log(f"\nSuccessfully generated {self.STORAGE[1]} Microsoft accounts!")

        log("Press any key to exit...")
        getch()
        exit()


PotatoGen()
