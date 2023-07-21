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
        "corte_vertical": 50,
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
        "coraza_magica": 15,
        "ataque_de_fuego":70,
        "esfera_oceanica":90,
        "esfera_carmesi":100,
        "esfera_oscura":110,
        "Dominio_del_mana":120,
        "nivel1":1,
        "nivel2":2,
        "nivel3":3
    }
    mago["danom"] = mago[random.choice(["ataque_magico", "bestia_magica", "fallom","ataque_de_fuego","esfera_oceanica","esfera_carmesi","esfera_oscura","Dominio_del_mana"])]
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
    invocador["niveles"]= invocador[random.choice(["nivel1","nivel2","nivel3""nivel4","nivel5","nivel6"])]
    return invocador        

print()
enemigo1 = espadachin()
print("Tu oponente sera:",enemigo1["Nombre"],"-nivel",enemigo1["niveles"])
print("La vida del oponente es: ",enemigo1["vidae"])
print()
while cp == 1 :    
    bool_value = True
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
        enemigo1["vidae"]-=zeus["Criatura_de_saturno"]
        print("Vida del oponente", enemigo1["vidae"])
    elif x ==4:
        enemigo1["vidae"]-=zeus["Campo_electrico"]
        print("Vida del oponente", enemigo1["vidae"])
    elif x ==5:
        enemigo1["vidae"]-=zeus["Control_del_clima"]        
        print("Vida del oponente", enemigo1["vidae"])
    elif x ==6:
        enemigo1["vidae"]-=zeus["Dominio_de_energia"]
        print("Vida del oponente", enemigo1["vidae"])
    elif x ==7:
        enemigo1["vidae"]-=zeus["rayo_curativo"]
        print("Vida del oponente", enemigo1["vidae"])
while cp == 2 :
    
    print("La vida de Khonshu es: ",khonshu["vida"])
    print("Poderes\n1-Two Moons\n2-Meteoro Lunar\n3-Luna Llena\n4-Media Luna\n5-Moon Fall\n6-Piedras Lunares\n6-Oz Lunar\n7-Vida de otras lunas")
        
while cp == 3:   
    print("La vida de Anubis es: ",anubis["vida"],"\n")
    print("Poderes\n1-Tumba del rey\n2-Ejercito de muertos\n3-Hacha de Muerte\n4-Apocalipsis Final\n5-Almas Perdidas\n6-Poder Prestado\n7-Muerte\n8-Oz de muerte\n9-Tomar vidas\n")

x=int(input("{ "))