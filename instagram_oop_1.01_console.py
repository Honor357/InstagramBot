import sys
import os
import re
import random
import time
import winsound
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
import datetime
import imaplib
# from PyQt5 import QtWidgets
# import inst

class instaClicker:
    '''Класс инстаграмм бота, лайкает по списку тегов из файла, запоминает время последнего запуска и не позволяет запускает чаще 1 раза в час,
     позволяет получать код безопасности из почты

     Class instagram bot, liked on list of tags, save time of last start script and don't let start more then 1 in 1 hour, if need get security code from emeil'''
    html = 'https://vk.com/honor5?w=wall6864019_13264%2Fall'
    html2 = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
    url = 'https://www.instagram.com/'
    count = 0
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3729.169 Safari/537.36')
    driver = webdriver.Chrome('lib\chromedriver.exe')
    driver.set_page_load_timeout(35)
    user = ''
    login = ''
    password = ''
    login1 = 'HMobileShots'
    password1 = 'GJPjL2wX'
    login2 = 'Hon0r5'
    password2 = 't%v8X^bR'
    email = ''
    email_password = ''
    email1 = '2335045T@gmail.com'
    email1_password = 'RyOQiD20SHnf'
    email2 = '2335045@gmail.com'
    email2_password = 'O0%gi8$!Ci'
    set_count = 0
    timeLastStart=''

    def main(self, user='HMobileShots', password='GJPjL2wX', set_count=9):
        '''Главная функция запускает бота (Параметры - login и пароль)
               Main function, run bot (Parametr's - Login and password)'''
        listoftags = []
        inst = instaClicker()
        # check which user chouse
        if user == 'Hon0r5':
            self.user = 'Hon0r5'
            self.login = self.login2
            self.password = self.password2
            self.email=self.email2
            self.email_password=self.email2_password
        elif user=='HMobileShots':
            self.user = 'HMobileShots'
            self.login = self.login1
            self.password = self.password1
            self.email=self.email1
            self.email_password=self.email1_password
        else:
            self.user = user
            self.login = user
            self.password = password
        count = 0

        self.loads()  # read list of tags

        #check passed hour from the moment last work of script or not, if yes logging in account, if not wait
        time1 = float(self.timeLastStart)
        time2 = float(time.mktime(datetime.datetime.now().timetuple()))
        timeZap=time2-time1
        if timeZap<0:
            timeZap*=-1
        if (timeZap) < 3600:
            print('sorry from the last run, not yet hour, wait', 3600 - timeZap, ' seconds')
            time.sleep(3600-timeZap)
        else:
            print('all okay, program run and now logging user')
            pass

        self.flogin(login=self.login, password=self.password)  # logging in instagram

        start_time = time.time()
        for i in self.listoftags[:set_count]:
            inst.fsearch(i)  # find page with tags
            cont = self.likedAndCommentPosts(commentYN=0)  # лайкаем 3 лучших и 6 новых фото
            print('tags', i, 'liked - ', cont)
            time.sleep(3)
            count = count + cont
            cont = 0
        inst.driver.quit()  #close driver
        end_time = time.time() - start_time #find and write time of work script
        print('by all tag\'s liked photo - ', count)
        print('Program run -', round(end_time) // 60, 'min :', round(end_time) % 60, 'sec in - ',
              datetime.datetime.now().time())
        print('for user - ', self.user)

        with open('info\\' + self.login + '_end.txt', 'w+', encoding='utf-8') as file_d:
            file_d.write(str(float(time.mktime(datetime.datetime.now().timetuple()))))
        #write time last work script in file
        winsound.Beep(440, 450)


    def loads(self):  #loads all data from file
        ''' Заходит в инстаграмм (Аргументы, логин и пароль)
        Login to instagram (Parametrs=login, password'''
        file1 = list()
        with open('info\ListOfTags.txt', 'r', encoding='utf-8') as file:
            self.listoftags = file.read().split('\n')
            random.shuffle(self.listoftags)
            if self.listoftags:
                print('list of tags load successful, count - ', len(self.listoftags))
        if os.path.exists('info\\' + str(self.login) + '_end.txt'):
            with open('info\\' + str(self.login) + '_end.txt', 'r', encoding='utf-8') as file2:
                self.timeLastStart = file2.read()
        else:
            # with open('info\\' + str(self.login) + '_end.txt', 'w+', encoding='utf-8') as file2:
            #     file2.write(str((time.mktime(datetime.datetime.now().timetuple() ))-3650))
            #     self.timeLastStart = file2.read()
            with open('info\\' + str(self.login) + '_end.txt', 'r', encoding='utf-8') as file3:
                self.timeLastStart = file3.read()

    if not os.path.exists:
        with open('logs\ListOfLikedUrltest.txt', 'w+', encoding='utf-8') as file1:
            pass

    def flogin(self, login, password):
        ''' Заходит в инстаграмм данных из файлов (список тегов, время последнего запуска программы
                load data drom file (list of tags, time last start program '''
        self.driver.implicitly_wait(10)
        self.driver.get(self.html2)
        elemname = self.driver.find_elements_by_name('username')
        elemname[0].send_keys(str(login))  # log
        elemname = self.driver.find_elements_by_name('password')
        elemname[0].send_keys(str(password))  # pass)
        elemname = self.driver.find_elements_by_xpath(
            '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button')
        if not elemname:
            self.driver.quit()
            time.sleep(1000)
            self.main(user=user, set_count=set_count)
        try:
            elemname[0].click()
        except IndexError:
            self.driver.quit()
            winsound.Beep(440, 300)
            winsound.Beep(440, 300)
            winsound.Beep(440, 300)
            # self.main(user=user, set_count=set_count)
            print('error log, try again')

        try:
            #check
            elemname = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div/p')
            if (elemname.text == 'Чтобы защитить ваш аккаунт, мы отправим вам код безопасности для подтверждения личности. Как вы хотите его получить?'):
            #click and send mail
                elemname = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div/div[3]/form/span/button')
                elemname.click()
            #insert code from email
            elemname = self.driver.find_element_by_xpath('//*[@id="security_code"]')
            time.sleep(20)
            elemname.send_keys(str(self.check_mail()))
            elemname = self.driver.find_element_by_xpath('// *[ @ id = "react-root"] / section / div / div / div[2] / form / span / button')
            elemname.click()
            print('window unusual loging and check with mail is close!')
        except:
            print('error find window unusual loging and check with mail!')



        try:
            elemname = self.driver.find_element_by_xpath('//*[@id="slfErrorAlert"]')
            if elemname.text == 'К сожалению, вы ввели неверный пароль. Проверьте свой пароль еще раз.' or elemname.text == 'Чтобы защитить ваш аккаунт, мы сбросили ваш пароль. ' \
                                                                                                                            'Нажмите «Забыли пароль?» на экране входа и следуйте инструкциям по восстановлению доступа к аккаунту.':
                print('Password incorrect or other problem in logging')
                self.driver.quit()
                exit()
        except:
            None

        try:
            elemname = self.driver.find_element_by_xpath(
                '/html/body/div[3]/div/div/div[3]/button[2]')  # close  window notification
            elemname.click()
            print('notification window is closed!')
        except:
            print('error on find window on main page')

        try:
            elemname = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/div/div/p[1]')  # close  window with cheked unusual loging try
            elemname = self.driver.find_element_by_xpath('// *[ @ id = "react-root"] / section / div / div / div[3] / form / div[2] / span / button')
            elemname.click()
            print('window cheked unusual loging try is close!')
        except:
            print('error on window cheked unusual loging!')

        #проверка зашли ли мы
        #переходим в профиль и смотрим имя
        try:
            elemname=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a')
            elemname.click()
            elemname  = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/h1')
            if elemname.text.upper()==str(self.user).upper():
                print('Logged user - ', login, 'in instagram')
            else:
                print('error, user not logged, program closed168')
                self.driver.quit()
                exit()
        except:
                print('error')


        self.driver.implicitly_wait(5)

    def fsearch(self, tag):
        '''Поиск фотографий по тегу (Параметр тэг)
        Search proto's in select tags(Parametr's tag)'''
        urls = self.url + 'explore/tags/' + str(tag)
        self.driver.get(urls)
        html = self.driver.page_source
        elemname = self.driver.find_elements_by_xpath(
            '// *[ @ id = "react-root"] / section / nav / div[2] / div / div / div[2]')
        print('go by tag', tag)
        time.sleep(2)

    def checkheart(self, url):
        '''Проверка есть ли лайк на фото (Параметр - url)
               Check if photo liked or not (Parametr's - url)'''
        # print('link', url)
        self.driver.refresh()
        soup = self.driver.page_source  # get raw full html code
        checkboth = re.findall('aria-label="Не нравится"|aria-label="Unlike"', soup)  # check liked or not photo
        if not checkboth:
            print('unliked in ', url)
            return 1
        else:
            print('liked in', url)
            return 0

    def likedAndCommentPosts(self, commentYN=0):
        countf = 0
        for i in range(1, 4):
            try:
                elemname = self.driver.find_element_by_xpath(
                    '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[' + str(i) + ']')  # best foto
                elemname.click()
            except WebDriverException:
                print('err find and click on photo')
                break

            time.sleep(1)

            if self.checkheart(self.driver.current_url):
                try:
                    elemname = self.driver.find_element_by_css_selector('#react-root > section > main > div > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > span')                        # serch button heart
                    # elemname = self.driver.find_element_by_class_name('coreSpriteHeartOpen')
                    # elemname = self.driver.find_element('coreSpriteHeartOpen')
                    time.sleep(2)
                    elemname.click()  # push
                    countf = countf + 1
                except:
                    print('error push heart on best foto')
                with open('logs\\' + str(self.user) + '_ListOfLikedUrl.txt', 'a', encoding='utf-8') as file1:
                    file1.write('\n' + self.driver.current_url)
                self.driver.back()  # close photo
                time.sleep(1)
            else:
                time.sleep(1)
                self.driver.back()
        for i in range(1, 4):
            for j in range(1, 3):
                try:
                    elemname = self.driver.find_element_by_xpath(
                        '//*[ @ id = "react-root"]/section/main/article/div[2] / div / div[' + str(
                            i) + '] / div[' + str(j) + ']')  # new foto
                    elemname.click()
                except:
                    print('err')
                    break
                time.sleep(1)
                if self.checkheart(self.driver.current_url):
                    try:
                        # elemname = self.driver.find_element_by_css_selector(
                        #      'body > div:nth-child(12) > div > div.zZYga > div > article > '
                        #      'div.eo2As > section.ltpMr.Slqrh > span.fr66n > button')                        # serch button heart
                        elemname = self.driver.find_element_by_css_selector(
                            '#react-root > section > main > div > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > span')  # serch button heart

                        time.sleep(1)
                        elemname.click()  # push
                        countf = countf + 1
                    except:
                        print('error push heart on new foto')

                    with open('logs\\' + str(self.user) + '_ListOfLikedUrl.txt', 'a', encoding='utf-8') as file1:
                        file1.write('\n' + self.driver.current_url)

                    self.driver.back()  # close photo
                else:
                    self.driver.back()
                    time.sleep(1)

        return countf

    def check_mail(self):
        '''Получение кода безопасности из емейла (Параметр - нет)
               Check and get security code in email(Parametr's - None)'''
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(self.email,self.email_password)
        mail.list()
        mail.select("inbox")  # Подключаемся к папке "входящие".
        result, data = mail.search(None, "ALL")

        ids = data[0]  # Получаем сроку номеров писем
        id_list = ids.split()  # Разделяем ID писем
        latest_email_id = id_list[-1]  # Берем последний ID

        result, data = mail.fetch(latest_email_id, "(RFC822)")  # Получаем тело письма (RFC822) для данного ID

        raw_email = data[0][1]  # Тело письма в необработанном виде
        print(raw_email)

        # включает в себя заголовки и альтернативные полезные нагрузки
        answ = re.findall(r'<font size=3D\"6\">.*<\/font>', str(raw_email))
        print(answ)
        answ=answ[0][17:23]
        return answ

inst = instaClicker()

if __name__ == "__main__" :
    if len(sys.argv)==1:
        user1 = 'Hon0r5'
        user2 = 'HMobileShots'
        set_count = 9
        inst.set_count = set_count
        inst.main(user=user1, set_count=set_count)
        a=input()
    else :
        inst.main(user=str(sys.argv[1]), password=str(sys.argv[2]), set_count=10)

# thread1 = Thread(target=inst.main, args=(user,set_count))
# thread2 = Thread(target=inst.main, args=(user,set_count))
#
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
