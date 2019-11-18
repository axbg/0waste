# 0waste 
#### Plastic waste detection app developed during Accenture's 2019 AI Hackathon
##### The app leverages Google Cloud AutoML Vision Platform to identify different categories of plastic waste in photos taken by drones and to measure the impact of cleanup activities
#
* Back-end
    * Python 3.7
    * Django REST
    * OpenCV
* Front-end
    * Vue.js
    * Vue Material
##### How to deploy
* install Python, preferably 3.7
* git clone https://github.com/axbg/0waste -b training-data
* unarchive training data photos
* create a [Google Cloud AutoML Vision Project](https://cloud.google.com/vision/automl/docs/quickstart) and load the training photos
* label the photos accordingly, using 5 distinct labels
    * bottle
    * cap
    * rope
    * bag
    * waste
* download the GCP Service account credentials json and add its path as *GOOGLE_APPLICATION_CREDENTIALS* environment variable
* ### Back-End
    * cd 0waste/back
    * preferably, you can create and activate a [virtual environment](https://docs.python.org/3/library/venv.html)
    * pip install -r requirements.txt
    * python manage.py migrate
    * python manage.py runserver 8081
* ### Front-end
    * cd 0waste/front 
    * install [vue-cli](https://www.npmjs.com/package/@vue/cli)
    * npm install 
    * npm run serve or vue serve
