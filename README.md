# Gaming Social Network
This was the final project for the Udacity's Intro to Computer Science course (cs101). It was an opportunity to not only put in practice what I had learned so far, but also to learn more and have fun.

For the MYOP (Make Your Own Procedure), what I was trying to do was to calculate the popularity of a user.

I assumed the following: if User_A is connected to User_B, then User_B is a connection of User_A and User_A is a follower of User_B.

Initially, I took a user's popularity as follows:

    user's popularity = (1 + number of user's followers) / number of users

But that was pedestrian for a MYOP. Later, I thought that more popular a follower of a user is, more popular the user should be. Then I changed the formula to:

    user's popularity = (1 + sum of follower's popularity for all the followers of the user) / number of users;

and it's calculated recursively. On the other hand, I had to ensure that my code avoids a follower loop.

Based on this, I took a game's popularity as follows:

    game's popularity = sum of user's popularity for all the users who like this game / number of games

If we had more data we could analyse these to find out the areas each user is interested in. MYOP could be enhanced to calculate a user's popularity in an area of interest. For example, a user's popularity in politics, computer science or football, etc.

# Background
"You and your friend have decided to start a company that hosts a gaming social network site. Your friend will handle the website creation (they know what they are doing, having taken our web development class). However, it is up to you to create a data structure that manages the game-network information and to define several procedures that operate on the network.

In a website, the data is stored in a database. In our case, however, all the information comes in a big string of text. Each pair of sentences in the text is formatted as follows:

<user> is connected to <user1>, ..., <userM>.<user> likes to play <game1>, ..., <gameN>.

For example:

John is connected to Bryant, Debra, Walter.John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.

Note that each sentence will be separated from the next by only a period. There will not be whitespace or new lines between sentences.

Your friend records the information in that string based on user activity on the website and gives it to you to manage. You can think of every pair of sentences as defining a user's profile.

Consider the data structures that we have used in class - lists, dictionaries, and combinations of the two (e.g. lists of dictionaries). Pick one that will allow you to manage the data above and implement the procedures below.

You may assume that <user> is a unique identifier for a user. For example, there can be at most one 'John' in the network. Furthermore, connections are not symmetric - if 'Bob' is connected to 'Alice', it does not mean that 'Alice' is connected to 'Bob'."

# Project Description
"Your task is to complete the procedures according to their specifications as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged to define any additional helper procedures that can assist you in accomplishing a task. You are encouraged to test your code by using print statements and the Test Run button."

# Keywords
Python, Programming, Social Network, Udacity, cs101.

This project and its files are for educational purpose only.

## License
Copyright (C) 2014 Pack Heng

Licensed under the Apache License, Version 2.0 (the "License");
you may not use these files except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
