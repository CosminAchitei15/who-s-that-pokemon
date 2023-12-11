import socket, threading, struct, random,sys, time

if __name__ == '__main__':
    s = socket.create_connection( ('172.30.117.15',1111))

    finished=False

    data=s.recv(1024)
    print(data.decode('ascii'))
    step_count=0
    while not finished:
        my_pokemon = input("Your guess: ")
        s.send(my_pokemon.encode())
        answer=s.recv(1024)
        print(answer.decode('ascii'))

        step_count+=1
        print('Sent ',my_pokemon,' Answer ',answer.decode('ascii'))

        if answer== "NO".encode():
            print('Wrong guess! Try again ')
        if answer== "loser".encode() or answer== "winner".encode():
            finished=True
        time.sleep(0.25)

    s.close()
    if answer=="winner".encode():
        print("I am the winner with",my_pokemon,"in", step_count,"steps")
    else:
        print("I lost !!!")
