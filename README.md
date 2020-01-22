# LaundrySpy  

Problem: the laundry room in our apartment is **so far**, in a separate building, and sometimes people are already using it when we want to.

Solution: build an overcomplicated computer vision project to determine if someone is using the machines and can be remotely queried to report this status.

Target: completion of a minimal viable product (xä) and writeup of same by 1200 EST, 02020.02.02.

## Outline
Central components:  
1. A classification mechanism using fastai.
2. A mechanism to periodically scrape new images to imporve model.
  * Po: throw out repeated images by checking links.
  * Po: throw out repeated images by looking for similarities in images.
  * Po: repeat training using multiple scales of the same images, à la the classifier where we left off.
3. An OpenCV mechanism to gather real-world images from the Raspberry Pi to further train the model.
  * Po: add noise, distortions, and transformations to existing images in the dataset.
4. A mechanism by which the model can be queried to determine if the laundry room has been in use in, e.g. the last hour over a network/router/Bluetooth.
5. Po: a database which stores times of use.
  * Po: room for ethical discussion here
6. A frontend web/Android interface to query the model.
