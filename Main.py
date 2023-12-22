import time
import random
import keyboard
import pyautogui
import colorama

prayId = 970714446437703742
liste = ["77", "76", "75", "74", "73","72","70","69","68","67","66","65","56","55","54","53","52","51"]
colorama.init()

def task_one(task_one_count):
    print(f"Task One executed at: {time.strftime('%H:%M:%S')}, Number of Task One calls: {task_one_count}")
    dosya_islemleri("Phrases.txt")
    wait_time_task_one = random.uniform(1, 2)
    print(colorama.Fore.BLUE + "Write Time :" + str(wait_time_task_one))
    time.sleep(wait_time_task_one)
    wait_time_task_one = random.uniform(0, 2)
    print(colorama.Fore.GREEN + "Hunt Time :" + str(wait_time_task_one))
    pyautogui.typewrite("owo hunt")
    pyautogui.press("enter")
    time.sleep(wait_time_task_one)
    wait_time_task_one = random.uniform(0, 2)
    print(colorama.Fore.RED + "Battle Time :" + str(wait_time_task_one))
    pyautogui.typewrite("owo battle")
    pyautogui.press("enter")
    wait_time_task_one = random.uniform(1, 2)
    print(colorama.Fore.BLUE + "Write Time :" + str(wait_time_task_one))
    time.sleep(wait_time_task_one)
    dosya_islemleri("Phrases.txt")

def dosya_islemleri(dosya_adı):
    try:
        with open(dosya_adı, 'r', encoding='utf-8') as dosya:
            satırlar = dosya.readlines()
            rasgele_satır = random.choice(satırlar)
            pyautogui.typewrite(rasgele_satır)
            pyautogui.press("enter")

    except FileNotFoundError:
        print(f"{dosya_adı} dosyası bulunamadı.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

def sirayla_printle(liste):
    indeks = 0
    while True:
        pyautogui.typewrite( "owo use " + liste[indeks])
        print(colorama.Back.YELLOW + colorama.Fore.RED + liste[indeks]) 
        pyautogui.press("enter")
        indeks = (indeks + 1) % len(liste)
        wait_time_task_one = random.uniform(5, 10)
        time.sleep(wait_time_task_one)
        if indeks == 0:
         print(colorama.Back.BLACK)
         break

def task_two(task_one_count):
    print(colorama.Fore.YELLOW + f"Task Two executed at: {time.strftime('%H:%M:%S')}")
    pyautogui.typewrite("owo pray " + str(prayId))
    pyautogui.press("enter")
    if task_one_count == 20:
        return 20
    else:
        task_three()
        return 0

def task_three():
    print(colorama.Fore.WHITE + f"Task Tree executed at: {time.strftime('%H:%M:%S')}")
    sirayla_printle(liste)

def main():
    print(colorama.Fore.WHITE + f"Code start time: {time.strftime('%H:%M:%S')}")
    task_one_count = 0
    try:
        while not keyboard.is_pressed("x"):
            wait_time_task_one = random.uniform(15, 20)
            print(colorama.Fore.WHITE + "Wait Time :" + str(wait_time_task_one))
            time.sleep(wait_time_task_one)
            task_one_count += 1
            task_one(task_one_count)
            
          
            if task_one_count == 20 or task_one_count == 40:
                task_one_count = task_two(task_one_count)


    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()