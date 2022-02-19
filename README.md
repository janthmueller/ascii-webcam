<div id="top"></div>

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">ascii-webcam</h3>

  <p align="center">
    A simple interactive marching square simulator with pygame.
    <br />
    <a href="https://github.com/janthmueller/marching-square-simulator"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/janthmueller/ascii-webcam">View Demo</a>
    ·
    <a href="https://github.com/janthmueller/ascii-webcam/issues">Report Bug</a>
    ·
    <a href="https://github.com/janthmueller/ascii-webcam/issues">Request Feature</a>
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

Transform webcam frames to ascii art. A simple implementation with a GUI.  

![Product Name Screen Shot][product-screenshot]






### Built With

Major frameworks/libraries used to bootstrap the project. 

* [cv2](https://github.com/opencv/opencv-python)
* [PyQt5](https://doc.qt.io/)
* [pyvirtualcam](https://github.com/letmaik/pyvirtualcam)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
### Prerequisites
### Installation

<!-- USAGE EXAMPLES -->
## Usage

Use the Slider to change the size of displayed letters.  
Use the Buttons to switch between multiple display modes:  
  - single color
  - single color with brightness
  - color map (jet)
  - real color  

Use the line edit field to change the displayed letters. 
The letters used are displayed in terms of their order over the luminance on the image. 

<!-- ROADMAP -->
## Roadmap

- [ ] Refactor Code
- [ ] Fix shields in readme


See the [open issues](https://github.com/janthmueller/ascii-webcam/issues) for a full list of proposed features (and known issues).

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

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Jan Thomas Müller

Project Link: [https://github.com/janthmueller/ascii-webcam](https://github.com/janthmueller/ascii-webcam)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments


* [Embed An OpenCV Video Feed In A PyQt Window Using QThread](https://www.youtube.com/watch?v=dTDgbx-XelY&ab_channel=SamiHatna)
* [ASCII Art of Live Webcam Stream with OpenCV](https://www.learnpythonwithrune.org/ascii-art-of-live-webcam-stream-with-opencv/)



<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/janthmueller/ascii-webcam.svg?style=for-the-badge
[contributors-url]: https://github.com/janthmueller/ascii-webcam/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/janthmueller/ascii-webcam.svg?style=for-the-badge
[forks-url]: https://github.com/janthmueller/ascii-webcam/network/members
[stars-shield]: https://img.shields.io/github/stars/janthmueller/ascii-webcam.svg?style=for-the-badge
[stars-url]: https://github.com/janthmueller/ascii-webcam/stargazers/
[issues-shield]: https://img.shields.io/github/issues/janthmueller/ascii-webcam.svg?style=for-the-badge
[issues-url]: https://github.com/janthmueller/ascii-webcam/issues
[license-shield]: https://img.shields.io/github/license/janthmueller/ascii-webcam.svg?style=for-the-badge
[license-url]: https://opensource.org/licenses/MIT
[product-screenshot]: ascii-webcam.png 
