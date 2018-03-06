# Project-24POINTS-CS program
## I want to do a big online game system. There are a lot of different competitive game. People could win the money by winning the different games (kind of legal casino). :sunglasses:
STEPS
1. People could choose which games they are good at.
2. Choose how much money they want to wager
3. Connect with another online player
4. Game start.
5. Different game has different rules (I would like do 24 game)
6. They will be given the same numbers provided by the computer.
7. There will be a clock to judge who is faster.
8. Game will be absolutely equal and no one could cheat.

## First Round
In the two weeks, I would like to make a program about a small math game, called “24 Game”. The rule is that the player need to find a way to calculate four integers which would be provided by the system randomly (have to use all of them) so that the result is 24.
I will try to finish the “24 game” by using if/else statement.
### Eg.
1. The program will ask “Are you ready”. Player type “Yes” to play the game
2. The program will provide 4 random numbers and assign each of them as a,b,c,d
3. The reader will use a,b,c,d to do the math and get 24.
4. If the reader get 24, the program will type “Nice”
5. If the reader failed, the program will rerun the function until the reader get the correct answer.

## Test Plan For 1st Round
1. The program will ask “Are you ready”
2. The user types “test”
The program will give you 4 numbers “1,2,3,4”, and assign them as a.b.c.d
3. If the reader types a*b*c*d since the result is 24, the program will type “Yes”
4. If the reader types a+b+c+d, since the result is 10, the program will type “No” and rerun the function to ask you to type again.
 
## Reflections and revisions
It doesn't go well. There are two main problems in my program. :scream:
1. The Python cannot do the calculations in the input, so I need to change the imput to the string type, and let the Python to recognize every number in the input to calculate the answer.
2. If somebody just type 24 in the imput, the program will show that he passed the problem, even though he didn't use the four numbers that were given by the program randomly.

## Second Round
I need to fix this problem, and make some more math games. My next game will probably be a "picking matchsticks" game for two people. There will be three clusters of matchsticks with random matchsticks in that. The first people can pick any matchsticks they want in just one cluster. And the second people will do the same thing. The one who pick the last matchstick will win this game.
In addition, I would use the pygame to make a opening menu which lists every games I had.

## Test Plan For 2rd Round
1. The program will ask “Are you ready”
2. The user types “test”
The Program will show 3 clusters with matchsticks, and assign them as a.b.c
3. If the reader types "1", the program would choose the first cluster.
4. If the reader types "4", the program would show "Error".
5. Then, the reader could type number to move the matchsticks, like "5". The program would move 5 sticks from the a cluster.
6. If all the matchsticks were removed, the program would show "WIN".

