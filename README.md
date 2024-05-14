<h1 align="center"><em>Ustoz Shogird telegram bot</em></h1>


<p align="center">
  <a href="https://github.com/donBarbos/telegram-bot-template/actions/workflows/docker-image.yml"><img src="https://img.shields.io/github/actions/workflow/status/donBarbos/telegram-bot-template/docker-image.yml?label=docker%20image" alt="Docker Build Status"></a>
  <a href="https://www.python.org/downloads"><img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python"></a>
<p>

## 🚀 How to Use

### 🐳 Running in Docker _(recommended method)_

- configure environment variables in `.env` file

- start services

  ```bash
  docker compose up -d --build
  ```

- make migrations

  ```bash
  docker compose exec bot alembic upgrade head
  ```
## 🐋 If you want without clone project or without more python codes

- ### It's running with docker 
- ### Your device must be linux and you must be have docker in your terminal
- ### Firstly open terminal write this command for login docker
  
  ```bash
    docker login
  ```
- ### Secondly you pulling image ustoz_shogird_bot
  
  ```bash
    docker pull sarvarpydev/ustoz_shogird_bot
  ```

- ### Finally write this command (BOT_TOKEN=" " in there should be your bot token)

  ```bash
    docker run --name ustoz_shogird_bot_container -e BOT_TOKEN='' -d sarvarpydev/ustoz_shogird_bot
  ```

## 🌍 What I use in this project

- <h3>i18 used </h3>
- <h3>aiogram used</h3>
- <h3>aiogram State for queue </h3>
- <h3>Makefile for facilitate some commands</h3>

## 📂 Project Folder Structure

```bash
.
├── admin # Source code for admin panel
|   ├── __init__.py
|   └── admin.py
|
├── keyboards # Source code for keyboards 
|   ├── __init__.py
|   └── keyboarsd.py 
|
├── loacals # Locales for changeing language package
|   ├── ru
|   |   └── LC_MESSAGES
|   |   |   ├── messages.mo
|   |   |   ├── messages.po
|   ├── uz
|   |   └── LC_MESSAGES
|   |   |   ├── messages.mo
|   |   |   ├── messages.po
|   └── messages.pot
|
├── routers # routers package for routers
|   ├── __init__.py
|   ├── handler.py
|   ├── send_to_admin.py
|   └── user.py
|
├── .dockerignore
├── .env.example
├── .gitignore
├── config.py
├── Dockerfile # Dockerfile for Telegram Bot
├── main.py
├── Makefile # commands for change language with i18
├── requirements.txt # its for which library i use 
└── README.md # Documentation
```

## 🌐 Connect with me:

<p align="left">
<a href="https://linkedin.com/in/sarvarbek-davranbekov-3272212a5" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="sarvarbek-davranbekov-3272212a5" height="30" width="40" /></a>
<a href="https://www.facebook.com/profile.php?id=100081788845272" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg" alt="https://www.facebook.com/profile.php?id=100081788845272" height="30" width="40" /></a>
<a href="https://instagram.com/sarvar_py_dev" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="sarvar_py_dev" height="30" width="40" /></a>
<a href="https://www.leetcode.com/sarvar_py_dev" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/leet-code.svg" alt="sarvar_py_dev" height="30" width="40" /></a>
</p>