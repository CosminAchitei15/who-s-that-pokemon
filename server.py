import socket
import threading
import random
import struct
import sys
import time

pokemons = dict()
pokemons['bulbasaur'] = """\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&BJYPJ#&@@@@@@
@@@@@@@@@@@@@@@@@@@@&BPYJJJJYYYJ??777!JYB@@@@@@
@@@@@@@@@@@@@@@@@@#Y7!!!!77777!!!!7!!7YY@@@@@@@
@@@@@@@P?J5G#BBGBGJ?77777???!!!!777!!?YJG@@@@@@
@@@@@@P!~~~~^~~!777!!7!~!!!J?!777!!7?JYYJG@@@@@
@@@@@&?~^^^7?JYYY?!!!~!!!!!?J77???JJJJJYJ?5@@@@
@@@@B7!~~?!7JJ?7!!!~!!!!~!!7YYJJJJJJJJJJYJ?P@@@
@@@#!7J77J7!!?7!!7!!!J5Y7!7??JJYJJJJJJJJYJ??B@@
@@@?:J!7!~~7Y5?~!!!^^Y!~5????J?Y55YJJJJJJJJ?G@@
@@G^^Y7!~~!!!?!!!!! ^P7!5Y7????Y555555YJJJJJ#@@
@@G7!77~~~!!!~~~!!!:^JJJJJ??????J5555YJYJJYB@@@
@@@B5???77!7!!!77777??J??J?J???????JJ??J5B&@@@@
@@@@@&B5YYYJ????JJYYYJ???J?7!!!!7???777??B@@@@@
@@@@@@@G!7?JJJJJJJJJJJJYJ!!?7!~!7Y??JYJ??J&@@@@
@@@@@@@#7?JY??JYJJJJJJJY7????~!7J?7YY55???#@@@@
@@@@@@@@B?JY7777?B#GYJ5Y?Y7~~!!J577?JYJ??J&@@@@
@@@@@@@@@577777J#@@@#G5JJ7~!!75&&5???7???B@@@@@
@@@@@@@@@&PGPPB@@@@@@@5?!??J5#@@@@GG5P5P#@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@#@&@@@@@@@@@@@@@@@@@@@@"""

pokemons['mew']="""\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@&GY!?@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@GJ~::7#@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@&P?!!!?P#BGP5?7J@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@#57!!~~7?~:::::::~B@@@@@@@@@@@@@@@@@@@@
@@@@@@&5??YP5:::::::^^~~~^!B@@@@@@@@@@@@@@@@@@@
@@@@@GYG&@@@@7:~~^^^^~~?5~:Y@@@@@@@@@@@@@@@@@@@
@@@@PG@@@@@@&~^^Y7^^^^^~7!J#&###BBBBBBBBBBBB@@@
@@@P#@@@@@@@@B?!7!::^^~77J5Y5PG#@@@@@@@@@@@5B@@
@@BP@@@@@@@@@@&#GPJ!~!777~~7JJ7Y@@@@@@@@@#PG@@@
@@@BBB##B#BB###&#J7?5P!^^^^!P@@@@@@@@@&BPP#@@@@
@@@@@@@@@@@@@@@@&B&@@@7::^^^:~JG@@@&#BGB&@@@@@@
@@@@@@@@@@@@@@@@@@@@@&~::::^^^:^7GGB#&@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@Y^::::~^^^::7@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@J^~^:^^!!!!!7B@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@57?5P5Y5B&@B!!B@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@B!~J@@@@@@@@Y^~B@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@J^^?&@@@@@@G::~#@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@&J~~B@@@@@@&~::~&@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@&#@@@@@@@@7...J@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#J!?G@@@@@@@@"""

pokemons['charizard']= """\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@B5Y5GBB@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@&&&#G#@B7777??JG#&@@@@@@@#@@@@@@@@@@@
@@@@@@@&B5YYYYG@@@B5YJ???G#B@@@@@@@GP#@@@@@@@@@
@@@@&GPYJJJJ555&@@@@@@5775@@@@@@@@&GPPPP&@@@@@@
@@@&PJJ?JJJJ5YY5&@@@@@#7?7B@@@@@@#PPPPYJYB&@@@@
@@&PJJ5PP5JJ5YJY5GB#&@&!!7Y@@@&#GP5J5PYJJJYG@@@
@@PPG&@@@@#55Y5PGPPPYY5!!!?P5PPPGGJJPPG5JJJ5&@@
@@G#@@@@@@@&G&@#55PY?!!~!!!7?Y5YYBGYG#@#YP5PB@@
@@&&@@@@@@@@&GJ7J@@P7!^::::~?&@@Y!J5#@@G~J@GP@@
@@@@@@@@@@@@@&G&G&J!~:..::.^~Y@@GBY#&@&7~?&#G@@
@@@@@@@@@@&###&#Y7!!:...:::~~~G@@@@@@@B^.^Y@@@@
@@@@@@@@BYJ?JJJ!~!!?~^^^^^~~~!7?P@@@@@&JYG&@@@@
@@@@@@@P???JJJ7~!777~~~^^^~~!7!!~?#BBPG&@@@@@@@
@@@@@@@BY???JJ????7777?JJJJJJJ7!77YPG#@@@@@@@@@
@@@@@@@@&BGB5777?B&&&@@@@@@&&&GY??5&@@@@@@@@@@@
@@@@@@@@@@@@#GPBG@@@@@@@@@@@@@@@&&#@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""

pokemons['meowth']="""\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@&G@@@@@@B#@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@&&@@?@@@@@&J&@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@P5#@7G?!?&Y5@&#BGB@@@@@@@@@@@@@@
@@@@@@@@@@&@@@@&PYY7!^^^J~#&G55G#&BB&@@@@@@@@@@
@@@@@@@@@@#GG#@&?:..^~^~~:!!?JY&&7::^?@@@@@@@@@
@@@@@@@@@@@@&GP!::^:.^^^:::::^5&@&5!~~B@@@@@@@@
@@@@@@@@@@&##&B:::~:....:^~:::!YG5~:7&@@@@@@@@@
@@@@@@@@@@@@&##Y^^!::...:.7::^~PP^.J&@@@@@@@@@@
@@@@@@@@@@@@@@@@&PJ??7!~~!~^~7?!!YPB#@@@@@@@@@@
@@@@@@@@@@@@@@@&#GPY?7!!77~!?Y5B&@@@@@@@@@@@@@@
@@@@@@@@@@@&P?!!?5BJ:^~!~?B#&@@@@@@@@@@@@@@@@@@
@@@@@@@@&5!::?G&@@Y......!@@@@@@@@@@@@@@@@@@@@@
@@@@@@@G^ . ?@@@@&!.....:5@@@@@@@@@&&&@@@@@@@@@
@@@@@@@&GYP5B@@&P!5GYJ!^5@@@@@@@@BYJYY5&@@@@@@@
@@@@@@@@@@@@@#Y^.5@@@@?JGYPB&@@@@57Y557G@@@@@@@
@@@@@@@@@&B5J77?B@@@@?.7@&BP5Y5Y5PJJYYP@@@@@@@@
@@@@@@@@@#J??YB@@@@@#~^J@@@@@@&BBB##&@@@@@@@@@@
@@@@@@@@@@@&&@@@@@@@Y??B@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@5777B@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@G5Y5&@@@@@@@@@@@@@@@@@@@@@@@"""

pokemons['diglett'] = """\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@&&&&&&@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@#PY?77!!!77J5PB&@@@@@@@@@@@@@@@
@@@@@@@@@@@@@&P?~~~~~~~~~!!7777?Y#@@@@@@@@@@@@@
@@@@@@@@@@@@G7~~!7~~!!!!??777777775&@@@@@@@@@@@
@@@@@@@@@@@G7!!7G5!7777YB57777777?7Y&@@@@@@@@@@
@@@@@@@@@@&?777?GY77777JGY7777777??75@@@@@@@@@@
@@@@@@@@@@G7?7??7!7777???77?????????J@@@@@@@@@@
@@@@@@@@@@P7??Y7~^^^~~!?YJ???????????&@@@@@@@@@
@@@@@@@@@@P7??JJJ?????JY5J???????????&@@@@@@@@@
@@@@@@@@@@5??????JJJJJJJ?????????????&@@@@@@@@@
@@@@@@@@@@5??????????????????????????#@@@@@@@@@
@@@@@@@@@@5??????????????????????????#@@@@@@@@@
@@@@@@@@@@5????????????????????777777#@@@@@@@@@
@@@@@GJYPB5????????????????7777777777PG&&@@@@@@
@@@@57???J5?JJ???????????7777777777??5JYYYG@@@@
@@@BJ?JJJ7!!?5YJJJJJ??J???????????JJJJJJJJJB@@@
@@#?JJYY7!7?JJY?J5?~!77YJYJ?7!!!7JYJJJJJJJ?7B@@
@@&#&#BYJJ??JJYJ??J????J?JJJJJJJJYJJJJY???P&@@@
@@@@@@@&#GPB@&&#PJYYY5P55J?JYJ5555YYYP&&&&@@@@@
@@@@@@@@@@@@@@@@@@@@&@@@@&&&&&@@@@@&@@@@@@@@@@@"""

pokemons['jigglypuff'] = """\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@BG#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@P!7^^?P&@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@#!B&G?::^?B@@#BGGG#@@@@@@@@@@@@@@@@@@
@@@@@@@@@@?Y&&&#Y::^~7~::...:~Y&@@@@@@@@@@@@@@@
@@@@@@@@@&!55Y7~::~^:.:::::::::!&@@@@@@@@@@@@@@
@@@@@@@@@#~~:...:!::::::::::::::7G####&@@@@@@@@
@@@@@@@@G!::::::~^:::::::^^^^^^:::^^^^~!7?5B&@@
@@@@@@@5::^:~7?!7!:::::~!77!!^:::::^5BGGGPJ^G@@
@@@@@@B:^~.?PGP!?5^::::^!?!^::::::::!###&P7P@@@
@@@@@@?:~^^P5Y5PP7:^~!!!!!^^!!!~:::::JPY7J#@@@@
@@@@@@!:^~:!!!7?!::::^^^^.75G5~Y7::::~?YB@@@@@@
@@BJ?J7^::^^^^^^:^:::::~:^PPPP5P5::::?@@@@@@@@@
@@#J^:~~~^::::::^~~^~^:^~:JJ??YY!:::^#@@@@@@@@@
@@@@&BPY~~~^^^:::::^^^::^^^~~!!^:::^P@@@@@@@@@@
@@@@@@@@P!~~~~^^^^^^:::::::^^::^^^!G@@@@@@@@@@@
@@@@@@@@@&Y!~~~~~~~~~~~~~~~~:::7!5&@@@@@@@@@@@@
@@@@@@@&PJ77!!~~~~~~~~~~~~!7~^7B&@@@@@@@@@@@@@@
@@@@@@&!..::~?YG5Y?77777?7!!7!7G@@@@@@@@@@@@@@@
@@@@@@@BGPGB#&@@@@@@@&&@@BY!^:..J@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@&#BGB#@@@@@@@@@@@@@@"""

pokemons['pikachu'] = """\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@#PJ&@@@@@@@@@@@@@@@@@@@@@@@@@@@@#G@@@@
@@@@@@@@5~:~@@@@@@@@@@@@@&BPB@@&#&@@@@@G7:.G@@@
@@@@@@@&~::J@@@@@@@@@BP?!~:~#@&&&@@@&5!:.::!@@@
@@@@@@@@~:^!!!!7?J5Y!^:::^7#@@@@@@#Y~::^^^^^B@@
@@@@@@&Y^::::^J5?:::^!YPG#@@@@@@#Y~^^^^^^^::Y@@
@@@@@#PJ^^^^~^??!!7!~~P@@@@@@@&Y~^~~~~^^^!JP&@@
@@@@@5!^^7YYY^:^??J?~~~G@@@@@@J^~~~^^~7YB@@@@@@
@@@@@#Y~^^JYJ!^~7?7~~~~~B@@@@@&?~~!?5#@@@@@@@@@
@@@@@@@5!~~!!~~~~~~!7!~^~B@@@@@@J!P@@@@@@@@@@@@
@@&GPJ7!~^^^~~~~~~!7!!!^:~5@@&GY??5@@@@@@@@@@@@
@@G!~::::::^^^^^^^^~~~~~^::7##J75&@@@@@@@@@@@@@
@@@&#BGGPPY^^^^^^^^^^^^^^^^:~G&PYG@@@@@@@@@@@@@
@@@@@@@@@@@7:^^^^^^^^^^^^^^^^~YP#&@@@@@@@@@@@@@
@@@@@@@@@@@Y:^^^^^^^^^^^^^^^~!?B&@@@@@@@@@@@@@@
@@@@@@@@@@@B^:^^^^^~~~^^^^~!!!J@@@@@@@@@@@@@@@@
@@@@@@@@@@@@BY7!!?5GBBG5YJ?77?#@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@#J5@@@@@@@@@&Y?#@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@&&@@@@@@@@@@@#@@@@@@@@@@@@@@@@@"""

pokemons['squirtle'] = """\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@B5J?777?JPB@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@G?^^^~~~!~~~!?G@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@#7~!!!!!!5775777Y&@@@@@@@@@@@@@@@@@@
@@@@@@@@@@&P7~!!!!~J&&GY7??7P@@@@@@@@@@@@@@@@@@
@@@@@@@@@@Y!~!!!!~~7JJ77????Y@@@@@@@@@@@@@@@@@@
@@@@@@@@@@577??????777?JJ???B@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@BY???????????????&@@@@@@@@@@@@@@@@@@
@@@@@@@@@@&#GYJ???????JJJY?JYG@@@@@@@@@@@@@@@@@
@@@@@@&GY?!!7!~~!7777??!!7?JYJ5&@@@@@@@@@@@@@@@
@@@#5Y7~~~~7~^^^~!!!77~~~~7?JYJ5@@@@@@@@@@@@@@@
@@@B???!!~?~::::~7^~?!7!!!7??JJ7G@@@@@@@@@@@@@@
@@@&##BBB#5~:::^~~^77??77???~J?!5@@@@@@@@@@@@@@
@@@@@@@@@@5~!~~~!~~!!7???7?!~YJ?G@@@&&###@@@@@@
@@@@@@@@@@G7^^~~7~~~~~7777?7~YYY&@BJ7!!!7JP@@@@
@@@@@@@@@Y~7~^^:!^^^~!7?7!!!!YYB&5777?????75@@@
@@@@@@@@5:^~7?!!77!!!77!~!~~~7PP????J??????Y@@@
@@@@@@@@J~!!7??JJ?777J7~~~!~~!Y7????J?????J#@@@
@@@@@@@B?77???Y&@@&&&#B7!!!!!755YJJ??JYYPG&@@@@
@@@@@@@#GP5GB#&@@@@@@@@B7????7P@@@&&&&&@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@&PG5JPGP@@@@@@@@@@@@@@@@"""

pokemons['charmander']=  """\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@#5J?77?YG@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@B?^^~~~~~~!J#@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@#!~~!!~!!!!!YJ#@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@G!!!!!~!!!?75GY@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@B5!~!!~~!~7GGP?#@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@#??!!!~~~~~~7??7G@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@#?777!!!777?JJJ?#@@@@@@@@@@@@@@G5&@@@@@@
@@@@@@@@&G5YYJJ?77?Y??#@@@@@@@@@@@@@BYY?#@@@@@@
@@@@@@@@@@@&GY???????JPG#&@@@@@@@@@@?!?7J#@@@@@
@@@@@@&&BPJ?!77!~~7?7!~~!7J5GGG&@@@B?7?7:Y@@@@@
@@@@@G7!~~~~!?:....:!!!!!~~~!7?P@@#~^~!^~J&@@@@
@@@@@@GY555P5:....:..~77?5PPB#&@@@@#?^:~?G@@@@@
@@@@@@@@@@@@P ...:::..!!!?#@@@@@@@@@@B?P#@@@@@@
@@@@@@@@@@@@Y ....:::.:7~~!P@@@@@@@@@P7@@@@@@@@
@@@@@@@@@@BJ7:....::^^^!~~~~Y@@@@@&BY7G@@@@@@@@
@@@@@@@@@Y^^~7~^^^^^^^7^^~~~~YP55YJ?JG@@@@@@@@@
@@@@@@@@#~!77??7!~^^^:!!!!!!7?Y??JJP&@@@@@@@@@@
@@@@@@@@&Y??777YGBBBGPPGJ7????5GB#@@@@@@@@@@@@@
@@@@@@@P77?Y5PG&@@@@@@@@@577?7YB@@@@@@@@@@@@@@@
@@@@@@@&##&@@@@@@@@@@@@@@@BPJ5YP@@@@@@@@@@@@@@@"""

pokemons['eevee'] = """\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@&5#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@BG5B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@GGG5P@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@BPGG5P@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@&PBGB5#@@&@@#@@@@@@@@@@&&##B#GP#@@@@@@@@@
@@@@@@@&G#&BPGY7JY!PG#@@@#BGGPPPPPPP#@@@@@@@@@@
@@@@@@@@&BB5?7!!!!!!775#GB&&BGGP5P#@@@&P@@@@@@@
@@@@@@@@@@B7???7777??77JB&#BBGGB&@@&BY~:G@@@@@@
@@@@@@@@@@5YGG???77?JJ?7P##&##BGPY?!~~^^Y@@@@@@
@@@@@@@@@@JY&P777?7G##?J&@@B5JJJJJJJJ7^:5@@@@@@
@@@@@@@#?7??J????77PBP?5#@GJJJJJJJJJJ7!!#@@@@@@
@@@@@@#^.:^7???????????!~?55YJJJJJJJJYYG@@@@@@@
@@@@@@P:.:::^^!777777!~~~~J555YYYYYY55G@@@@@@@@
@@@@@@@P~^:.:..:::^!~!~~~?JJY5555555G#@@@@@@@@@
@@@@@@@@&B!^^:::..^!!7!!?J?JJBBBB##&@@@@@@@@@@@
@@@@@@@@@@&Y7!~~^~!?JYJYJ?JJJ#@@@@@@@@@@@@@@@@@
@@@@@@@@@@@&YJ??JJJJJ55BB?7?J&@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@B??JJ???5PG&&?77P@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@G77?777YGB@&Y??5@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@#GGGJJY&@@@@&##@@@@@@@@@@@@@@@@@@@@
"""


choice = random.choice(list(pokemons.keys()))

print('pokemon to guess: ' + choice)
mylock = threading.Lock()
client_guessed=False
winner_thread=0
e = threading.Event()
e.clear()
threads = []
client_count=0




def worker(cs):
    global mylock, client_guessed, winner_thread, client_count,e, choice, pokemons

    my_idcount=client_count
    print('client #',client_count,'from: ',cs.getpeername(), cs )
    message='Hello client #'+str(client_count)+ pokemons[choice]
    cs.sendall(bytes(message,'ascii'))
    while not client_guessed:

        cpokemon=cs.recv(1024).decode()
        print('Client number' + str(client_count)+ ' attempted: ' + cpokemon)
        if cpokemon == choice:
            mylock.acquire()
            client_guessed=True
            winner_thread=threading.get_ident()
            mylock.release()
        else:
            cs.sendall(bytes("NO", 'ascii'))

    if client_guessed:
        if threading.get_ident() == winner_thread:
            cs.sendall(bytes("winner", 'ascii'))
            print('We have a winner', cs.getpeername())
            print("Thread ",my_idcount," winner")
            e.set()
        else:
            cs.sendall(bytes("loser", 'ascii'))
            print("Thread ",my_idcount," looser")
    time.sleep(1)
    cs.close()
    print("Worker Thread ",my_idcount, " end")
def resetSrv():
    global mylock, client_guessed, winner_thread, choice, threads,e, client_count
    while True:
        e.wait()
        for t in threads:
            t.join()
        print("all threads are finished now")
        e.clear()
        mylock.acquire()
        threads = []
        client_guessed = False
        winner_thread=-1
        client_count = 0
        choice = random.choice(list(pokemons.keys()))
        print('Selected pokemon: ', choice)
        mylock.release()


if __name__=='__main__':
    try:
        rs=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        rs.bind( ('0.0.0.0',1111) )
        rs.listen(5)
    except socket.error as msg:
        print(msg.strerror)
        exit(-1)
    t=threading.Thread(target=resetSrv, daemon=True)
    t.start()
    while True:
        client_socket,addrc = rs.accept()
        t = threading.Thread(target=worker, args=(client_socket,) )
        threads.append(t)
        client_count+=1
        t.start()
