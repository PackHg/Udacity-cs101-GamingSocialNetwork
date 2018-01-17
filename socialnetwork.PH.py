# --------------------------- #
# Intro to CS Final Project   #
# Gaming Social Network       #
# --------------------------- #
#
# For students who have subscribed to the course,
# please read the submission instructions in the Instructor Notes below.
# ----------------------------------------------------------------------------- 

# Background
# ==========
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know 
# what they are doing, having taken our web development class). However, it is 
# up to you to create a data structure that manages the game-network information 
# and to define several procedures that operate on the network. 
#
# In a website, the data is stored in a database. In our case, however, all the 
# information comes in a big string of text. Each pair of sentences in the text 
# is formatted as follows: 
# 
# <user> is connected to <user1>, ..., <userM>.<user> likes to play <game1>, ..., <gameN>.
#
# For example:
# 
# John is connected to Bryant, Debra, Walter.John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
# 
# Note that each sentence will be separated from the next by only a period. There will 
# not be whitespace or new lines between sentences.
# 
# Your friend records the information in that string based on user activity on 
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a user's profile.
#
# Consider the data structures that we have used in class - lists, dictionaries,
# and combinations of the two (e.g. lists of dictionaries). Pick one that
# will allow you to manage the data above and implement the procedures below. 
# 
# You may assume that <user> is a unique identifier for a user. For example, there
# can be at most one 'John' in the network. Furthermore, connections are not 
# symmetric - if 'Bob' is connected to 'Alice', it does not mean that 'Alice' is
# connected to 'Bob'.
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged 
# to define any additional helper procedures that can assist you in accomplishing 
# a task. You are encouraged to test your code by using print statements and the 
# Test Run button. 
# ----------------------------------------------------------------------------- 

# Example string input. Use it to test your code.
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."


## == Pack Heng (pack@oz-heng.com) ===========================================
##
## Version:
## 1.0 23/08/14 Checked with Udacity's autograder, and submitted to introcs-project@udacity.com.
## 1.1 28/08/14 Added "P.S." comment on MYOP
##
## Data Structure
## ==============
##
## My chosen data structure is a child class of dictionary, called Network. Why
## dictionary? Because it is a data structure that on one hand provides a fast
## access to its data, and on the other hand can accomodate a large quantity
## of users.
## 
## A Network object is a dictionary which key is the user's name and which
## value is an object, instance of class User, having two variable attributes:
##   
##   - connection_set: set of names the user is connected to; and
##   - game_set: set of games the user likes to play.
## 
## This will help the readibility of the code, e.g.: net['John'].connection_set and
## net['John'].game_set refer repectively to the names John is connected to and the
## games John likes to play.
## Using set prevents duplication when recording names the user is connected to, and
## and games the user likes. 
##
## Contructor and methods are defined for both class User and class Network.
## See the below sections for further details.  
##
## =============================================================================

import re       # module providing regular expression matching operations
import pprint   # pretty print

# Testing flags
testing                 = True
#verbose                 = testing and False


## =============================================================================
## Class User:
## ----------
##
## Variable attributes:
## -------------------
##  connection_set:     Set of names (string) an User object (an instance of class User)
##                      is connected to.
##  game_set:           Set of games (string) the user likes to play.
##

class User:
    ## ----------------------------------------------------------------------
    ##  Constructor User(connection_list=[], game_list=[]):
    ##      Creates an object of class User.
    ##      Default arguments:
    ##        connection_list:  list of names (string) an User object is connected
    ##                          to, is [] by default;
    ##        game_list:        list of games (string) an User object likes to play,
    ##                          is [] by default.
    ##        
    def __init__(self, connection_list=[], game_list=[]):
        self.connection_set = set(connection_list)
        self.game_set = set(game_list)
        
    ## ----------------------------------------------------------------------
    ##  update_connections(connection_list):
    ##      Updates the names an User object is connected to.
    ##      Argument:
    ##         connection_list: list of names (string).
    ##
    def update_connections(self, connection_list):
        self.connection_set = self.connection_set | set(connection_list)

    ## ----------------------------------------------------------------------
    ##  update_games(game_list):
    ##      Updates the games an User object likes to play.
    ##      Argument:
    ##         games_list: list of games (string).
    ##  
    def update_games(self, game_list):
        self.game_set  = self.game_set | set(game_list)


## =============================================================================
## Class Network(dict):
## -------------------
##  Is a child class of the class dict (dictionary).
##  An Network object (instance of class Network) is an unordered set of
##  key:value pairs with
##
##      Key: unique name (string) of an user; and
##      Value: an User object (instance of class User)
##
## Example:
## -------
##  net = Network('user_A is connected to user_B, user_C. user_A likes to play Game1, Game2.')
##  print net['user_A'].connection_set
##  >>> set(['user_B', 'user_C'])
##  print net['user_A'].game_set
##  >>> set(['Game1', 'Game2'])
##

## A helper class for exception handling in the Network constructor 
class SyntaxError(Exception):
    def __init__(self, sentence):
        self.sentence = sentence
    def display(self):
        print ("Syntax Error. " + self.sentence)


class Network(dict):
    ## -----------------------------------------------------------------------
    ## Regular expression pattern objects
    ##
    
    # For matching <sentence>.<sentence>
    expr_pattern = re.compile(r"""
        (?P<left>[^\.]+)            # Left expression
        (?P<full_stop>\.)           # Full stop mark
        (?P<right>.*)               # Right expression
        """, re.VERBOSE)

    # For matching a connection statement such as 'John is connected to Mary, Peter'
    connect_pattern = re.compile(r"""
        (?P<user>.+)                # User  
        is \s+ connected \s+ to     # "is connected to" with one or more
                                    # whitespace characters between the words
        (?P<connections>.+)         # Connections
        """, re.VERBOSE)

    # For matching a liking games statement such as 'John likes to play Game1, Game2'
    like_game_pattern = re.compile(r"""
        (?P<user>.+)                # User  
        likes \s+ to \s+ play       # "likes to play" with one or more
                                    # whitespace characters between the words
        (?P<games>.+)               # Games
        """, re.VERBOSE)

    # For a string consisting uniquely of 1 or more consecutive white space characters
    white_space = re.compile(r"""
        ^\s*$                       # a string consisting uniquely of 1
                                    # or more consecutive white space
                                    # characters
        """, re.VERBOSE)    

    ## -----------------------------------------------------------------------
    ## Variables
    ##
    game_set = set()                # includes the games the users like,
                                    # used in MYOP

    SyntaxError_enabled = False     # for SyntaxError exception handling

    ## ----------------------------------------------------------------------
    ##  Constructor Network(string_input):
    ##      Parses a block of text and stores relevant information into a Network object.
    ##
    ##      Argument: 
    ##          string_input:   block of text containing the network information,
    ##                          is '' by default.
    ##
    ##      Return:
    ##          Creates a Network object of users. Creates an empty dictionary ({})
    ##          if the argument is an emptry string ('').
    ##
    ##      How:
    ##          The constructor parses for the following grammar:
    ##
    ##          <expr> -->  <expr>.<expr>
    ##                      Create a network object by checking the left expression,
    ##                      and add to it the network created by a recursive call on
    ##                      the right expression
    ##          
    ##          Terminal cases:
    ##          <expr> -->  empty string
    ##                      Do nothing
    ##          <expr> -->  sequence of 1 or more white space characters
    ##                      Do nothing
    ##          <expr> -->  a connection statement
    ##                      Create user and his/her connections
    ##          <expr> -->  a liking games statement
    ##                      Create user and the games he/she likes
    ##            
    ##      Exception:
    ##          Exception handling in this constructor was for my learning, and
    ##          is disabled for testing with Udacity's autograder.
    ##  
    def __init__(self, string_input=''):
        try:          
            # Do nothing if empty string
            if not string_input:    
                return

            # Do nothing if sequence of 1 or more white space characters
            if Network.white_space.match(string_input):
                return
            
            # Matches a pattern of <sentence>.<sentence>
            match = Network.expr_pattern.search(string_input)
            if self.SyntaxError_enabled and not match:
                raise SyntaxError('Can\'t match this expression: "' + \
                    string_input + '"')
            
            left_expr = match.group('left')
            full_stop = match.group('full_stop')
            right_expr = match.group('right')

            # Matches a pattern of connection statement
            connect_statement = Network.connect_pattern.search(left_expr)
            
            if connect_statement:
                user = self.tidy_up(connect_statement.group('user'))
                if self.SyntaxError_enabled and not user:
                    raise SyntaxError('No user in: "' + left_expr + '."')
                
                connection_list = [self.tidy_up(connection) for connection in \
                    connect_statement.group('connections').split(',') \
                    if self.tidy_up(connection)]
                if self.SyntaxError_enabled and not connection_list:
                    return SyntaxError('No connection in: "' + left_expr + '."')

                # Adds user and his/her connections in the network
                self.add_user(user, connection_list)
                for connection in connection_list:
                    self.add_user(connection)
                    
            else:
                # Matches a pattern of liking games statement
                like_game_statement = Network.like_game_pattern.search(left_expr)
                
                if like_game_statement:
                    user = self.tidy_up(like_game_statement.group('user'))
                    if self.SyntaxError_enabled and not user:
                        raise SyntaxError('No user in: "' + left_expr + '."')
                    
                    game_list = [self.tidy_up(game) for game in \
                        like_game_statement.group('games').split(',') \
                        if self.tidy_up(game)]
                    if self.SyntaxError_enabled and not game_list:
                        raise SyntaxError('No games in: "' + left_expr + '."')
                    
                    # Adds user and the games he/she likes
                    self.add_user(user, [], game_list)
                    
                elif self.SyntaxError_enabled and full_stop:
                    raise SyntaxError('Can\'t match a statement with: "' \
                        + left_expr + '."')
                    return

            if right_expr:
                # Add the network created by a recursive call on the right expression
                self.add_network(Network(right_expr))
           
        except SyntaxError as e:
            e.display()

    ## ----------------------------------------------------------------------
    ##  tidy_up(string_input):
    ##      A helper method used in the constructor. Removes duplicates of white
    ##      space characters from string_input.
    ##
    ##      Argument:
    ##          string_input:   a string.
    ##
    ##      Return:
    ##          The same block of text as string_input but without duplicates of white
    ##          space characters.
    ## 
    def tidy_up(self, string_input):
        return re.sub(r'\s*\.\s*', '.', 
                    re.sub(r'\s*,\s*', ',', 
                        re.sub(r'\s{2:}', ' ', 
                            re.sub(r'^\s*|\s*$', '', string_input)
                              )
                          )
                      )

    ## ----------------------------------------------------------------------
    ##  add_user(user, connection_list=[], game_list=[]):
    ##      Adds an User object to the network with any connection the user has, 
    ##      and any game the user likes to play.
    ##
    ##      Arguments:
    ##          user:               a string containing the name of the user to be
    ##                              added to the network;
    ##          connection_list:    a list of strings containing names the user is
    ##                              connected to, is [] by default;
    ##          game_list:          a list strings containing the user's favorite
    ##                              games, is [] by default.
    ##      Return:
    ##          The updated network with the added user with any of her/his connections
    ##          and any of her/his favorite games.
    ##          If the user already exists in the network, her/his connection_set and
    ##          game_set are updated.
    ##
    def add_user(self, user, connection_list=[], game_list=[]):
        if user not in self:
            self[user] = User(connection_list, game_list)
        else:
            self[user].update_connections(connection_list)
            self[user].update_games(game_list)
        self.game_set = self.game_set | set(game_list)
        for connection in connection_list:
            self.add_user(connection)

    ## ----------------------------------------------------------------------
    ##  add_network(other_network):
    ##      A helper method. Adds the users of other_network and their profile into
    ##      the network.
    ##
    ##      Argument:
    ##          other_network:  a Network object.
    ##
    ##      Return:
    ##          The updated network with other_network's users and their profile.
    ##
    def add_network(self, other_network):
        for user in other_network:
            self.add_user(user, list(other_network[user].connection_set), \
                list(other_network[user].game_set))

    ## ----------------------------------------------------------------------
    ##  display():
    ##      A helper method. Prints the network's users, their connection_set and
    ##      game_set.
    ##
    def display(self):
        print '{'
        for user in self:
            print '\'%s\':' % user
            pprint.pprint(self[user].connection_set)
            pprint.pprint(self[user].game_set)
        print '}'
        
    ## ----------------------------------------------------------------------
    ##  get_connections(user):
    ##      Returns a list of connections that user has.
    ##
    ##      Argument:
    ##          user:   a string containing the name of the user.
    ##
    ##      Return:
    ##          - A list of connections (string) the user has.
    ##          - None if the user is not in the network.
    ##          - Empty list if the user has no connection.
    ##
    def get_connections(self, user):
        if user not in self:
            return None
        return list(self[user].connection_set)

    ## ----------------------------------------------------------------------
    ##  get_games_liked(user):
    ##      Returns a list of all the games the user likes to play.
    ##
    ##      Argument:
    ##          user:   a string containing the name of the user.
    ##          
    ##      Return:
    ##          - A list of games (string) the user likes to play.
    ##          - None if the user is not in the network.
    ##          - Empty list if the user has no favorite game.
    ##
    def get_games_liked(self, user):
        if user not in self:
            return None
        return list(self[user].game_set)

    ## ----------------------------------------------------------------------
    ##  add_connection(user_A, user_B):
    ##      Adds a connection from user_A to user_B. If a connection already
    ##      exists from user_A to user_B, the network is unchanged. 
    ##
    ##      Arguments:
    ##          user_A: a string with the name of the user the connection is from;
    ##          user_B: a string with the name of the user the connection is to.
    ##
    ##      Return:
    ##          If user_A or user_B is not in network, return False; else return True.
    ##
    def add_connection(self, user_A, user_B):
        if (user_A not in self) or (user_B not in self):
            return False
        if user_B not in self[user_A].connection_set:
            self[user_A].update_connections([user_B])
        return True

    ## ----------------------------------------------------------------------
    ##  get_secondary_connections(user):
    ##      Finds all the secondary connections (i.e. connections of connections) of a 
    ##      given user.
    ##
    ##      Arguments:
    ##          user:   a string containing the name of the user.
    ##
    ##      Return:
    ##          - A list containing the secondary connections (connections of connections).
    ##          - None if the user is not in the network.
    ##          - An empty list if the user has no primary connections.
    ##
    def get_secondary_connections(self, user):
        if user not in self:
            return None
        secondary_connections = set()
        for connection in self[user].connection_set:
            secondary_connections |= self[connection].connection_set
        return list(secondary_connections)

    ## ----------------------------------------------------------------------
    ##  connections_in_common(user_A, user_B):
    ##      Finds the number of people that user_A and user_B have in common.
    ##
    ##      Arguments:
    ##          user_A: a string containing the name of user_A;
    ##          user_B: a string containing the name of user_B.
    ##      Return:
    ##          - The number of connections in common (as an integer).
    ##          - False if user_A or user_B is not in network.
    ##
    def connections_in_common(self, user_A, user_B):
        if user_A not in self or user_B not in self:
            return False
        return len(self[user_A].connection_set & self[user_B].connection_set)


    ## ----------------------------------------------------------------------
    ##  find_a_path(user_A, user_B, visited_path=[]):
    ##      Finds a connections path from user_A to user_B.
    ##
    ##      Arguments:
    ##          user_A:         string holding the starting username;
    ##          user_B:         string holding the ending username;
    ##          visited_path:   a list of usernames that have been visited
    ##                          by the method in order to find a connection
    ##                          path from user_A to user_B, is [] by default.
    ##                          This argument is used to avoid connection loop.
    ##
    ##      Return:
    ##          A couple of elements:
    ##              1st element:
    ##                  - A list showing the path from user_A to user_B.
    ##                  - None if such a path does not exist.
    ##                  - None if user_A or user_B is not in network.
    ##              2nd element:
    ##                  - a list of usernames that have been visited by the
    ##                    the method.
    ##
    def find_a_path(self, user_A, user_B, visited_path=[]):
        path = [user_A]
        visited_path = visited_path + [user_A]
        
        if user_A not in self or user_B not in self:
            return None, []
        
        connections = self[user_A].connection_set
        
        if user_B in connections:
            return path + [user_B], visited_path + [user_B]
        
        for connection in connections - set(visited_path):
            another_path, visited_path = self.find_a_path(connection, user_B, visited_path)
            if another_path and user_B in another_path:
                path = path + another_path
                break

        if path == [user_A]:
            path = None

        return path, visited_path

    ## == MYOP ==============================================================    
    ##
    ## The purpose is to build these two methods:
    ##      user_popularity(user)
    ##          to calculate the popularity of an user
    ##      game_popularity(game)
    ##          to calculate the popularity of a game
    ##

    ## ----------------------------------------------------------------------
    ##  user_popularity(user, visited_path=[]):
    ##      Calculates the user's popularity.
    ##
    ##      Arguments:
    ##          user:           string holding the username;
    ##          visited_path:   a list of usernames that have been visited
    ##                          by the method, is [] by default.
    ##                          This argument is used to avoid follower loop.
    ##
    ##      Return:
    ##          A couple of elements:
    ##              1st element:
    ##                  - user's popularity, a floating point number.
    ##                  - None if user is not in network.
    ##              2nd element:
    ##                  - a list of usernames that have been visited by the
    ##                    the method.
    ##  How
    ##  ---
    ##
    ##  Let's assume the following:
    ##      If user_A is connected to user_B then user_B is a connection of
    ##      user_A and user_A is a follower of user_B.
    ##
    ##  A user's popularity = 1/nbr_of_users + sum of the popularity of each
    ##  of user's followers/nbr_of_users
    ##
    ##  More popular a user's follower is, more poplular the user is.
    ##
    ##  In order to avoid follower loop, the default argument visited_path,  
    ##  a list, is used to keep track of the usernames the method has gone  
    ##  through. If a follower is already in visited_path, we skip and 
    ##  take 1/nbr_of_users as the follower's popularity.  
    ##
    ##
    ##  P.S.: If we had more data we could analyse these to find out the areas
    ##        each user is interested in. MYOP could be enhanced to calculate
    ##        a user's popularity in an area of interest. For example: a user's
    ##        popularity in politics, computer science or football, etc.
    ##
    def user_popularity(self, user, visited_path=[]):
        if user not in self:
            return None, []
        visited_path = visited_path + [user]
        nbr_of_users = len(self)
        popularity = 0.0
        
        followers = self.get_followers(user)
        for follower in followers:
            if follower in visited_path:
                popularity = popularity + 1.0/nbr_of_users
            else:
                follower_popularity, visited_path = self.user_popularity(follower, \
                    visited_path)
                popularity = popularity + follower_popularity     
                
        popularity = (1.0 + popularity)/nbr_of_users
        return popularity, visited_path
        
    ## ----------------------------------------------------------------------
    ##  print_users_popularity():
    ##      Prints name, number of followers and popularity of all users  
    ##      in the descending order of popularity
    ##
    def print_users_popularity(self):
        display_tuple = [(user, len(self.get_followers(user)), \
            self.user_popularity(user)[0]) for user in self]
        display_tuple = sorted(display_tuple, key=lambda display:display[2], \
            reverse=True)
        
        print '%-10s\t%s\t%s' % ('USER', 'NBR_FOLLOWERS', 'POPULARITY')
        for display in display_tuple:
            print '%-10s\t%2d\t\t%2.10f' % (display[0], display[1], display[2])
        
    ## ----------------------------------------------------------------------
    ##  game_popularity(game):
    ##      Calculates the game's popularity.  
    ##
    ##      Argument:
    ##          game:   a string containing the name of the game.
    ##
    ##      Return:
    ##          - The game's popularity, a floating point number.
    ##          - None if the game isn't liked by any user in the network.
    ##
    ##  How
    ##  ---
    ##
    ##  game's popularity = sum of user's popularity for all users who like
    ##  to play this game / nbr_of_games
    ##
    ##  More popular a user who likes that game is, more popular the game is. 
    ##
    def game_popularity(self, game):
        if game not in self.game_set:
            return None
        return sum(self.user_popularity(user)[0] for user in self if \
            self.likes_game(user,game))/len(self.game_set)
    
    ## ----------------------------------------------------------------------
    ##  print_games_popularity():
    ##      Prints game, number of likes and popularity of all the games   
    ##      in the descending order of popularity.
    ##
    def print_games_popularity(self):
        display_tuple = [(game, self.nbr_likes(game), self.game_popularity(game)) \
            for game in self.game_set]
        display_tuple = sorted(display_tuple, key=lambda display:display[2], \
            reverse=True)

        print '%-35s\t%s\t%s' % ('GAME', 'NBR LIKES', 'POPULARITY')
        for display in display_tuple:
            print '%-35s\t%2d\t\t%2.10f' % (display[0], display[1], display[2])

    ## ----------------------------------------------------------------------
    ##  get_followers(user):
    ##      Lists the user's followers.
    ##
    ##      Argument:
    ##          user:   a string contaning the user's name.
    ##
    ##      Return:
    ##          - A list of user's followers.
    ##          - Empty list ([]) if the user doesn't have followers.
    ##          - None if the user isn't in the network.
    ##
    def get_followers(self, user):
        if user not in self:
            return None
        return [member for member in self if user in \
            self[member].connection_set] 

    ## ----------------------------------------------------------------------
    ##  likes_game(user, game):
    ##      Indicates if the user like this game
    ##
    ##      Arguments:
    ##          - user: a string contaning the user's name;
    ##          - game: a string contaning the game's name
    ##
    ##      Return:
    ##          - True if the user likes to play this game.
    ##          - False if the game is not in the user's favorite games.
    ##          - None if the game is not in any user's favorite games
    ##            in the network.
    ##      
    def likes_game(self, user, game):
        if game not in self.game_set:
            return None
        return game in self[user].game_set

    ## ----------------------------------------------------------------------
    ##  nbr_likes(self, game):
    ##      Calculated the number of likes the game has among the users
    ##      in the network.
    ##
    ##      Argument:
    ##          - game: a string contaning the game's name.
    ##
    ##      Return:
    ##          - The number of likes, an interger.
    ##          - None if the game is not in any user's favorite games
    ##            in the network.
    ##      
    def nbr_likes(self, game):
        if game not in self.game_set:
            return None
        return sum(self.likes_game(user, game) for user in self)
    

# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. You are free to choose and design any 
#   data structure you would like to use to manage the information.
# 
# Arguments: 
#   string_input: block of text containing the network information
#
#   You may assume that for all the test cases we will use, you will be given the 
#   connections and games liked for all users listed on the right-hand side of an
#   'is connected to' statement. For example, we will not use the string 
#   "A is connected to B.A likes to play X, Y, Z.C is connected to A.C likes to play X."
#   as a test case for create_data_structure because the string does not 
#   list B's connections or liked games.
#   
#   The procedure should be able to handle an empty string (the string '') as input, in
#   which case it should return a network with no users.
# 
# Return:
#   The newly created network data structure
def create_data_structure(string_input):
    return Network(string_input)

# ----------------------------------------------------------------------------- # 
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        # 
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- 
# get_connections(network, user): 
#   Returns a list of all the connections that user has
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.
def get_connections(network, user):
    return network.get_connections(user)

# ----------------------------------------------------------------------------- 
# get_games_liked(network, user): 
#   Returns a list of all the games a user likes
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.
def get_games_liked(network,user):
    return network.get_games_liked(user)

# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: the gamer network data structure 
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return: 
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.
def add_connection(network, user_A, user_B):
    if not network.add_connection(user_A, user_B):
        return False
    return network

# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. The new user 
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's game preferences)
def add_new_user(network, user, games):
    if user not in network:
        network.add_user(user, [], games)
    return network

# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections (i.e. connections of connections) of a 
#   given user.
# 
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.
def get_secondary_connections(network, user):
    return network.get_secondary_connections(user)

# ----------------------------------------------------------------------------- 	
# connections_in_common(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return: 
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.
#
def connections_in_common(network, user_A, user_B):
    return network.connections_in_common(user_A, user_B)

# ----------------------------------------------------------------------------- 
# path_to_friend(network, user_A, user_B): 
#   Finds a connections path from user_A to user_B. It has to be an existing 
#   path but it DOES NOT have to be the shortest path.
#   
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#
# Sample output:
#   >>> print path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.
# 
# NOTE:
#   You must solve this problem using recursion!
# 
# Hints: 
# - Be careful how you handle connection loops, for example, A is connected to B. 
#   B is connected to C. C is connected to B. Make sure your code terminates in 
#   that case.
# - If you are comfortable with default parameters, you might consider using one 
#   in this procedure to keep track of nodes already visited in your search. You 
#   may safely add default parameters since all calls used in the grading script 
#   will only include the arguments network, user_A, and user_B.
def path_to_friend(network, user_A, user_B):
    # your RECURSIVE solution here!
    # Please see the method find_a_path of class Network
    return network.find_a_path(user_A, user_B)[0]
    

# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
# Your MYOP should either perform some manipulation of your network data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.

# Replace this with your own procedure! You can also uncomment the lines below
# to see how your code behaves. Have fun!
#
# Plese see MYOP in the class Network.


## =============================================================================
##  Testing
##
testing_tidy_up                     = testing and False
testing_class_network               = testing and False

testing_create_data_structure       = testing and False
testing_get_connections             = testing and False
testing_get_games_liked             = testing and False
testing_add_connection              = testing and False
testing_add_new_user                = testing and False
testing_get_secondary_connections   = testing and False
testing_connections_in_common       = testing and False
testing_path_to_friend              = testing and False
testing_udacity                     = testing and False

testing_MYOP                        = testing and True

if testing_tidy_up:
    net = Network('A is connected to B.')
    print '"%s"' %net.tidy_up(' Pierre  ,   Marie     . Paul.  ')
    #>>> "Pierre,Marie.Paul."
    print '"%s"' %net.tidy_up('                         ')
    #>>> ""
    print '"%s"' %net.tidy_up('')
    #>>> ""

if testing_class_network:
    net = Network()
    net.display()
    #>>> {}
    net = Network('')
    net.display()
    #>>> {}   
    test_input = "A is connected to B. A likes to play Game1. \
B is connected to C. B likes to play Game2."
    net = Network(test_input)
    net.display()
    #>>> {'A':
    #>>> set(['B'])
    #>>> set(['Game1'])
    #>>> 'C':
    #>>> set([])
    #>>> set([])
    #>>> 'B':
    #>>> set(['C'])
    #>>> set(['Game2'])
    #>>> }

if testing_create_data_structure:
    net = create_data_structure("")
    net.display()
    #>>> {}
    net = create_data_structure(example_input)
    net.display()

if testing_get_connections:
    net = create_data_structure(example_input)
    print get_connections(net, "Bryant")
    #>>> ['Olive', 'Ollie', 'Freda', 'Mercedes']    # order may change
    print get_connections(net, "Louis")
    #>>> None
    net.add_user("Pierre")
    print get_connections(net, "Pierre")
    #>>> []

if testing_get_games_liked:
    net = create_data_structure(example_input)
    print get_games_liked(net, "Robin")
    #>>> ['Call of Arms', 'Dwarves and Swords']    # order may change
    print get_games_liked(net, "Louis")
    #>>> None
    net.add_user("Pierre")
    print get_games_liked(net, "Pierre")
    #>>> []

if testing_add_connection:
    net = create_data_structure(example_input)
    print add_connection(net, 'Louis', 'John')
    #>>> False
    print add_connection(net, 'John', 'Louis')
    #>>> False
    print get_connections(net, "Bryant")
    add_connection(net, "Bryant", "John")
    #>>> ['Olive', 'Mercedes', 'Ollie', 'Freda']
    print get_connections(net, "Bryant")
    #>>> ['Olive', 'Mercedes', 'John', 'Ollie', 'Freda']

if testing_add_new_user:
    net = create_data_structure(example_input)
    net.display()
    add_new_user(net, 'Pierre', ['Le Tour de France','Marco Polo'])
    print net.get_connections('Pierre')
    #>>> []
    print net.get_games_liked('Pierre')
    #>>> ['Le Tour de France', 'Marco Polo']
    print net.get_games_liked('Bryant')
    #>>> ['City Comptroller: The Fiscal Dilemma', 'Super Mushroom Man']
    add_new_user(net, 'Bryant', ['Diner Time','Coffee Break'])
    print net.get_games_liked('Bryant')
    #>>> ['City Comptroller: The Fiscal Dilemma', 'Super Mushroom Man']
    
if testing_get_secondary_connections:
    net = create_data_structure(example_input)
    add_new_user(net, 'Pierre', ['Le Tour de France','Marco Polo'])
    net.display()
    print get_secondary_connections(net, 'Pierre')
    #>>> []   
    print get_secondary_connections(net, 'John')
    #>>> ['Freda', 'Ollie', 'Olive', 'Levi', 'Jennie', 'Mercedes', 'John', 'Robin', 'Bryant', 'Walter']

if testing_connections_in_common:
    net = create_data_structure(example_input)
    net.display()
    print connections_in_common(net, 'Pierre', 'Bryant')
    #>>> False
    print connections_in_common(net, 'John', 'Louis')
    #>>> False
    print connections_in_common(net, 'Levi', 'Walter')
    #>>> 1
    print connections_in_common(net, 'Walter', 'Jennie')
    #>>> 2
    print connections_in_common(net, 'Walter', 'Bryant')
    #>>> 0
    
if testing_path_to_friend:
    net = create_data_structure("Pierre is connected to Marie.\
Charles is connected to Helene.\
Marie is connected to Louis, Jules, Pierre.\
Helene is connected to Marie, Jeanne.\
Jules is connected to Helene.\
Anne is connected to Helene, Louis, Therese.\
Louis is connected to Michelle, Therese.\
Michelle is connected to Therese.\
Therese is connected to Anne.")
    net.display()
    print path_to_friend(net, 'Pierre', 'Therese')
    #>>> ['Pierre', 'Marie', 'Louis', 'Therese']
    print path_to_friend(net, 'Pierre', 'Marie')
    #>>> ['Pierre', 'Marie']
    print path_to_friend(net, 'Pierre', 'Jules')
    #>>> ['Pierre', 'Marie', 'Jules']
    print path_to_friend(net, 'Francois', 'Therese')
    #>>> None
    print path_to_friend(net, 'Pierre', 'Charles')
    #>>> None
    print path_to_friend(net, 'Charles', 'Pierre')
    #>>> ['Charles', 'Helene', 'Marie', 'Pierre']
 
if testing_udacity:
    net = create_data_structure(example_input)
    print net
    #net.display()
    print path_to_friend(net, "John", "Ollie")
    print get_connections(net, "Debra")
    print add_new_user(net, "Debra", []) 
    print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"])
    print get_connections(net, "Mercedes")
    print get_games_liked(net, "John")
    print add_connection(net, "John", "Freda")
    print get_secondary_connections(net, "Mercedes")
    print connections_in_common(net, "Mercedes", "John")

if testing_MYOP:    
    net = Network("A is connected to C. A likes to play Game1. C is connected \
to B. C likes to play Game3. B is connected to A. B likes to play Game2.")
    net.display()
    print net.user_popularity('Redfoo')
    #>>> None
    net.print_users_popularity()
    #>>> USER      	NBR_FOLLOWERS	POPULARITY
    #>>> A         	 1		0.4938271605
    #>>> C         	 1		0.4938271605
    #>>> B         	 1		0.4938271605
    net.print_games_popularity()
    #>>> GAME                               	NBR LIKES	POPULARITY
    #>>> Game3                              	 1		0.1646090535
    #>>> Game2                              	 1		0.1646090535
    #>>> Game1                              	 1		0.1646090535
    net.add_user('D', ['B'], ['Game2','Game4'])
    net.print_users_popularity()
    #>>> USER      	NBR_FOLLOWERS	POPULARITY
    #>>> B         	 2		0.3945312500
    #>>> A         	 1		0.3476562500
    #>>> C         	 1		0.3359375000
    #>>> D         	 0		0.2500000000
    net.print_games_popularity()
    #>>> GAME                               	NBR LIKES	POPULARITY
    #>>> Game2                              	 2		0.1611328125
    #>>> Game1                              	 1		0.0869140625
    #>>> Game3                              	 1		0.0839843750
    #>>> Game4                              	 1		0.0625000000
    print net.game_popularity('Game5')
    #>>> None

    net = Network('B is connected to A. C is connected to A.\
        D is connected to C. E is connected to C. F is connected to C.\
        B is connected to X. Y is connected to X.')
    net.print_users_popularity()

    net = Network(example_input)   
    net.print_users_popularity()
    net.print_games_popularity()
