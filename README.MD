<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![JQuery][JQuery.com]][JQuery-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://user-images.githubusercontent.com/79105382/188027338-fbf0be1e-5259-4936-bbf0-fdffcb467a7d.png" alt="Logo" width='350' hieght='350'>
  </a>

  <h3 align="center">SuperCardSet</h3>

  <p align="center">
    An Amazing Collection of 10K Randomized Visa and Master Card Images with Random Names and Card Types.
    <br />
    <a href="https://github.com/OttomanZ/SuperCardSet"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/OttomanZ/SuperCardSet/Visa">View Demo</a>
    ·
    <a href="https://github.com/OttomanZ/SuperCardSet/issues">Report Bug</a>
    ·
    <a href="https://github.com/OttomanZ/SuperCardSet/discussions">Request Feature</a>
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
![supercardset](https://user-images.githubusercontent.com/79105382/188027809-e108d0b2-9576-47c2-8dde-21d964d0a114.PNG)

There are many usecases for a dataset with Credit Card Images, from multiple payment handlers like Visa or Mastercard, therefore I decided to go ahead and create this dataset from scratch. 
Here's why:
* Train Object Classification Models in Various Scenarios where you need to know the type of Card.
* Create Algorithms to Extract Key Information from the Card.
* Cards are Randomized in Platinum, Gold and Standard Catagories for Diversity :smile:

There has been a severe lack of a good ready to use dataset in terms of debit/credit cards, so therefore, you can see below the various snapshots of the extracted results.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Getting Started :car:

To get started all you need to go ahead and do is clone the existing github repository, the folders are marked as <kbd>Visa</kbd> and <kbd>MasterCard</kbd> respectively for ease where you will find 5004 images precisely for each of the Catagory.

```bash
git clone https://github.com/OttomanZ/SuperCardSet.git
```

### Custom Generation :thumbsup:

To go ahead and start generating your own dataset you need to first install the dependencies of the program, to do that you need to have `python3` and `pip3` installed in your enviorment of choice.

```python
pip install -r requirements.txt
```
After this the Project Requirements should be installed and we are ready to rock. :guitar:

* ### Command Line Generation

To go ahead and generate the dataset via. the command line you need to go ahead and follow the following syntax, to get help run:

```sh
ubuntu@ip-172-31-56-240:~/SuperCardSet$ python generate_data.py -h
usage: generate_data.py [-h] [-a AMMOUNT]

Generates a Dataset of Visa & MasterCard Images with Randomized Names and Card Types.

options:
  -h, --help            show this help message and exit
  -a AMMOUNT, --ammount AMMOUNT
                        ammount of images to generate
```
* Running the Command-Line Interface :wink:

```bash
python generate_data.py -a 100
```

### Downloading Results

<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://user-images.githubusercontent.com/79105382/188029506-e30fe530-e9c2-4cd5-b6bd-b966c34b1efa.png" >
  </a>
</div>




<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Code Integration :book:

This is an example of how you may use the integrated Python Module `GenerateDataset` in *generate_data.py*

### Prerequisites

To get started ensure that <kbd>generate_data.py</kbd> <kbd>**is in the same directory as your python script**.</kbd> :smile:

### Adding in Application

* #### Custom Generating Dataset
```python
from generate_data import GenerateDataset

# to automatically generate a dataset of 10 (50/50 Distribution) images from the API.
# stores the images in Visa & MasterCard folders.
generator = GenerateDataset()
generator.generate_dataset(ammount=10)
```
* ### Customized Card Generation

```python
from generate_data import GenerateDataset
import cv2

# Possible Values 'Visa' or 'MasterCard'
# Possible Values, 'A Name'.
# Result: An Numpy Image Object.
generator = GenerateDataset()
img = generator.generate_img('Visa','John Doe')
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```


### Sample Data

<div>
  <a href="https://github.com/OttomanZ/SuperCardSet">
    <img src="https://user-images.githubusercontent.com/79105382/188030613-3ceabd81-3c4c-42ae-8fb1-7f6499f92bac.png" alt="Logo" width='350' hieght='350'>
    <img src="https://github.com/OttomanZ/SuperCardSet/blob/master/MasterCard/01fc7f8b-112d-4846-b745-23c19128fe2b.png?raw=true" alt="Logo" width="350" hieght="350">
  </a>
<div>



<p align="right">(<a href="#readme-top">back to top</a>)</p>



# Classification Model Results


Here you can go ahead and see the performance of MobileNet Model trained using `tensorflow.keras` over 50 epochs on the following dataset distribution.
* ### Train Distribution
```sh
[+] Train Generator
Found 9524 images belonging to 2 classes.
[+] Validation Generator
Found 482 images belonging to 2 classes.
```
<ol>
  <li> ![download](https://user-images.githubusercontent.com/79105382/188279558-59a5fa3c-8622-4be0-9925-e7012fdb03af.png) </li>

  <li> ![lowest](https://user-images.githubusercontent.com/79105382/188279844-65d6e54c-8508-42f0-ba76-c263d46cd272.png) </li>
<li> ![download](https://user-images.githubusercontent.com/79105382/188280018-421e9ed4-d4b6-478c-be01-cfec2a57786d.png) </li>

 </ol>


  

<!-- ROADMAP -->
## Roadmap

- [x] Generating 10K Dataset
- [x] Customized Cards
- [x] Customized Names
- [x] Command Line Interface
- [x] Python API
    - [x] Adding Custom Names
    - [x] Adding Card Types
    - [ ] Adding Card Edition
    - [ ] Custom Card Number Generator

See the [open issues](https://github.com/OttomanZ/SuperCardSet/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Muneeb Ahmad - [@MuneebAhmad](mailto:muneeb@muneeb.co) - muneeb@muneeb.co

Project Link: [https://github.com/OttomanZ/SuperCardSet](https://github.com/OttomanZ/SuperCardSet)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

I found this API on a rather wierd old looking website, so I decided to go ahead and create a wrapper around it and create this much needed dataset. Kudos to it's Original Maintainers, and I hope that people do not overdo it, resulting in their website being slowed down. I would suggest highly ratelimiting each request. Be nice and Kind!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/Python-0769AD?style=for-the-badge&logo=python&logoColor=white
[JQuery-url]: https://jquery.com 
