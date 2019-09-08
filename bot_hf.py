import sys,os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
from random import randrange
import codecs
from shutil import copyfile
#from pynput.keyboard import Key, Controller
#keyboard = Controller()


MDP="abracadabra"
NOMS_RESSOURCES=['Poisson', 'Pain', 'Fruit', 'Légume', 'Fromage', 'Miel', 'Lait', 'Oeuf', 'Epice', 'Foin', 'Blé', 'Farine', 'Orge', 'Lin', 'Chanvre', 'Chèvre', 'Vache', 'Poule', 'Chevaux', 'Vêtement', 'Fourrure', 'Plante médicinale', 'Cire d’abeille', 'Bateau de pêche', 'Navire de fret', 'Zeppelin', 'Bois', 'Bois précieux', 'Peau de bête', 'Cuir', 'Gemme', 'Argile', 'Fer', 'Fleur', 'Armure', 'Arme', 'Tunique', 'Arc', 'Arme de siège', 'Navire de guerre']
LB_PROD_BASE=[]
LB_PROD_TRANSF=[]
LB_MARCHAND=[]
LB_PRETRE=[]
ATTENTE=[]
ATTENTE_QUETE_FAIT=[]
LIST_PSEUDO=[]
LIST_BOT_ATK=[]
LIST_ATK_ESC=["Znia","Mogo","Iria","Youzu"]
LIST_ATK_ESC2=["Ouya","Briho","Mardi","Ganza"]
POURCENT_DRAGON_DESC=30
terr_atk=6
nb_partisan_opt=1200
time_now=time.time()-90000
sys.path.append(os.getcwd())


fich=codecs.open("fich_tresors.txt",'r', encoding='utf-8',errors='ignore')
TAB_MOTS=fich.read().split('\n')
fich.close()

def create_chromedriver(ua=False):
    options = webdriver.ChromeOptions()
    CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver.exe'
    FLASK_CONFIG = os.getenv('FLASK_CONFIG')



    if FLASK_CONFIG and FLASK_CONFIG == "production":
        # CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
        CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver.exe'
        GOOGLE_CHROME_SHIM = os.getenv('$GOOGLE_CHROME_SHIM') or 'no path found'

        print(GOOGLE_CHROME_SHIM)
        print(GOOGLE_CHROME_SHIM)
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")

    if ua:
        print('ua block33')

        mobile_emulation =  {"deviceName": "iPad Mini"}
        options.add_experimental_option("mobileEmulation", mobile_emulation)

    return webdriver.Chrome(executable_path='/app/.chromedriver/bin/chromedriver.exe', chrome_options=options)

def creation_mail():
#    unpacked_extension_path = 'C:/Users/Durieu/Desktop/omdakjcmkglenbhjadbccaookpfjihpa/3.2.5_0'
#    options = Options()
##    options.add_argument('--load-extension={}'.format(unpacked_extension_path))
#    options.add_argument("--headless")
#    options.binary_location="/app/.apt/usr/bin/google-chrome"
    driver = create_chromedriver()
    driver.get("https://www.mohmal.com/fr/create/random")
    elem = driver.find_element_by_class_name("email")
    mail=elem.text
    return(driver,mail)


def creation_compte(pseudo):
    driver,mail=creation_mail()
#    unpacked_extension_path = 'C:/Users/Durieu/Desktop/omdakjcmkglenbhjadbccaookpfjihpa/3.2.5_0'
#    options = Options()
##    options.add_argument('--load-extension={}'.format(unpacked_extension_path))
#    options.add_argument("--headless")
#    options.binary_location="/app/.apt/usr/bin/google-chrome"
    driver2 = create_chromedriver()
    driver2.get("http://www.heroic-fantasy.fr/")
    elem = driver2.find_element_by_name("ins_pseudo")
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(pseudo)
    elem = driver2.find_element_by_name("ins_mdp")
    elem.send_keys(MDP)
    elem = driver2.find_element_by_name("ins_email")
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(mail)
    elem = driver2.find_element_by_name("ins_lu")
    elem.click()
    elem = driver2.find_element_by_name("ins_email")
    elem.send_keys(Keys.ENTER)
    driver2.close()
    return(driver)

def validation_compte(driver):
    k=0
    while True:
        if k > 80:
            driver.close()
            return(0)
        driver.refresh()
        try:
            elem=driver.find_element_by_class_name("unseen")
            elem.click()
            break
        except:
            k+=1
            print(k)
    driver.switch_to.frame(frame_reference=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[7]/div[1]/div[2]/iframe"))
    while True:
        elem = driver.find_element_by_xpath("/html/body/div[2]/div[1]/a[1]")
        if len(elem.text) != 0:
            driver.get(elem.text)
            break
    driver.close()
    return(1)

def connexion(pseudo):
#    unpacked_extension_path = 'C:/Users/Durieu/Desktop/omdakjcmkglenbhjadbccaookpfjihpa/3.2.5_0'
#    options = Options()
##    options.add_argument('--load-extension={}'.format(unpacked_extension_path))
#    options.add_argument("--headless")
#    options.binary_location="/app/.apt/usr/bin/google-chrome"
    driver = create_chromedriver()
    driver.get("http://www.heroic-fantasy.fr/")
    elem = driver.find_element_by_name("pseudo")
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(pseudo)
    elem = driver.find_element_by_name("mdp")
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(Keys.BACK_SPACE)
    elem.send_keys(MDP)
    elem.send_keys(Keys.ENTER)
    return(driver)

def delete(pseudo):
    driver=connexion(pseudo)
    elem = driver.find_element_by_class_name("profil")
    elem.click()
    elem = driver.find_element_by_name("profilMDP")
    elem.send_keys(MDP)
    elem = driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/div/form/div[1]/div[1]/div[7]/select")
    elem.send_keys(Keys.ARROW_DOWN)
    elem = driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/div/form/div[2]/div[2]/input")
    elem.click()
    driver.close()

def achat(driver,pseudo,id_ressource,quantite,ide):
    if ide==-1:
        driver.get("http://www.heroic-fantasy.fr/index.php?p=commerce&r2="+str(id_ressource))
        l=driver.find_element_by_xpath("//*[@id='acheter"+str(1)+"']")
        l.click()
        elem = driver.find_element_by_xpath("//*[@id='acheterQuantite']")
        k=20
        while k>0:
            elem.send_keys(Keys.BACK_SPACE)
            k-=1
        elem.send_keys(quantite)
        elem.send_keys(Keys.ENTER)
    else:
        driver.get("http://www.heroic-fantasy.fr/index.php?p=commerce&r2="+str(id_ressource))
        for i in range(1,len(driver.find_elements_by_class_name("top5"))-9):
            l=driver.find_element_by_xpath("//*[@id='acheter"+str(i)+"']")
            if pseudo in l.text:
                l.click()
                elem = driver.find_element_by_xpath("//*[@id='acheterQuantite']")
                k=20
                while k>0:
                    elem.send_keys(Keys.BACK_SPACE)
                    k-=1
                elem.send_keys(quantite)
                elem.send_keys(Keys.ENTER)

def verif_mot(tab_lettre):
    for k in TAB_MOTS:
        l=1
        for i in tab_lettre:
            if i not in k:
                l=0
                break
        if l==1:
            return k
    return('0')

def swap(i,j,driver):
    driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/div[2]/a[4]/div").click()
    source=driver.find_element_by_xpath("//*[@id='sortable']/div["+str(i)+"]/div")
    dest=driver.find_element_by_xpath("//*[@id='sortable']/div["+str(j)+"]/div")
    ActionChains(driver).drag_and_drop(source,dest).perform()

def cherche_tresor(driver):
    driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/div[2]/a[4]/div").click()
    tab_lettre=[]
    i=1
    while True:
        try:
            tab_lettre.append(driver.find_element_by_xpath("//*[@id='sortable']/div["+str(i)+"]/div").text.lower())
            i+=1
        except:
            break
    mot=verif_mot(tab_lettre)
    print(mot)
    if mot=='0':
        print("mot inconnu !")
        print(tab_lettre)
        return 0
    else:
        for r in range(len(mot)):
            for k in range(r,len(mot)):
                if tab_lettre[k]==mot[r]:
                    swap(k+1,r+1,driver)
                    tab_lettre=tab_lettre[0:r]+[mot[r]]+tab_lettre[r:k]+tab_lettre[k+1:]
                    break
        return 1

def quetes(pseudo,pseudo2,ide):
    driver=connexion(pseudo)
    elem = driver.find_element_by_xpath("/html/body/div[9]/div[3]/div/button/span")
    elem.click()
    elem = driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/button/span")
    elem.click()
    elem = driver.find_element_by_id("messnonlu")
    elem.click()
    elem = driver.find_element_by_class_name("tuto")
    elem.click()
    elem = driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/button[2]/span")
    elem.click()
    elem = driver.find_element_by_xpath("/html/body/div[1]/div[1]")
    elem.click()
    elem = Select(driver.find_element_by_xpath("//*[@id='depRegion']"))
    elem.select_by_index(10)
    elem = driver.find_element_by_xpath("//*[@id='depButton']")
    elem.click()
    elem = driver.find_element_by_class_name("tuto")
    elem.click()
    elem = driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/button[2]/span")
    elem.click()
    elem = driver.find_element_by_xpath("//*[@id='ressourceProd']")
    elem.click()
    elem = driver.find_element_by_xpath("/html/body/div[11]/div[3]/div/button[1]/span")
    elem.click()
    elem = driver.find_element_by_class_name("tuto")
    elem.click()
    elem = driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/button[2]/span")
    elem.click()
    elem = driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/button[1]/span")
    elem.click()
    try:
        elem = driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/div[2]/a[3]/div")
    except:
        elem = driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/div[3]/a[3]/div")
    elem.click()
    elem = driver.find_element_by_xpath("/html/body/div[1]/div[1]")
    elem.click()
    elem = Select(driver.find_element_by_xpath("//*[@id='depRegion']"))
    elem.select_by_index(7)
    elem = driver.find_element_by_xpath("//*[@id='depButton']")
    elem.click()
    time.sleep(2)
    elem = driver.find_element_by_xpath("//*[@id='ressourceProd']")
    elem.click()
    elem = driver.find_element_by_xpath("/html/body/div[11]/div[3]/div/button[1]/span")
    elem.click()
    elem = driver.find_element_by_class_name("tuto")
    elem.click()
    elem = driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/button[2]/span")
    elem.click()
    elem = driver.find_element_by_xpath("/html/body/div[1]/div[1]")
    elem.click()
    elem = Select(driver.find_element_by_xpath("//*[@id='depRegion']"))
    elem.select_by_index(3)
    elem = driver.find_element_by_xpath("//*[@id='depButton']")
    elem.click()
    time.sleep(2)
    elem = driver.find_element_by_xpath("//*[@id='ressourceProd']")
    elem.click()
    elem = driver.find_element_by_xpath("/html/body/div[11]/div[3]/div/button[1]/span")
    elem.click()
    elem = driver.find_element_by_class_name("tuto")
    elem.click()
    elem = driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/button[2]/span")
    elem.click()
    driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/button[1]").click()
    achat(driver,pseudo2,17,28,ide)
    achat(driver,pseudo2,6,260,ide)
    achat(driver,pseudo2,56,2,ide)
    driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
    driver.find_element_by_class_name("tuto").click()
    driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/button[2]/span").click()
    driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/button[1]").click()
    driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div/div[3]/div[6]/div[2]/input").click()
    driver.find_element_by_class_name("tuto").click()
    driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/button[2]/span").click()
    driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/button[1]/span").click()
    t=0
    while t!=1:
        try:
            driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/div[2]/a[4]/div").click()
        except:
            driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/div[3]/a[4]/div").click()
        x1=int(driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/div[2]/div[1]/strong").text.split(' : ')[1].split(' / ')[0])
        x2=int(driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/div[2]/div[1]/strong").text.split(' : ')[1].split(' / ')[1])
        if x1==x2:
            t=1
            nb=cherche_tresor(driver)
            if nb==0:
                print("bla")
            else:
                driver.find_element_by_xpath("//*[@id='tresorConfirm']").click()
                driver.find_element_by_xpath("/html/body/div[9]/div[3]/div/button[1]/span").click()
                driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
        else:
            driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
            tot=abs(x1-x2)
            while tot>0:
                driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
                deplacer1(driver,1+randrange(24))
                tot-=1
    driver.find_element_by_xpath("//*[@id='tutoriel']").click()
    try:
        driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/button[2]/span").click()
    except:
        try:
            driver.find_elements_by_xpath("/html/body/div[9]/div[3]/div/button[1]/span").click()
        except:
            driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/button[2]/span").click()
    driver.find_element_by_xpath("/html/body/div[8]/div[3]/div/button[1]/span").click()
    driver.close()
    

def nbr_pa(driver):
    return(int(driver.find_element_by_xpath("//*[@id='pa']").text[:-3].replace(' ','')))

def nbr_po(driver):
    return(int(driver.find_element_by_xpath("//*[@id='po']").text[:-3].replace(' ','')))

def id_ressource(ressource):
    for i in range(len(NOMS_RESSOURCES)):
        if NOMS_RESSOURCES[i]==ressource:
            return(i)
    return(-1)

def list_ressources(driver):
    driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
    try:
        driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/div[2]/a[3]/div").click()
    except:
        driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/div[3]/a[3]/div").click()
    liste=[0 for i in range(len(NOMS_RESSOURCES))]
    for k in driver.find_elements_by_class_name("back1"):
        h=k.text.split('\n')
        i=id_ressource(h[0])
        if i!=-1:
            liste[i]= int(h[1].replace(' ',''))
    return(liste)

def deplacer(driver,i):
    Select(driver.find_element_by_xpath("//*[@id='depRegion']")).select_by_index(i-1)
    driver.find_element_by_xpath("//*[@id='depButton']").click()

def deplacer1(driver,i):
    driver.find_element_by_xpath("//*[@id='depNoble']").send_keys(Keys.ARROW_DOWN)
    Select(driver.find_element_by_xpath("//*[@id='depRegion']")).select_by_index(i-1)
    driver.find_element_by_xpath("//*[@id='depButton']").click()

def completer(liste_bot_atk):
    for i in range(24):
        try:
            if liste_bot_atk[i].region != i+1:
                l=ATTENTE_QUETE_FAIT.pop()
                liste_bot_atk=liste_bot_atk[:i]+[bot(l,0,i+1,"")]+liste_bot_atk[i:]
                recrute_soldats(l,"",-1)
        except:
            l=ATTENTE_QUETE_FAIT.pop()
            liste_bot_atk.append(bot(l,0,i+1,""))
            recrute_soldats(l,"",-1)

def del_troupes(pseudo):
    driver=connexion(pseudo)
    driver.find_element_by_xpath("/html/body/div[1]/a[4]/div").click()
    try:
        nb=driver.find_element_by_xpath("//*[@id='Recru1']/div[2]/div[2]/strong").text
        driver.find_element_by_xpath("//*[@id='demob1']").click()
        driver.find_element_by_xpath("//*[@id='demobForm']/div[3]/input[1]").send_keys(Keys.BACK_SPACE)
        driver.find_element_by_xpath("//*[@id='demobForm']/div[3]/input[1]").send_keys(nb)
        driver.find_element_by_xpath("/html/body/div[10]/div[3]/div/button[1]/span").click()
    except:
        print("pas d'archers")
    driver.close()
     

def attaque_dragon(driver):
    t=0
    if nbr_pa(driver)<100:
        return("200%",1)
    for i in range(1,25):
        deplacer1(driver,i)
        if nbr_pa(driver)<100:
            return("200%",1)
        print(i)
        driver.find_element_by_xpath("/html/body/div[1]/a[4]/div").click()
        driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/div[2]/a[2]/div").click()
        for k in driver.find_elements_by_tag_name("strong"):
            if k.text=="Chasse au Dragon":
                driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
                deplacer(driver,i)
                driver.find_element_by_xpath("/html/body/div[1]/a[4]/div").click()
                driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/div/a[2]/div").click()
                for l in driver.find_elements_by_tag_name("strong"):
                    if l.text=="Chasse au Dragon":
                        prc=driver.find_element_by_xpath("//*[@id='pnj6']/div[2]/div/div[1]/div[7]").text
                        print(prc)
                        l.click()
                        t=1
                        driver.find_element_by_xpath("/html/body/div[9]/div[3]/div/button[1]").click()
                        driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
                        if nbr_pa(driver)<100:
                            return(prc,1)
                        else:
                            return(prc,0)
                driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
                break
        if t==1:
            break
        else:
            driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
    driver.close()
    return("200%",0)

def attaque_baisse_dragon():
    current=ATTENTE_QUETE_FAIT.pop()
    recrute_soldats(current,"",-1)
    distributions(current)
    driver=connexion(current)
    prc,ind=attaque_dragon(driver)
    if ind==1 or current in LIST_ATK_ESC or current in LIST_ATK_ESC2:
        ATTENTE_QUETE_FAIT.insert(0,current)
        current=ATTENTE_QUETE_FAIT.pop()
    tot=0
    while int(prc[:-1])>POURCENT_DRAGON_DESC or tot==100:
        prc,ind=attaque_dragon(driver)
        if ind==1:
            driver.close()
            ATTENTE_QUETE_FAIT.insert(0,current)
            current=ATTENTE_QUETE_FAIT.pop()
            recrute_soldats(current,"",-1)
            driver=connexion(current)
        tot+=1

def productions_base(liste_bot):
    for k in liste_bot:
        driver=connexion(k.pseudo)
        deplacer(driver,k.region)
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='ressourceProd']").click()
        elem=driver.find_element_by_xpath("//*[@id='prodNB']")
        elem.send_keys(Keys.BACK_SPACE)
        elem.send_keys(str(int(k.pa/10)))
        driver.find_element_by_xpath("/html/body/div[11]/div[3]/div/button[1]/span").click()
        k.pa=nbr_pa(driver)
        k.po=nbr_po(driver)
        k.ressources=list_ressources(driver)
        driver.close()


def ajout(pseudo,typ,region,ressources):
    chaine=pseudo+'---'+str(typ)+'---'+str(region)+'---'+ressources+'\n'
    fich=open("liste_compte.txt",'a')
    fich.write(chaine)
    fich.close()

def don_or(pseudo,pseudo2,id_ressource):
    driver=connexion(pseudo)
    driver.get("http://www.heroic-fantasy.fr/index.php?p=commerce&r2="+str(id_ressource))
    for i in range(1,len(driver.find_elements_by_class_name("top5"))-9):
        l=driver.find_element_by_xpath("//*[@id='acheter"+str(i)+"']")
        print(l.text)
        if pseudo2 in l.text:
            l.click()
            driver.find_element_by_xpath("//*[@id='acheter']/div[2]/div[6]/div[2]").click()
            driver.find_element_by_xpath("/html/body/div[10]/div[3]/div/button[1]").click()
    driver.close()
    
def recrute_soldats(pseudo,pseudo2,i=0):
    driver=connexion(pseudo)
    achat(driver,pseudo2,46,60,i)
    achat(driver,pseudo2,47,60,i)
    achat(driver,pseudo2,17,60,i)
    driver.find_element_by_xpath("/html/body/div[1]/a[4]/div").click()
    driver.find_element_by_xpath("//*[@id='Recru1']/div[2]").click()
    driver.find_element_by_xpath("//*[@id='newTroupe']/div[2]/div[6]/div[2]").click()
    driver.find_element_by_xpath("/html/body/div[9]/div[3]/div/button[1]").click()
    driver.close()

def construit_listes():
    fich=codecs.open("liste_compte.txt",'r', encoding='utf-8',errors='ignore')
    tab=fich.read().split('\n')
    fich.close()
    for i in range (len(tab)-1):
        k=tab[i]
        tab2=k.split('---')
        pseudo=tab2[0]
        typ=int(tab2[1])
        region=int(tab2[2])
        ressources=tab2[3]
        LIST_PSEUDO.append(pseudo)
        if typ == 0:
            LIST_BOT_ATK.append(bot(pseudo,typ,region,ressources))
        elif typ == 1:
            LB_PROD_BASE.append(bot(pseudo,typ,region,ressources))
        elif typ == 2:
            LB_PROD_TRANSF.append(bot(pseudo,typ,region,ressources))
        elif typ == 3:
            LB_MARCHAND.append(bot(pseudo,typ,region,ressources))
        elif typ == 4:
            LB_PRETRE.append(bot(pseudo,typ,region,ressources))
        elif typ == 5:
            ATTENTE.append(pseudo)
        else:
            ATTENTE_QUETE_FAIT.append(pseudo)


def construit_fichier():
    fich=open("liste_compte.txt",'w')
    chaine=""
    for k in LIST_BOT_ATK:
        chaine=chaine+k.pseudo+'---'+str(k.type)+'---'+str(k.region)+'---'+k.ressources_respo+'\n'
    for k in LB_MARCHAND:
        chaine=chaine+k.pseudo+'---'+str(k.type)+'---'+str(k.region)+'---'+k.ressources_respo+'\n'
    for k in LB_PRETRE:
        chaine=chaine+k.pseudo+'---'+str(k.type)+'---'+str(k.region)+'---'+k.ressources_respo+'\n'
    for k in LB_PROD_BASE:
        chaine=chaine+k.pseudo+'---'+str(k.type)+'---'+str(k.region)+'---'+k.ressources_respo+'\n'
    for k in LB_PROD_TRANSF:
        chaine=chaine+k.pseudo+'---'+str(k.type)+'---'+str(k.region)+'---'+k.ressources_respo+'\n'
    for k in ATTENTE:
        chaine=chaine+k+'---'+str(5)+'---'+str(1)+'---'+""+'\n'
    for k in ATTENTE_QUETE_FAIT:
        chaine=chaine+k+'---'+str(6)+'---'+str(1)+'---'+""+'\n'
    fich.write(chaine)
    fich.close()

# Liste des types de bot :
# 0 : Attaquant Dragon
# 1 : producteur ressource base
# 2 : producteur ressource transfo
# 3 : Marchand
# 4 : prieur

class bot:
    def __init__(self,p,typ,region,list_ressource):
#        driver=connexion(p)
        self.pseudo=p
#        self.pa=nbr_pa(driver)
#        self.po=nbr_po(driver)
#        self.ressources=list_ressources(driver)
        self.pa=0
        self.po=0
        self.ressources_respo=list_ressource
        self.type=typ
        self.region=region
#        driver.close()
        
def creation_bot(pseudo,typ,region,list_ressource):
    p=pseudo
    validation_compte(creation_compte(p))
    quetes(p,"Arkenus")
    if typ==0:
        recrute_soldats(p,"Arkenus")
    driver=connexion(p)
    deplacer(driver,region)
    return(bot(pseudo,typ,region,list_ressource))

def connexion_bots():
    t=0
    l=len(LIST_PSEUDO)
    for k in LIST_PSEUDO:
        print(k)
        t+=1
        driver = connexion(k)
        deplacer(driver,1)
        driver.close()
        print(str(int(100*t/l))+"%")

def achats_ressources_distribution(driver):
    elem=driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div/div[3]/div[2]/div/div/div[2]/div[2]/strong").text
    if int(elem.split(' / ')[0].replace(' ',''))<int(elem.split(' / ')[1].replace(' ','')):
        nbr_achat=int(elem.split(' / ')[1].replace(' ',''))
        elem=driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div/div[3]/div[2]/div/a")
        driver.execute_script("return arguments[0].scrollIntoView();",elem)
        elem.click()
        driver.find_element_by_xpath("//*[@id='acheter1']").click()
        elem = driver.find_element_by_xpath("//*[@id='acheterQuantite']")
        k=20
        while k>0:
            elem.send_keys(Keys.BACK_SPACE)
            k-=1
        elem.send_keys(nbr_achat)
        elem.send_keys(Keys.ENTER)
        try:
            if "Vous n’avez pas toutes les pièces d’or" in driver.find_element_by_xpath("//*[@id='info']/div/table/tbody/tr[1]/td[2]/div/p").text or "Pour éviter les dérives du commerce abusif, les échanges entres deux joueurs sont limités par heure." in driver.find_element_by_xpath("//*[@id='info']/div/table/tbody/tr[1]/td[2]/div/p").text:
                return(0)
            else:
                driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
        except:
            driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
    elem=driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div/div[3]/div[3]/div/div/div[2]/div[2]/strong").text
    if int(elem.split(' / ')[0].replace(' ',''))<int(elem.split(' / ')[1].replace(' ','')):
        nbr_achat=int(elem.split(' / ')[1].replace(' ',''))
        elem=driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div/div[3]/div[3]/div/a")
        driver.execute_script("return arguments[0].scrollIntoView();",elem)
        elem.click()
        driver.find_element_by_xpath("//*[@id='acheter1']").click()
        elem = driver.find_element_by_xpath("//*[@id='acheterQuantite']")
        k=20
        while k>0:
            elem.send_keys(Keys.BACK_SPACE)
            k-=1
        elem.send_keys(nbr_achat)
        elem.send_keys(Keys.ENTER)
        try:
            if "Vous n’avez pas toutes les pièces d’or" in driver.find_element_by_xpath("//*[@id='info']/div/table/tbody/tr[1]/td[2]/div/p").text or "Pour éviter les dérives du commerce abusif, les échanges entres deux joueurs sont limités par heure." in driver.find_element_by_xpath("//*[@id='info']/div/table/tbody/tr[1]/td[2]/div/p").text:
                return(0)
            else:
                driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
        except:
            driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
    elem=driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div/div[3]/div[4]/div/div/div[2]/div[2]/strong").text
    if int(elem.split(' / ')[0].replace(' ',''))<int(elem.split(' / ')[1].replace(' ','')):
        nbr_achat=int(elem.split(' / ')[1].replace(' ',''))
        elem=driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div/div[3]/div[4]/div/a")
        driver.execute_script("return arguments[0].scrollIntoView();",elem)
        elem.click()
        driver.find_element_by_xpath("//*[@id='acheter1']").click()
        elem = driver.find_element_by_xpath("//*[@id='acheterQuantite']")
        k=20
        while k>0:
            elem.send_keys(Keys.BACK_SPACE)
            k-=1
        elem.send_keys(nbr_achat)
        elem.send_keys(Keys.ENTER)
        try:
            if "Vous n’avez pas toutes les pièces d’or" in driver.find_element_by_xpath("//*[@id='info']/div/table/tbody/tr[1]/td[2]/div/p").text or "Pour éviter les dérives du commerce abusif, les échanges entres deux joueurs sont limités par heure." in driver.find_element_by_xpath("//*[@id='info']/div/table/tbody/tr[1]/td[2]/div/p").text:
                return(0)
            else:
                driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
        except:
            driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
    elem=driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div/div[3]/div[5]/div/div/div[2]/div[2]/strong").text
    if int(elem.split(' / ')[0].replace(' ',''))<int(elem.split(' / ')[1].replace(' ','')):
        nbr_achat=int(elem.split(' / ')[1].replace(' ',''))
        elem=driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div/div[3]/div[5]/div/a")
        driver.execute_script("return arguments[0].scrollIntoView();",elem)
        elem.click()
        driver.find_element_by_xpath("//*[@id='acheter1']").click()
        elem = driver.find_element_by_xpath("//*[@id='acheterQuantite']")
        k=20
        while k>0:
            elem.send_keys(Keys.BACK_SPACE)
            k-=1
        elem.send_keys(nbr_achat)
        elem.send_keys(Keys.ENTER)
        try:
            if "Vous n’avez pas toutes les pièces d’or" in driver.find_element_by_xpath("//*[@id='info']/div/table/tbody/tr[1]/td[2]/div/p").text or "Pour éviter les dérives du commerce abusif, les échanges entres deux joueurs sont limités par heure." in driver.find_element_by_xpath("//*[@id='info']/div/table/tbody/tr[1]/td[2]/div/p").text:
                return(0)
            else:
                driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
        except:
            driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
    return(1)
    
def nb_partisan(driver):
    return(int(driver.find_element_by_xpath("//*[@id='partisan']").text.replace(' ','')))

def distributions(pseudo):
    driver=connexion(pseudo)
    nb_partisans=nb_partisan(driver)
    while nb_partisans<nb_partisan_opt:
        t=achats_ressources_distribution(driver)
        if t==1:
            elem = driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div/div[3]/div[6]/div[2]/input")
            driver.execute_script("return arguments[0].scrollIntoView();",elem)
            elem.click()
        else:
            break
        nb_partisans=nb_partisan(driver)
        driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
    driver.close()

def attaques_esclaves(nb):
    if nb==1:
        for k in LIST_ATK_ESC:
            driver=connexion(k)
            while True:
                try:
                    driver.find_element_by_xpath("/html/body/div[1]/a[4]/div").click()
                    driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/div[2]/a[2]/div").click()
                    driver.find_element_by_xpath("//*[@id='guerre1']").click()
                    driver.find_element_by_xpath("/html/body/div[9]/div[3]/div/button[1]/span").click()
                    driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
                except:
                    break
            driver.close()
    else:
        for k in LIST_ATK_ESC2:
            driver=connexion(k)
            while True:
                try:
                    driver.find_element_by_xpath("/html/body/div[1]/a[4]/div").click()
                    driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td[2]/div[2]/a[2]/div").click()
                    driver.find_element_by_xpath("//*[@id='guerre1']").click()
                    driver.find_element_by_xpath("/html/body/div[9]/div[3]/div/button[1]/span").click()
                    driver.find_element_by_xpath("/html/body/div[1]/div[1]").click()
                except:
                    break
            driver.close()
    

construit_listes()

tour_atk=1
while True:
    h=time.time()
    if h>time_now+80000:
        time_now=h
        connexion_bots()
        print(TAB_MOTS)
        print(LIST_PSEUDO)
        print("ok !")
        attaque_baisse_dragon()
        attaques_esclaves(tour_atk)
        tour_atk=1-tour_atk
    else:
        time.sleep(40500)