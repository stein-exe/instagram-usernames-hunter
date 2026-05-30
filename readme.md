# 🔍 Instagram Username Hunter

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux%20%7C%20Windows-lightgrey.svg)

A powerful multi-threaded Instagram username availability checker that helps you find available usernames on Instagram. Get instant notifications via Telegram when rare usernames become available!

---

## 📋 Table of Contents

- [Features](#-features)
- [Use Cases](#-use-cases)
- [Installation](#-installation)
  - [Termux Setup](#termux-android)
  - [Linux/Windows Setup](#linuxwindows)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Screenshots](#-screenshots)
- [Developer](#-developer)

---

## ✨ Features

- 🚀 **Multi-threaded checking** - Check up to 20 usernames simultaneously
- 🎲 **Random username generation** - Auto-generate random usernames with custom patterns
- 📝 **Batch checking** - Check multiple usernames from a text file
- 📱 **Telegram notifications** - Get instant alerts when available usernames are found
- 🎨 **Colorful interface** - Beautiful terminal UI with random color schemes
- ⚡ **Fast & efficient** - Optimized for speed with concurrent requests
- 🔧 **Customizable** - Choose specific characters for each position in random mode

---

## 💡 Use Cases

- **Brand Protection** - Monitor when specific usernames become available
- **Username Hunting** - Find rare, short, or OG usernames
- **Business Accounts** - Secure the perfect username for your business
- **Personal Branding** - Get notified when your desired username is free
- **Bulk Checking** - Validate availability of multiple username options at once

---

## 📦 Installation

### Termux (Android)

**Copy and paste this entire block into Termux:**

```bash
pkg install python -y && pkg install git -y && git clone https://github.com/stein-exe/instagram-usernames-hunter && cd instagram-usernames-hunter && pip install -r requirements.txt && python instagram.py
```

**That's it! The script will start automatically after installation.**

---

**Or follow step-by-step:**

1. Install required packages:
```bash
pkg install python -y
pkg install git -y
```

2. Clone the repository:
```bash
git clone https://github.com/stein-exe/instagram-usernames-hunter
cd instagram-usernames-hunter
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Run the script:
```bash
python instagram.py
```

### Linux/Windows

1. **Install Python 3.7+** (if not already installed)
   - Download from [python.org](https://www.python.org/downloads/)

2. **Clone the repository:**
```bash
git clone https://github.com/stein-exe/instagram-usernames-hunter
cd instagram-usernames-hunter
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the script:**
```bash
python "instagram username checker.py"
```

---

## ⚙️ Configuration

### Setting Up Telegram Bot

To receive notifications when available usernames are found, you need to set up a Telegram bot:

#### Step 1: Create a Telegram Bot

1. Open Telegram and search for **[@BotFather](https://t.me/BotFather)**
2. Start a chat and send `/newbot`
3. Follow the instructions to create your bot
4. **Copy the bot token** (looks like: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

#### Step 2: Get Your Chat ID

1. Search for **[@userinfobot](https://t.me/userinfobot)** on Telegram
2. Start a chat with the bot
3. It will automatically send you your **Chat ID** (looks like: `123456789`)

#### Step 3: Activate Your Bot

1. Search for your bot on Telegram (using the username you created)
2. Click **START** to activate it

Now you're ready to use the script with your bot token and chat ID!

---

## 🚀 Usage

When you run the script, you'll be prompted to enter:

### 1. **Telegram Bot Token**
```
Enter Telegram bot token: 123456789:ABCdefGHIjklMNOpqrsTUVwxyz
```

### 2. **Chat ID**
```
Enter chat ID: 123456789
```

### 3. **Choose Checking Mode**

#### Option 1: Random Username Generation

Generate random usernames and check their availability.

**Auto Mode:**
- Generates completely random lowercase usernames
- Example: `abcde`, `xyzpq`, `mnbvc`

**Custom Mode:**
- Choose specific characters for each position
- Example: For a 5-character username, you can specify:
  - Position 1: `abc` (only a, b, or c)
  - Position 2: `123` (only 1, 2, or 3)
  - Position 3: Press Enter (any allowed character)
  - And so on...

```
Choose an option:
1. Check random
2. Check from list
Enter choice (1/2): 1

Random format:
1. Auto
2. Choose specific randomness
Enter choice (1/2): 1

Enter username length: 5
```

#### Option 2: Check from List

Check usernames from a text file.

1. Create a text file (e.g., `usernames.txt`) with one username per line:
```
coolname
awesome_user
brand.official
my_username
```

2. Run the script and choose option 2:
```
Choose an option:
1. Check random
2. Check from list
Enter choice (1/2): 2

Enter path to username list: usernames.txt
```

---

## 🔍 How It Works

1. **Cookie Generation** - The script first generates Instagram session cookies
2. **Username Validation** - Validates usernames (minimum 5 characters)
3. **Availability Check** - Sends requests to Instagram's signup endpoint
4. **Multi-threading** - Uses 20 concurrent threads for fast checking
5. **Telegram Notification** - Sends a message to your Telegram when an available username is found
6. **Color-coded Output** - Shows results in terminal:
   - 🟢 **Green** = Available
   - 🔴 **Red** = Unavailable

---

## 📸 Screenshots

The script features a beautiful ASCII art banner with random color schemes that change on each run, making your username hunting experience more enjoyable!

---

## 📝 Notes

- **Minimum username length:** 5 characters
- **Allowed characters:** Letters (a-z), numbers (0-9), periods (.), and underscores (_)
- **Thread count:** 20 concurrent threads (optimized for speed)
- **Rate limiting:** The script handles Instagram's rate limits automatically
- **Usernames starting with @:** The script automatically removes the @ symbol

---

## ⚠️ Disclaimer

This tool is for educational purposes only. Use responsibly and respect Instagram's Terms of Service. The developer is not responsible for any misuse of this tool.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Developer

**Developed by:** [@rejerk](https://t.me/rejerk)

**Join our community:** [@keped](https://t.me/keped)

---

## 💬 Support

If you have any questions or need help, feel free to:
- Message me on Telegram: [@rejerk](https://t.me/rejerk)
- Join our group chat: [@keped](https://t.me/keped)

---

<div align="center">

### ⭐ Star this repo if you find it useful!

Made with ❤️ by [@rejerk](https://t.me/rejerk)

</div>
