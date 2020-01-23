# 02020.01.22  
## Goals for the Day  
1. Use the existing Horseless MPS code as a reference.
2. Evaluate the necessity of making the existing MPS multiclass.
3. Gather a larger initial dataset of images and retrain the model.
4. Po: migrate code from Jupyter notebooks.
5. Search for options for automating web scraping for new images.
  * Look for resources on best practices for avoiding data leakage, drift, etc. when retraining in this manner.
6. Evaluate status of the Raspberry Pi.
  * Check OpenCV, fastai, TF installations.

## Links  
* [Scraping images with Python and Scrapy](https://www.pyimagesearch.com/2015/10/12/scraping-images-with-python-and-scrapy/)
  * [Scrapy](https://scrapy.org/)
  * [Django](https://www.djangoproject.com/)
    * This comes up because of the MVC model, not because it is actually used in the tutorial.
  * This tutorial is where the `timecoverspider` project is discussed.
  * Finally started using `tree` here.
  * Apprehension: unsure of how this will interface with, e.g. Google Images
  * Getting the impression that the specifics of the article, especially the interface with Time Magazine's search functionality, is too old and will require modification.
* [Scrapy Vs Selenium Vs Beautiful Soup for Web Scraping.](https://medium.com/@srimanikantapalakollu/scrapy-vs-selenium-vs-beautiful-soup-for-web-scraping-24008b6c87b8)
  * Looking here for a broader perspective on which direction to go in.
* [Image Scraping with Python](https://towardsdatascience.com/image-scraping-with-python-a96feda8af2d)
  * [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
  * Mentions that BeautifulSoup is useful for scraping static content. While potentially useful later, this is not what we need at the moment.
  * The XML and HTML parser `lxml` is mentioned.
  * Selenium is mentioned, but we don't want this project to be involved with something resembling an entire browser unless it is necessary.
  * Opted to go through tutorial, downloading [Chrome](https://itsfoss.com/install-chrome-ubuntu/#install-chrome-terminal).
  * Ran into a problem pip installing webdriver; used chromedriver and need to figure out how to use it.
  * Found webdriver in the selenium module. Now wondering how much of this tutorial needs to be changed to make it work locally.
  * Point of confusion: the code format switches when moving from the bs4 section to the selenium/webdriver section, then back again.
  * Problem (resolved): download and installation of Chrome for webdriver needed an additional packaged that I overlooked.
  * Problem (resolved): the placement of `chromedriver` into the same directory as the code itself. Can also be appended to PATH.
  * Can Selenium be run headless?
  * Tutorial completed; skeleton operational
