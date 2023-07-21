#Batallas seguidas

import random
zeus= {
        "Nombre": "Zeus",
        "vida": random.randint(160, 240),
        "rayo": 40,
        "tormenta": 50,
        "rayo_critico": 80,
        "Criatura_de_saturno": 70,
        "Campo_electrico": 90,
        "Control_del_clima":140,
        "Dominio_de_energia":120,
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
    "vida":random.randint(170, 300),
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
    "vida":random.randint(250,500),
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
    
print("1- Zeus\n2- Khonshu\n3- Anubis")
cp = int(input("Elige tu personaje: "))


# Berserk
def berserk():
    berserk = {
        "Nombre": "berserk",
        "vidab": random.randint(10, 210),
        "ira": 40,
        "golpes": 50,
        "ola_golpeante": 60,
        "Furia_berserker": 75,
        "fallob": 0,
        "puño_de_hierro":90,
        "mi_sangre":100,
        "cuerpo_carmesi":125,
        "nivel1":1,
        "nivel2":2,
        "nivel3":3,
        "nivel4":4
    }
    berserk["danob"] = berserk[random.choice(["ira", "golpes", "fallob", "ola_golpeante", "Furia_berserker","puño_de_hierro","mi_sangre","cuerpo_carmesi"])]
    berserk["niveles"]= berserk[random.choice(["nivel1","nivel2","nivel3","nivel4"])]
    return berserk
# Espadachin
def espadachin():
    espadachin = {
        "Nombre": "espadachin",
        "vidae": random.randint(200, 400),
        "slash": 30,
        "corte_vertical": 60,
        "triple_slash":90 ,
        "desenvaine_rapido": 70,
        "doble_corte": 120,
        "falloe": 0,
        "corte_perfecto":100,
        "espada_del_rey":85,
        "Haki_del_rey":110,
        "nivel1":1,
        "nivel2":2
                
        
    }
    espadachin["danoe"] = espadachin[random.choice(["slash", "corte_vertical", "falloe", "triple_slash", "desenvaine_rapido", "doble_corte","corte_perfecto","espada_del_rey"])]
    espadachin["niveles"]= espadachin[random.choice(["nivel1","nivel2"])]
    return espadachin
# Mago
def mago():
    mago = {
        "Nombre": "mago",
        "vidam": random.randint(500,750),
        "ataque_magico": 40,
        "bestia_magica": 50,
        "fallom": 0,
        "coraza_magica": 30,
        "ataque_de_fuego":70,
        "esfera_oceanica":90,
        "esfera_carmesi":100,
        "esfera_oscura":110,
        "Dominio_del_mana":120,
        "nivel1":1,
        "nivel2":2,
        "nivel3":3
        #"copia":None
    }
    mago["danom"] = mago[random.choice(["ataque_magico", "bestia_magica", "fallom","ataque_de_fuego","esfera_oceanica","esfera_carmesi","esfera_oscura","Dominio_del_mana"#,"copia"
                                        ])]
    mago["niveles"]= mago[random.choice(["nivel1","nivel2","nivel3"])]
    
    return mago
# Invocador
def invocador():
    invocador = {
        "Nombre": "invocador",
        "vidai": random.randint(500, 1000),
        "perro_infernal": 40,
        "duende":50,
        "lagartija_multiple":60,
        "ogro": 90,
        "jabali":70,
        "minotauro":110,
        "dragon":130,
        "Hidra":140,
        "falloi": 0,
        "nivel1":1,
        "nivel2":2,
        "nivel3":3,
        "nivel4":4,
        "nivel5":5,
        "nivel6":6
    }
    invocador["danoi"] = invocador[random.choice(["perro_infernal", "ogro","jabali","minotauro","dragon","falloi","duende","lagartija","Hidra"])]
    invocador["niveles"]= invocador[random.choice(["nivel1","nivel2","nivel3","nivel4","nivel5","nivel6"])]
    return invocador        

print()
enemigo1 = espadachin()
enemigo2 = mago()
enemigo3 = berserk()
enemigo4 = invocador()
bool_value = True
print("Tu oponente sera:",enemigo1["Nombre"],"-nivel",enemigo1["niveles"])

print("La vida del oponente es: ",enemigo1["vidae"])
print()
bool_value = True
if cp == 1 :
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

        
            if enemigo1["niveles"] == enemigo1["nivel1"] :
                enemigo1["danoe"] = enemigo1["danoe"] * 1.5
            elif enemigo1["niveles"] == enemigo1["nivel2"] :
                enemigo1["danoe"] = enemigo1["danoe"] * 2
            daño = enemigo1["danoe"]
            if daño == 45 or daño == 60 :
                print("El oponente ha utilizado (slash) y te ha quitado",enemigo1["danoe"],"de vida")
            elif daño == 90 or daño == 120:
                print("El oponente ha utilizado (corte vertical) y te ha quitado",enemigo1["danoe"],"de vida")
            elif daño == 0:
                print("El enemigo ha fallado")
            elif daño == 135 or daño == 180:
                print("El oponente ha utilizado (triple slash) y te ha quitado",enemigo1["danoe"],"de vida")
            elif daño == 105 or daño == 140:
                print("El oponente ha utilizado (desenvaine rápido) y te ha quitado",enemigo1["danoe"],"de vida")
            elif daño == 180 or daño == 240:
                print("El oponente ha utilizado (doble corte) y te ha quitado",enemigo1["danoe"],"de vida")
            elif daño == 150 or daño == 200:
                print("El oponente ha hecho un corte perfecto y te a quitado",enemigo1["danoe"],"de vida")
            elif daño == 127.5 or daño == 170:
                print("El oponente ha utilizado la espada del rey y te ha quitado",enemigo1["danoe"],"de vida")
            elif daño == 165 or daño == 220:
                print("El oponente ha utilizado el haki del rey y te a quitado",enemigo1["danoe"],"de vida")
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
        print("¡Ganaste contra el espadachin!\n")
        print("Tu siguiente oponente sera:",enemigo2["Nombre"],"-nivel",enemigo2["niveles"])
        print("La vida del oponente es: ",enemigo2["vidam"])
        #copia = zeus["copias"]
        if enemigo2["vidam"] > 0 :
            while bool_value :
    
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
                
                enemigo2["vidam"] += enemigo2["coraza_magica"]
                print("Mago se a puesto una capa magica",enemigo2["coraza_magica"])
                if enemigo2["niveles"] == enemigo2["nivel1"] :
                    enemigo2["danom"] = enemigo2["danom"] * 2
                    enemigo2["coraza_magica"] = enemigo2["coraza_magica"] * 2
                elif enemigo1["niveles"] == enemigo1["nivel2"] :
                    enemigo2["danom"] = enemigo2["danom"] * 2.5
                    enemigo2["coraza_magica"] = enemigo2["coraza_magica"] * 2.5
                elif enemigo2["danom"] == enemigo2["nivel3"]:
                    enemigo2["danom"] = enemigo2["danom"] * 3
                    enemigo2["coraza_magica"] = enemigo2["coraza_magica"] * 3
                dañom = enemigo2["danom"]
                if dañom == 80 or dañom == 100 or dañom == 120 :
                    print("El oponente ha utilizado (ataque magico) y te ha quitado",enemigo1["danoe"],"de vida")
                elif dañom == 100 or dañom == 125 or dañom == 150:
                    print("El oponente ha utilizado (bestia magica) y te ha quitado",enemigo1["danoe"],"de vida")
                elif dañom == 0:
                    print("El enemigo ha fallado")
                elif dañom == 140 or dañom == 175 or dañom == 210 :
                    print("El oponente ha utilizado (ataque de fuego) y te ha quitado",enemigo1["danoe"],"de vida")
                elif dañom == 180 or dañom == 225 or dañom == 270:
                    print("El oponente ha utilizado (esfera oceanica) y te ha quitado",enemigo1["danoe"],"de vida")
                elif dañom == 200 or dañom == 250 or dañom == 300:
                    print("El oponente ha utilizado (esfera carmesi) y te ha quitado",enemigo1["danoe"],"de vida")
                elif dañom == 220 or dañom == 275 or dañom == 330:
                    print("El oponente ha utilizado (esfera oscura) y te a quitado",enemigo1["danoe"],"de vida")
                elif dañom == 240 or dañom == 300 or dañom == 360:
                    print("El oponente ha utilizado (dominio del mana) y te ha quitado",enemigo1["danoe"],"de vida")
                #elif dañom == enemigo1["copia"]:
                    #dañom = copia
                    #print("El mago a copiado un poder tuyo")
                    #if dañom == zeus["rayo"]:
                        #print("Rayo")
                    #elif dañom == zeus["tormenta"]:
                        #print("Tormenta")
                    #elif dañom == zeus["Criatura_de_saturno"]:
                        #print("Criatura de saturno")
                    #if dañom == zeus["Campo_electrico"]:
                        #print("Campo electrico")
                    #elif dañom == zeus["Control_del_clima"]:
                        #print("Control del clima")
                    #elif dañom == zeus["Dominio_de_energia"]:
                        #print("Dominio de energia")
                     
                    
                zeus["vida"] -= dañom
                zeus["copias"]=zeus[random.choice(["rayo","tormenta","rayo_curativo","Criatura_de_saturno","Campo_electrico","fallo","Control_del_clima","Dominio_de_energia"])]    
                zeus["rayos"] = zeus[random.choice(["rayo", "rayo_critico"])]
                zeus["fallo_rayo"] = zeus[random.choice(["rayos", "fallo"])]
                zeus["fallo_tormenta"] = zeus[random.choice(["tormenta", "fallo"])]
                zeus["fallo_criatura"] = zeus[random.choice(["Criatura_de_saturno", "fallo"])]
                zeus["fallo_campo"] = zeus[random.choice(["Campo_electrico", "fallo"])]
                zeus["fallodo"]= zeus[random.choice(["Dominio_de_energia","fallo"])]
                zeus["falloco"]= zeus[random.choice(["Control_del_clima","fallo"])]
                mago["danom"] = mago[random.choice(["ataque_magico", "bestia_magica", "fallom","ataque_de_fuego","esfera_oceanica","esfera_carmesi","esfera_oscura","Dominio_del_mana"#,"copia"
                                        ])]
                if zeus["vida"] <= 0:
                    print("¡Perdiste!")
                    bool_value = False
    if enemigo2["vidam"] > 0 :
            while bool_value :
    
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

                if enemigo3["niveles"] == enemigo3["nivel1"] :
                    enemigo3["danob"] = enemigo3["danob"] * 2.5
                    
                elif enemigo1["niveles"] == enemigo1["nivel2"] :
                    enemigo2["danob"] = enemigo2["danob"] * 3
                    
                elif enemigo2["danob"] == enemigo2["nivel3"]:
                    enemigo2["danob"] = enemigo2["danob"] * 3.5
                elif enemigo2["danob"] == enemigo2["nivel4"]:
                    enemigo2["danob"] == enemigo2["danob"] * 4
                dañob = enemigo2["danob"]
                if dañob == 100 or dañob == 120 or dañob == 140 or dañob == 160:
                    print("El oponente ha utilizado (ira) y te ha quitado",enemigo3["danob"],"de vida")
                elif dañob == 125 or dañob == 150 or dañob == 175 or dañob == 200:
                    print("El oponente ha utilizado (golpes) y te ha quitado",enemigo3["danob"],"de vida")
                elif dañob == 0:
                    print("El enemigo ha fallado")
                elif dañob == 150 or dañob == 180 or dañob == 210 or dañob == 240 :
                    print("El oponente ha utilizado (ola golpeante) y te ha quitado",enemigo3["danob"],"de vida")
                elif dañob == 187.5 or dañob == 225 or dañob == 262.5 or dañob == 300:
                    print("El oponente ha utilizado (furia berserker) y te ha quitado",enemigo3["danob"],"de vida")
                elif dañob == 225 or dañob == 270 or dañob == 315 or dañob == 360:
                    print("El oponente ha utilizado (puño de hierro) y te ha quitado",enemigo3["danob"],"de vida")
                elif dañob == 250 or dañob == 300 or dañob == 350 or dañob == 400:
                    print("El oponente ha utilizado (sangre berserk) y te a quitado",enemigo3["danob"],"de vida")
                elif dañob == 312.5 or dañob == 375 or dañob == 437.5 or dañob == 500:
                    print("El oponente ha utilizado (cuerpo carmesi) y te ha quitado",enemigo3["danob"],"de vida")

                zeus["vida"] -= dañob
                zeus["copias"]=zeus[random.choice(["rayo","tormenta","rayo_curativo","Criatura_de_saturno","Campo_electrico","fallo","Control_del_clima","Dominio_de_energia"])]    
                zeus["rayos"] = zeus[random.choice(["rayo", "rayo_critico"])]
                zeus["fallo_rayo"] = zeus[random.choice(["rayos", "fallo"])]
                zeus["fallo_tormenta"] = zeus[random.choice(["tormenta", "fallo"])]
                zeus["fallo_criatura"] = zeus[random.choice(["Criatura_de_saturno", "fallo"])]
                zeus["fallo_campo"] = zeus[random.choice(["Campo_electrico", "fallo"])]
                zeus["fallodo"]= zeus[random.choice(["Dominio_de_energia","fallo"])]
                zeus["falloco"]= zeus[random.choice(["Control_del_clima","fallo"])]
                berserk["danob"] = berserk[random.choice(["ira", "golpes", "fallob", "ola_golpeante", "Furia_berserker","puño_de_hierro","mi_sangre","cuerpo_carmesi"])]
                if zeus["vida"] <= 0:
                    print("¡Perdiste!")
                    bool_value = False
        
    
    

while cp == 2 :
    print()
    print("La vida de Khonshu es: ",khonshu["vida"])
    print("Poderes\n1-Two Moons\n2-Meteoro Lunar\n3-Luna Llena\n4-Media Luna\n5-Moon Fall\n6-Piedras Lunares\n6-Oz Lunar\n7-Vida de otras lunas")
        
while cp == 3:   
    print("La vida de Anubis es: ",anubis["vida"],"\n")
    print("Poderes\n1-Tumba del rey\n2-Ejercito de muertos\n3-Hacha de Muerte\n4-Apocalipsis Final\n5-Almas Perdidas\n6-Poder Prestado\n7-Muerte\n8-Oz de muerte\n9-Tomar vidas\n")

print()
print("Batalla finalizada")