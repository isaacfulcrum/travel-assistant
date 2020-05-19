# Travel Assistant
Algorithmics final project :)

#### Contributors: 
+ [César](https://github.com/hiromi00)
+ [Isaac](https://github.com/isaacfulcrum)

#### About this project:
Our final project was to make an app that applied something we learned 
in algorithmics class, so we decided to make a travel assistant.

It implements Dijkstra's algorithm to find the shortest path from one
country to another. The graph we work on is a preset one, stored in the
JSON file called database.json, so in order for our program to work properly
database and the app must be in the same directory.

This project is made with python, and the only requirements 
for running it are having python 3 and pyside2 installed. There's
also an .exe file in the dist folder for windows users so you can 
access the whole app with only one click, just make sure database is 
in the same folder.

#### Instructions:

Once you open the app you'll be greeted by this window, just click travel.

![alt text](https://raw.githubusercontent.com/isaacfulcrum/Travel_Assistant/master/assets/instructions/welcome.png "Welcome")


Now you're on the main menu, and as the next image describes there are 
two ways of traveling:

![alt text](https://raw.githubusercontent.com/isaacfulcrum/Travel_Assistant/master/assets/instructions/menu.png "Menu")


First mode (Personalized) is pretty straight forward, you select a departure 
and an arrival country. Then you click start and the app will return the 
shortest path (the one that costs less) from both your countries.

![alt text](https://raw.githubusercontent.com/isaacfulcrum/Travel_Assistant/master/assets/instructions/personalized_1.png "Personalized")


![alt text](https://raw.githubusercontent.com/isaacfulcrum/Travel_Assistant/master/assets/instructions/personalized_2.png "Personalized")


Second mode (Adventure) is a little more complicated. First, you'll need to 
enter your name and your budget (we wanted to add the personal preference 
of each user but due to time constraints we could only use the budget).

![alt text](https://raw.githubusercontent.com/isaacfulcrum/Travel_Assistant/master/assets/instructions/adventure_1.png "Adventure")

Once you click Ready! just select your departure country and the app will 
tell how far you can get with that amount of money:

![alt text](https://raw.githubusercontent.com/isaacfulcrum/Travel_Assistant/master/assets/instructions/adventure_2.png "Adventure")

If you want to check the costs of a trip from one country to another 
you just need to click in the button Countries.

![alt text](https://raw.githubusercontent.com/isaacfulcrum/Travel_Assistant/master/assets/instructions/costs.png "Costs")


#### Version:
Travel Assistant 1.0

This is the first pyside2 project we make on our own, and we're still
learning better and more efficient ways to implement algorithms so you
can expect progress in those two areas in the future.

Thanks for reading! 
