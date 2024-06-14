# Twitch Point Farmer

![Repository Size](https://img.shields.io/github/repo-size/Mephisto-Grumpy/twitch-point-farmer?style=for-the-badge)
![Sourcery](https://img.shields.io/badge/SOURCERY-ENABLED-green?style=for-the-badge)
![License](https://img.shields.io/github/license/Mephisto-Grumpy/twitch-point-farmer?style=for-the-badge)

Automatically collect channel points for your favorite Twitch streamers.

> [!NOTE]
> This script is for educational purposes only. Use it at your own risk.

> [!WARNING]
> Cannot clicking on collect points (Active watching)

## Installation

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Download [Chromedriver](https://chromedriver.chromium.org/downloads) or [Geckodriver](https://github.com/mozilla/geckodriver) and add it to your system's `PATH`:

   - **Windows**: Add the directory containing `chromedriver.exe` to your `PATH`.
   - **Linux**: Move `chromedriver` to `/usr/local/bin/` or `/usr/bin/`.

3. Obtain your Twitch authentication cookie (`auth-token`):

   - Go to Twitch and log in.
   - Follow instructions to retrieve the `auth-token` cookie:
     - **Chrome**: Go to `chrome://settings/cookies/detail?site=twitch.tv`.
     - **Firefox**: Use Developer Tools (`Ctrl+Shift+I` or `F12`), go to Storage tab > Cookies > `https://www.twitch.tv`.
   - Copy the value of the `auth-token` cookie.

> [!NOTE]
> To get the `auth-token` cookie, you can also use the following JavaScript code in the browser console:
>
> ```javascript
> document.cookie.match(/auth-token=([^;]+)/)[1]
> ```

4. Rename `config.example.json` to `config.json` and fill in your details:

   ```json
   {
     "browser": "chrome", // or "firefox"
     "driverPath": "", // path to chromedriver or geckodriver
     "authTokenCookie": "", // Twitch auth-token cookie
     "streamers": [], // list of streamers to watch
     "hideTheBot": true, // hide the bot in the viewer list
     "logs": true // enable logging
   }
   ```

5. Launch the script:
   ```bash
   python main.py
   ```

## Features

- Automatically collects points every 5 minutes (+10pts).
- Retrieves drops (+50pts).
- Watches consecutive streams (+450pts).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This project is licensed under the [GPLv3 License](LICENSE).

## Owner

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Darkempire78">
        <img src="https://avatars.githubusercontent.com/u/50015928" width="100px;" alt="Darkempire78"/>
        <br />
        <sub><b>Darkempire78</b></sub>
      </a>
    </td>
  </tr>
</table>
