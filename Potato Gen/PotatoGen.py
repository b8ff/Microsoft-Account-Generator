from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from selenium.webdriver.common.by import By
from random import randint, sample, choice
from win32api import GetSystemMetrics
from random_word import RandomWords
import undetected_chromedriver
from time import sleep
import ctypes
import msvcrt
import sys
import os

def log(step):
    print(step)

def setup():
    ctypes.windll.kernel32.SetConsoleTitleW("PotatoGen v3")
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
        self.PREFERENCES = {"credentials_enable_service" : False, "profile.password_manager_enabled" : False}
        self.DRIVERVERSION = 103

        self.MICROSOFTSIGNUP = "https://signup.live.com/signup?wa=wsignin1.0&rpsnv=13&ct=1656322628&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d84195185-8c5b-4818-2f7d-dc10a1b164aa&id=292841&aadredir=1&whr=outlook.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&contextid=7CD0ACC3A36D208A&bk=1656322628&uiflavor=web&lic=1&mkt=EN-EN&lc=1040&uaid=304f33a463d341388d71ab5068be748c"

        self.WORDS = RandomWords()
        self.CHARACTERS = f"{ascii_lowercase}{ascii_uppercase}{digits}{punctuation}"

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

        self.STORAGE = [0, 0]

        self.start()

    def credentials(self):
        log("\nGenerating credentials...")

        self.NAME_LENGTH = randint(5, 8)
        self.LASTNAME_LENGTH = randint(5, 8)

        try:
            self.NAME_INPUT = "".join(filter(str.isascii, self.WORDS.get_random_word(hasDictionaryDef="true", minLength=self.NAME_LENGTH, maxLength=self.NAME_LENGTH).title()))
            self.LASTNAME_INPUT = "".join(filter(str.isascii, self.WORDS.get_random_word(hasDictionaryDef="true", minLength=self.LASTNAME_LENGTH, maxLength=self.LASTNAME_LENGTH).title()))
        except (Exception,):
            log("\nPotatoGen could not generate credentials. This is probably caused by a failed connection to the dictionary website.\nPress any key to exit...")
            os.system("color 0C")
            msvcrt.getch()
            exit()

        self.FULLNAME_INPUT = f"{self.NAME_INPUT}{self.LASTNAME_INPUT}{randint(1000, 9999)}"
        self.PASSWORD_INPUT = "".join(sample(self.CHARACTERS, 15))

        self.COUNTRY_INPUT = choice(["United States", "United Kingdom", "Canada"])
        self.BIRTHMONTH_INPUT = choice(["May", "October", "January"])
        self.BIRTHDAY_INPUT = randint(1, 31)
        self.BIRTHYEAR_INPUT = randint(1989, 2003)

    def driver(self):
        self.DRIVEROPTIONS = undetected_chromedriver.ChromeOptions()
        self.DRIVEROPTIONS.add_argument("--log-level=3")
        self.DRIVEROPTIONS.add_experimental_option("prefs", self.PREFERENCES)
        if not os.path.exists("chromedriver.exe"):
            undetected_chromedriver.install(executable_path="", target_version=self.DRIVERVERSION)
        log("Starting Chrome Driver...")
        self.DRIVER = undetected_chromedriver.Chrome(executable_path=self.DRIVERDIRECTORY, options=self.DRIVEROPTIONS)

        self.DRIVER.set_window_size(450, 600)
        self.DRIVER.set_window_position((round(GetSystemMetrics(0) / 2) - round(450 / 2)), (round(GetSystemMetrics(1) / 2) - round(600 / 2)))

    def generate(self):
        delete(2)

        log("Connecting to signup page...")
        self.DRIVER.get(self.MICROSOFTSIGNUP)

        log("Generating account...")
        while True:
            sleep(0.1)
            try:
                if self.DRIVER.find_element(By.NAME, "MemberName").is_displayed() and self.DRIVER.find_element(By.ID, "iSignupAction").is_displayed() and self.STORAGE[0] == 0:
                    self.DRIVER.find_element(By.NAME, "MemberName").send_keys(self.FULLNAME_INPUT)
                    self.DRIVER.find_element(By.ID, "iSignupAction").click()

                    self.STORAGE[0] += 1
            except (Exception,):
                pass

            try:
                if self.DRIVER.find_element(By.ID, "PasswordInput").is_displayed() and self.DRIVER.find_element(By.ID, "iOptinEmail").is_displayed() and self.DRIVER.find_element(By.ID, "iSignupAction").is_displayed() and self.STORAGE[0] == 1:
                    self.DRIVER.find_element(By.ID, "PasswordInput").send_keys(self.PASSWORD_INPUT)
                    self.DRIVER.find_element(By.ID, "iOptinEmail").click()
                    self.DRIVER.find_element(By.ID, "iSignupAction").click()

                    self.STORAGE[0] += 1
            except (Exception,):
                pass

            try:
                if self.DRIVER.find_element(By.ID, "FirstName").is_displayed() and self.DRIVER.find_element(By.ID, "LastName").is_displayed() and self.DRIVER.find_element(By.ID, "iSignupAction").is_displayed() and self.STORAGE[0] == 2:
                    self.DRIVER.find_element(By.ID, "FirstName").send_keys(self.NAME_INPUT)
                    self.DRIVER.find_element(By.ID, "LastName").send_keys(self.LASTNAME_INPUT)
                    self.DRIVER.find_element(By.ID, "iSignupAction").click()

                    self.STORAGE[0] += 1
            except (Exception,):
                pass

            try:
                if self.DRIVER.find_element(By.ID, "Country").is_displayed() and self.DRIVER.find_element(By.ID, "BirthMonth").is_displayed() and self.DRIVER.find_element(By.ID, "BirthDay").is_displayed() and self.DRIVER.find_element(By.ID, "BirthYear").is_displayed() and self.DRIVER.find_element(By.ID, "iSignupAction").is_displayed() and self.STORAGE[0] == 3:
                    self.DRIVER.find_element(By.ID, "Country").send_keys(self.COUNTRY_INPUT)
                    self.DRIVER.find_element(By.ID, "BirthMonth").send_keys(self.BIRTHMONTH_INPUT)
                    self.DRIVER.find_element(By.ID, "BirthDay").send_keys(self.BIRTHDAY_INPUT)
                    self.DRIVER.find_element(By.ID, "BirthYear").send_keys(self.BIRTHYEAR_INPUT)
                    self.DRIVER.find_element(By.ID, "iSignupAction").click()

                    self.STORAGE[0] += 1
            except (Exception,):
                pass

            try:
                if self.DRIVER.find_element(By.ID, "enforcementFrame").is_displayed() and self.STORAGE[0] == 4:
                    log("Complete the bot verification to continue...")
                    os.system("color 08")

                    self.STORAGE[0] += 1
            except (Exception,):
                pass

            try:
                if self.DRIVER.find_element(By.ID, "KmsiCheckboxField").is_displayed() and self.DRIVER.find_element(By.ID, "idBtn_Back").is_displayed() and self.STORAGE[0] == 5:
                    os.system("color 03")
                    self.DRIVER.find_element(By.ID, "KmsiCheckboxField").click()
                    self.DRIVER.find_element(By.ID, "idBtn_Back").click()
                    self.DRIVER.close()

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

                    break
            except (Exception,):
                pass

    def start(self):
        setup()

        if input("Do you want to generate a new Microsoft account? (y, n): ").lower() != "y":
            exit()

        try:
            self.STORAGE[1] = int(input("How many accounts do you want to generate? (max 3): "))
        except (Exception,):
            self.STORAGE[1] = 1

        if self.STORAGE[1] > 3:
            self.STORAGE[1] = 3
        elif self.STORAGE[1] < 1:
            self.STORAGE[1] = 1

        log("\nIF THE PHONE VERIFICATION SCREEN APPEARS CHANGE IP AND RESTART POTATOGEN")
        for _ in range(self.STORAGE[1]):
            self.STORAGE[0] = 0

            self.credentials()
            self.driver()
            self.generate()

        os.system("color 0A")
        if self.STORAGE[1] == 1:
            log(f"\nSuccessfully generated {self.STORAGE[1]} Microsoft account!")
        else:
            log(f"\nSuccessfully generated {self.STORAGE[1]} Microsoft accounts!")

        log("Press any key to exit...")
        msvcrt.getch()
        exit()


PotatoGen()
