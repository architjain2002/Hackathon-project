# Welcome to our VirtualDoctor Application!

Lets make things virtual!

Things which were once just a vision are turning into reality using **Machine Learning and Artificial Intelligence**.

We team **Sigma Coders** have brought to you a very first personalized doctor whose house resides inside your phone.

This doctor will be your very personal health diagnostics specialist who will take care of you **anytime and every time 24/7**

# What can my VirtualDoctor do?
Well our Virtual Doctor can diagnose you by taking our patients input of symptoms and then our doctor will basically give his diagnosis and give you instructions such as precautions and steps to taken to cure the disease which is predicted by our doctor. It can also provide you the location of doctors nearby to you to cure the problem your facing.

# How my VirtualDoctor work?
VirtualDoctor basically works through a machine learning model at behind the scenes which is being trained on a dataset which comprises the symptoms and the disease(being predicted).

**Note: Currently the VirtualDoctor application is an idea and the application is a prototype. It is far from a full fledged Business product.**

**Due to limited amount of dataset, resources and members, the prototype serves as a decent application to illustrate our vision.**  

# How is VirtualDoctor different from other  related applications?
The application available right now in market give your instructions related to the disease you search for but our application diagnose the disease your have!

**A doctor's Job is to diagnose the disease by the problems your undergoing but other applications available right now give you detail about a disease but it doesn't predict whether your suffering by it or not!**

# How successful can VirtualDoctor can turn out to be?
The application what we are working right now is a basic prototype does not have enough features but this application can turn out to be a huge change in the current way of getting diagnosed.

If we can get enough resources and dataset regarding diseases their symptoms, medicines and other tests to be taken then we could train our model onto these huge data and make our model very accurate with large number of features(like one could send image data of a body part he is suffering from and the application could predict according to that) and we could fetch many API's and make our application a all in one product. Further more we could also make our user interface more elegant and easy to use.

The biggest advantage of our virtual doctor application would be the availability is 24/7 unlike actual doctors where you need to get yourself an appointment and then undergo the time taking process. Moreover our VirtualDoctor consults our patients without asking for payments i.e. It is free of cost! What else is needed!

# One could ask why trust a machine in case of health?
Well things are getting automated and in the upcoming generation everything is getting automated by artificial intelligence.
Things like automated cars and aero-planes and the public flights are also automated using machine learning models.

**Right now our human mindset has never experienced being consulted or diagnosed by virtual doctors but when we realize how realistic and accurate diagnostics the machine can give we will sooner or later be adjusted and the life of automation will begin. There will be time when machines will surpass humans in health too and this application could be the first step towards it!!**

***Fun fact: The covid-19 vaccines were tested by huge neural network model which were used in full capacity to produce vaccine.***
## Technologies used
**Front-end:** Android studio, Kotlin,Retrofit.

**Back-end:** Nodejs,Expressjs,Ejs

**Database:** Mongodb

**Machine-Learning Model:** Tensorflow,Keras,Scikit-Learn

## Alright lets begin the Installation
#### Step1:
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the **requirements.txt** to install the Machine Learning libraries used.

```bash
pip install -r /root/backend
```

#### Step2:

Use the package manager [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) to install the libraries under **package.json** first by going to the root/backend directory
```bash
npm install
```
#### Step3:
If you are using Android studio to run our app you can run it on the emulator and you are good to go and can use our prototype but if you do not want to run it on android studio you can follow from step4.

#### Step4:

Now you need to first open our app.js in the backend and change the hostname from 127.0.0.1 to the ip address of your internet service provider.
```javascript
const hostname = "x.x.x.x"  // Enter your ip address of your internet service provider here
```
#### Step5:
And there you go now you have your personal doctor ready!!

![screenshot](https://github.com/architjain2002/Hackathon-project/tree/master/Visuals/Screenshot_2021-10-21-03-14-41-853_com.example.hackathonapp.jpg?raw=true)
## Issues we ran into
- While integrating our machine learning model with the backend and later the front end integration to display the contents were being timed out.
- While fetching API's.
- Couldn't fetch google maps api because of google's billing issue.
## Authors and acknowledgment
I would like to thank @eddy1006 for his contribution in this wonderful project and ideas.

I would also thank bit by bit hackathon team to provide us with a great opportunity to display our ideas and vision.
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
