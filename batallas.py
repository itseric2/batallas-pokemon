#Batallas seguidas
import climage
import random
zeus= {
        "Nombre": "Zeus",
        "vida": random.randint(800, 1000),
        "rayo": 60,
        "tormenta": 80,
        "rayo_critico": 120,
        "Criatura_de_saturno": 100,
        "Campo_electrico": 120,
        "Control_del_clima":140,
        "Dominio_de_energia":1700,
        "fallo": 0,
        "rayo_curativo":0        
    }
zeus["copias"]=zeus[random.choice(["rayo","tormenta","rayo_curativo","Criatura_de_saturno","Campo_electrico","fallo","Control_del_clima","Dominio_de_energia"])]    
zeus["rayos"] = zeus[random.choice(["rayo", "rayo_critico"])]
zeus["fallo_rayo"] = zeus[random.choice(["rayos", "fallo"])]
zeus["fallo_tormenta"] = zeus[random.choice(["tormenta", "fallo"])]
zeus["fallo_criatura"] = zeus[random.choice(["Criatura_de_saturno", "fallo"])]
zeus["fallo_campo"] = zeus[random.choice(["Campo_electrico", "fallo"])]
zeus["fallodo"]= zeus[random.choice(["Dominio_de_energia","fallo"])]
zeus["falloco"]= zeus[random.choice(["Control_del_clima","fallo"])]
    
khonshu= {
    "Nombre":"Khonshu",
    "vida":random.randint(800, 2000),
    "Two_moons":60,
    "Meteoro_lunar":70,
    "Luna_llena":100,
    "Media_luna":50,
    "Moon_fall":130,
    "Piedras_lunares":40,
    "Oz_lunar":120,
    "fallo":0
    }
khonshu["fallot"]= khonshu[random.choice(["Two_moons","fallo"])]
khonshu["fallome"]= khonshu[random.choice(["Meteoro_lunar","fallo"])]
khonshu["fallol"]= khonshu[random.choice(["Luna_llena","fallo"])]
khonshu["falloml"]=khonshu[random.choice(["Media_luna","fallo"])]
khonshu["fallomf"]= khonshu[random.choice(["Moon_fall","fallo"])]
khonshu["fallop"]= khonshu[random.choice(["Piedras_lunares","fallo"])]
khonshu["falloozl"]= khonshu[random.choice(["Oz_lunar","fallo"])]
    
anubis= {
    "Nombre":"Anubis",
    "vida":random.randint(800,4000),
    "Tumba_del_rey":70,
    "Ejercito_de_muertos":80,
    "Hacha_de_muerte":90,
    "Apocalipsis_final":60,
    "Almas_perdidas":40,
    "Poder_prestado":110,
    "Muerte":120,
    "fallo":0,
    "Oz_de_muerte":140
    }
anubis["fallotr"]= anubis[random.choice(["Tumba_del_rey","fallo"])]
anubis["falloem"]= anubis[random.choice(["Ejercito_de_muertos","fallo"])]
anubis["fallohm"]= anubis[random.choice(["Hacha_de_muerte","fallo"])]
anubis["falloaf"]= anubis[random.choice(["Apocalipsis_final","fallo"])]
anubis["falloap"]= anubis[random.choice(["Almas_perdidas","fallo"])]
anubis["fallopp"]= anubis[random.choice(["Poder_prestado","fallo"])]
anubis["fallomt"]= anubis[random.choice(["Muerte","fallo"])]
anubis["fallooz"]= anubis[random.choice(["Oz_de_muerte","fallo"])]



import pyfiglet
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
        "vidab": random.randint(4000, 7000),
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
        "vidae": random.randint(700, 2500),
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
        "vidam": random.randint(2600,5000),
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
        "vidai": random.randint(8000, 12000),
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

#  ENEMIGOS ZEUS
espadachinImage = climage.convert('pixil-frame-0.png', width=50)
berserkImage = climage.convert("berserker.png" , width=55)
print("Tu oponente sera:",enemigo1["Nombre"],"-nivel",nivele1)

print("La vida del oponente es: ",enemigo1["vidae"])
print()
if cp == 1 :
    print(espadachinImage)
    if enemigo1["vidae"] > 0 :
        while bool_value :
    
            print("Tu vida es: ",zeus["vida"])
            print("Poderes\n1-Rayo\n2-Tormenta\n3-Criatura de saturno\n4-Campo electrico\n5-Control del clima\n6-Dominio de energia\n7-Rayo curativo")
            x=int(input("{ "))
            if x == 1:
                enemigo1["vidae"] -= zeus["fallo_rayo"]
                if zeus["fallo_rayo"]== zeus["rayo_critico"]:
                    print("Has hecho un critico")
                elif zeus["fallo_rayo"] == zeus["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo1["vidae"])
            elif x ==2:
                enemigo1["vidae"]-=zeus["fallo_tormenta"]
                if zeus["fallo_tormenta"] == zeus["fallo"]:
                    print("¡Fallaste!")
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
                zeus["vida"] += 300000
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
            zeus["fallo_rayo"] = zeus[random.choice(["rayos", "fallo"])]
            zeus["fallo_tormenta"] = zeus[random.choice(["tormenta", "fallo"])]
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
    
    if enemigo2["vidam"] > 0 :
        while bool_valuem :
    
            print("Tu vida es: ",zeus["vida"])
            print("Poderes\n1-Rayo\n2-Tormenta\n3-Criatura de saturno\n4-Campo electrico\n5-Control del clima\n6-Dominio de energia\n7-Rayo curativo")
            x=int(input("{ "))
            if x == 1:
                enemigo2["vidam"] -= zeus["fallo_rayo"]
                if zeus["fallo_rayo"]== zeus["rayo_critico"]:
                    print("Has hecho un critico")
                elif zeus["fallo_rayo"] == zeus["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo2["vidam"])
            elif x ==2:
                enemigo2["vidam"]-=zeus["fallo_tormenta"]
                if zeus["fallo_tormenta"] == zeus["fallo"]:
                    print("¡Fallaste!")
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
            zeus["fallo_rayo"] = zeus[random.choice(["rayos", "fallo"])]
            zeus["fallo_tormenta"] = zeus[random.choice(["tormenta", "fallo"])]
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
            
    if enemigo3["vidab"] > 0 :
        print(berserkImage)
        while bool_valueb :
            
            print("Tu vida es: ",zeus["vida"])
            print("Poderes\n1-Rayo\n2-Tormenta\n3-Criatura de saturno\n4-Campo electrico\n5-Control del clima\n6-Dominio de energia\n7-Rayo curativo")
            x=int(input("{ "))
            if x == 1:
                enemigo2["vidam"] -= zeus["fallo_rayo"]
                if zeus["fallo_rayo"]== zeus["rayo_critico"]:
                    print("Has hecho un critico")
                elif zeus["fallo_rayo"] == zeus["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo2["vidam"])
            elif x ==2:
                enemigo2["vidam"]-=zeus["fallo_tormenta"]
                if zeus["fallo_tormenta"] == zeus["fallo"]:
                    print("¡Fallaste!")
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
            zeus["fallo_rayo"] = zeus[random.choice(["rayos", "fallo"])]
            zeus["fallo_tormenta"] = zeus[random.choice(["tormenta", "fallo"])]
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
    
    if enemigo4["vidai"] > 0 :
                
        while bool_valuei :
    
            print("Tu vida es: ",zeus["vida"])
            print("Poderes\n1-Rayo\n2-Tormenta\n3-Criatura de saturno\n4-Campo electrico\n5-Control del clima\n6-Dominio de energia\n7-Rayo curativo")
            x=int(input("{ "))
            if x == 1:
                enemigo4["vidai"] -= zeus["fallo_rayo"]
                if zeus["fallo_rayo"]== zeus["rayo_critico"]:
                    print("Has hecho un critico")
                elif zeus["fallo_rayo"] == zeus["fallo"]:
                    print("¡Fallaste!")
                print("Vida del oponente", enemigo4["vidai"])
            elif x ==2:
                enemigo4["vidai"]-=zeus["fallo_tormenta"]
                if zeus["fallo_tormenta"] == zeus["fallo"]:
                    print("¡Fallaste!")
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
                enemigo4["vidam"]-=zeus["fallodo"]
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
            zeus["fallo_rayo"] = zeus[random.choice(["rayos", "fallo"])]
            zeus["fallo_tormenta"] = zeus[random.choice(["tormenta", "fallo"])]
            zeus["fallo_criatura"] = zeus[random.choice(["Criatura_de_saturno", "fallo"])]
            zeus["fallo_campo"] = zeus[random.choice(["Campo_electrico", "fallo"])]
            zeus["fallodo"]= zeus[random.choice(["Dominio_de_energia","fallo"])]
            zeus["falloco"]= zeus[random.choice(["Control_del_clima","fallo"])]
            invocador["danoi"] = invocador[random.choice(["perro_infernal", "ogro","jabali","minotauro","dragon","falloi","duende","lagartija_multiple","Hidra"])]
            
            if zeus["vida"] <= 0:
                print("¡Perdiste!")
                bool_valueb = False
            elif enemigo4["vidai"] <= 0:
                bool_valueb = False
    
    ganaste = pyfiglet.figlet_format("¡Felicitaciones Ganaste!")
    print(ganaste)
    if zeus["vida"] >= 15000 or zeus["vida"] >= 15000:
        premio = pyfiglet.figlet_format("Has ganado una medalla de Esmeralda")
    if zeus["vida"] >= 12000 or zeus["vida"] >= 12000:
        pyfiglet.figlet_format("Has ganado una medalla de Diamante")
    if zeus["vida"] <= 8000 or zeus["vida"] >= 8000:
        premio = pyfiglet.figlet_format("Has ganado una medalla de Platino")
    if zeus["vida"] <= 5000 or zeus["vida"] >= 5000:
        pyfiglet.figlet_format("Has ganado una medalla de Oro")
    if zeus["vida"] <= 3000 or zeus["vida"] >= 3000:
        premio = pyfiglet.figlet_format("Has ganado una medalla de Hierro")
    if zeus["vida"] <= 1000 or zeus["vida"] >= 1000:
        pyfiglet.figlet_format("Has ganado una medalla de Bronce")
    
    
        
    
            
                   
while cp == 2 :
    print()
    print("La vida de Khonshu es: ",khonshu["vida"])
    print("Poderes\n1-Two Moons\n2-Meteoro Lunar\n3-Luna Llena\n4-Media Luna\n5-Moon Fall\n6-Piedras Lunares\n6-Oz Lunar\n7-Vida de otras lunas")
        
while cp == 3:   
    print("La vida de Anubis es: ",anubis["vida"],"\n")
    print("Poderes\n1-Tumba del rey\n2-Ejercito de muertos\n3-Hacha de Muerte\n4-Apocalipsis Final\n5-Almas Perdidas\n6-Poder Prestado\n7-Muerte\n8-Oz de muerte\n9-Tomar vidas\n")

print()
print("Batalla finalizada")