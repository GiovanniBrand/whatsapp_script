from selenium import webdriver
import time

class whatsappBot:
    def __init__(self):
        self.mensagem = ""
        self.Person = [""]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def enviarMensagem(self):
        #<span dir="auto" title="name of the person in your whatsapp" class=""> name of the person in your whatsapp</span>
        #<div tabindex="-1" class="########">
        #<span data-testid="send" data-icon="send" class="">

        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        Ju = self.driver.find_element_by_xpath(f"//span[@title='']")
        Ju.click()
        time.sleep(3)
        chatbox = self.driver.find_element_by_class_name('########')
        chatbox.click
        time.sleep(3)
        chatbox.send_keys(self.mensagem)
        botaoEnviar = self.driver.find_element_by_xpath("//span[@data-testid='send']")
        time.sleep(3)
        botaoEnviar.click
        time.sleep(3)

bot = whatsappBot()
bot.enviarMensagem()
