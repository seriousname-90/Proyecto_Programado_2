import random 
"""Import del random para muchas funciones del proyecto"""

def mensajes(num,agente):
    """Funcion que se usa para alamcenar prints mensajes y algunas listas (la mayoria pero no todos por comodidad de escritura)"""

    if num == 0:
        print('Amistad'.center(80,'-'))
        """Titulo del texto"""

    if num == 1:
        print(f"""
            __________________________________________________
           |                                                  |
           |    _________________________________________     |
           |   |                                         |    |
           |   |  Hola {agente} te habla D, tenemos una  |    |
           |   |  mision muy importante para ti, estaba  |    |
           |   |  mos hablando con el doctor vegapunk y  |    |
           |   |  dice que se aproxima una gran amenaza  |    |
           |   |  ambiental, por ello te vamos a mandar  |    |
           |   |  a un futuro distopico en el cual la    |    |
           |   |  sociedad prospero mas conocido como    |    |
           |   |  "Solarpunk". Todo el equipo dice que   |    |
           |   |  eres el mas apto solo neesitas almace  |    |
           |   |  nar informacion basica de la gente.    |    |
           |   |                                         |    |
           |   |  ¿Que dices, aceptas?                   |    |
           |   |_________________________________________|    |
           |                                                  |
           |__________________________________________________|
                   \\___________________________________/
                ___________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_
:-------------------------------------------------------------------------:
`---._.-------------------------------------------------------------._.---""")

    if num == 2:
        print("""        
            | Agente D: INCROYABLE! Veo que has aceptado, así que esto esta es tu misión: 
            | Necesitamos de tu ayuda para recolectar informacion de una sociedad distopica
            | llamada solarpunk. Para esto cuentas con un portal que te deberías de tener atras tuyo, ESPERA!!, 
            | Para activarlo deberás indicarme cuantas zonas puedes cubrir hoy
            |
            |                             ███▓▒░░ IMPORTANTE ░░▒▓███ 
                ╔═══════════════════════════════════════════════════════════════════════════════╗ 
                ║ Utiliza SOLAMENTE numeros enteros positivos para indicar la cantidad de zonas ║ 
                ╚═══════════════════════════════════════════════════════════════════════════════╝ 
            """)
        print()

    if num == 2.5:
        print("""        
            | Agente D: Ahora!, tenemos un limite de capacidad con los habitantes que podrás interactuar. 
            | Por ser la primera vez te dejaremos escojer la cantidad que creas conveniente y nosotros nos encargamos
            | del rendimiento, no te preocupes, ahora solo dinos, 
            | ¿Cuál va ser esa cantidad?
            |
            |                                ███▓▒░░ IMPORTANTE ░░▒▓███  
                ╔════════════════════════════════════════════════════════════════════════════════════╗ 
                ║ Utiliza SOLAMENTE numeros enteros positivos para indicar la cantidad de habitantes ║ 
                ╚════════════════════════════════════════════════════════════════════════════════════╝ 
            """)
        print()

    if num == 3:
        print("""_____________________________________________________________")

*ERROR*: Has ingresado algo que no es un numero o un entero por favor
ingresa un numero valido
_____________________________________________________________""")
        print()
    
    elif num == 5:
         print (f"""
    | Agente D: Ya está listo!, la cantidad de zonas que elegiste ya se encuentran generadas, bien hecho!.
    | Espera...WOPS!, hubo un fallo en el sistema y los habitantes se han repartido entre todas las zonas.
    | La única manera de saber donde quedaron es buscándolos zona por zona.  
    | Ahora se muestran los nombres de las zonas, empezemos, ¿Cuál zona quieres visitar de primero?
    |  
    | 
    |                              ███▓▒░░ IMPORTANTE ░░▒▓███  
        ╔══════════════════════════════════════════════════════════════════════════════════╗ 
        ║ Escribe el NOMBRE de la zona que deseas visitar TAL CUAL se muestra en la lista  ║ 
        ╚══════════════════════════════════════════════════════════════════════════════════╝ 
            """)

    elif num == 6:
        print (f"""
    | Agente D: Ahora escucha, como parte de tu misión tienes varias opciones:
    | 1. Puedes interactuar con cualquiera de ellos digitando su nombre tal y como se muestra  
    | 2. Puedes digitar "Irse" para volver al menú de listas

""")
    
    elif num == 7:
        print(f"""_____________________________________________________________")

*ERROR*: Agente no has ingresado un texto el cual este dentro de la lista de
zonas correspondiente por favor selecciona alguno de los elementos dados
_____________________________________________________________""")
    
    elif num == 8:
        print()
        print (f"""
    | Agente D: Vaya!, hemos llegado muy rápido, bienvenido a *redoble de tambores*: """)
        print()
    
    elif num == 9:
        print (f"""
Agente D: Bien, ahora tu mision es hablar con las personas de estas lista , tienes que hacerles preguntas 
basicas de si.""")
    
    elif num == 10:
        print (f"""________________________________________________________________________")

*ERROR*: Agente no has ingresado un texto el cual este dentro de la lista de
habitantes correspondiente por favor selecciona alguno de los elementos dados
________________________________________________________________________""")
        
    elif num== 11:
        print(f"""
            __________________________________________________
           |                                                  |
           |    _________________________________________     |
           |   |                                         |    |
           |   |  Oh vaya! Pensabamos que si aceptarias  |    |
           |   |  ,de todos modos hay muchos que         |    |
           |   |  quisieran tomar este papel, no te      |    |
           |   |  preocupes agente {agente} lo tenemos   |    |
           |   |  cubierto                               |    |
           |   |                                         |    |
           |   |   firma:                                |    |
           |   |   Agente D                              |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |_________________________________________|    |
           |                                                  |
           |__________________________________________________|
                   \\___________________________________/
                ___________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_
:-------------------------------------------------------------------------:
`---..-------------------------------------------------------------..---
""")

    elif num == 11.5:
        print (f"""________________________________________________________________________")

*ERROR*: Responde digitando "S" para aceptar o "N" para rechazar porfavor
________________________________________________________________________""")

    if num == 12:
        agente=input("Cual es tu seudonimo: ")
    
    elif num == 13:
        print("""Agente D: Oh vaya! Parece que somos los unicos aqui, hecha un vistazo y despues vuelve tenemos 
otras zonas las cuales visitar""")

    elif num == 14:
        print("""Agente D: Quieres hacerle otra pregunta? (ten en cuenta que si dices "no" te regresara a la seleccion de personas)""")


    elif num == 15:
        print("""
▀█▀ █▀▀   █▀▀ █▀ ▀█▀ ▄▀█ █▄░█   █░░ █░░ ▄▀█ █▀▄▀█ ▄▀█ █▄░█ █▀▄ █▀█ ░ ░ ░
░█░ ██▄   ██▄ ▄█ ░█░ █▀█ █░▀█   █▄▄ █▄▄ █▀█ █░▀░█ █▀█ █░▀█ █▄▀ █▄█ ▄ ▄ ▄""")
        print()
        print("""
           ,-.
           | |
           | |
  ,-"""""""-.|
 |  __:::__()L
J ."_______". L
JJ,"       ".LL
|J|         |L|
|||         |||
L||         ||J
LJ|Wny      |LJ
LJ._________,LJ
L ___     ___ J
| \\__)---(__/ |
J----(===)----L
 L\\ "-___-" /J
 | "-------" |
 |           |
 |           |
 |           |
 |           |
 |           |
 |           |
 |           |
 |    ...    |
 "-----------"
 """.center(80))
        
    elif num == 16:
        print()
        print (f"""________________________________________________________________________

*ERROR*: Agente No has ingresado una respuesta valida por favor ingresa 
algo coherente conforme a lo que te pedimos.
________________________________________________________________________""")
    
    elif num == 17:
        print()
        print("""
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                     .                                              
                                          ........:::::.....                                        
                                     .....::----==++===--:.:........                                
                                  ...:-----====++++++=++===--=---:.....                             
                                ..::--===-=====---------===++====-::...                             
                             ..::--========-------------------=======-:..                           
                            .::--======-=----------------:-----=++====--:...                        
                           .:-:=====+=---------------------------=+++==----..                       
                          .:-:.:-=++=------------------------------++++===-:.                       
                         .:===:=+++=-------------------------------=++++=--:..                      
                        ..-=+==++===-::-----------------------------==+==---..                      
                       .:-===++=+===------------------------=-------=======-:..                     
                      .:-===++++======------------------===-------=====+===-:..                     
                     ..-===+++++========-=---------------==-------::=======-:.                      
                     .::==+++++==============-------------=----------========:..                    
                     ..-=++++++================------------------------=+====-:..                   
                      .-=+++++================-----------====--=-------=++=+=--:..                  
                      .-=+:+++=========---------------------------------++=++--:..                  
                     .:-=+-*++====-==-----------------------------------+*+++=::..                  
                   ..:-===+++=====--------------------------------------=+++==-:..                  
                  ..:-=++*+++=====--------------------------------------=+++==-:...                 
                 ..:-=-==++++====----------------------------------------=+=-----:..                
                 ..:---==+*++====-=-------------------------------------=======:-:..                
                  .--===+++++========--------------------------------:--=======--:...  ..           
                  .:--==+++++========-----------------------------------=======::...                
                   .:==+=++++===========----------------------------======+++=--.                   
                   .:==+++++=======------------------------------------====++==-:..                 
                 ..:-==++==++=====-----------------:---------------------===++=-....                
                 ..:-=++**++======--------------------------------------==++++=-:...                
                ..:-=+++***+====----------------------------------------=++*++=-:...                
                ..:-++++*+++==-------------------------------------------+++++=-....                
                ..:-+*+****+=-------------------------------------------=+*=++++-...                
                 .:-+******+=---------::-::::::::::::::------::::::::---=*+++*+=-..                 
                 .:-+++****+=---------:-:--:::::::::::::::::::::::::::--=*+*++==:..                 
                  .:==++***+=-----::::::-::::::::::::::::::::::::::::---=+++++=::..                 
                   .-++***+==-------::-----------::::::::::::::::::::---++++==-:...                 
                   .:=++*-:=+=-:.--------------------------:::::::::----+++++=-:....                
                   ..-=+*+*=+==--------------------------------::::----=+*++=-:.....                
                   ..:=++++**+===-------------------------------------=++-++=-:...                  
                   ..:-=++*+**+====-===--========-=-=-=--------:-----=+***+=--::..                  
                 . ..:-++++++**++============================--:---===***+=---:...                  
                    ..-=+++*+***++===================================+***+=---:....                 
                    ..:==++*****+=====+=++=========++=============+++****===-::.....                
                     .:--==*+=+=+===-=++++++++++++++++++++++++++++++*****+=-::......                
                     ..:---=*+-=+++===+++++++++++++++++++++++++++++****++-:::......                 
                       ..:-+**+=====-=+-++++++++++++++++++++++++++***++=-:.......                   
                        ..:-++*+====++++++++++++++++++++++++++++****++=-::.......                   
                          ..:-=+**+*****++++=:=+++++++++--+++++****++::::....                       
                            ...--=+******++++++++++++++++++++***++==-:....                          
                              ....:-=++******+++++++++++++****+=-...                                
                                  ....:-=++*******+++******++=:...=.                                
                              :==+-   .. .=+++**#######*+==..   .+===:                              
                            :+====:  .++*####%%%%%%%%%#**##**+:  .=====.                            
                           -++=*:. .++*###*+==---------=+**####+-   -++.                            
                           =++=    =+*%%%%%*==---------=+#%%%%#*=-  .++:                            
                           ***.   -*++*%%%%%%+=========*%%%%%%+===.  .::                            
                          .=:.   .++++++**#%%%#*******#%#**+======:                                 
                                 .++++++++++++++++================-                                 
                               :#%#+*+++++++++++++===============*%#*.                              
                             .-%%%%%#*+++++++++++++++========+****%%%-                              
                           +%%%#*%@@@%%%%%##***++++++++++*##**#%%#%#%%#:.                           
                      :#%%#%##%%%#%%%%%@@@%%%%%%%%%%#####%%%%%%%*%%*#%%%%%%%=.                      
                  .:*@@%%#*#%%%%%%%####%@@@%%%%%%%%######@@%%##%%#%%%%#**#%%@%==***++********+:     
    .#@@@@%%%%%%%%%#=***+*##=.+*###%%@%#*%@@%%%%%%%%####%#*#%%%%##*#%***#****#%%%%%%%%%%%%%%%%%-    
    =%%%%%%%%%%#*++++=+#*+.:***#%%%%%#*##***####%%%%%#**+##**%%###*#*#- .-+##*+++++*%%%%%%%#*+.     
     ................    .**#%%%%%%@%####%#****+++++++**#%*#*#%%%%%%#**=                            
                        =**%%@%%%%%##*###@@@@%%%%%%%%%%%%%**#*#%@%%%%%#*+                           
                      :*#%%@@@@@@%%**##*:...::--------:...:**#*#%%@@@%*=**.                         
                    .+*%%%#%@@@@%#**#**-                   :*+#**%#######**-                        
                  .=**%%@%%#+**#+*##*+.                     .-**#*###%%####**+=.                    
               .=**%%%%%%%%#==**##*=.                         .-**#*##%%%#####***+:                 
            :*#%%%%%%%%%%%%#*#***-.                              =*****#%%%%########=.              
         .+@@%%%%%%%%%%%#*##**+.                                   :=++****#%%%%%#####:             
         +%%%%%%%%%%%%###*+=.                                         .:-==+########%*.       

""")
        
    elif num == 18:
        print()
        print(f"""Agente D: usa el portal para irnos a donde escogiste {agente}""")
        print()

    elif num == 19:
        print()
        print("""*No pasa absolutamente nada*""")

    elif num == 20:
        print()
        print("""agente D: Oh que es eso?!?!?!?
*Aparece epicamente un capibara salvaje*""")
    
    elif num == 21:
        print()
        print("""
                                                                                                                                          
    ##**************########*********#####***********************####******************####****#############**************#####*****=--    
    ++++++++**+++++++++#####*************************************####******************####****#############**************#####******=-    
    ==+**+=+***+=+*++=+******************************************####******************####****############******************##******=-    
    ==***+=+##*==+**+=+*********++++++++*+***********************####******************####****###########*********++++******##******=-    
    ==================+***++***+++++++++++****+******+++++++++++*####**+++++++***+++++*###################***++***++++++++***##***+++=-    
    +**++===+++++*#####***********************+******+++++++++++*##*#*++++++++******++*********###########*************************++=-    
    ***++===+++++########********************++******+++++++++++******++++++++******++++++++++*###########*************************++=-    
    ========+++++#########***************************+++++++++++******++++++++******++++++++++*#############***********************++=-    
    ========*****############**************++*************************++++++++*******************############***********++*********++=-    
    ========*****###########**************+++********######****************+++*******************############***********++*********++=-    
    ========*****###########*+++++******+++++*****#%%%%%%%%**********#%%%%%*++***+++**+++++++++*****########*+++++++++++++*********++=-    
    **+++***+++**###########*+++++******++++++*#%%*+++++++*%%#++**#%%#*+***%%%**********************########*++++++**********+++++***=-    
    **+++***+++**###########*+++++******++++++*#%%*********####*######**#########+++*+*+*+++***+****#########******+**+*****++++++***=-    
    **+++********###########*+++++******+++++++*%%#********++*%%%%%*+*#####***%%%+++++**++*****++***##############*+++*+++**++++++***=-    
    ++######***#############*+++++******+++++++*%%#**********#%%*++###########%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%###***********###++***=-    
    ++#########################+++*************#%%#*************++++++++++*+*+*********************************#%%################***=-    
    ++#########################+++*************#%%************+++++++++++++++++++++++++++++++++++++++++++++++++#%%#################**=-    
    ++#########*****###################*+++++**#%%************+++++++++++++++++++++++++++++++++++++++++++++++++++*%%%##############**=-    
    ++#########*****+++################*+++****#%%*************************************************************+++++*%%%###########**=-    
    ++#########*****+++################*+++*****##**************************************************************++++*%%#**#########**=-    
    ++*########*****+++#%%%%###########*+++****+=+#%%*+************%%%%%%%%%%%%%%*******+++************+**###########%%+--########***=-    
    --*#######*-------=#%%%%+--########+-----+*+--*%%######++******%%%%%%%%%%%%%%*********+*******+**********####***#%%*++########***=-    
    ++########*=======+#%%%%+==########*=====+++==#%%######++******##############****************************####*++*%%*++########*++=-    
    %%#########*++*+++*#%%%%***########*++++++++++#%%######+*++****************************************++****####*++*%%*++########*++--    
    **#########++++****#%%%%***#########%%%%#***+*#%%######+*******************************************++*+*******++*%%#**########**+=-    
    **########*++++++++*****+++#########**#%#*****#%%**************************************************+++++******++*%%#**########*++=-    
    +*#########+++++++++++++++*########***#%#*****#%%**************************************************++++*******++*%%#**########*++=-    
    ++#########*+****+****%%%%%########***#%#***+*#%%***++++*************************************######**+++*##*++++*%%#**########***=-    
    ++########*+++++******%%***########*++###++++*#%%***+**+*************************************###***++**+*##**+++*%%***########***=-    
    ++*********+++****+++*##*++########*++*##+++**#%%********************************************###*****+++******++*%%#**########***=-    
    +*+++++++++******++++*##*++########*++*##++*%%%%%########**+**************************+******######*+++++++****+#%%%%%########***=-    
    +++******++++++++++++++++*++++++++++++#%%%%#+++++****************************##*******+****#####***##*+********+#%%#**########***=-    
    ****++++++++++*++++++++++**+++++*#####******+++++######*****************++****************######**************###%%*++########***=-    
    ++***+++++++***+++++++**+*++++***%%%%%*+++++++++*######***##********************###################***##******%%%%%*++########***=-    
    ++*++**+++*++***+********+**+*%%#++++++++*++++*+*######***********########***######################********%%#++*##*++########***=-    
    +++++++++++++++++++++**+***#%#**++++++++*++++**+*******########******##******#####%%%%%%%%%%%%%%%%%%%%%%%%%#**++*##*++########*++--    
    ***************************#%#++++++++***+**++*********########*****###******#####%%%%%%%%%%%%%%%%%%%%%%%%%**+++*##*++*#######*++--    
    ************************#%%++++*+++*********+*******+**##*++*#####################%%%********************+******++++**++++++++++*=-    
    *********************#%%*+++++++**+*+*****+++*************######################**#%%************+********++++++++++++++++++++***=-    
    *******************#####*++++*****+++***********************####################*+#%%***************++++++++++++++***++++++++++++=-    
    *******************%%#+++*++**##*+**+****#####***************###################++#%%***************+++++++++***********+++++++++--    
    **+++***********%%#+++*+++++*********************************################**#%%#*****************++***************************=-    
    *************###***++*****+*********++************+************##############**#%%#*****************++***************************=-    
    *************#%%*++******+**********+*************+*###********##############**#%%#*****************++***************************=-    
    **********#%%*+++*+******##*********##*************************###########******%%##***#*#**********++***************************=-    
    *###**#***#%%*++*#**+******************************************###########++*%%%####****##*******+*******************************=-    
    ********###%%*++*#*********************************************###########***%%%##************************#**********************=-    
    ********%%#++**************++*****************************##******#####******%%%*###****##****************#**********************=-    
    **++++++%%#++*******+***************#######***************##******##*******+*%%#**************************#***#******#****#******=-    
    **+++++*%%#++***********************#######***************##******##*********%##**************************#***************#******=-    
    ********%%#++***********************#######************##******######***++%%%*****##***************+++****#***********#***#****++=-    
    ********%%#++*************************########***###***********######***++%%%***#**#*********#*****++++++++++++++****************=-    
    ********%%#++**************************########**###********#########***++%%%*****#***********#**************************++++++++=-    
    ********%%#++***************+++**********##############################**+%%%*****#**************************************++++++++=-    
    ********%%#++***#####*******++++*********##############################*++%%%****************************************************=-    
    ++++++++%%#++****************+*+*##******###########################***#%%+++*****++++++***********+++++++++++++******++++++*****=-    
    ++++++++%%#++********************##******###########################**+%%%++++***+++++++***********++++++++++++++*****++++++*****=-    
    ********%%#++*#####********######*****##############################*++%%%+++***********+++++++++++***++++++++*****+++--------=++=-    
    **********#%%###########************##############################**#%%**************###++++++++******++++++++##*+=------++=--+**=-    
    ***********%%###########************##############################*+#%%**************###++++++++***##*+++++++*#+=----------=--+**=-    
    **+++++++++**#%%##################################################++#%%*++++++++++*#####++++++++**#####****###+===+#==+*------+##=-    
    **++++++++****##%%%###############################################%%*+++++++++++++**#*########*****+++++++++++===-==**------=+*##=-    
    **+++++++++****#####################################################*+++++++++++++*****************++++++++===----=-+**------=+##=-    
    **+++++++++****#*****####**######****###############**####****####**++++++++++++++***+++++++++++***++++++++=------=*--++------+**=-    
    ##***********+++++++++********************************************##*****************+++++++++++***********=--------------==--=**=-    
    *****########********************+++++++******###**************########******########***********######*****=--------------==--+##=-    
    ***##########********************++++++++***#####**************######################***********##########*=-------+**=-------+##=-    
    """)
    if num == 548:
        print ("""

░░░░░░░░░░░░░░░░░░  ░█████╗░███╗░░░███╗██╗░██████╗████████╗░█████╗░██████╗░  ░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░  ██╔══██╗████╗░████║██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗  ░░░░░░░░░░░░░░░░░░
█████╗█████╗█████╗  ███████║██╔████╔██║██║╚█████╗░░░░██║░░░███████║██║░░██║  █████╗█████╗█████╗
╚════╝╚════╝╚════╝  ██╔══██║██║╚██╔╝██║██║░╚═══██╗░░░██║░░░██╔══██║██║░░██║  ╚════╝╚════╝╚════╝
░░░░░░░░░░░░░░░░░░  ██║░░██║██║░╚═╝░██║██║██████╔╝░░░██║░░░██║░░██║██████╔╝  ░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░  ╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░  ░░░░░░░░░░░░░░░░░░
""")
    """de aqui para rriba son print usados para varias partes de la simulacion"""


def listas(num,zona,nombre):
    """Funcion que almacena la mayoria de las listas de el proyecto"""

    if num == 1:
        ran = random.randint(0,12)
        color = ["rojo", "azul", "amarillo", "verde", "anaranjado", "negro", "morado", "rosado", "gris", "blanco", "truquesa", "cafe", "salmon"]
        return color[ran]
    
    elif num == 2:
        como_estas = ["bastante bien", "no muy bien la verdad, pero"]
        ran = random.randint(0,1)
        return como_estas[ran]
    
    elif num == 3:
        ran = random.randint(0,12)
        musica = ["el pop", "el rock", "el reguetton", "el alternativ0", "el RB", "las rancheras", "la bachata", "el merengue", "el reggue", "el trap", "el rap", "el LO-FI", "la plancha", "la cumbia metalera"]
        return musica[ran]
    
    elif num == 4:
        ran = random.randint(0,5)
        vacas = ["Soy mas de playa", "La playa me gusta bastante mas", "Me gustan los dos sinceramente", "La montaña es mil veces mejor", "Me gusta mas la montaña la verdad", "No me gusta ninguno de los dos la verdad"]
        return vacas[ran]
    
    elif num == 5:
        ran = random.randint(0,9)
        materias = ["fisica", "quimica", "biologia", "matematicas", "español", "estudios sociales", "civica", "ingles","mate discreta", "Cafetales II", "Intro de Programación con Aurelio"]
        return materias[ran]
     
    elif num == 6:
        ran = random.randint(0,6)
        generos = ["el terror", "la accion", "el suspenso", "el drama", "el thriller", "animado", "la comedia"]
        return generos[ran]
    
    elif num == 7:
        ran = random.randint(0,6)
        frutas = ["la manzana", "la pera", "el limon", "el banano", "la naranja", "la sandia", "el kiwi"]
        return frutas[ran]

    elif num == 8:
        preguntas = ["como estas?","que hora es?","que edad tienes?","en donde estamos?"\
                    ,"como te llamas?","cual es tu color favorito?","cual es tu fecha de nacimiento?"\
                    ,"donde naciste?","quien es tu cantante favorito?","que tipo de musica escuchas?",\
                    "quien es tu programador favorito?","te gustan los capibaras?",\
                    "si tubieras un capibara que nombre le pondrias?","Eres mas de playa o montaña?",\
                    "cual es tu materia favortia de colegio?","cual es tu genero de peliculas favorito?",\
                    "te gustan los croissants?","ya no se que preguntarte","dime algo filosofico",\
                    "dame un consejo de via", "cual es tu fruta favorita?"]
        return preguntas
    
    elif num == 9:
        respuestas = [f"{listas(2,zona,nombre)}, gracias por preguntar!", f"Mmm creo que son las {random.randint(1,24)}:{random.randint(00,59)}"\
                    ,f"Yo? tengo {random.randint(10,100)} años", f"estamos en {zona}", f"Mi nombre es {nombre}", f"Mi color favorito es el {listas(1,zona,nombre)}"\
                    ,f"Es el {random.randint(1,30)}/{random.randint(1,12)}/{random.randint(1500,2010)}", f"Yo naci en {zona}", "kanye west forever"\
                    ,f"escucho mas que todo {listas(3,zona,nombre)}", "Aurelio por siempre, SUPREMACY", "La mejor especie del mundo, simbolo planetario!!!!", "Terreneitor goku alfredo tercero", f"{listas(4,zona,nombre)}"\
                    , f"Oh! yo creo que {listas(5,zona,nombre)}", f"Sin ninguna duda {listas(6,zona,nombre)}", "OBVIOOOOOOOOOOO, QUASOOOOOO", "Ni yo se que responderte", "Viva la anarquia"\
                    ,"mas vale el diablo por viejo que por diablo", f"MMM, yo creo que {listas(7,zona,nombre)}"]
        return respuestas

        """todos son if y elifs usados en la funcion y definidos aqui"""

def impre_zonas(zonas,largo,ind):
    """funcion que imprime las zonas de forma ordenada"""
    if ind == largo:
        return
        """si el ind es igual al largo que solo haga return a donde quedo en la funcion la cual usaba esta"""

    else:
        print(f"""_____________________________________________________""".center(80))
        print(f"""|{ind+1}.{zonas[ind]}|""".center(80,"-"))

        return impre_zonas(zonas,largo,ind+1)
        """si no es igual el ind y el largo que haga print de forma ordenada de la posicion ind de la lista zonas y le sumes uno al ind para que pase con el siguiente"""

def impre_personas(habitantes,largo,ind):
    """funcion que imprime los habitantes de la zona seleccionada de forma ordenada (no usan la misma por el print "salir" """

    if habitantes == []:
        mensajes(13,agente)
        print(f"""_____________________________________________________""".center(80))
        print(f"""|0.Irse|""".center(80,"-"))
        print(f"""_____________________________________________________""".center(80))
        print(f"""|-1.Esperar|""".center(80,"-"))
        return
        """si la lista de los habitantes es vacia que imprima un mensaje de que estas solo en la zona """
    
    elif ind == largo:
        print(f"""_____________________________________________________""".center(80))
        print(f"""|0.Irse|""".center(80,"-"))
        print(f"""_____________________________________________________""".center(80))
        print(f"""|-1.Esperar|""".center(80,"-"))
        mensajes(9,agente)
        return
        """cuando el largo es igual al ind que haga return a la funcion la cual esta usando esta y imprima
        un extra que es constante para devolverse a las zonas de la simulacion"""

    else:
        print(f"""_____________________________________________________""".center(80))
        print(f"""|{ind+1}.{habitantes[ind]}|""".center(80,"-"))
        return impre_personas(habitantes,largo,ind+1)
        """cuando el ind no es igual al largo que imprima la posicion ind de los habitantes y le sume uno para la siguiente vuelta"""

mensajes(548,"Agende D")
agente=input("Cual es tu seudonimo: ")
"""Pregunta del seudonimo para el inicio (si no lo defino afuera definirlo adentro es aburrido)"""

def mensajes_presentacion(interactivo,zona):
    """funcion que elige un mensaje inicial de el habitante al cual le hablas"""

    ran = random.randint(0,38)
    """random que elige cual mensaje usar"""

    if ran == 0:
        print()
        print (f"{interactivo}: Hola, soy {interactivo}, ¡siempre da gusto ver nuevas personas paseando por aquí!, (ojalá se largue pronto...)")
        print()
    if ran == 1:
        print()
        print (f"{interactivo}: ¡Saludos aventurero! {interactivo} para servirle, servido y servirá...¿sirve?")
        print()
    if ran == 2:
        print()
        print (f"{interactivo}: ¡Hey hola! ¿Caluroso, verdad? Sí, el clima en {zona} está TERRIBLEEE.")
        print()

    if ran == 3:
        print()
        print (f"{interactivo}: Doscientos... trescientos... ¡EPA!, no te había visto, ¿andas perdido o algo?")

    if ran == 4:
        print()
        print (f"{interactivo}: ¿Te gustaría unirte a mi club secreto de unicornios invisibles?")
        print()

    if ran == 5:
        print()
        print (f"{interactivo}: ¡Hola! ¿Quieres ayudarme a encontrar mis gafas de sol? Se me cayeron en algún lugar por aquí.")
        print()

    if ran == 6:
        print()
        print (f"{interactivo}: ¡Oye tú! ¡Cuidado con mis flores! Son muy delicadas.")
        print()

    if ran == 7:
        print()
        print (f"{interactivo}: ¿Buscas algo en especial o solo andas curioseando?")
        print()
    
    if ran == 8:
        print()
        print (f"{interactivo}: ¡Ah! Otro visitante más... bueno, bienvenido supongo.")
        print()

    if ran == 9:
        print()
        print (f"{interactivo}: ¡Hola! ¿Te has dado cuenta de cuántos pájaros hay por aquí? Es increíble.")

    if ran == 10:
        print()
        print (f"{interactivo}: La perdí en algún lugar cerca del lago...")
        print()

    if ran == 11:
        print()
        print (f"{interactivo}: ¡Hola! Si buscas aventuras, ¡este es el lugar perfecto!, creo...")
        print()
    if ran == 12:
        print()
        print (f"{interactivo}: ¡Oh! No esperaba visitas hoy. ¿Quién eres?")
        print()

    if ran == 13:
        print()
        print (f"{interactivo}: ¡Saludos, extraño! ¿Qué te trae por aquí?")
        print()
    
    if ran == 13:
        print()
        print (f"{interactivo}: Hola, soy {interactivo}. Me encanta esta parte de la zona verde, ¿verdad que es genial?")
        print()

    if ran == 14:
        print()
        print (f"{interactivo}: ¡Hola! ¡Ten cuidado por donde pisas, hay hormigueros por todas partes!")

    if ran == 15:
        print()
        print (f"{interactivo}: ¡Hey! ¿Has visto una capibara? La he estado buscando todo el día.")
        print()

    if ran == 16:
        print()
        print (f"{interactivo}: ¡Hola! No hay nada como un buen paseo por la naturaleza, ¿no crees?")
        print()

    if ran == 17:
        print()
        print (f"{interactivo}: ¿Qué haces por aquí? No es muy común ver caras nuevas.")
        print()

    if ran == 18:
        print()
        print (f"{interactivo}: ¡Hey! ¿Te gustaría unirte a nuestro club de observadores de estrellas marinas?")
        print()
    
    if ran == 19:
        print()
        print (f"{interactivo}: ¡Saludos! Estoy buscando setas especiales. ¿Me ayudarías a encontrarlas?")
        print()

    if ran == 20:
        print()
        print (f"{interactivo}: ¡Hola!, ¿También nuevo por aquí?, sí, sí, ando buscando la historia origen de esta zona")

    if ran == 21:
        print()
        print (f"{interactivo}: ¡Ah! Una cara nueva. ¡Qué emoción! Bienvenido/a.")
        print()

    if ran == 22:
        print()
        print (f"{interactivo}: ¡Hey! ¿Necesitas ayuda para encontrar algo?, si es así dígale a alguien más")
        print()

    if ran == 23:
        print()
        print (f"{interactivo}: ¡Hola! Soy {interactivo}. Cuidado con los charcos, ¡resbalan mucho!")
        print()

    if ran == 24:
        print()
        print (f"{interactivo}: ¡Saludos! , Ahora no tengo tiempo. Necesito recolectar flores raras.")
        print()
    
    if ran == 25:
        print()
        print (f"{interactivo}: ¡Hola! ¡Qué bueno verte! ¿Necesitas alguna orientación?")
        print()

    if ran == 26:
        print()
        print (f"{interactivo}: ¡Hey! ¡Qué bueno ver a alguien nuevo por aquí! ¿Quieres unirte a una caza del tesoro?")

    if ran == 27:
        print()
        print (f"{interactivo}: Y POR ESO ESPERAAAAAAAABA CON LA CAARITA EMPAPAAAADA")
        print()

    if ran == 28:
        print()
        print (f"{interactivo}: ¡Hey! ¿Sabes algo sobre la leyenda de este lugar? Es fascinante.")
        print()

    if ran == 29:
        print()
        print (f"{interactivo}: ¡Hola! ¿Buscando animales? Este lugar está lleno de ellos, ahora mismo estoy viendo a uno fijamente...")
        print()

    if ran == 30:
        print()
        print (f"{interactivo}: ¡Hey! No todos los días veo una cara nueva por aquí. ¿Qué te trae por estos montes?")
        print()
    
    if ran == 31:
        print()
        print (f"{interactivo}: ¡Hola! Ten cuidado, hay muchos usuarios de Windows en esta parte de la zona verde.")
        print()

    if ran == 32:
        print()
        print (f"{interactivo}: ¿Te gustaría unirte a nuestra patrulla canina de conservación del medio ambiente?")

    if ran == 33:
        print()
        print (f"{interactivo}: ¡Hey! ¿Has visto alguna piedra peculiar por aquí? Estoy coleccionándolas.")
        print()

    if ran == 34:
        print()
        print (f"{interactivo}: ¡Hola! ¿Tienes tiempo para un desafío? Estoy organizando una carrera de orientación.")
        print()
    if ran == 35:
        print()
        print (f"{interactivo}: ¡Hola! Soy {interactivo}. ¿Te gustaría escuchar algunas historias locales? A mí también, ¿te sabés alguna?")
        print()

    if ran == 36:
        print()
        print (f"{interactivo}: PEDRO PEDRO PEDRO PEEEEE")
        print()
    
    if ran == 37:
        print()
        print (f"{interactivo}: ¡Buenas!, desconozco que te trajo por aquí, pero no matricule bloque completo")
        print()

    if ran == 38:
        print()
        print (f"{interactivo}: ...")
        print()

    if ran == 39:
        print()
        print (f"{interactivo}: ¿NOS SACAMOS UN FORO JUNTOS?")
        print()
        """Mensajes iniciales de los habitantes"""

def asignar_nombres(num, nombres1, nombres2, lista_nombres):
    """Función que combina los elementos de dos listas de manera aleatoria
    cantidad = el número ingresado por el usuario que determinara la cantidad de veces que se repetirá la función
    nombres1 = lista con los nombres que van primeros
    nombres2 = lista con los nombres que van segundos
    lista_nombres = lista con todas las combinaciones generadas
    """
    if num <= 0:
        return lista_nombres
        """caso inicial que si sucede devuelve la lista de nombres ya combinados"""
    
    else:
        indice2 = random.randint(0,len(nombres1)-1)
        indice3 = random.randint(0,len(nombres2)-1)
        lista_nombres += [f"{nombres1[indice2]} {nombres2[indice3]}"]
        return asignar_nombres(num-1, nombres1, nombres2, lista_nombres) 
        """si no sucede el caso base va combinando los nombres de las dos listas de manera random
        (se usa tanto para zonas como para habitantes ya que las listas que usas las defines afuera de la funcion)"""

def combinar_palabras(oracion):
    """Función que combina los elementos de tres listas de manera aleatoria
    cantidad = el número ingresado por el usuario que determinara la cantidad de veces que se repetirá la función
    nombres1 = lista con los nombres que van primeros
    nombres2 = lista con los nombres que van segundos
    nombres3 = lista con los nombres que van terceros
    lista_nombres = lista con todas las combinaciones generadas
    """

    sujetos = ['El perro', 'La gata', 'El niño', 'La niña', 'El árbol', 'El coche', 'Juan', 'María', 'Él', 'Ella', 'Nosotros', 'Ellos', 'Tú', 'Yo', \
        'Pedro',"La capibara", "El usuario de Windows", "La cucaracha", "El elefante", "el profesor", "el estudiante de compu", "Un extranjero", "El deportista", \
        "Caramelito", "La noche", "El semestre", "La vida"]
    verbos = ['espabila', 'tortura', 'duerme', 'juega con', 'estudia', 'baila', 'canta', 'trabaja', 'ama', 'odia', 'piensa', "EXPLOTA","apoda", "GRITA", \
        "rapa", "le da mano épicamente a ", "sobrevive con", "programa un simulador usando", "viaja con", "speaks english with", "susurra", "devora", "se rinde con" \
        "reprueba", "controla", "domina", "arruina", "destruye", "arregla", "resuelve", "se sienta en silencio con", "revisa el proyecto de progra"]
    objetos = ['la pelota', 'el libro', 'la manzana', 'el agua', 'la mesa', 'la casa', 'el sol', 'la luna', 'el mundo', 'la vida', 'el amor', 'la amistad', \
        "el acta de despido", "el cafetal", "el estudiante de forestal", "tus sentimientos", "un estudiante de la UCR", "el examen de progra", "la facultad de mate", \
        "la banda de rock", "el Toyota Supra", "los estudiantes"]
    """listas de las partes que conforman una oracion basica (estan definidas adentro ya que esta funcion solo se usa con estas variables)"""

    if oracion != "":
        return oracion
        """caso base que si ocurre se detiene (si oracion no es vacia por que cuando entra se recibe vacia, returnas solo la oracion)"""
    
    else:
        indice1 = random.randint(0,len(sujetos)-1)
        indice2 = random.randint(0,len(verbos)-1)
        indice3 = random.randint(0,len(objetos)-1)
        oracion += f"{sujetos[indice1]} {verbos[indice2]} {objetos[indice3]}"
        return combinar_palabras(oracion)
        """combina los lelementos de las tres listas con un random para cada uno y devuelve la funcion junto a la oracion remplazando la variable que antes era
        una lista vacia"""


def nombres_zonas():
    """Función que devuelve una lista con dos listas, la primer lista con los primeros nombres y la segunda con los segundos"""

    primeros_nombres = ["Bosque","Lago","Mirador","Plaza","Arboleda",\
        "Jardín","Santuario","Valle","Alameda","Cerro", "Playa", "Alameda", \
        "Mercado", "Jungla", "Museo", "Area", "Bioma", "Tundra", "Manglar", \
        "Desierto", "Oasis", "Pastizal", "Finca", "Charral", "Choza", "Aerodromo", \
        "Restaurante", "Cancha", "Acuario", "Planeta", "Parque de Diversiones", "Sabana", \
        "Oceano", "Isla", "Distrito", "Instituto Tecnológico de Costa Rica", "McDonnals", \
        "Delta"] 
    """lista con los primeros nombres (zonas)"""
    
    segundos_nombres = ["Verde","Capicuo","Recursivo","Sanabria","La Cangreja",\
        "De los Niños", "Abismal", "Colorido", "Depresivo", "Neuronal", \
        "Backroom", "Solarpunk", "Ubita", "Turrialba", "Espinoza", "Ávalos", "Naval", \
        "Paradisiaco", "Inóspito", "Green", "Alegre", "Puntos Extra", \
        "José Figueres", "Alucinante", "Anarquico", "42", "Pascal", "Vega", "Tantalus V", "Janus V", "Ardana", \
        "Capibara"]
    """lista con los segundos nombres (zonas)"""

    nombres_zonas = [primeros_nombres]+[segundos_nombres] # Variable que almacena las dos listas en una sola lista 
    return nombres_zonas
    """almacena las dos listas como lista en una sola lista y lo devuelve (mas practico para la funcion de asignar nombres)"""

def desplegar_preguntas():
    print (f"""   | Agende D: Aquí hay una lista de preguntas que su respuesta tendrán coherencia: 
    ╔══════════════════════════════════════════════════════════════════════════════╗                
    ║   "como estas?"   ║ "que hora es?" ║ "que edad tienes?"║ "en donde estamos?" ║
    ║ "como te llamas?" ║    "cual es tu color favorito?"    ║   "donde naciste?"  ║ 
    ║   "cual es tu fecha de nacimiento?"   ║   "quien es tu cantante favorito?"   ║
    ║   "que tipo de musica escuchas?"   ║   "quien es tu programador favorito?"   ║
    ║    "te gustan los capibaras?"      ║      "Eres mas de playa o montaña?"     ║
    ║"si tubieras un capibara que nombre le pondrias?"║"cual es tu fruta favorita?"║
    ║ "cual es tu materia favortia de colegio?"  ║  "te gustan los croissants?"    ║
    ║ "cual es tu genero de peliculas favorito?" ║    "dame un consejo de via"     ║
    ║         dime algo filosofico"      ║          "ya no se que preguntarte"     ║
    ╚══════════════════════════════════════════════════════════════════════════════╝
    ║           ESCRIBE LA PREGUNTA TAL Y COMO SE MUESTRA EN PANTALLA              ║
    ╚══════════════════════════════════════════════════════════════════════════════╝
    
    """)

def nombres_personas():
    """Función que devuelve una lista con dos listas, la primer lista con los primeros nombres y la segunda con los segundos"""

    nombres = ["Doctor","Mr.","Doña","Rigoberto","Dayana",\
        "Elefante","Patito","Mario","Ragnar","Windows", "Aurelio", \
        "Sufrostico", "Carlos", "Santiago", "Naruto", "Fanático", \
        "Don Quijote", "Kirstein", "Aldo", "Benavides", "Terreneitor", \
        "42", "Patata", "Spock", "Nyota", "Leonard", "Worf", "Lobo", "Jesse", \
        "Juan","Marito","Wanchope","Saprissa", "Juanki","Cartaguito", "Memes", \
        "Ingenieria en", "Joctan", "Naruto", "Tortas de", "Bryan", "La", "Jake", \
        "Ivannia", "Armando", "Max"]
    """lista de nombres 1 (habitantes)"""

    apellidos = ["Piedras","Heisenberg","Panaderia","Sanabria","Aesthetic",\
        "Frijoles" ,"Marin","Solitario","Santamaria","Mortadela","Campeón", "Loko", \
        "Piolin", "Vegapunk", "Atlantis", "Oppenhaimer", "Shippuden", "Uchiha", "Yamamoto", \
        "Tanaka", "Yawanawa", "Fuji", "De la Mancha", "Macarrones", "Ruiz", "Sexta", "Vago", \
        "Inevitable", "Matata", "11111101000", "Compuertas Lógicas", "Iteración", "Tiki Taka", \
        "Ronaldo", "Heredia", "Tamales", "Relaciones", "Tartaria", "Florinda", "Deportista", \
        "42", "Cola", "Pila", "Cerdas", "Agua", "Fuego", "Hambriento", "Verstappen"]
    """lista de nombres 2 (habitantes)"""

    nombres_personas = [nombres]+[apellidos] # Variable que almacena las dos listas en una sola lista
    return nombres_personas
    """almacena las dos listas como lista en una sola lista y lo devuelve (mas practico para la funcion de asignar nombres)"""


def preguntar_cantidad():
    # Función que pregunta por la cantidad de elementos que se quieren generar
   
    cantidad = input()

    if cantidad.isdigit() == False:
        mensajes(3,agente)
        return preguntar_cantidad()
    return int(cantidad)


def generar_zonas(cantidad_zonas,cantidad_personas):
    # Funcion que genera las zonas 
    zonas= nombres_zonas()
    # Lista con todos los primeros y segundos nombres de las zonas 

    lista_zonas = asignar_nombres(int(cantidad_zonas), zonas[0], zonas[1], [])
    # lista de zonas con nombres aleatorios con la cantidad elegida por el usuario     

    hab = nombres_personas()
    # lista con todos los primeros y segundos nombres de los habitantes 

    habitantes = asignar_nombres(cantidad_personas, hab[0], hab[1],[])
    # lista de habitantes con nombres aleatorios con la cantidad elegida por el usuario 

    asignaciones = repartir_habitantes(lista_zonas,habitantes,0,len(lista_zonas),{})
    # diccionario con los habitantes repartidos en todas las zonas generadas 
     
    return preguntar_seleccion(asignaciones,lista_zonas,len(lista_zonas),0,"")
    # l

def repartir_habitantes(zonas,habitantes,indice,fin,asignaciones):
    # Función que para cada zona asigna habitantes de manera aleatoria 
    if indice == fin: # Caso base
        return asignaciones

    else:
        cantidad_aleatoria = random.randrange(0,len(habitantes)) # Cantidad de habitantes por zona generada aleatoriamente 
        asignaciones[zonas[indice]] = elegir_habitantes(habitantes,[],0,cantidad_aleatoria) 
       
        # Variable que guarda cada zona con un llamado a una función que selecciona a los habitantes de manera aleatoria con la cantidad
        # Generada anteriormente 
        return repartir_habitantes(zonas,habitantes,indice+1,fin,asignaciones) 

def elegir_habitantes(habitantes,seleccionados,indice,cantidad_aleatoria):
    # Devuelve una cantidad aleatoria de habitantes de los habitantes ya asignados para meterlos en cada zona
    
    if indice == cantidad_aleatoria: # Caso base
        return seleccionados
    
    if cantidad_aleatoria == 0: # Validación cuando se asignen 0 habitantes a una zona
        return seleccionados
    
    else:
        habitante_aleatorio = random.randrange(0,len(habitantes)) # Generador aleatorio de cualquier habitante de la lista de habitantes 
        seleccionados += [habitantes[habitante_aleatorio]] # Variable que va guardar los habitantes que se escojen aleatoriamente 
        return elegir_habitantes(habitantes,seleccionados,indice+1,cantidad_aleatoria)

def easter_egg():
    """funcion que hace una probabilidad del 1 al 100 para ver si aparece un capibara"""

    ran = random.randint(1,8)
    """random que se usa para la probabilidad"""

    if ran == 4:
        mensajes(20,agente)
        mensajes(21,agente)
        """si aparece este numero justo en el ran da el easter egg"""
    
    else:
        mensajes(19,agente)
        """si no tira que no a pasado nada"""

def preguntar_seleccion(valor,var,largo,ind,zona):
    """Funcion que compara la lista "var" con las keys, si son iguales pregunta a que zona quieres acceder y pasa a otra funcion para busacr dicha zona
    si no son iguales pasa a preguntarte con que habitante quieres interacturar (como viene de una funcion anterior siempre el primer caso va a ser igual
    a las keys osea va a ser preguntar las zonas por lo que nunca te va a preguntar habitantes sin antes pasar por las zonas y meterte a una)"""

    zonas = valor.keys()
    """define las keys de el diccionario valor como una variable"""

    if  list(zonas) == var:
        impre_zonas(var,len(var),0)
        mensajes(5,agente)
        seleccion = input()
        return entrar_zonas(valor,var,largo,ind,seleccion,zona,zonas)
        """cuando es igual la list de las list de las keys a una lista de las zonas manda mensaje y pregunta por medio de un imput a cual zona quiere acceder 
        pasando a entrar_zonas para buscar si existe dentro de la lista de zonas"""
    
    else:
        impre_personas(var,len(var),0)
        mensajes(6,agente)
        seleccion = input()
        return interaccion(valor,var,largo,ind,seleccion,zona,zonas)
        """si no es igual a la lista de las keys significa que fijo son los habitantes por lo que pasa a pregutarte con quien quieres interactuar pasando a otra
        funcion para buscar si ese habitante existe"""

def entrar_zonas(valor,var,largo,ind,seleccion,zona,zonas):
    """funcion la cual revisa si la zona existe en la lista"""

    if largo == ind:
        mensajes(7,agente)
        return preguntar_seleccion(valor,var,largo,0,[])
        """caso base: si ocurre el caso base significa que el input no existe en la lista de las zonas por lo que tira errro y te devuelve a que reescribas
        el input"""

    elif seleccion == var[ind]:
        entrar_zona(seleccion)
        return preguntar_seleccion(valor,valor[seleccion],len(valor[seleccion]),0,seleccion)
        """si la posicion ind coincide con el input significa que si existe dentro de la lista por lo que vuelve a preguntar seleccion pero cambiando la lista
        de zonas por lista de habitantes (se agarra del diccionario) y se guarda la zona seleccionada para otras funciones futuras"""

    else:
        return entrar_zonas(valor,var,largo,ind+1,seleccion,zona,zonas)
        """si no pasa ninguna de los dos le suma uno al ind para que busque con el siguiente termino y repita la funcion"""

def interaccion(valor,var,largo,ind,seleccion,zona,zonas):
    """funcion que busca en la lista de habitantes el input para ver si existe"""

    if seleccion == "irse" or seleccion == "Irse" or seleccion == "IRSE":
        return preguntar_seleccion(valor,list(zonas),len(list(zonas)),0,[])
        """condicion extra la cual si el input es irse te devuelve a la seleccion de zonas"""
    
    elif seleccion == "esperar" or seleccion == "Esperar":
        easter_egg()
        return preguntar_seleccion(valor,var,largo,0,zona)

    elif largo == ind:
        mensajes(10,agente)
        return preguntar_seleccion(valor,var,largo,0,zona)
        """si el ind es igual al largo significa que el input no existe en la lista de habitantes por lo que te tira error y te pide reescribir un nuevo input"""
    
    elif seleccion == var[ind]:
        mensajes_presentacion(seleccion,zona)
        return acc(valor,var,var[ind],zona,"")
        """si el input es igual a la posicion ind de la lista de habitantes actua la funcion mensajes_presentacion y pasa a la funcion acc (input de la pregunta
        hacia el habitante)"""
        
    else:
        return interaccion(valor,var,largo,ind+1,seleccion,zona,zonas)
        """si no pasa ninguna de las dos cosas significa que la lista no a terminado de devolverse por lo que le suma uno al ind y vuelve a efectuar la funcion"""

def entrar_zona(zona): 
    """Función que imprime la Zona que estamos visitando"""

    mensajes(18,agente)
    mensajes(17,agente)
    mensajes(8,agente)
    print (f"""{zona}""".center(80,"-"))
    """dos prints de la funcion mensajes para contexto y la zona escrita de forma ordenada"""
        
def acc(valor,var,nombre,zona,pregunta):
    """funcion del input para la eleccion de la respuesta"""

    if pregunta == "":
        """si la pregunta es vacia significa que aun no le has preguntado nada por lo que te pasa al primer if que te tira el input de pregunta"""
        desplegar_preguntas()
        print(f"""Agente D: Que le vas decir a {nombre}? 
                                        * AVISO *
    ╔════════════════════════════════════════════════════════════════════════════════╗ 
    ║ Al ser una dimesión alterna, las respuestas pueden llegar a tener 0 coherencia ║ 
    ╚════════════════════════════════════════════════════════════════════════════════╝ 
    (DIGITA "Irse" PARA REGRESAR)
""")
        pregunta = input()
        """input que se usa para ver que le vas a preguntar al habitante"""

        preguntas = listas(8,zona,nombre)
        """lista de todos las preguntas coherentes definidas en otra funcion por orden"""

        respuestas = listas(9,zona,nombre)
        """lista de respuestas con varias posibles respuestas dadas en otra funcion por orden"""

        if pregunta == "irse" or pregunta == "Irse":
            return preguntar_seleccion(valor,var,len(var),0,zona)
            """despues de definir si escribes en el input irse te devuelve a la seleccion de hablar con habitantes"""
        
        else:
            return respuesta(preguntas,respuestas,pregunta,valor,var,nombre,zona)
            """cualquier otra cosa te pasa a la funcion que genera la respuesta"""
    
    else:
        otra_pregunta(valor,var,nombre,zona,pregunta)
        """en este else (el de afuera) si la "pregunta" no esta vacia osea que ya paso por una respuesta te pasa a una funcion que te pregunta si quieres decirle
        algo mas"""

def respuesta(preguntas,respuestas,pregunta,valor,var,nombre,zona):
    """funcion que cuando seleccionas hablar con alguien tire texto"""

    if type(pregunta)!=str:
        print("EMMM eso no es algo que te pueda responder")
        return respuesta(preguntas,respuestas,pregunta,valor,var,nombre,zona)
        """si la respuesta no es str te devuelve a que pongas otra respuesta"""
    
    else:
        return respuesta_aux(preguntas,respuestas,pregunta,len(preguntas),0,valor,var,nombre,zona)
        """"si si es str pasa a la funcon auxiliar"""

def respuesta_aux(preguntas,respuestas,pregunta,largo,ind,valor,var,nombre,zona):
    """funcion auxiliar"""

    impro = combinar_palabras("")
    """definicion de variable dada por la funcion que combina tres listas (partes de una oracion simple)"""

    if largo==ind:
        print()
        print(impro)
        print()
        return acc(valor,var,nombre,zona,pregunta)
        """si llega al final significa que no esta en las preguntas entonces tira random"""
    
    elif preguntas[ind]==pregunta:
        print()
        print(respuestas[ind])
        print()
        return acc(valor,var,nombre,zona,pregunta)
        """si tira igual al numero que va significa que si esta dentro de las preguntas
         por lo que pasa a tirar su resptectiva respuesta(estaria en el mismo lugar que 
         el de la pregunta) """
    
    else:
        return respuesta_aux(preguntas,respuestas,pregunta,largo,ind+1,valor,var,nombre,zona)
        """si no llego al final o la encontro lo pasa a la siguiente a ver si la encuentra"""


def otra_pregunta(valor,var,nombre,zona,pregunta):
    """funcion que pregunta si quieres decirle algo mas al habitante con el cual estas hablando"""

    mensajes(14,agente)
    int2= (input("""
(S)Si
(N)No

"""))
    """mensaje mas input el de pregunta sobre si quieres decirle algo mas al habitante"""
    
    if int2 == "S" or int2 == "s":
        return acc(valor,var,nombre,zona,"")
        """si el input es "S" significa que si le quiere volver a hacer otra pregunta por lo que te devuelve a la parte del input de
        preguntas"""

    elif int2 == "N" or int2 == "n":
        return preguntar_seleccion(valor,var,len(var),0,zona)
        """si el input es "N" significa que no le quieres volver a hacer una pregunta por lo que te devuelve al menu de seleccion de
        habitantes"""
    
    else:
        mensajes(16,agente)
        return otra_pregunta(valor,var,nombre,zona,pregunta)
        """cualquier otra cosa no tiene sentido en el imput por lo que tira error y te devuelve a reescribir el input"""


def bienvenida(entrada):
    if entrada == 1:
        """primera funcion, te da la bienvenida al juego"""


        print("Oh vaya parece que te llego un email:")

        mensajes(1,agente)

    irse= (input("""     - ¿ACEPTAS LA MISIÓN?: - 
    |   (S) SI   |   (N) NO   |
"""))
    """mensajes de bienvenida y contextualizacion mas un input del inicio para ver si aceptas la "mision" """

    if irse=="S" or irse=="s":
        mensajes(15,agente)
        mensajes(2,agente)
        numero_de_zonas = preguntar_cantidad()
        mensajes(2.5,agente) # mostrar mensaje que pide numero de personas 
        numero_de_personas = preguntar_cantidad()
        return generar_zonas(numero_de_zonas, numero_de_personas)
        """si la respuesta al input es "s" tira mensajes de contexto e historia y avanza con las siguientes funciones"""
    
    elif irse=="N" or irse=="n":
        print(mensajes(11,agente))
        exit()
        """Si la respuesta al input es "N" tira mensaje de finalizacion y termina la ejecucion """
    else: 
        print(mensajes(11.5,agente))
        return bienvenida(42)

bienvenida(1)
"""llama a la primera funcion para que empiece todo"""