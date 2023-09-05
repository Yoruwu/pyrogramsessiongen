
# Pyrogram Session ID Generator

This little script will allow you to generate an SessionID for use in Telegram bots.



## Requirements

1. Python
2. Pyrogram - script will check for it and auto install it via pip if needed. **Make sure to have the newest version or you may run into errors**
3. pip
4. A working brain (**very important**)


## How to use

1. Download the **gen.py** script from this repo.
2. Install **python and pip** (if not already done)
3. Go to the location where you saved the script and run it with:

```bash
python3 gen.py
```

4. Enter your details (**API ID** & **API HASH**) - you can get them from the [Telegram](https://my.telegram.org/auth) page.
5. Enter phone number (and your 2FA pass if you have one) then the login code. If everything goes right you should get an session id printed in your terminal. You should also see a new session pop up in telegram itself.
6. Use your ID. Make sure to never share it!


## How to disable an ID

1. Login into Telegram
2. Go to your active sessions
3. Remove the infected session


## Features

- Easy to use
- Install requiremnts script (for those who cant install pyrogram by themselfs)
- Better design

## ToDo

- [x] First Release
- [x] Better Code...
- [ ] GUI for not so techy users
- [x] Start working on making it look more professional
