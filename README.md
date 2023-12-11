# Who's that pokemon
A python implementation of the childhood game 
"Who's that pokemon" using socket programming
(TCP) and threading.

## 1.Setup
This is a python game meant to play between
computers using the same network. Whoever runs
the server has to modify line 297 with their ip
and a random port. The server is meant to be run
on something that has bridged addapter, so WSL
won't work for this purpose. Whoever wants to
play has to modify line 4 of client.py with the
server's ip and port.

## 2. How does it work?
The server generates one out of 10 stored
pokemon and outputs its ascii shape to each user.
More than one person can play simultaneously
thanks to threading. Each player then tries to
guess the name of the pokemon that is shown to
them, and whoever guesses first wins! After a
round is over, the server generates a new pokemon
and each player has to run client.py again to 
commence.

## 3. Final thoughts
This project was made during my "Computer 
Networks" class in my 3rd semester of college,
and I can say it was a great way to get introduced
to socket programming.