```
██████  ██░ ██ ▓█████  ██▀███   ██▓     ▒█████   ▄████▄   ██ ▄█▀
▒██    ▒ ▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒▓██▒    ▒██▒  ██▒▒██▀ ▀█   ██▄█▒ 
░ ▓██▄   ▒██▀▀██░▒███   ▓██ ░▄█ ▒▒██░    ▒██░  ██▒▒▓█    ▄ ▓███▄░ 
  ▒   ██▒░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄  ▒██░    ▒██   ██░▒▓▓▄ ▄██▒▓██ █▄ 
▒██████▒▒░▓█▒░██▓░▒████▒░██▓ ▒██▒░██████▒░ ████▓▒░▒ ▓███▀ ░▒██▒ █▄
▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░▓  ░░ ▒░▒░▒░ ░ ░▒ ▒  ░▒ ▒▒ ▓▒
░ ░▒  ░ ░ ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░░ ░ ▒  ░  ░ ▒ ▒░   ░  ▒   ░ ░▒ ▒░
░  ░  ░   ░  ░░ ░   ░     ░░   ░   ░ ░   ░ ░ ░ ▒  ░        ░ ░░ ░ 
      ░   ░  ░  ░   ░  ░   ░         ░  ░    ░ ░  ░ ░      ░  ░   
                                                  ░               
```

# 📱 **InstaDel - Instagram Activity Cleaner**

`instdel.py` is a simple yet powerful Python script that helps you clean up your Instagram activity, including comments, likes, reels, and posts. Built with Selenium and ChromeDriver, this script interacts with your Instagram account and allows you to quickly delete various types of activity. 🚀

## ✨ **Features**

* 📝 **Delete Comments**
* ❤️ **Delete Likes**
* 🎬 **Delete Reels**
* 🖼️ **Delete Posts**
* 🔑 **Manual Login**: Log in manually through the browser, then proceed to clean your account.
* 🔄 **No Quit After Deletion**: After deleting items, the script returns you to the main menu to select another option.

## ⚙️ **Requirements**

* **Python** (version 3.x)
* **Selenium**: Used for automating web interactions.
* **ChromeDriver**: Needed to interact with the Chrome browser. Ensure you have the appropriate version for your operating system.

### 📦 **Installation**

1. Install Python (if not already installed).
   Download Python from [here](https://www.python.org/downloads/).

2. Install the required Python packages by running the following command:

   ```bash
   pip install selenium
   ```

3. Download **ChromeDriver** from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
   Ensure the version matches the version of Google Chrome you're using.

4. Make sure **chromedriver** is in your system's PATH or provide the path to chromedriver in the script.

---

## 🛠️ **How to Use**

1. Clone or download the repository and save the file as `instdel.py`.

2. Before running the script, log into your Instagram account manually via the Chrome browser that will be used by the script.

3. Run the script:

   ```bash
   python instdel.py
   ```

4. The script will open a Chrome browser window. After logging in, you will see the following options:

   ```
   === INSTAGRAM WIPE TOOL ===
   1. Delete Comments 📝
   2. Delete Likes ❤️
   3. Delete Reels 🎬
   4. Delete Posts 🖼️
   5. Exit ❌
   6. Update/Info ℹ️
   ```

   * Select an option (1-6) to choose the action you want to perform.
   * After completing an action (deleting items), you will be returned to the main menu to choose another action. The program will not quit unless you select "Exit."

---

## 🗑️ **Deletion Details**

* **Delete Comments 📝**: Deletes comments from posts you have interacted with.
* **Delete Likes ❤️**: Removes likes from posts and media.
* **Delete Reels 🎬**: Deletes reels that you have liked or interacted with.
* **Delete Posts 🖼️**: Deletes your Instagram posts.
* **Items per Deletion**: The number of items to delete at once is set in the script as `AT_ONCE_DELETE`. You can modify this value based on your preference.

---

## 🔑 **Manual Login Process**

1. When you run the script, it will prompt you to log in.
2. After logging in manually, click **"Not now"** on any pop-up dialogs asking whether you want to save your login information.
3. The script will then proceed to the activity page and perform the selected action.

---

## ⚠️ **Notes**

* **Please ensure that you are using the script with caution**, as deleting posts, comments, and likes is irreversible.
* The script **does not quit automatically** after completing an action; it will return to the menu, allowing you to choose another action.
* In case Instagram throws rate limits or issues, the script will handle these gracefully by refreshing the page and retrying the action.

---

## 🛠️ **Troubleshooting**

* **Browser Window Closes Unexpectedly**: Ensure that ChromeDriver is installed correctly and the version matches your installed version of Google Chrome.
* **Rate Limits**: If you hit Instagram's rate limits, the script will retry after refreshing the page.

---

## 📝 **License**

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---