<div id="top"></div>
<!--
*** Jose Santiago
*** 2022 Server Checker
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/JDSanti/Server_Checker">
    <img src="images/Logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Server Checker</h3>

  <p align="center">
    Server checker script 
    <br />
    <a href="https://github.com/JDSanti/Server_Checker"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/JDSanti/Server_Checker/issues">Report Bug</a>
    ·
    <a href="https://github.com/JDSanti/Server_Checker/issues">Request Feature</a>
    ·
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#documentation">Documentation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product  Screen Shot][product-screenshot]](https://www.amazon.com/iUniker-Expansion-Breakout-Raspberry-Inserted/dp/B07NKNBZYG?ref_=ast_sto_dp)
[![Email Name Screen Shot][email-screenshot]](https://github.com/JDSanti/Server_Checker)
[![Text  Screen Shot][text-screenshot]](https://github.com/JDSanti/Server_Checker)

### Built With

* [Python](https://www.python.org/downloads/)
* [Twilio](https://www.twilio.com/)
* [Yagmail](https://yagmail.readthedocs.io/en/latest/setup.html)
* [Gmail](https://mail.google.com/)
* [Raspberry Pi](https://www.raspberrypi.com/products/raspberry-pi-zero/)

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
1. Sign up for (or log in to) your Twilio account (<https://www.twilio.com/try-twilio>)

2. Get a phone number with SMS (and MMS) capabilities from Twilio

3. Get your Twilio account SID and Auth Token

5. Use your own Gmail account or create a new one for the usage of this script

### Installation

1. If using a Rapsberry Pi, make sure to install your flavor of OS and run its appropriate updates, also make sure that python is installed and updated
  ```sh
  python -V 
  ```
2. Install required packages:
* Twilio
  ```sh
  pip3 install twilio 
  ```
* Yagmail
  ```sh
  pip3 install yagmail 
  ```
3. Send an SMS message in Python via the REST API to make sure your account is properly setup
https://www.twilio.com/docs/sms/tutorials/how-to-send-sms-messages-python#send-an-sms-message-in-python-via-the-rest-api

4. Test sending email with simple one liner:
  ```sh
  yagmail.SMTP('mygmailusername').send('to@someone.com', 'subject', 'This is the body')
  ```
### Documentation
For additonal help please refer to libraries documentation below:

* Yagmail
See the [Yagmail Documentation](https://pypi.org/project/yagmail/) for project description.

* Twilio
See the [Twilio Documentation](https://www.twilio.com/docs/libraries/python#install-the-library) for project description.

<!-- USAGE EXAMPLES -->
## Usage
1. Clone the repo
   ```sh
   git clone https://github.com/JDSanti/Server_Checker.git
   ```
2. Setup your own email and password on script by replacing "email" and "password" with your own **NOTE: This method is not recommended, since you would be storing the full credentials to your account in your script in plain text. I did it for simplicity purposes but please refer to https://yagmail.readthedocs.io/en/latest/setup.html#configuring-credentials for proper storage of passwords.
   ```sh
   yag = yagmail.SMTP('email', 'password')
   ```
3. Setup your own phone numbers on script by replacing "from" and "to" variables with your own
   ```sh
    from_='+15555555555',
            to='+15555555555'
        )
   ```
3. Replace "server.com" with the domain of the web server you want to test. It can test multiple servers ["server.com","server2.com"] 
   ```sh
   servers_to_check=["server.com"]
   ```
4. Run script 
   ```sh
   python3 server.py
   ```
5. Setup as cron job
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Implement texting ability
- [x] Implement email ability
- [x] Setup as cron job on Pi Zero


See the [open issues](https://github.com/JDSanti/Server_Checker/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Jose Santiago - [@Capt_Santiago](https://twitter.com/Capt_Santiago) - jduhamel.santiago@outlook.com

Project Link: [https://github.com/JDSanti/Server_Checker](https://github.com/JDSanti/Server_Checker)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Larymak for his script of server checking](https://github.com/larymak/Python-project-Scripts/tree/main/ServerChecker)
* [How to send text message on python guide](https://www.twilio.com/blog/2016/04/how-to-send-a-text-message-with-python.html)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/JDSanti/Server_Checker.svg?style=for-the-badge
[contributors-url]: https://github.com/JDSanti/Server_Checker/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/JDSanti/Server_Checker.svg?style=for-the-badge
[forks-url]: https://github.com/JDSanti/Server_Checker/network/members
[stars-shield]: https://img.shields.io/github/stars/JDSanti/Server_Checker.svg?style=for-the-badge
[stars-url]: https://github.com/JDSanti/Server_Checker/stargazers
[issues-shield]: https://img.shields.io/github/issues/JDSanti/Server_Checker.svg?style=for-the-badge
[issues-url]: https://github.com/JDSanti/Server_Checker/issues
[license-shield]: https://img.shields.io/github/license/JDSanti/Server_Checker.svg?style=for-the-badge
[license-url]: https://github.com/JDSanti/Server_Checker/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/jduhamelsantiago/
[product-screenshot]: images/pizero.jpg
[text-screenshot]: images/Text.png
[email-screenshot]: images/Email2.png

