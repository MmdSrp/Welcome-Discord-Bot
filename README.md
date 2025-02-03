<a id="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/mmdsrp">
    <img src="https://img.icons8.com/?size=512&id=30998&format=png" alt="Logo" width="100" height="100">
  </a>

  <h3 align="center">Welcome Bot Discord </h3>

  <p align="center">
    Welcome bot source code for Discord
    <br />
  <p align="center">
    سورس کد بات خوش آمد گویی برای دیسکورد
    <br />
    <a href="https://mmdsrp.ir"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://mmdsrp.ir/">Creator Site</a>
    &middot;
    <a href="https://discord.com/users/671944662113583114">Report Bug</a>
  </p>
</div>



<!-- ABOUT THE PROJECT -->
## About The Project (درباره این کد)


- English -
Discord bot python code for welcome after a person joins the server

- فارسی -
کد پایتون بات دیسکورد برای خوش آمد گویی بعد از جوین شدن فرد در سرور


Use the `python welcome.py` to get started.

برای شروع از `python welcome.py` استفاده کنید.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Bot setup instructions (دستورالعمل های راه اندازی بات)

* pip
  ```sh
  pip install discord
  ```

  * pip
  ```sh
  pip install discord.py
  ```

1.
```python
   TOKEN = 'Your Bot Token'
   ```
2.
```python
   WELCOME_CHANNEL_ID = Your Welcome Channel Id'
   ```
3. Start Bot (روشن کردن بات)
   ```sh
   python welcome.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Explanation of the Bot in English
This Discord bot is designed to send a welcome message to new members who join any server where the bot is present. Here's how it works:

1. **Initialization**: The bot initializes with a command prefix of `!` and uses all intents to access necessary events and data.

2. **Welcome Message Embed**: A welcome message embed is created with a title, description, and color.

3. **Checking for New Members**: A loop runs every 5 seconds to check for new members who joined after the bot was launched. If a new member is found, their ID is added to a global list, and a welcome message is sent.

4. **On Ready Event**: When the bot is ready, it prints a message in the console and starts the loop to check for new members.

5. **Sending Welcome Messages**: When a new member is detected, the bot sends a personalized welcome message to a specified channel with the member's avatar and a friendly greeting.

### Explanation of the Bot in Persian
این ربات دیسکورد برای ارسال یک پیام خوش آمد گویی به اعضای جدیدی که به هر سروری که ربات در آن حضور دارد، طراحی شده است. نحوه کار آن به این صورت است:

1. **راه‌اندازی**: ربات با پیشوند دستوری `!` راه‌اندازی می‌شود و از تمام intents برای دسترسی به رویدادها و داده‌های لازم استفاده می‌کند.

2. **پیام خوش آمد گویی**: یک پیام خوش آمد گویی با عنوان، توضیحات و رنگ ایجاد می‌شود.

3. **بررسی اعضای جدید**: یک حلقه هر ۵ ثانیه اجرا می‌شود تا اعضای جدیدی که بعد از راه‌اندازی ربات به سرور پیوسته‌اند را بررسی کند. اگر یک عضو جدید پیدا شود، شناسه آن به یک لیست سراسری اضافه می‌شود و یک پیام خوش آمد گویی ارسال می‌شود.

4. **رویداد آماده**: وقتی ربات آماده می‌شود، یک پیام در کنسول چاپ می‌کند و حلقه بررسی اعضای جدید را آغاز می‌کند.

5. **ارسال پیام‌های خوش آمد گویی**: وقتی یک عضو جدید شناسایی می‌شود، ربات یک پیام خوش آمد گویی شخصی‌سازی شده به یک کانال مشخص ارسال می‌کند که شامل آواتار عضو و یک خوش آمد گویی دوستانه است.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Creators

### MmdSrp

<a href="https://mmdsrp.ir">
  <img src="https://cdn.discordapp.com/avatars/671944662113583114/ad61e5d849293185a835bcdc8f995f34.webp?size=1024&width=409&height=409" alt="hamidmine image" width="100" height="100" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

MmdSrp - [mmdsrp.ir](https://mmdsrp.ir)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Python-url]: https://www.python.org/
