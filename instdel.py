import os
import logging
import pathlib
import platform
import random
import sys
import time

# suppress TensorFlow Lite logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService

logging.basicConfig(format="[%(levelname)s] instdel: %(message)s", level=logging.INFO)

# Do not edit
MODE = -1
LIKES_URL    = "https://www.instagram.com/your_activity/interactions/likes"
COMMENTS_URL = "https://www.instagram.com/your_activity/interactions/comments"
REELS_URL    = "https://www.instagram.com/your_activity/photos_and_videos/reels"
POSTS_URL    = "https://www.instagram.com/your_activity/photos_and_videos/posts"

AT_ONCE_DELETE = 20

logging.info("Starting...")
try:
    # configure ChromeDriver to send logs to null
    service = ChromeService(executable_path='./chromedriver', log_path=os.devnull)

    options = Options()
    # suppress ChromeDriver “DevTools listening” & lower Chrome logs
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--log-level=3")

    if platform.system() == "Windows":
        wd = pathlib.Path().absolute()
        options.add_argument(f"user-data-dir={wd}\\chrome-profile")
    else:
        options.add_argument("user-data-dir=chrome-profile")
    
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1200, 900)
    logging.info("Opened Chrome browser")

    # Big ASCII title in red
    ascii_title = r"""
██████  ██░ ██ ▓█████  ██▀███   ██▓     ▒█████   ▄████▄   ██ ▄█▀
▒██    ▒ ▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒▓██▒    ▒██▒  ██▒▒██▀ ▀█   ██▄█▒ 
░ ▓██▄   ▒██▀▀██░▒███   ▓██ ░▄█ ▒▒██░    ▒██░  ██▒▒▓█    ▄ ▓███▄░ 
  ▒   ██▒░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄  ▒██░    ▒██   ██░▒▓▓▄ ▄██▒▓██ █▄ 
▒██████▒▒░▓█▒░██▓░▒████▒░██▓ ▒██▒░██████▒░ ████▓▒░▒ ▓███▀ ░▒██▒ █▄
▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░▓  ░░ ▒░▒░▒░ ░ ░▒ ▒  ░▒ ▒▒ ▓▒
░ ░▒  ░ ░ ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░░ ░ ▒  ░  ░ ▒ ▒░   ░  ▒   ░ ░▒ ▒░
░  ░  ░   ░  ░░ ░   ░     ░░   ░   ░ ░   ░ ░ ░ ▒  ░        ░ ░░ ░ 
      ░   ░  ░  ░   ░  ░   ░         ░  ░    ░ ░  ░ ░      ░  ░   
"""
    print("\033[31m" + ascii_title + "\033[0m")  # Red color

    # Menu
    while True:
        print("\n=== INSTAGRAM WIPE TOOL ===")
        print("1. Delete Comments")
        print("2. Delete Likes")
        print("3. Delete Reels")
        print("4. Delete Posts")
        print("5. Exit")
        print("6. Update/Info")
        mode = input("Choose mode [1/2/3/4/5/6]: ").strip()

        if mode not in ["1", "2", "3", "4", "5", "6"]:
            continue
        
        MODE = int(mode)

        if MODE == 5:
            print("Exiting the program...")
            sys.exit(0)

        if MODE == 6:
            print("\nUpdate/Info:")
            print("This tool helps you delete comments, likes, reels, and posts from your Instagram account.")
            print("Before using the tool, you must manually log into your Instagram account in the opened Chrome browser.")
            print("You also need to click the 'Not now' button in case Instagram prompts you to save login info.")
            print(f"You can choose the number of items to delete at once by modifying the AT_ONCE_DELETE variable (current value: {AT_ONCE_DELETE}).")
            print("The program works by interacting with your Instagram activity page via Selenium and ChromeDriver.")
            print("It will allow you to delete comments, likes, reels, or posts based on the option you choose from the menu.")
            print("After deletion, the program will return to the menu for you to choose another action.")
            print("\nNow, returning to main menu...\n")
            time.sleep(2)
            continue  # back to the menu

        # Navigate based on choice
        if MODE == 1:
            driver.get(COMMENTS_URL)
            logging.info("Opening " + COMMENTS_URL)
        elif MODE == 2:
            driver.get(LIKES_URL)
            logging.info("Opening " + LIKES_URL)
        elif MODE == 3:
            driver.get(REELS_URL)
            logging.info("Opening " + REELS_URL)
        else:  # MODE == 4
            driver.get(POSTS_URL)
            logging.info("Opening " + POSTS_URL)

        # Wait for manual login & “Not now” dialog
        target_url = COMMENTS_URL if MODE == 1 else LIKES_URL if MODE == 2 else REELS_URL if MODE == 3 else POSTS_URL
        while True:
            if driver.current_url.startswith(target_url):
                logging.info("Login detected")
                break
            try:
                logging.info("Waiting for sign in... (Sign in manually and don't touch anything else after!)")
                wait = WebDriverWait(driver, 60)

                def is_not_now_div_present(drv):
                    try:
                        div = drv.find_element(By.CSS_SELECTOR, "div[role='button']")
                    except:
                        return False
                    return div.text == "Not now"

                wait.until(is_not_now_div_present)
                logging.info("Login detected")
                driver.find_element(By.CSS_SELECTOR, "div[role='button']").send_keys(Keys.ENTER)
                logging.info("Clicked 'Not now' on login save dialog")
                break
            except TimeoutException:
                pass

        # Function to start the deletion process
        def start_deletion():
            # Main Loop
            while True:
                # 1) Click “Select”
                is_clicked_select = False
                while not is_clicked_select:
                    logging.info(
                        "Waiting for "
                        + ("comments" if MODE == 1 else "likes" if MODE == 2 else "reels" if MODE == 3 else "posts")
                        + " to load..."
                    )
                    time.sleep(2)
                    for el in driver.find_elements(By.XPATH, "//span[text()='Sélectionner']"):
                        try:
                            # check for no results
                            try:
                                if driver.find_elements(By.XPATH, "//span[text()='Aucun résultat']"):
                                    logging.info("No items found. DONE. Returning to menu")
                                    return  # Return to the menu, not quit
                            except StaleElementReferenceException:
                                pass
                            driver.execute_script("arguments[0].click();", el)
                            logging.info("Clicked 'Sélectionner'")
                            is_clicked_select = True
                            break
                        except StaleElementReferenceException:
                            continue
                    # Check for "You haven't"
                    try:
                        if driver.find_elements(By.XPATH, "//span[starts-with(text(),'Vous n')]"):
                            logging.info("No items found. Returning to menu")
                            return  # Return to the menu, not quit
                    except StaleElementReferenceException:
                        pass

                # 2) Select up to AT_ONCE_DELETE items
                selected_count = 0
                while selected_count == 0:
                    time.sleep(1)
                    icons = driver.find_elements(By.CSS_SELECTOR, 'div[data-bloks-name="ig.components.Icon"]')
                    for icon in icons:
                        style = icon.get_attribute("style") or ""
                        if style.startswith('mask-image: url("https://i.instagram.com/static/images/bloks/icons/generated/circle__outline'):
                            driver.execute_script("arguments[0].click();", icon)
                            selected_count += 1
                            logging.info(f"Selected item (Total: {selected_count})")
                            if selected_count >= AT_ONCE_DELETE:
                                break
                if selected_count == 0:
                    logging.info("No selectable items found. Returning to menu")
                    return  # Return to the menu, not quit

                # 3) Click Delete/Unlike
                delete_clicked = False
                delete_text = "Supprimer" if MODE in (1, 3, 4) else "Ne plus aimer"
                for span in driver.find_elements(By.XPATH, f"//span[text()='{delete_text}']"):
                    try:
                        time.sleep(1)
                        driver.execute_script("arguments[0].click();", span)
                        logging.info(f"Clicked '{delete_text}'")
                        delete_clicked = True
                        break
                    except StaleElementReferenceException:
                        continue

                if not delete_clicked:
                    logging.warning("Delete/Remove button not found. Refreshing the page and retrying...")
                    driver.refresh()
                    continue

                # 4) Confirm deletion dialog
                is_clicked_confirmation = False
                while not is_clicked_confirmation:
                    time.sleep(1)
                    for btn in driver.find_elements(By.CSS_SELECTOR, 'div[role="dialog"] button'):
                        try:
                            btn_text = btn.find_element(By.CSS_SELECTOR, "div").text
                        except:
                            continue
                        try:
                            if btn_text == delete_text:
                                driver.execute_script("arguments[0].click();", btn)
                                logging.info(f"Confirmed '{delete_text}'")
                                is_clicked_confirmation = True
                                break
                            elif btn_text == "OK":
                                driver.execute_script("arguments[0].click();", btn)
                                logging.warning("Rate limit hit. Clicked 'OK'. Refreshing...")
                                driver.refresh()
                                time.sleep(2)
                                is_clicked_confirmation = True
                                break
                        except StaleElementReferenceException:
                            continue

        # Start deletion process
        start_deletion()

except KeyboardInterrupt:
    print()
    logging.info("Quitting on keyboard interrupt...")
    driver.quit()
    sys.exit(0)
except NoSuchWindowException:
    logging.exception("Browser window closed unexpectedly")
    sys.exit(1)
except Exception:
    logging.exception("Something went wrong")
    sys.exit(1)
