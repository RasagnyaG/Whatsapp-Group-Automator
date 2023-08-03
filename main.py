from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

groupName = input("Enter the group name: ")
contacts = input("Enter the contacts that you want to add (space seperated): ").split()
print(contacts)
chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

#open WA web
driver.get('https://web.whatsapp.com/')

snap = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "side")))

# step 1 : click on the three dot menu
def clickMenu():
    menu = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id=\"app\"]/div/div/div[4]/header/div[2]/div/span/div[4]/div/span")))
    menu.click()
    print("menu clicked")

# step 2 : choose to create a new group
def clickNewGroup():
    item = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id=\"app\"]/div/div/div[4]/header/div[2]/div/span/div[4]/span/div/ul/li[1]")))
    item.click()
    print("new group clicked")

# step 3 : a function to search for a particular contact and add it (call it as many as needed according to the input)
def chooseContact(contact):
    try:
        input = snap.find_element(By.XPATH,
                                  "//*[@id=\"app\"]/div/div/div[3]/div[1]/span/div/span/div/div/div[1]/div/div/div[2]/input")
        input.send_keys(contact)
        cont = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, f"//*[@id=\"app\"]//div[@role=\"button\"]//span[@title=\"{contact}\"]")))
        cont.click()
        print(f"{contact} added")
    except:

        # incase the contact is not found, clear the search and throw and exception
        input.clear()
        print(f"Couldn't find the contact {contact}")

# step 4 : the forward button to br clicked once all the contacts are added
def forwardButton():
    button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH,  "//*[@id=\"app\"]/div/div/div[3]/div[1]/span/div/span/div/div/span/div/span")))
    button.click()

# step 5 : give a name to the group and finish the process
def addName(name):
    input = snap.find_element(By.XPATH, "//div[contains(@title, 'Group Subject')]")
    input.send_keys(name)

    doneBtn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH,  "//*[@id=\"app\"]/div/div/div[3]/div[1]/span/div/span/div/div/span/div/div")))
    doneBtn.click()


try:
    clickMenu()
    clickNewGroup()
    for contact in contacts:
        chooseContact(contact)
    forwardButton()
    addName(groupName)
    print("Group created!")
except Exception as exception:
    print("Exception: {}".format(type(exception).__name__))
    print("Exception message: {}".format(exception))