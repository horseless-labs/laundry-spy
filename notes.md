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

# 02020.01.23  
## Goals for the day  
1. Survey Horseless MPS code.
2. Determine whether multiclassing is necessary.
3. Read documentation and determine next steps for:  
  * scrapy
  * BeautifulSoup4
  * PIL
  * io, requests, and hashlib modules
4. Determine web scraping skeleton operability on Salamander.
5. Look at the use cases of Docker and determine if it would be appropriate here.

## Links  
* [Headless browser testing using Selenium Webdriver](https://medium.com/@nauman.sheikh/headless-browser-testing-using-selenium-webdriver-fcddf62eb3d5)
  * cron jobs mentioned; must remember to get back to these
  * Chrome 59 and Firefox 56 wer the first respectively to be able to run this way.
  * This article is for Java versions of Selenium.
* [How to make firefox headless programmatically in Selenium with python?](https://stackoverflow.com/questions/46753393/how-to-make-firefox-headless-programmatically-in-selenium-with-python)
  * This is for Firefox, but a quick test indicates it works for Chrome, too.
  * Running the full notebook to see if it works all the way through.
* A quick look at [this GitHub repo](https://github.com/JianhaoZhang/g_img_scraper/blob/master/core.py) seems to suggest just using retries.
* [Selenium working with Chrome, but not headless Chrome](https://stackoverflow.com/questions/45370018/selenium-working-with-chrome-but-not-headless-chrome)
  * Had to pip install pyvirtualdisplay. Testing now.
  * Additionally had to sudo install xvfb. Testing now.
* Useful stuff for later:  
  * [Pro tips for Selenium](https://medium.com/@igorzabukovec/pro-tips-for-selenium-6cca1c47b02c)
  * [Running Selenium with Headless Chrome](https://intoli.com/blog/running-selenium-with-headless-chrome/)
  * [Speeding up Selenium](https://helpfulsheep.com/2017-05-24-speeding-up-selenium/)

## Notes  
* Preliminary test indicates that it will not be easy to run webdriver on Salamander.  Next step: go over the code and determine how it can be made to run headless.
* Ran into what might be timeout issues on 01.22, which seem to be made worse when trying to run this headless.
* Headless mode seems to have a problem using `wd.find_elements_by_css_selector`, or possibly with `img.irc_mi`. No links can be extracted this way with the code as it is written.
* Status: walking through code line by line to see where headless Selenium fails.
  * It is getting page source.
  * Will `wd.execute_script("...")` say if it fails?
  * The above is of nothing. Using `wd.execute_script("...")` to go to the bottom of the Google Images search, wait for a moment for the loading to complete, and check the length of the page source reveals that that part is working. The webdriver fails at `wd.find_elements_by_css_selector()`.
    * Hypothesis: Selenium recovers a version of the page that does not include the `img.rg_ic` element, so it is behaving correctly. Testing.
    * Using above test, managed to get results from `img.rg_ic`. Still have not managed to get results from `wd.find_elements_by_css_selector('img.irc_mi')`.
    * I hadn't paid attention to this before, but sometimes there is some kind of failure to load images in the headed version, as well. These return 80 thumbnail results.
* Hypothesis: Google changes its Images CSS when it encounteres headless Selenium instances. Pivoting

# 02020.01.24  
##  Goals for the Day
1. Survey existing Horseless MPS code and determine if multiclassing is necessary.
2. Look at readiness for uploading the writeup for the MPS existence experiment. It will at least be something.
3. Consider a writeup that goes through the Scraper Skeleton code. **On further inspection, we think this could be a really good writeup**.
  * Simple explication of the skeleton itself.
  * Locations where it can be improved, especially possible conversion into a class. Considering where this is meant to be plugged into LaundrySpy and the variety of platforms that it could theoretically be running on (xäxä!), it will be important for the system to know when it won't be able to use headless mode for something.
  * Exactly where the problem fell apart (use of headless) and hypothesis for why (Google interference).
  * Hypothesizing about other places where the use of this technology might be a problem.

## Notes
I am willing to bet right off that, yes, using code from the Minimal People Sensor or any future iterations thereof will require the use of multiclassing for this project in particular. We last left off with an experiment where the model would determine whether there was a human in the frame. Being that this is meant to be a showy elaboration of these capabities, there are a number of directions to consider:  
* Our models need to be trained with more data.
* Classification can be broken into a location being empty, populated by one or two people, a handful, or a crowd.
  * Without knowing the outcome of this experiment, we are not confident as to the feasibility of higher granularities of people counting.
* We can use OpenCV to scan through subsections of the image.
  * Is this considered image segmentation? We need to look into this.
  * We know that PyImageSearch had something like this, but the old notes are a bit scattered.
* OpenCV can be used to artificially add noise and distortions to images
  * Use this to determine if generalization can be improved in this way.

## Links  
* [Fastai's resnet.py](https://github.com/pytorch/vision/blob/master/torchvision/models/resnet.py)
* [“A CASE OF MULTI-LABEL IMAGE CLASSIFICATION”](https://towardsdatascience.com/fast-ai-season-1-episode-3-a-case-of-multi-label-classification-a4a90672a889)
* [Lesson 3: Data blocks; Multi-label classification; Segmentation](https://course.fast.ai/videos/?lesson=3)
  * We can't believe this fell by the wayside.

# 02020.01.25
## Links  
* [Finding Data Block Nirvana (a journey through the fastai data block API)](https://blog.usejournal.com/finding-data-block-nirvana-a-journey-through-the-fastai-data-block-api-c38210537fe4)

# 02020.01.27
## Goals for the Day  
1. Lit review: constellation of links associated with the FastAI Lesson 3 video.
2. Code review of same.
3. Outline and begin experiments for people sensing
  * We suspect this will be chiefly gathering datasets from the internet.
  * Importantly, we would like the main thrust of the experiments to be done by end of operations 01.28; we want to have a goodly margin of time to work with the Pi and however the frontend ends up working out.

## Links  
* [Finding Data Block Nirvana (a journey through the fastai data block API)](https://blog.usejournal.com/finding-data-block-nirvana-a-journey-through-the-fastai-data-block-api-c38210537fe4)
  * [Custom ItemList](https://docs.fast.ai/tutorial.itemlist.html)
  * [GitHub - medium-finding-data-block-nirvana](https://github.com/ohmeow/dl-experiments/tree/master/medium-finding-data-block-nirvana)
* [Multi-label prediction with Planet Amazon dataset](https://nbviewer.jupyter.org/github/fastai/course-v3/blob/master/nbs/dl1/lesson3-planet.ipynb)

## Notes  
Thinking about the data collection procedure. We can use the Selenium scraper to get a workable dataset. Thoughts:  
* The main problem is "existence," that is, the presence of a human in the frame.
  * Initial thought was to collect 1000 images of each of the following:
    * Indoor images with humans
    * Indoor images without humans
    * Outdoor images with humans
    * Outdoor images without humans
  * Thinking about these, we started considering the following:  
    * As mentioned in the articulation of goals, we want to experiment with the introduction of artifacts into the images to test generalization capacity.
    * Having a small handful of categories for densities of humans.
    * Additionally, natural variations in environment, lighting conditions, and subjects themselves may need to be considered, though this might be overdoing it for this preliminary stage of the project.
    * Currently considering using the initial four types of variability for this stage of the project.
    * Alternately, considering using images that exclusively have either *zero or one humans* in the frame. 
