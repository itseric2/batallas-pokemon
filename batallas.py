#Batallas seguidas
import climage
import random
import pyfiglet
zeus= {
        "Nombre": "Zeus",
        "vida": random.randint(800, 1000),
        "rayo": 60,
        "tormenta": 80,
        "rayo_critico": 120,
        "Criatura_de_saturno": 100,
        "Campo_electrico": 120,
        "Control_del_clima":140,
        "Dominio_de_energia":160,
        "fallo": 0,
        "rayo_curativo":0,
        "super_rayo" : 300,
        "mega_rayo" : 600,
        "ultra_rayo" :2000,
        "tormenta_de_ira": 1500 
    }
zeus["copias"]=zeus[random.choice(["rayo","tormenta","rayo_curativo","Criatura_de_saturno","Campo_electrico","fallo","Control_del_clima","Dominio_de_energia"])]    
zeus["rayos"] = zeus[random.choice(["rayo", "rayo_critico"])]
zeus["fallo_rayo"] = zeus[random.choice(["rayos", "fallo","rayos", "fallo","rayos", "fallo","rayos", "fallo","rayos","ultra_rayo","fallo","rayos", "fallo","super_rayo","rayos","mega_rayo","fallo","rayos", "fallo","rayos", "fallo","rayos", "fallo","super_rayo","super_rayo","mega_rayo"])]
zeus["fallo_tormenta"] = zeus[random.choice(["tormenta", "fallo","tormenta", "fallo","tormenta", "fallo","tormenta", "fallo","tormenta_de_ira"])]
zeus["fallo_criatura"] = zeus[random.choice(["Criatura_de_saturno", "fallo"])]
zeus["fallo_campo"] = zeus[random.choice(["Campo_electrico", "fallo"])]
zeus["fallodo"]= zeus[random.choice(["Dominio_de_energia","fallo"])]
zeus["falloco"]= zeus[random.choice(["Control_del_clima","fallo"])]
    
khonshu= {
    "Nombre":"Khonshu",
    "vida":random.randint(800, 2000),
    "Two_moons":280,
    "Meteoro_lunar":130,
    "Luna_llena":140,
    "Media_luna":70,
    "Moon_fall":150,
    "Piedras_lunares":120,
    "Oz_lunar":200,
    "fallo":0,
    "Oz_lunar_manchada":300,
    "triple_piedras_lunares":360,
    "Quad_moons":560,
    "lluvia_lunar":1300
    }

khonshu["fallot"]= khonshu[random.choice(["Two_moons","fallo","Two_moons","fallo","Two_moons","fallo","Two_moons","fallo","Two_moons","fallo","Two_moons","fallo","Quad_moons"])]
khonshu["fallome"]= khonshu[random.choice(["Meteoro_lunar","fallo","Meteoro_lunar","fallo","Meteoro_lunar","fallo","Meteoro_lunar","fallo","Meteoro_lunar","fallo","Meteoro_lunar","fallo","lluvia_lunar"])]
khonshu["fallol"]= khonshu[random.choice(["Luna_llena","fallo"])]
khonshu["falloml"]=khonshu[random.choice(["Media_luna","fallo"])]
khonshu["fallomf"]= khonshu[random.choice(["Moon_fall","fallo"])]
khonshu["fallop"]= khonshu[random.choice(["Piedras_lunares","fallo","Piedras_lunares","fallo","Piedras_lunares","fallo","Piedras_lunares","fallo","Piedras_lunares","fallo","triple_piedras_lunares"])]
khonshu["falloozl"]= khonshu[random.choice(["Oz_lunar","fallo","Oz_lunar","fallo","Oz_lunar","fallo","Oz_lunar","fallo","Oz_lunar","fallo","Oz_lunar","fallo","Oz_lunar_manchada"])]
    
anubis= {
    "Nombre":"Anubis",
    "vida":random.randint(800,4000),
    "Tumba_del_rey":70,
    "Ejercito_de_muertos":80,
    "Hacha_de_muerte":250,
    "Apocalipsis_final":60,
    "Almas_perdidas":40,
    "Poder_prestado":110,
    "Muerte":400,
    "fallo":0,
    "Oz_de_muerte":350,
    "triple_hacha":750,
    "Doble_oz":700,
    "lluvia_de_muerte":4000
    }

anubis["fallotr"]= anubis[random.choice(["Tumba_del_rey","fallo"])]
anubis["falloem"]= anubis[random.choice(["Ejercito_de_muertos","fallo"])]
anubis["fallohm"]= anubis[random.choice(["Hacha_de_muerte","fallo","Hacha_de_muerte","fallo","Hacha_de_muerte","fallo","Hacha_de_muerte","fallo","Hacha_de_muerte","fallo","triple_hacha"])]
anubis["falloaf"]= anubis[random.choice(["Apocalipsis_final","fallo"])]
anubis["falloap"]= anubis[random.choice(["Almas_perdidas","fallo"])]
anubis["fallopp"]= anubis[random.choice(["Poder_prestado","fallo"])]
anubis["fallomt"]= anubis[random.choice(["Muerte","fallo","Muerte","fallo","Muerte","fallo","Muerte","fallo","Muerte","fallo","Muerte","fallo","Muerte","fallo","lluvia_de_muerte"])]
anubis["fallooz"]= anubis[random.choice(["Oz_de_muerte","fallo","Oz_de_muerte","fallo","Oz_de_muerte","fallo","Oz_de_muerte","fallo","Oz_de_muerte","fallo","Oz_de_muerte","fallo","Doble_oz"])]



titulo = pyfiglet.figlet_format("Welcome to pokemon fights")
print(titulo)
print("1- Zeus\n2- Khonshu\n3- Anubis")
cp = int(input("Elige tu personaje: "))
while cp <= 0 or cp >=4 :
    cp = int(input("Elige tu personaje: "))

# Berserk
def berserk():
    berserk = {
        "Nombre": "berserk",
        "vidab": random.randint(6000, 10000),
        "ira": 40,
        "golpes": 50,
        "ola_golpeante": 60,
        "Furia_berserker": 75,
        "fallob": 0,
        "puño_de_hierro":90,
        "mi_sangre":100,
        "cuerpo_carmesi":125,
        "nivel1":2.5,
        "nivel2":3,
        "nivel3":3.5,
        "nivel4":4
    }
    berserk["danob"] = berserk[random.choice(["ira", "golpes", "fallob", "ola_golpeante", "Furia_berserker","puño_de_hierro","mi_sangre","cuerpo_carmesi"])]
    berserk["niveles"]= berserk[random.choice(["nivel1","nivel2","nivel3","nivel4"])]
    return berserk
# Espadachin
def espadachin():
    espadachin = {
        "Nombre": "espadachin",
        "vidae": random.randint(1000, 3000),
        "slash": 30,
        "corte_vertical": 60,
        "triple_slash":90 ,
        "desenvaine_rapido": 70,
        "doble_corte": 120,
        "falloe": 0,
        "corte_perfecto":100,
        "espada_del_rey":85,
        "Haki_del_rey":110,
        "nivel1":1.5,
        "nivel2":2
                
        
    }
    espadachin["danoe"] = espadachin[random.choice(["slash", "corte_vertical", "falloe", "triple_slash", "desenvaine_rapido", "doble_corte","corte_perfecto","espada_del_rey"])]
    espadachin["niveles"]= espadachin[random.choice(["nivel1","nivel2"])]
    return espadachin
# Mago
def mago():
    mago = {
        "Nombre": "mago",
        "vidam": random.randint(4000,8000),
        "ataque_magico": 40,
        "bestia_magica": 50,
        "fallom": 0,
        "coraza_magica": 100,
        "ataque_de_fuego":70,
        "esfera_oceanica":90,
        "esfera_carmesi":100,
        "esfera_oscura":110,
        "Dominio_del_mana":120,
        "nivel1":2,
        "nivel2":2.5,
        "nivel3":3
    }
    mago["danom"] = mago[random.choice(["ataque_magico", "bestia_magica", "fallom","ataque_de_fuego","esfera_oceanica","esfera_carmesi","esfera_oscura","Dominio_del_mana"])]
    mago["niveles"]= mago[random.choice(["nivel1","nivel2","nivel3"])]
    
    return mago
# Invocador
def invocador():
    invocador = {
        "Nombre": "invocador",
        "vidai": random.randint(10000, 14000),
        "perro_infernal": 50,
        "duende":60,
        "lagartija_multiple":80,
        "ogro": 100,
        "jabali":90,
        "minotauro":120,
        "dragon":150,
        "Hidra":200,
        "falloi": 0,
        "nivel1":3,
        "nivel2":3.5,
        "nivel3":4,
        "nivel4":4.5,
        "nivel5":5,
        "nivel6":6
    }
    invocador["danoi"] = invocador[random.choice(["perro_infernal", "ogro","jabali","minotauro","dragon","falloi","duende","lagartija_multiple","Hidra"])]
    invocador["niveles"]= invocador[random.choice(["nivel1","nivel2","nivel3","nivel4","nivel5","nivel6"])]
    return invocador        

print()

#   ENEMIGOS Y VARIABLE DE BUCLE
enemigo1 = espadachin()
enemigo2 = mago()
enemigo3 = berserk()
enemigo4 = invocador()
bool_value = True
bool_valuem = True
bool_valueb = True
bool_valuei = True


#  NIVELES
nivele1 = 0
nivele2 = 0
nivele3 = 0
nivele4 = 0
#  NIVELES ESPADACHIN
if enemigo1["niveles"] == enemigo1["nivel1"]:
    nivele1 = 1
elif enemigo1["niveles"] == enemigo1["nivel2"]:
    nivele1 = 2
#  NIVELES MAGO
if enemigo2["niveles"] == enemigo2["nivel1"]:
    nivele2 = 1
elif enemigo2["niveles"] == enemigo2["nivel2"]:
    nivele2 = 2
elif enemigo2["niveles"] == enemigo2["nivel3"]:
    nivele2 = 3
#  NIVELES BERSERK
if enemigo3["niveles"] == enemigo3["nivel1"]:
    nivele3 = 1
elif enemigo3["niveles"] == enemigo3["nivel2"]:
    nivele3 = 2
elif enemigo3["niveles"] == enemigo3["nivel3"]:
    nivele3 = 3
elif enemigo3["niveles"] == enemigo3["nivel4"]:
    nivele3 = 4
#  NIVELES INVOCADOR
if enemigo4["niveles"] == enemigo4["nivel1"]:
    nivele4 = 1
elif enemigo4["niveles"] == enemigo4["nivel2"]:
    nivele4 = 2
elif enemigo4["niveles"] == enemigo4["nivel3"]:
    nivele4 = 3
elif enemigo4["niveles"] == enemigo4["nivel4"]:
    nivele4 = 4
elif enemigo4["niveles"] == enemigo4["nivel5"]:
    nivele4 = 5
elif enemigo4["niveles"] == enemigo4["nivel6"]:
    nivele4 = 6


#  MULTIPLICADOR DEL ENEMIGO
daño = enemigo1["danoe"]
daño *= enemigo1["niveles"]

dañom = enemigo2["danom"]
dañom *= enemigo2["niveles"]
enemigo2["coraza_magica"] *= enemigo2["niveles"]
enemigo2["vidam"] += enemigo2["coraza_magica"]

dañob = enemigo3["danob"]
dañob *= enemigo3["niveles"]

dañoi = enemigo4["danoi"]
dañoi *= enemigo4["niveles"]

#  Representacion de enemigos
espadachinImage = climage.convert("pixil-frame-0.png", width=50)
berserkImage = climage.convert("berserker.png" , width=55)
magoImage = climage.convert("magito.png" , width=55)
invocadorImage = climage.convert("invocador.png" , width=55)

    

# enemigos zeus
print("Tu oponente sera:",enemigo1["Nombre"],"-nivel",nivele1)
print("La vida del oponente es: ",enemigo1["vidae"])
print()
if cp == 1 :
    print(espadachinImage)
    if enemigo1["vidae"] > 0 :
        while bool_value :
            enemigo1["danoe"] = enemigo1[random.choice(["slash", "corte_vertical", "falloe", "triple_slash", "desenvaine_rapido", "doble_corte","corte_perfecto","espada_del_rey"])]

            print("Tu vida es: ",zeus["vida"])
            print("Poderes\n1-Rayo (60 daño) \n2-Tormenta (80 daño) \n3-Criatura de saturno (100 daño) \n4-Campo electrico (120 daño) \n5-Control del clima (140 daño) \n6-Dominio de energia (160 daño) \n7-Rayo curativo (300 vida)")
            x=int(input("{ "))
            if x == 1:
                enemigo1["vidae"] -= zeus["fallo_rayo"]
                if zeus["fallo_rayo"]== zeus["rayo_critico"]:
                    print("Has hecho un critico")
                elif zeus["fallo_rayo"]== zeus["super_rayo"]:
                    print("Has lanzado un super rayo")
                elif zeus["fallo_rayo"]== zeus["mega_rayo"]:
                    print("Has lanzado un mega rayo")
                elif zeus["fallo_rayo"]== zeus["ultra_rayo"]:
                    print("Has lanzado un ultra rayo")
                elif zeus["fallo_rayo"] == zeus["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo1["vidae"])
            elif x ==2:
                enemigo1["vidae"]-=zeus["fallo_tormenta"]
                if zeus["fallo_tormenta"] == zeus["fallo"]:               
                    print("¡Fallaste!")
                elif zeus["fallo_tormenta"] == zeus["tormenta_de_ira"]:
                    print("Has lanzado una tormenta con ira")
                print("Vida del oponente", enemigo1["vidae"])
            elif x ==3:
                enemigo1["vidae"]-=zeus["fallo_criatura"]
                if zeus["fallo_criatura"] == zeus["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo1["vidae"])
        
            elif x ==4:
                enemigo1["vidae"]-=zeus["fallo_campo"]
                if zeus["fallo_campo"] == zeus["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo1["vidae"])
        
            elif x ==5:
                enemigo1["vidae"]-=zeus["falloco"]
                if zeus["falloco"] == zeus["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo1["vidae"])
            elif x ==6:
                enemigo1["vidae"]-=zeus["fallodo"]
                if zeus["fallodo"] == zeus["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo1["vidae"])
            elif x ==7:
                zeus["vida"] += 25000
                print("+300 vida")

            
            
            
            if daño == 45 or daño == 60 :
                print("El oponente ha utilizado (slash) y te ha quitado",daño,"de vida")
            elif daño == 90 or daño == 120:
                print("El oponente ha utilizado (corte vertical) y te ha quitado",daño,"de vida")
            elif daño == 0:
                print("El enemigo ha fallado")
            elif daño == 135 or daño == 180:
                print("El oponente ha utilizado (triple slash) y te ha quitado",daño,"de vida")
            elif daño == 105 or daño == 140:
                print("El oponente ha utilizado (desenvaine rápido) y te ha quitado",daño,"de vida")
            elif daño == 180 or daño == 240:
                print("El oponente ha utilizado (doble corte) y te ha quitado",daño,"de vida")
            elif daño == 150 or daño == 200:
                print("El oponente ha hecho un corte perfecto y te a quitado",daño,"de vida")
            elif daño == 127.5 or daño == 170:
                print("El oponente ha utilizado la espada del rey y te ha quitado",daño,"de vida")
            elif daño == 165 or daño == 220:
                print("El oponente ha utilizado el haki del rey y te a quitado",daño,"de vida")
            zeus["vida"] -= daño
        
        

            zeus["copias"]=zeus[random.choice(["rayo","tormenta","rayo_curativo","Criatura_de_saturno","Campo_electrico","fallo","Control_del_clima","Dominio_de_energia"])]    
            zeus["rayos"] = zeus[random.choice(["rayo", "rayo_critico"])]
            zeus["fallo_rayo"] = zeus[random.choice(["rayos", "fallo","rayos", "fallo","rayos", "fallo","rayos", "fallo","rayos","ultra_rayo","fallo","rayos", "fallo","super_rayo","rayos","mega_rayo","fallo","rayos", "fallo","rayos", "fallo","rayos", "fallo","super_rayo","super_rayo","mega_rayo"])]
            zeus["fallo_tormenta"] = zeus[random.choice(["tormenta", "fallo","tormenta", "fallo","tormenta", "fallo","tormenta", "fallo","tormenta_de_ira"])]
            zeus["fallo_criatura"] = zeus[random.choice(["Criatura_de_saturno", "fallo"])]
            zeus["fallo_campo"] = zeus[random.choice(["Campo_electrico", "fallo"])]
            zeus["fallodo"]= zeus[random.choice(["Dominio_de_energia","fallo"])]
            zeus["falloco"]= zeus[random.choice(["Control_del_clima","fallo"])]
            enemigo1["danoe"] = enemigo1[random.choice(["slash", "corte_vertical", "falloe", "triple_slash", "desenvaine_rapido", "doble_corte","corte_perfecto","espada_del_rey"])]

            if zeus["vida"] <= 0:
                print("¡Perdiste!")
                bool_value = False
            elif enemigo1["vidae"] <= 0:
                bool_value = False
    
    print("¡Ganaste contra el espadachin!\n")
    print("Tu siguiente oponente sera:",enemigo2["Nombre"],"-nivel",nivele2)
    print("La vida del oponente es: ",enemigo2["vidam"])
    print(magoImage)
    
    if enemigo2["vidam"] > 0 :

        while bool_valuem :
            enemigo2["danom"] = enemigo2[random.choice(["ataque_magico", "bestia_magica", "fallom","ataque_de_fuego","esfera_oceanica","esfera_carmesi","esfera_oscura","Dominio_del_mana"])]
            
            print("Tu vida es: ",zeus["vida"])
            print("Poderes\n1-Rayo (60 daño) \n2-Tormenta (80 daño) \n3-Criatura de saturno (100 daño) \n4-Campo electrico (120 daño) \n5-Control del clima (140 daño) \n6-Dominio de energia (160 daño) \n7-Rayo curativo (300 vida)")
            x=int(input("{ "))
            if x == 1:
                enemigo2["vidam"] -= zeus["fallo_rayo"]
                if zeus["fallo_rayo"]== zeus["rayo_critico"]:
                    print("Has hecho un critico")
                elif zeus["fallo_rayo"]== zeus["super_rayo"]:
                    print("Has lanzado un super rayo")
                elif zeus["fallo_rayo"]== zeus["mega_rayo"]:
                    print("Has lanzado un mega rayo")
                elif zeus["fallo_rayo"]== zeus["ultra_rayo"]:
                    print("Has lanzado un ultra rayo")
                elif zeus["fallo_rayo"] == zeus["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo2["vidam"])
            elif x ==2:
                enemigo2["vidam"]-=zeus["fallo_tormenta"]
                if zeus["fallo_tormenta"] == zeus["fallo"]:
                    print("¡Fallaste!")
                elif zeus["fallo_tormenta"] == zeus["tormenta_de_ira"]:
                    print("Has lanzado una tormenta con ira")
                print("Vida del oponente", enemigo2["vidam"])
            elif x ==3:
                enemigo2["vidam"]-=zeus["fallo_criatura"]
                if zeus["fallo_criatura"] == zeus["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo2["vidam"])
    
            elif x ==4:
                enemigo2["vidam"]-=zeus["fallo_campo"]
                if zeus["fallo_campo"] == zeus["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo2["vidam"])
    
            elif x ==5:
                enemigo2["vidam"]-=zeus["falloco"]
                if zeus["falloco"] == zeus["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo2["vidam"])
            elif x ==6:
                enemigo2["vidam"]-=zeus["fallodo"]
                if zeus["fallodo"] == zeus["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo2["vidam"])
            elif x ==7:
                zeus["vida"] += 300
                print("+300 vida")
            
            print("Mago se a puesto una capa magica +",enemigo2["coraza_magica"])           


                        

            if dañom == 80 or dañom == 100 or dañom == 120 :
                print("El oponente ha utilizado (ataque magico) y te ha quitado",dañom,"de vida")
            elif dañom == 100 or dañom == 125 or dañom == 150:
                print("El oponente ha utilizado (bestia magica) y te ha quitado",dañom,"de vida")
            elif dañom == 0:
                print("El enemigo ha fallado")
            elif dañom == 140 or dañom == 175 or dañom == 210 :
                print("El oponente ha utilizado (ataque de fuego) y te ha quitado",dañom,"de vida")
            elif dañom == 180 or dañom == 225 or dañom == 270:
                print("El oponente ha utilizado (esfera oceanica) y te ha quitado",dañom,"de vida")
            elif dañom == 200 or dañom == 250 or dañom == 300:
                print("El oponente ha utilizado (esfera carmesi) y te ha quitado",dañom,"de vida")
            elif dañom == 220 or dañom == 275 or dañom == 330:
                print("El oponente ha utilizado (esfera oscura) y te a quitado",dañom,"de vida")
            elif dañom == 240 or dañom == 300 or dañom == 360:
                print("El oponente ha utilizado (dominio del mana) y te ha quitado",dañom,"de vida")
              
            zeus["vida"] -= dañom
            zeus["copias"]=zeus[random.choice(["rayo","tormenta","rayo_curativo","Criatura_de_saturno","Campo_electrico","fallo","Control_del_clima","Dominio_de_energia"])]    
            zeus["rayos"] = zeus[random.choice(["rayo", "rayo_critico"])]
            zeus["fallo_rayo"] = zeus[random.choice(["rayos", "fallo","rayos", "fallo","rayos", "fallo","rayos", "fallo","rayos","ultra_rayo","fallo","rayos", "fallo","super_rayo","rayos","mega_rayo","fallo","rayos", "fallo","rayos", "fallo","rayos", "fallo","super_rayo","super_rayo","mega_rayo"])]
            zeus["fallo_tormenta"] = zeus[random.choice(["tormenta", "fallo","tormenta", "fallo","tormenta", "fallo","tormenta", "fallo","tormenta_de_ira"])]
            zeus["fallo_criatura"] = zeus[random.choice(["Criatura_de_saturno", "fallo"])]
            zeus["fallo_campo"] = zeus[random.choice(["Campo_electrico", "fallo"])]
            zeus["fallodo"]= zeus[random.choice(["Dominio_de_energia","fallo"])]
            zeus["falloco"]= zeus[random.choice(["Control_del_clima","fallo"])]
            enemigo2["danom"] = enemigo2[random.choice(["ataque_magico", "bestia_magica", "fallom","ataque_de_fuego","esfera_oceanica","esfera_carmesi","esfera_oscura","Dominio_del_mana"])]
            

            
            if zeus["vida"] <= 0:
                print("¡Perdiste!")
                bool_valuem = False
            elif enemigo2["vidam"] <= 0:
                bool_valuem = False
    

    print("¡Ganaste contra el mago!\n")
    print("Tu siguiente oponente sera:",enemigo3["Nombre"],"-nivel",nivele3)
    print("La vida del oponente es: ",enemigo3["vidab"])
    print(berserkImage)
    if enemigo3["vidab"] > 0 :
        
        while bool_valueb :
            enemigo3["danob"] = enemigo3[random.choice(["ira", "golpes", "fallob", "ola_golpeante", "Furia_berserker","puño_de_hierro","mi_sangre","cuerpo_carmesi"])]
            print("Tu vida es: ",zeus["vida"])
            print("Poderes\n1-Rayo (60 daño) \n2-Tormenta (80 daño) \n3-Criatura de saturno (100 daño) \n4-Campo electrico (120 daño) \n5-Control del clima (140 daño) \n6-Dominio de energia (160 daño) \n7-Rayo curativo (300 vida)")
            x=int(input("{ "))
            if x == 1:
                enemigo3["vidab"] -= zeus["fallo_rayo"]
                if zeus["fallo_rayo"]== zeus["rayo_critico"]:
                    print("Has hecho un critico")
                elif zeus["fallo_rayo"]== zeus["super_rayo"]:
                    print("Has lanzado un super rayo")
                elif zeus["fallo_rayo"]== zeus["mega_rayo"]:
                    print("Has lanzado un mega rayo")
                elif zeus["fallo_rayo"]== zeus["ultra_rayo"]:
                    print("Has lanzado un ultra rayo")
                elif zeus["fallo_rayo"] == zeus["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo3["vidab"])
            elif x ==2:
                enemigo3["vidab"]-=zeus["fallo_tormenta"]
                if zeus["fallo_tormenta"] == zeus["fallo"]:
                    print("¡Fallaste!")
                elif zeus["fallo_tormenta"] == zeus["tormenta_de_ira"]:
                    print("Has lanzado una tormenta con ira")
                print("Vida del oponente", enemigo3["vidab"])
            elif x ==3:
                enemigo3["vidab"]-=zeus["fallo_criatura"]
                if zeus["fallo_criatura"] == zeus["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo3["vidab"])
        
            elif x ==4:
                enemigo3["vidab"]-=zeus["fallo_campo"]
                if zeus["fallo_campo"] == zeus["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo3["vidab"])

            elif x ==5:
                enemigo3["vidab"]-=zeus["falloco"]
                if zeus["falloco"] == zeus["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo3["vidab"])
            elif x ==6:
                enemigo3["vidab"]-=zeus["fallodo"]
                if zeus["fallodo"] == zeus["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo3["vidab"])
            elif x ==7:
                zeus["vida"] += 300
                print("+300 vida")

            
            

            if dañob == 100 or dañob == 120 or dañob == 140 or dañob == 160:
                print("El oponente ha utilizado (ira) y te ha quitado",dañob,"de vida")
            elif dañob == 125 or dañob == 150 or dañob == 175 or dañob == 200:
                print("El oponente ha utilizado (golpes) y te ha quitado",dañob,"de vida")
            elif dañob == 0:
                print("El enemigo ha fallado")
            elif dañob == 150 or dañob == 180 or dañob == 210 or dañob == 240 :
                print("El oponente ha utilizado (ola golpeante) y te ha quitado",dañob,"de vida")
            elif dañob == 187.5 or dañob == 225 or dañob == 262.5 or dañob == 300:
                print("El oponente ha utilizado (furia berserker) y te ha quitado",dañob,"de vida")
            elif dañob == 225 or dañob == 270 or dañob == 315 or dañob == 360:
                print("El oponente ha utilizado (puño de hierro) y te ha quitado",dañob,"de vida")
            elif dañob == 250 or dañob == 300 or dañob == 350 or dañob == 400:
                print("El oponente ha utilizado (sangre berserk) y te a quitado",dañob,"de vida")
            elif dañob == 312.5 or dañob == 375 or dañob == 437.5 or dañob == 500:
                print("El oponente ha utilizado (cuerpo carmesi) y te ha quitado",dañob,"de vida")

            zeus["vida"] -= dañob
            zeus["copias"]=zeus[random.choice(["rayo","tormenta","rayo_curativo","Criatura_de_saturno","Campo_electrico","fallo","Control_del_clima","Dominio_de_energia"])]    
            zeus["rayos"] = zeus[random.choice(["rayo", "rayo_critico"])]
            zeus["fallo_rayo"] = zeus[random.choice(["rayos", "fallo","rayos", "fallo","rayos", "fallo","rayos", "fallo","rayos","ultra_rayo","fallo","rayos", "fallo","super_rayo","rayos","mega_rayo","fallo","rayos", "fallo","rayos", "fallo","rayos", "fallo","super_rayo","super_rayo","mega_rayo"])]
            zeus["fallo_tormenta"] = zeus[random.choice(["tormenta", "fallo","tormenta", "fallo","tormenta", "fallo","tormenta", "fallo","tormenta_de_ira"])]
            zeus["fallo_criatura"] = zeus[random.choice(["Criatura_de_saturno", "fallo"])]
            zeus["fallo_campo"] = zeus[random.choice(["Campo_electrico", "fallo"])]
            zeus["fallodo"]= zeus[random.choice(["Dominio_de_energia","fallo"])]
            zeus["falloco"]= zeus[random.choice(["Control_del_clima","fallo"])]
            enemigo3["danob"] = enemigo3[random.choice(["ira", "golpes", "fallob", "ola_golpeante", "Furia_berserker","puño_de_hierro","mi_sangre","cuerpo_carmesi"])]
            if zeus["vida"] <= 0:
                print("¡Perdiste!")
                bool_valueb = False
            elif enemigo3["vidab"] <= 0:
                bool_valueb = False
        
    print("¡Ganaste contra el berserk!\n")
    print("Tu siguiente oponente sera:",enemigo4["Nombre"],"-nivel",nivele4)
    print("La vida del oponente es: ",enemigo4["vidai"])
    print(invocadorImage)
    if enemigo4["vidai"] > 0 :
                
        while bool_valuei :
            enemigo4["danoi"] = enemigo4[random.choice(["perro_infernal", "ogro","jabali","minotauro","dragon","falloi","duende","lagartija_multiple","Hidra"])]
            print("Tu vida es: ",zeus["vida"])
            print("Poderes\n1-Rayo (60 daño) \n2-Tormenta (80 daño) \n3-Criatura de saturno (100 daño) \n4-Campo electrico (120 daño) \n5-Control del clima (140 daño) \n6-Dominio de energia (160 daño) \n7-Rayo curativo (300 vida)")
            x=int(input("{ "))
            if x == 1:
                enemigo4["vidai"] -= zeus["fallo_rayo"]
                if zeus["fallo_rayo"]== zeus["rayo_critico"]:
                    print("Has hecho un critico")
                elif zeus["fallo_rayo"]== zeus["super_rayo"]:
                    print("Has lanzado un super rayo")
                elif zeus["fallo_rayo"]== zeus["mega_rayo"]:
                    print("Has lanzado un mega rayo")
                elif zeus["fallo_rayo"]== zeus["ultra_rayo"]:
                    print("Has lanzado un ultra rayo")
                elif zeus["fallo_rayo"] == zeus["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo4["vidai"])
            elif x ==2:
                enemigo4["vidai"]-=zeus["fallo_tormenta"]
                if zeus["fallo_tormenta"] == zeus["fallo"]:
                    print("¡Fallaste!")
                elif zeus["fallo_tormenta"] == zeus["tormenta_de_ira"]:
                    print("Has lanzado una tormenta con ira")
                print("Vida del oponente", enemigo4["vidai"])
            elif x ==3:
                enemigo4["vidai"]-=zeus["fallo_criatura"]
                if zeus["fallo_criatura"] == zeus["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo4["vidai"])
        
            elif x ==4:
                enemigo4["vidai"]-=zeus["fallo_campo"]
                if zeus["fallo_campo"] == zeus["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo4["vidai"])
    
            elif x ==5:
                enemigo4["vidai"]-=zeus["falloco"]
                if zeus["falloco"] == zeus["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo4["vidai"])
            elif x ==6:
                enemigo4["vidai"]-=zeus["fallodo"]
                if zeus["fallodo"] == zeus["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo4["vidai"])
            elif x ==7:
                zeus["vida"] += 300
                print("+300 vida")
            
            if dañoi == 150 or dañoi == 175 or dañoi == 200 or dañoi == 225 or dañoi == 250 or dañoi == 300 :
                print("El oponente a invocado un perro infernal y te a quitado",dañoi)
            elif dañoi == 180 or dañoi == 210 or dañoi == 240 or dañoi == 270 or dañoi == 300 or dañoi == 360 :
                print("El oponente a invocado un duende y te a quitado",dañoi)
            elif dañoi == 240 or dañoi == 280 or dañoi == 320 or dañoi == 360 or dañoi == 400 or dañoi == 480 :
                print("El oponente a invocado multiples lagartijas de otro mundo y te a quitado",dañoi)
            elif dañoi == 300 or dañoi == 350 or dañoi == 400 or dañoi == 450 or dañoi == 500 or dañoi == 600 :
                print("El oponente a invocado un ogro y te a quitado",dañoi)
            elif dañoi == 270 or dañoi == 315 or dañoi == 360 or dañoi == 405 or dañoi == 450 or dañoi == 540 :
                print("El oponente a invocado un jabali y te a quitado",dañoi)
            elif dañoi == 360 or dañoi == 420 or dañoi == 480 or dañoi == 540 or dañoi == 600 or dañoi == 720 :
                print("El oponente a invocado un minotauro y te a quitado",dañoi)
            elif dañoi == 450 or dañoi == 525 or dañoi == 600 or dañoi == 675 or dañoi == 750 or dañoi == 900 :
                print("El oponente a invocado un dragon y te a quitado",dañoi)
            elif dañoi == 600 or dañoi == 700 or dañoi == 800 or dañoi == 900 or dañoi == 1000 or dañoi == 1200 :
                print("El oponente a invocado una hidra y te a quitado",dañoi)


            zeus["vida"] - dañoi
            zeus["copias"]=zeus[random.choice(["rayo","tormenta","rayo_curativo","Criatura_de_saturno","Campo_electrico","fallo","Control_del_clima","Dominio_de_energia"])]    
            zeus["rayos"] = zeus[random.choice(["rayo", "rayo_critico"])]
            zeus["fallo_rayo"] = zeus[random.choice(["rayos", "fallo","rayos", "fallo","rayos", "fallo","rayos", "fallo","rayos","ultra_rayo","fallo","rayos", "fallo","super_rayo","rayos","mega_rayo","fallo","rayos", "fallo","rayos", "fallo","rayos", "fallo","super_rayo","super_rayo","mega_rayo"])]
            zeus["fallo_tormenta"] = zeus[random.choice(["tormenta", "fallo","tormenta", "fallo","tormenta", "fallo","tormenta", "fallo","tormenta_de_ira"])]
            zeus["fallo_criatura"] = zeus[random.choice(["Criatura_de_saturno", "fallo"])]
            zeus["fallo_campo"] = zeus[random.choice(["Campo_electrico", "fallo"])]
            zeus["fallodo"]= zeus[random.choice(["Dominio_de_energia","fallo"])]
            zeus["falloco"]= zeus[random.choice(["Control_del_clima","fallo"])]
            enemigo4["danoi"] = enemigo4[random.choice(["perro_infernal", "ogro","jabali","minotauro","dragon","falloi","duende","lagartija_multiple","Hidra"])]
            enemigo4["danoi"] = enemigo4[random.choice(["perro_infernal", "ogro","jabali","minotauro","dragon","falloi","duende","lagartija_multiple","Hidra"])]
            enemigo4["danoi"] = enemigo4[random.choice(["perro_infernal", "ogro","jabali","minotauro","dragon","falloi","duende","lagartija_multiple","Hidra"])]
            
            if zeus["vida"] <= 0:
                print("¡Perdiste!")
                bool_valuei = False
            elif enemigo4["vidai"] <= 0:
                bool_valuei = False
    premio1 = ""
    premio2 = ""
    premio3 = ""
    premio4 = ""
    premio5 =""
    premio6 = ""
    premio7 = ""
    premio8 = ""



    if zeus["vida"] <= 0:
        perdiste = pyfiglet.figlet_format("¡Perdiste!")
        print(perdiste)
    elif enemigo4["vidai"] <= 0:
        ganaste = pyfiglet.figlet_format("¡Felicitaciones Ganaste!")
        print(ganaste)
        medallas = pyfiglet.figlet_format("Tus Medallas")
        print(medallas)
        if zeus["vida"] >= 25000 :
            premio8 = climage.convert("Maestro.png", width=30)
            print(premio8)
        if zeus["vida"] >= 20000:
            premio7 = climage.convert("Heroe.png", width=30)
            print(premio7)
        if zeus["vida"] >= 15000:
            premio6 = climage.convert("Esmeralda.png", width=30)
            print(premio6)
        if zeus["vida"] >= 12000:
            premio5 = climage.convert("Diamante.png", width=30)
            print(premio5)
        if zeus["vida"] >= 8000 :
            premio4= climage.convert("Platino.png", width=30)
            print(premio4)
        if zeus["vida"] >= 5000:
            premio3 = climage.convert("Oro.png", width=30)
            print(premio3)
        if zeus["vida"] >= 3000 :
            premio2 = climage.convert("Hierro.png", width=30)
            print(premio2)
        if zeus["vida"] >= 1000 or zeus["vida"] <= 1000:
            premio1 = climage.convert("Bronce.png", width=30)
            print(premio1)
    exit()
        
    
            
                   
while cp == 2 :
    
    print(espadachinImage)
    if enemigo1["vidae"] > 0 :
        while bool_value :
            enemigo1["danoe"] = enemigo1[random.choice(["slash", "corte_vertical", "falloe", "triple_slash", "desenvaine_rapido", "doble_corte","corte_perfecto","espada_del_rey"])]
            print("La vida de Khonshu es: ",khonshu["vida"])
            
            print("Poderes\n1-Two mooons (280 daño)\n2-Meteoro lunar (130 daño)\n3-Luna llena (140 daño)\n4-Media luna (70 daño)\n5-Moon fall (150 daño)\n6-piedras lunares (120 daño)\n7-Oz lunar (200 daño)\n8-Vida de otras lunas(450 vida)")
            x=int(input("{ "))
            if x == 1:
                enemigo1["vidae"] -= khonshu["fallot"]
                if khonshu["fallot"] == khonshu["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo1["vidae"])
            elif x ==2:
                enemigo1["vidae"] -= khonshu["fallome"]
                if khonshu["fallom"] == khonshu["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo1["vidae"])
            elif x ==3:
                enemigo1["vidae"] -= khonshu["fallol"]
                if khonshu["fallol"] == khonshu["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo1["vidae"])
            elif x ==4:
                enemigo1["vidae"] -= khonshu["falloml"]
                if khonshu["falloml"] == khonshu["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo1["vidae"])
        
            elif x ==5:
                enemigo1["vidae"] -= khonshu["fallomf"]
                if khonshu["falloml"] == khonshu["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo1["vidae"])
            elif x ==6:
                enemigo1["vidae"] -= khonshu["fallop"]
                if khonshu["fallop"] == khonshu["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo1["vidae"])
            elif x ==7:
                enemigo1["vidae"] -= khonshu["falloozl"]
                if khonshu["falloozl"] == khonshu["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo1["vidae"])
            elif x == 8:
                khonshu["vida"] += 450
                print("+450 vida ")
            
            
            
            if daño == 45 or daño == 60 :
                print("El oponente ha utilizado (slash) y te ha quitado",daño,"de vida")
            elif daño == 90 or daño == 120:
                print("El oponente ha utilizado (corte vertical) y te ha quitado",daño,"de vida")
            elif daño == 0:
                print("El enemigo ha fallado")
            elif daño == 135 or daño == 180:
                print("El oponente ha utilizado (triple slash) y te ha quitado",daño,"de vida")
            elif daño == 105 or daño == 140:
                print("El oponente ha utilizado (desenvaine rápido) y te ha quitado",daño,"de vida")
            elif daño == 180 or daño == 240:
                print("El oponente ha utilizado (doble corte) y te ha quitado",daño,"de vida")
            elif daño == 150 or daño == 200:
                print("El oponente ha hecho un corte perfecto y te a quitado",daño,"de vida")
            elif daño == 127.5 or daño == 170:
                print("El oponente ha utilizado la espada del rey y te ha quitado",daño,"de vida")
            elif daño == 165 or daño == 220:
                print("El oponente ha utilizado el haki del rey y te a quitado",daño,"de vida")
            khonshu["vida"] -= daño
        
        

            khonshu["fallot"]= khonshu[random.choice(["Two_moons","fallo"])]
            khonshu["fallome"]= khonshu[random.choice(["Meteoro_lunar","fallo"])]
            khonshu["fallol"]= khonshu[random.choice(["Luna_llena","fallo"])]
            khonshu["falloml"]=khonshu[random.choice(["Media_luna","fallo"])]
            khonshu["fallomf"]= khonshu[random.choice(["Moon_fall","fallo"])]
            khonshu["fallop"]= khonshu[random.choice(["Piedras_lunares","fallo"])]
            khonshu["falloozl"]= khonshu[random.choice(["Oz_lunar","fallo"])]
            enemigo1["danoe"] = enemigo1[random.choice(["slash", "corte_vertical", "falloe", "triple_slash", "desenvaine_rapido", "doble_corte","corte_perfecto","espada_del_rey"])]

            if khonshu["vida"] <= 0:
                print("¡Perdiste!")
                bool_value = False
            elif enemigo1["vidae"] <= 0:
                bool_value = False
    
    print("¡Ganaste contra el espadachin!\n")
    print("Tu siguiente oponente sera:",enemigo2["Nombre"],"-nivel",nivele2)
    print("La vida del oponente es: ",enemigo2["vidam"])
    print(magoImage)
    
    if enemigo2["vidam"] > 0 :

        while bool_valuem :
            enemigo2["danom"] = enemigo2[random.choice(["ataque_magico", "bestia_magica", "fallom","ataque_de_fuego","esfera_oceanica","esfera_carmesi","esfera_oscura","Dominio_del_mana"])]
            
            print("La vida de Khonshu es: ",khonshu["vida"])
            print("Poderes\n1-Two mooons (280 daño)\n2-Meteoro lunar (130 daño)\n3-Luna llena (140 daño)\n4-Media luna (70 daño)\n5-Moon fall (150 daño)\n6-piedras lunares (120 daño)\n7-Oz lunar (200 daño)\n8-Vida de otras lunas(450 vida)")
            x=int(input("{ "))
            if x == 1:
                enemigo2["vidam"] -= khonshu["fallot"]
                if khonshu["fallot"] == khonshu["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo2["vidam"])
            elif x ==2:
                enemigo2["vidae"] -= khonshu["fallome"]
                if khonshu["fallom"] == khonshu["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo2["vidam"])
            elif x ==3:
                enemigo2["vidam"] -= khonshu["fallol"]
                if khonshu["fallol"] == khonshu["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo2["vidam"])
            elif x ==4:
                enemigo2["vidam"] -= khonshu["falloml"]
                if khonshu["falloml"] == khonshu["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo2["vidam"])
        
            elif x ==5:
                enemigo2["vidam"] -= khonshu["fallomf"]
                if khonshu["falloml"] == khonshu["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo2["vidam"])
            elif x ==6:
                enemigo2["vidam"] -= khonshu["fallop"]
                if khonshu["fallop"] == khonshu["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo2["vidam"])
            elif x ==7:
                enemigo2["vidam"] -= khonshu["falloozl"]
                if khonshu["falloozl"] == khonshu["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo2["vidam"])
            elif x == 8:
                khonshu["vida"] += 450
                print("+450 vida ")
                
            print("Mago se a puesto una capa magica +",enemigo2["coraza_magica"])           


                        

            if dañom == 80 or dañom == 100 or dañom == 120 :
                print("El oponente ha utilizado (ataque magico) y te ha quitado",dañom,"de vida")
            elif dañom == 100 or dañom == 125 or dañom == 150:
                print("El oponente ha utilizado (bestia magica) y te ha quitado",dañom,"de vida")
            elif dañom == 0:
                print("El enemigo ha fallado")
            elif dañom == 140 or dañom == 175 or dañom == 210 :
                print("El oponente ha utilizado (ataque de fuego) y te ha quitado",dañom,"de vida")
            elif dañom == 180 or dañom == 225 or dañom == 270:
                print("El oponente ha utilizado (esfera oceanica) y te ha quitado",dañom,"de vida")
            elif dañom == 200 or dañom == 250 or dañom == 300:
                print("El oponente ha utilizado (esfera carmesi) y te ha quitado",dañom,"de vida")
            elif dañom == 220 or dañom == 275 or dañom == 330:
                print("El oponente ha utilizado (esfera oscura) y te a quitado",dañom,"de vida")
            elif dañom == 240 or dañom == 300 or dañom == 360:
                print("El oponente ha utilizado (dominio del mana) y te ha quitado",dañom,"de vida")
              
            khonshu["vida"] -= dañom

            khonshu["fallot"]= khonshu[random.choice(["Two_moons","fallo"])]
            khonshu["fallome"]= khonshu[random.choice(["Meteoro_lunar","fallo"])]
            khonshu["fallol"]= khonshu[random.choice(["Luna_llena","fallo"])]
            khonshu["falloml"]=khonshu[random.choice(["Media_luna","fallo"])]
            khonshu["fallomf"]= khonshu[random.choice(["Moon_fall","fallo"])]
            khonshu["fallop"]= khonshu[random.choice(["Piedras_lunares","fallo"])]
            khonshu["falloozl"]= khonshu[random.choice(["Oz_lunar","fallo"])]
            enemigo2["danom"] = enemigo2[random.choice(["ataque_magico", "bestia_magica", "fallom","ataque_de_fuego","esfera_oceanica","esfera_carmesi","esfera_oscura","Dominio_del_mana"])]
            

            
            if khonshu["vida"] <= 0:
                print("¡Perdiste!")
                bool_valuem = False
            elif enemigo2["vidam"] <= 0:
                bool_valuem = False
    

    print("¡Ganaste contra el mago!\n")
    print("Tu siguiente oponente sera:",enemigo3["Nombre"],"-nivel",nivele3)
    print("La vida del oponente es: ",enemigo3["vidab"])
    print(berserkImage)
    if enemigo3["vidab"] > 0 :
        
        while bool_valueb :
            enemigo3["danob"] = enemigo3[random.choice(["ira", "golpes", "fallob", "ola_golpeante", "Furia_berserker","puño_de_hierro","mi_sangre","cuerpo_carmesi"])]
            print("La vida de Khonshu es: ",khonshu["vida"])
            print("Poderes\n1-Two mooons (280 daño)\n2-Meteoro lunar (130 daño)\n3-Luna llena (140 daño)\n4-Media luna (70 daño)\n5-Moon fall (150 daño)\n6-piedras lunares (120 daño)\n7-Oz lunar (200 daño)\n8-Vida de otras lunas(450 vida)")
            x=int(input("{ "))
            if x == 1:
                enemigo3["vidab"] -= khonshu["fallot"] # Two moons
                if khonshu["fallot"] == khonshu["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo3["vidab"])
            elif x ==2:
                enemigo3["vidae"] -= khonshu["fallome"] # Media luna
                if khonshu["fallob"] == khonshu["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo3["vidab"])
            elif x ==3:
                enemigo3["vidab"] -= khonshu["fallol"] 
                if khonshu["fallol"] == khonshu["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo3["vidab"])
            elif x ==4:
                enemigo3["vidab"] -= khonshu["falloml"]
                if khonshu["falloml"] == khonshu["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo3["vidab"])
        
            elif x ==5:
                enemigo3["vidab"] -= khonshu["fallomf"]
                if khonshu["falloml"] == khonshu["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo3["vidab"])
            elif x ==6:
                enemigo3["vidab"] -= khonshu["fallop"]
                if khonshu["fallop"] == khonshu["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo3["vidab"])
            elif x ==7:
                enemigo3["vidab"] -= khonshu["falloozl"]
                if khonshu["falloozl"] == khonshu["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo3["vidab"])
            elif x == 8:
                khonshu["vida"] += 450
                print("+450 vida ")
                

            
            

            if dañob == 100 or dañob == 120 or dañob == 140 or dañob == 160:
                print("El oponente ha utilizado (ira) y te ha quitado",dañob,"de vida")
            elif dañob == 125 or dañob == 150 or dañob == 175 or dañob == 200:
                print("El oponente ha utilizado (golpes) y te ha quitado",dañob,"de vida")
            elif dañob == 0:
                print("El enemigo ha fallado")
            elif dañob == 150 or dañob == 180 or dañob == 210 or dañob == 240 :
                print("El oponente ha utilizado (ola golpeante) y te ha quitado",dañob,"de vida")
            elif dañob == 187.5 or dañob == 225 or dañob == 262.5 or dañob == 300:
                print("El oponente ha utilizado (furia berserker) y te ha quitado",dañob,"de vida")
            elif dañob == 225 or dañob == 270 or dañob == 315 or dañob == 360:
                print("El oponente ha utilizado (puño de hierro) y te ha quitado",dañob,"de vida")
            elif dañob == 250 or dañob == 300 or dañob == 350 or dañob == 400:
                print("El oponente ha utilizado (sangre berserk) y te a quitado",dañob,"de vida")
            elif dañob == 312.5 or dañob == 375 or dañob == 437.5 or dañob == 500:
                print("El oponente ha utilizado (cuerpo carmesi) y te ha quitado",dañob,"de vida")

            khonshu["vida"] -= dañob

            khonshu["fallot"]= khonshu[random.choice(["Two_moons","fallo"])]
            khonshu["fallome"]= khonshu[random.choice(["Meteoro_lunar","fallo"])]
            khonshu["fallol"]= khonshu[random.choice(["Luna_llena","fallo"])]
            khonshu["falloml"]=khonshu[random.choice(["Media_luna","fallo"])]
            khonshu["fallomf"]= khonshu[random.choice(["Moon_fall","fallo"])]
            khonshu["fallop"]= khonshu[random.choice(["Piedras_lunares","fallo"])]
            khonshu["falloozl"]= khonshu[random.choice(["Oz_lunar","fallo"])]
            enemigo3["danob"] = enemigo3[random.choice(["ira", "golpes", "fallob", "ola_golpeante", "Furia_berserker","puño_de_hierro","mi_sangre","cuerpo_carmesi"])]
            if khonshu["vida"] <= 0:
                print("¡Perdiste!")
                bool_valueb = False
            elif enemigo3["vidab"] <= 0:
                bool_valueb = False
        
    print("¡Ganaste contra el berserk!\n")
    print("Tu siguiente oponente sera:",enemigo4["Nombre"],"-nivel",nivele4)
    print("La vida del oponente es: ",enemigo4["vidai"])
    print(invocadorImage)
    if enemigo4["vidai"] > 0 :
                
        while bool_valuei :
            enemigo4["danoi"] = enemigo4[random.choice(["perro_infernal", "ogro","jabali","minotauro","dragon","falloi","duende","lagartija_multiple","Hidra"])]
            print("La vida de Khonshu es: ",khonshu["vida"])
            print("Poderes\n1-Two mooons (280 daño)\n2-Meteoro lunar (130 daño)\n3-Luna llena (140 daño)\n4-Media luna (70 daño)\n5-Moon fall (150 daño)\n6-piedras lunares (120 daño)\n7-Oz lunar (200 daño)\n8-Vida de otras lunas(450 vida)")
            x=int(input("{ "))
            if x == 1:
                enemigo4["vidai"] -= khonshu["fallot"]
                if khonshu["fallot"] == khonshu["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo4["vidai"])
            elif x ==2:
                enemigo4["vidai"] -= khonshu["fallome"]
                if khonshu["fallom"] == khonshu["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo4["vidai"])
            elif x ==3:
                enemigo4["vidai"] -= khonshu["fallol"]
                if khonshu["fallol"] == khonshu["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo4["vidai"])
            elif x ==4:
                enemigo4["vidai"] -= khonshu["falloml"]
                if khonshu["falloml"] == khonshu["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo4["vidai"])
        
            elif x ==5:
                enemigo4["vidai"] -= khonshu["fallomf"]
                if khonshu["falloml"] == khonshu["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo4["vidai"])
            elif x ==6:
                enemigo4["vidai"] -= khonshu["fallop"]
                if khonshu["fallop"] == khonshu["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo4["vidai"])
            elif x ==7:
                enemigo4["vidai"] -= khonshu["falloozl"]
                if khonshu["falloozl"] == khonshu["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo4["vidai"])
            elif x == 8:
                khonshu["vida"] += 450
                print("+450 vida ")
               
            
            if dañoi == 150 or dañoi == 175 or dañoi == 200 or dañoi == 225 or dañoi == 250 or dañoi == 300 :
                print("El oponente a invocado un perro infernal y te a quitado",dañoi)
            elif dañoi == 180 or dañoi == 210 or dañoi == 240 or dañoi == 270 or dañoi == 300 or dañoi == 360 :
                print("El oponente a invocado un duende y te a quitado",dañoi)
            elif dañoi == 240 or dañoi == 280 or dañoi == 320 or dañoi == 360 or dañoi == 400 or dañoi == 480 :
                print("El oponente a invocado multiples lagartijas de otro mundo y te a quitado",dañoi)
            elif dañoi == 300 or dañoi == 350 or dañoi == 400 or dañoi == 450 or dañoi == 500 or dañoi == 600 :
                print("El oponente a invocado un ogro y te a quitado",dañoi)
            elif dañoi == 270 or dañoi == 315 or dañoi == 360 or dañoi == 405 or dañoi == 450 or dañoi == 540 :
                print("El oponente a invocado un jabali y te a quitado",dañoi)
            elif dañoi == 360 or dañoi == 420 or dañoi == 480 or dañoi == 540 or dañoi == 600 or dañoi == 720 :
                print("El oponente a invocado un minotauro y te a quitado",dañoi)
            elif dañoi == 450 or dañoi == 525 or dañoi == 600 or dañoi == 675 or dañoi == 750 or dañoi == 900 :
                print("El oponente a invocado un dragon y te a quitado",dañoi)
            elif dañoi == 600 or dañoi == 700 or dañoi == 800 or dañoi == 900 or dañoi == 1000 or dañoi == 1200 :
                print("El oponente a invocado una hidra y te a quitado",dañoi)

            khonshu["vida"] -= dañoi

            khonshu["fallot"]= khonshu[random.choice(["Two_moons","fallo"])]
            khonshu["fallome"]= khonshu[random.choice(["Meteoro_lunar","fallo"])]
            khonshu["fallol"]= khonshu[random.choice(["Luna_llena","fallo"])]
            khonshu["falloml"]=khonshu[random.choice(["Media_luna","fallo"])]
            khonshu["fallomf"]= khonshu[random.choice(["Moon_fall","fallo"])]
            khonshu["fallop"]= khonshu[random.choice(["Piedras_lunares","fallo"])]
            khonshu["falloozl"]= khonshu[random.choice(["Oz_lunar","fallo"])]
            enemigo4["danoi"] = enemigo4[random.choice(["perro_infernal", "ogro","jabali","minotauro","dragon","falloi","duende","lagartija_multiple","Hidra"])]

            if khonshu["vida"] <= 0:
                print("¡Perdiste!")
                bool_valuei = False
            elif enemigo4["vidai"] <= 0:
                bool_valuei = False



    if khonshu["vida"] <= 0 :
        perdiste = pyfiglet.figlet_format("¡Perdiste!")
        print(perdiste)
    elif enemigo4["vidai"] <= 0:    
        ganaste = pyfiglet.figlet_format("¡Felicitaciones Ganaste!")
        print(ganaste)
        medallas = pyfiglet.figlet_format("Tus Medallas")
        print(medallas)
        if khonshu["vida"] >= 25000 :
            premio8 = climage.convert("Maestro.png", width=30)
            print(premio8)
        if khonshu["vida"] >= 20000:
            premio7 = climage.convert("Heroe.png", width=30)
            print(premio7)
        if khonshu["vida"] >= 15000:
            premio6 = climage.convert("Esmeralda.png", width=30)
            print(premio6)
        if khonshu["vida"] >= 12000:
            premio5 = climage.convert("Diamante.png", width=30)
            print(premio5)
        if khonshu["vida"] >= 8000 :
            premio4= climage.convert("Platino.png", width=30)
            print(premio4)
        if khonshu["vida"] >= 5000:
            premio3 = climage.convert("Oro.png", width=30)
            print(premio3)
        if khonshu["vida"] >= 3000 :
            premio2 = climage.convert("Hierro.png", width=30)
            print(premio2)
        if khonshu["vida"] >= 1000 or khonshu["vida"] <= 1000 :
            premio1 = climage.convert("Bronce.png", width=30)
            print(premio1)
    exit()



while cp == 3:   
    
    print(espadachinImage)
    if enemigo1["vidae"] > 0 :
        while bool_value :
            enemigo1["danoe"] = enemigo1[random.choice(["slash", "corte_vertical", "falloe", "triple_slash", "desenvaine_rapido", "doble_corte","corte_perfecto","espada_del_rey"])]

            print("La vida de Anubis es: ",anubis["vida"],"\n")
            
            print("Poderes\n1-Tumba del rey(70 daño)\n2-Ejercito de muertos(80 daño)\n3-Hacha de Muerte(250 daño)\n4-Apocalipsis Final(60 daño)\n5-Almas Perdidas(40 daño)\n6-Poder Prestado(110)\n7-Muerte(400 daño)\n8-Oz de muerte(350 daño)\n9-Tomar vidas(600 vida)")
            x=int(input("{ "))
            if x == 1:
                enemigo1["vidae"] -= anubis["fallotr"]
                if anubis["fallotr"] == anubis["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo1["vidae"])
            elif x ==2:
                enemigo1["vidae"]-= anubis["falloem"]
                if anubis["falloem"] == anubis["fallo"] :  
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo1["vidae"])
            elif x ==3:
                enemigo1["vidae"]-= anubis["fallohm"]
                if anubis["fallohm"] == anubis["fallo"] :
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo1["vidae"])
        
            elif x ==4:
                enemigo1["vidae"]-= anubis["falloaf"]
                if anubis["falloaf"] == anubis["fallo"] :
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo1["vidae"])      
            elif x ==5:
                enemigo1["vidae"]-= anubis["falloap"]
                if anubis["falloap"] == anubis["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo1["vidae"])
            elif x ==6:
                enemigo1["vidae"]-= anubis["fallopp"]
                if anubis["fallopp"] == anubis["fallo"] :
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo1["vidae"])
            elif x ==7:
                enemigo1["vidae"] -= anubis["fallomt"]
                if anubis["fallomt"] == anubis["fallo"] :
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo1["vidae"])
            elif x ==8:
                enemigo1["vidae"] -= anubis["fallooz"]
                if anubis["fallooz"] == anubis["fallo"] :
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo1["vidae"])
                
            elif x ==9:
                anubis["vida"] += 600
                print("+600 vida")
            
            
            if daño == 45 or daño == 60 :
                print("El oponente ha utilizado (slash) y te ha quitado",daño,"de vida")
            elif daño == 90 or daño == 120:
                print("El oponente ha utilizado (corte vertical) y te ha quitado",daño,"de vida")
            elif daño == 0:
                print("El enemigo ha fallado")
            elif daño == 135 or daño == 180:
                print("El oponente ha utilizado (triple slash) y te ha quitado",daño,"de vida")
            elif daño == 105 or daño == 140:
                print("El oponente ha utilizado (desenvaine rápido) y te ha quitado",daño,"de vida")
            elif daño == 180 or daño == 240:
                print("El oponente ha utilizado (doble corte) y te ha quitado",daño,"de vida")
            elif daño == 150 or daño == 200:
                print("El oponente ha hecho un corte perfecto y te a quitado",daño,"de vida")
            elif daño == 127.5 or daño == 170:
                print("El oponente ha utilizado la espada del rey y te ha quitado",daño,"de vida")
            elif daño == 165 or daño == 220:
                print("El oponente ha utilizado el haki del rey y te a quitado",daño,"de vida")
            anubis["vida"] -= daño
        
        

            anubis["fallotr"]= anubis[random.choice(["Tumba_del_rey","fallo"])]
            anubis["falloem"]= anubis[random.choice(["Ejercito_de_muertos","fallo"])]
            anubis["fallohm"]= anubis[random.choice(["Hacha_de_muerte","fallo","Hacha_de_muerte","fallo","Hacha_de_muerte","fallo","Hacha_de_muerte","fallo","Hacha_de_muerte","fallo","triple_hacha"])]
            anubis["falloaf"]= anubis[random.choice(["Apocalipsis_final","fallo"])]
            anubis["falloap"]= anubis[random.choice(["Almas_perdidas","fallo"])]
            anubis["fallopp"]= anubis[random.choice(["Poder_prestado","fallo"])]
            anubis["fallomt"]= anubis[random.choice(["Muerte","fallo","Muerte","fallo","Muerte","fallo","Muerte","fallo","Muerte","fallo","Muerte","fallo","Muerte","fallo","lluvia_de_muerte"])]
            anubis["fallooz"]= anubis[random.choice(["Oz_de_muerte","fallo","Oz_de_muerte","fallo","Oz_de_muerte","fallo","Oz_de_muerte","fallo","Oz_de_muerte","fallo","Oz_de_muerte","fallo","Doble_oz"])]
            enemigo1["danoe"] = enemigo1[random.choice(["slash", "corte_vertical", "falloe", "triple_slash", "desenvaine_rapido", "doble_corte","corte_perfecto","espada_del_rey"])]

            if zeus["vida"] <= 0:
                print("¡Perdiste!")
                bool_value = False
            elif enemigo1["vidae"] <= 0:
                bool_value = False
    
    print("¡Ganaste contra el espadachin!\n")
    print("Tu siguiente oponente sera:",enemigo2["Nombre"],"-nivel",nivele2)
    print("La vida del oponente es: ",enemigo2["vidam"])
    print(magoImage)
    
    if enemigo2["vidam"] > 0 :

        while bool_valuem :
            enemigo2["danom"] = enemigo2[random.choice(["ataque_magico", "bestia_magica", "fallom","ataque_de_fuego","esfera_oceanica","esfera_carmesi","esfera_oscura","Dominio_del_mana"])]
            
            print("La vida de Anubis es: ",anubis["vida"],"\n")
            print("Poderes\n1-Tumba del rey(70 daño)\n2-Ejercito de muertos(80 daño)\n3-Hacha de Muerte(250 daño)\n4-Apocalipsis Final(60 daño)\n5-Almas Perdidas(40 daño)\n6-Poder Prestado(110)\n7-Muerte(400 daño)\n8-Oz de muerte(350 daño)\n9-Tomar vidas(600 vida)")
            x=int(input("{ "))
            if x == 1:
                enemigo2["vidam"] -= anubis["fallotr"]
                if anubis["fallotr"] == anubis["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo2["vidam"])
            elif x ==2:
                enemigo2["vidam"]-= anubis["falloem"]
                if anubis["falloem"] == anubis["fallo"] :  
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo2["vidam"])
            elif x ==3:
                enemigo2["vidam"]-= anubis["fallohm"]
                if anubis["fallohm"] == anubis["fallo"] :
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo2["vidam"])
        
            elif x ==4:
                enemigo2["vidam"]-= anubis["falloaf"]
                if anubis["falloaf"] == anubis["fallo"] :
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo2["vidam"])      
            elif x ==5:
                enemigo2["vidam"]-= anubis["falloap"]
                if anubis["falloap"] == anubis["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo2["vidam"])
            elif x ==6:
                enemigo2["vidam"]-= anubis["fallopp"]
                if anubis["fallopp"] == anubis["fallo"] :
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo2["vidam"])
            elif x ==7:
                enemigo2["vidam"] -= anubis["fallomt"]
                if anubis["fallomt"] == anubis["fallo"] :
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo2["vidam"])
            elif x ==8:
                enemigo2["vidam"] -= anubis["fallooz"]
                if anubis["fallooz"] == anubis["fallo"] :
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo2["vidam"])
                
            elif x ==9:
                anubis["vida"] += 600
                print("+600 vida")
            
            print("Mago se a puesto una capa magica +",enemigo2["coraza_magica"])           
            if dañom == 80 or dañom == 100 or dañom == 120 :
                print("El oponente ha utilizado (ataque magico) y te ha quitado",dañom,"de vida")
            elif dañom == 100 or dañom == 125 or dañom == 150:
                print("El oponente ha utilizado (bestia magica) y te ha quitado",dañom,"de vida")
            elif dañom == 0:
                print("El enemigo ha fallado")
            elif dañom == 140 or dañom == 175 or dañom == 210 :
                print("El oponente ha utilizado (ataque de fuego) y te ha quitado",dañom,"de vida")
            elif dañom == 180 or dañom == 225 or dañom == 270:
                print("El oponente ha utilizado (esfera oceanica) y te ha quitado",dañom,"de vida")
            elif dañom == 200 or dañom == 250 or dañom == 300:
                print("El oponente ha utilizado (esfera carmesi) y te ha quitado",dañom,"de vida")
            elif dañom == 220 or dañom == 275 or dañom == 330:
                print("El oponente ha utilizado (esfera oscura) y te a quitado",dañom,"de vida")
            elif dañom == 240 or dañom == 300 or dañom == 360:
                print("El oponente ha utilizado (dominio del mana) y te ha quitado",dañom,"de vida")
              

            anubis["vida"] -= dañom
            anubis["fallotr"]= anubis[random.choice(["Tumba_del_rey","fallo"])]
            anubis["falloem"]= anubis[random.choice(["Ejercito_de_muertos","fallo"])]
            anubis["fallohm"]= anubis[random.choice(["Hacha_de_muerte","fallo","Hacha_de_muerte","fallo","Hacha_de_muerte","fallo","Hacha_de_muerte","fallo","Hacha_de_muerte","fallo","triple_hacha"])]
            anubis["falloaf"]= anubis[random.choice(["Apocalipsis_final","fallo"])]
            anubis["falloap"]= anubis[random.choice(["Almas_perdidas","fallo"])]
            anubis["fallopp"]= anubis[random.choice(["Poder_prestado","fallo"])]
            anubis["fallomt"]= anubis[random.choice(["Muerte","fallo","Muerte","fallo","Muerte","fallo","Muerte","fallo","Muerte","fallo","Muerte","fallo","Muerte","fallo","lluvia_de_muerte"])]
            anubis["fallooz"]= anubis[random.choice(["Oz_de_muerte","fallo","Oz_de_muerte","fallo","Oz_de_muerte","fallo","Oz_de_muerte","fallo","Oz_de_muerte","fallo","Oz_de_muerte","fallo","Doble_oz"])]
            enemigo2["danom"] = enemigo2[random.choice(["ataque_magico", "bestia_magica", "fallom","ataque_de_fuego","esfera_oceanica","esfera_carmesi","esfera_oscura","Dominio_del_mana"])]
            

            
            if anubis["vida"] <= 0:
                print("¡Perdiste!")
                bool_valuem = False
            elif enemigo2["vidam"] <= 0:
                bool_valuem = False
    

    print("¡Ganaste contra el mago!\n")
    print("Tu siguiente oponente sera:",enemigo3["Nombre"],"-nivel",nivele3)
    print("La vida del oponente es: ",enemigo3["vidab"])
    print(berserkImage)
    if enemigo3["vidab"] > 0 :
        
        while bool_valueb :
            enemigo3["danob"] = enemigo3[random.choice(["ira", "golpes", "fallob", "ola_golpeante", "Furia_berserker","puño_de_hierro","mi_sangre","cuerpo_carmesi"])]
            print("La vida de Anubis es: ",anubis["vida"],"\n")
            print("Poderes\n1-Tumba del rey(70 daño)\n2-Ejercito de muertos(80 daño)\n3-Hacha de Muerte(250 daño)\n4-Apocalipsis Final(60 daño)\n5-Almas Perdidas(40 daño)\n6-Poder Prestado(110)\n7-Muerte(400 daño)\n8-Oz de muerte(350 daño)\n9-Tomar vidas(600 vida)")
            x=int(input("{ "))
            
            if x == 1:
                enemigo3["vidab"] -= anubis["fallotr"]
                if anubis["fallotr"] == anubis["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo3["vidab"])
            elif x ==2:
                enemigo3["vidab"]-= anubis["falloem"]
                if anubis["falloem"] == anubis["fallo"] :  
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo3["vidab"])
            elif x ==3:
                enemigo3["vidab"]-= anubis["fallohm"]
                if anubis["fallohm"] == anubis["fallo"] :
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo3["vidab"])
        
            elif x ==4:
                enemigo3["vidab"]-= anubis["falloaf"]
                if anubis["falloaf"] == anubis["fallo"] :
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo3["vidab"])      
            elif x ==5:
                enemigo3["vidab"]-= anubis["falloap"]
                if anubis["falloap"] == anubis["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo3["vidab"])
            elif x ==6:
                enemigo3["vidab"]-= anubis["fallopp"]
                if anubis["fallopp"] == anubis["fallo"] :
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo3["vidab"])
            elif x ==7:
                enemigo3["vidab"] -= anubis["fallomt"]
                if anubis["fallomt"] == anubis["fallo"] :
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo3["vidab"])
            elif x ==8:
                enemigo3["vidab"] -= anubis["fallooz"]
                if anubis["fallooz"] == anubis["fallo"] :
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo3["vidab"])
                
            elif x ==9:
                anubis["vida"] += 600
                print("+600 vida")
            
            
            

            if dañob == 100 or dañob == 120 or dañob == 140 or dañob == 160:
                print("El oponente ha utilizado (ira) y te ha quitado",dañob,"de vida")
            elif dañob == 125 or dañob == 150 or dañob == 175 or dañob == 200:
                print("El oponente ha utilizado (golpes) y te ha quitado",dañob,"de vida")
            elif dañob == 0:
                print("El enemigo ha fallado")
            elif dañob == 150 or dañob == 180 or dañob == 210 or dañob == 240 :
                print("El oponente ha utilizado (ola golpeante) y te ha quitado",dañob,"de vida")
            elif dañob == 187.5 or dañob == 225 or dañob == 262.5 or dañob == 300:
                print("El oponente ha utilizado (furia berserker) y te ha quitado",dañob,"de vida")
            elif dañob == 225 or dañob == 270 or dañob == 315 or dañob == 360:
                print("El oponente ha utilizado (puño de hierro) y te ha quitado",dañob,"de vida")
            elif dañob == 250 or dañob == 300 or dañob == 350 or dañob == 400:
                print("El oponente ha utilizado (sangre berserk) y te a quitado",dañob,"de vida")
            elif dañob == 312.5 or dañob == 375 or dañob == 437.5 or dañob == 500:
                print("El oponente ha utilizado (cuerpo carmesi) y te ha quitado",dañob,"de vida")

            anubis["vida"] -= dañob
            anubis["fallotr"]= anubis[random.choice(["Tumba_del_rey","fallo"])]
            anubis["falloem"]= anubis[random.choice(["Ejercito_de_muertos","fallo"])]
            anubis["fallohm"]= anubis[random.choice(["Hacha_de_muerte","fallo","Hacha_de_muerte","fallo","Hacha_de_muerte","fallo","Hacha_de_muerte","fallo","Hacha_de_muerte","fallo","triple_hacha"])]
            anubis["falloaf"]= anubis[random.choice(["Apocalipsis_final","fallo"])]
            anubis["falloap"]= anubis[random.choice(["Almas_perdidas","fallo"])]
            anubis["fallopp"]= anubis[random.choice(["Poder_prestado","fallo"])]
            anubis["fallomt"]= anubis[random.choice(["Muerte","fallo","Muerte","fallo","Muerte","fallo","Muerte","fallo","Muerte","fallo","Muerte","fallo","Muerte","fallo","lluvia_de_muerte"])]
            anubis["fallooz"]= anubis[random.choice(["Oz_de_muerte","fallo","Oz_de_muerte","fallo","Oz_de_muerte","fallo","Oz_de_muerte","fallo","Oz_de_muerte","fallo","Oz_de_muerte","fallo","Doble_oz"])]
            enemigo3["danob"] = enemigo3[random.choice(["ira", "golpes", "fallob", "ola_golpeante", "Furia_berserker","puño_de_hierro","mi_sangre","cuerpo_carmesi"])]
            if anubis["vida"] <= 0:
                print("¡Perdiste!")
                bool_valueb = False
            elif enemigo3["vidab"] <= 0:
                bool_valueb = False
        
    print("¡Ganaste contra el berserk!\n")
    print("Tu siguiente oponente sera:",enemigo4["Nombre"],"-nivel",nivele4)
    print("La vida del oponente es: ",enemigo4["vidai"])
    print(invocadorImage)
    if enemigo4["vidai"] > 0 :
                
        while bool_valuei :
            enemigo4["danoi"] = enemigo4[random.choice(["perro_infernal", "ogro","jabali","minotauro","dragon","falloi","duende","lagartija_multiple","Hidra"])]

            print("La vida de Anubis es: ",anubis["vida"],"\n")
            print("Poderes\n1-Tumba del rey(70 daño)\n2-Ejercito de muertos(80 daño)\n3-Hacha de Muerte(250 daño)\n4-Apocalipsis Final(60 daño)\n5-Almas Perdidas(40 daño)\n6-Poder Prestado(110)\n7-Muerte(400 daño)\n8-Oz de muerte(350 daño)\n9-Tomar vidas(600 vida)")
            x=int(input("{ "))
            
            if x == 1:
                enemigo4["vidai"] -= anubis["fallotr"]
                if anubis["fallotr"] == anubis["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo4["vidai"])
            elif x ==2:
                enemigo4["vidai"]-= anubis["falloem"]
                if anubis["falloem"] == anubis["fallo"] :  
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo4["vidai"])
            elif x ==3:
                enemigo4["vidai"]-= anubis["fallohm"]
                if anubis["fallohm"] == anubis["fallo"] :
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo4["vidai"])
        
            elif x ==4:
                enemigo4["vidai"]-= anubis["falloaf"]
                if anubis["falloaf"] == anubis["fallo"] :
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo4["vidai"])      
            elif x ==5:
                enemigo4["vidai"]-= anubis["falloap"]
                if anubis["falloap"] == anubis["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo4["vidai"])
            elif x ==6:
                enemigo4["vidai"]-= anubis["fallopp"]
                if anubis["fallopp"] == anubis["fallo"] :
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo4["vidai"])
            elif x ==7:
                enemigo4["vidai"] -= anubis["fallomt"]
                if anubis["fallomt"] == anubis["fallo"] :
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo4["vidai"])
            elif x ==8:
                enemigo4["vidai"] -= anubis["fallooz"]
                if anubis["fallooz"] == anubis["fallo"] :
                    print("¡Fallaste!")
                print("Vida del oponente",enemigo4["vidai"])
                
            elif x ==9:
                anubis["vida"] += 600
                print("+600 vida")
            

            if dañoi == 150 or dañoi == 175 or dañoi == 200 or dañoi == 225 or dañoi == 250 or dañoi == 300 :
                print("El oponente a invocado un perro infernal y te a quitado",dañoi)
            elif dañoi == 180 or dañoi == 210 or dañoi == 240 or dañoi == 270 or dañoi == 300 or dañoi == 360 :
                print("El oponente a invocado un duende y te a quitado",dañoi)
            elif dañoi == 240 or dañoi == 280 or dañoi == 320 or dañoi == 360 or dañoi == 400 or dañoi == 480 :
                print("El oponente a invocado multiples lagartijas de otro mundo y te a quitado",dañoi)
            elif dañoi == 300 or dañoi == 350 or dañoi == 400 or dañoi == 450 or dañoi == 500 or dañoi == 600 :
                print("El oponente a invocado un ogro y te a quitado",dañoi)
            elif dañoi == 270 or dañoi == 315 or dañoi == 360 or dañoi == 405 or dañoi == 450 or dañoi == 540 :
                print("El oponente a invocado un jabali y te a quitado",dañoi)
            elif dañoi == 360 or dañoi == 420 or dañoi == 480 or dañoi == 540 or dañoi == 600 or dañoi == 720 :
                print("El oponente a invocado un minotauro y te a quitado",dañoi)
            elif dañoi == 450 or dañoi == 525 or dañoi == 600 or dañoi == 675 or dañoi == 750 or dañoi == 900 :
                print("El oponente a invocado un dragon y te a quitado",dañoi)
            elif dañoi == 600 or dañoi == 700 or dañoi == 800 or dañoi == 900 or dañoi == 1000 or dañoi == 1200 :
                print("El oponente a invocado una hidra y te a quitado",dañoi)

            anubis["vida"] -= dañoi

            anubis["fallotr"]= anubis[random.choice(["Tumba_del_rey","fallo"])]
            anubis["falloem"]= anubis[random.choice(["Ejercito_de_muertos","fallo"])]
            anubis["fallohm"]= anubis[random.choice(["Hacha_de_muerte","fallo","Hacha_de_muerte","fallo","Hacha_de_muerte","fallo","Hacha_de_muerte","fallo","Hacha_de_muerte","fallo","triple_hacha"])]
            anubis["falloaf"]= anubis[random.choice(["Apocalipsis_final","fallo"])]
            anubis["falloap"]= anubis[random.choice(["Almas_perdidas","fallo"])]
            anubis["fallopp"]= anubis[random.choice(["Poder_prestado","fallo"])]
            anubis["fallomt"]= anubis[random.choice(["Muerte","fallo","Muerte","fallo","Muerte","fallo","Muerte","fallo","Muerte","fallo","Muerte","fallo","Muerte","fallo","lluvia_de_muerte"])]
            anubis["fallooz"]= anubis[random.choice(["Oz_de_muerte","fallo","Oz_de_muerte","fallo","Oz_de_muerte","fallo","Oz_de_muerte","fallo","Oz_de_muerte","fallo","Oz_de_muerte","fallo","Doble_oz"])]
            enemigo4["danoi"] = enemigo4[random.choice(["perro_infernal", "ogro","jabali","minotauro","dragon","falloi","duende","lagartija_multiple","Hidra"])]
            
            if anubis["vida"] <= 0:
                print("¡Perdiste!")
                bool_valuei = False
            elif enemigo4["vidai"] <= 0:
                bool_valuei = False
    premio1 = ""
    premio2 = ""
    premio3 = ""
    premio4 = ""
    premio5 =""
    premio6 = ""
    premio7 = ""
    premio8 = ""


    if anubis["vida"] <= 0:
        perdiste = pyfiglet.figlet_format("¡Perdiste!")
        print(perdiste)
    elif enemigo4["vidai"] <= 0:
        ganaste = pyfiglet.figlet_format("¡Felicitaciones Ganaste!")
        print(ganaste)
        medallas = pyfiglet.figlet_format("Tus Medallas")
        print(medallas)
        if anubis["vida"] >= 25000 :
            premio8 = climage.convert("Maestro.png", width=30)
            print(premio8)
        if anubis["vida"] >= 20000:
            premio7 = climage.convert("Heroe.png", width=30)
            print(premio7)
        if anubis["vida"] >= 15000:
            premio6 = climage.convert("Esmeralda.png", width=30)
            print(premio6)
        if anubis["vida"] >= 12000:
            premio5 = climage.convert("Diamante.png", width=30)
            print(premio5)
        if anubis["vida"] >= 8000 :
            premio4= climage.convert("Platino.png", width=30)
            print(premio4)
        if anubis["vida"] >= 5000:
            premio3 = climage.convert("Oro.png", width=30)
            print(premio3)
        if anubis["vida"] >= 3000 :
            premio2 = climage.convert("Hierro.png", width=30)
            print(premio2)
        if anubis["vida"] >= 1000 or anubis["vida"] <= 1000:
            premio1 = climage.convert("Bronce.png", width=30)
            print(premio1)
    exit()


print()
print("Batalla finalizada")