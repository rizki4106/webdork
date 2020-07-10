from googlesearch import search
from prettytable import PrettyTable
import os, platform, urllib, datetime, hashlib, requests
from bs4 import BeautifulSoup

class ModuleCode:
    """
    Data Processing
    """

    def __init__(self):
        self.data_url = []
        self.local_file = []

    def search_url(self, keyword):
        """
        Search url with spesific keyword
        """
        data = []
        no = 0
        for i in search(keyword):
            no += 1
            self.data_url.append(i)
            print(no, i)
        
        # save search result
        print('\n')
        ask = str(input('Do you want to save your search result ? [y/t] : '))
        if ask == "y" or ask == "Y":
            for i in self.data_url:
                with open('log/history/result.txt', 'a') as files:
                    files.write(i + '\n')
            print('\ndone..! your result saved to log/history/result.txt\n')
        else:
            print('ok\n')

        return no

    def keyword_parser(self, keyword):
        """
        Create keyword from user input
        """
        length_word = len(keyword) - 1
        result_word = keyword[1] + ' '
        for i in range(1, length_word):
            if i >= length_word - 1:
                result_word += keyword[i + 1]
            else:
                result_word += keyword[i + 1] + ' '
        return result_word
    
    def clear_screen(self):
        """
        This method used for clear terminal / cmd screen
        """
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    def read_file(self, index):
        """
        Read file from url
        """

        try:
            file_url = self.data_url[int(index) - 1]
            domain = self.url_filter(file_url)

            #get domain data

            req = requests.get('http://api.ipapi.com/'+ domain +'?access_key=91553e8f4e352e51576a5d7732a343e0&format=1')
            res = req.text

            #end of detail data

            #create folder
            time = str(datetime.datetime.now().day) + '-'  + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().year)
            try:
                os.makedirs("log/"+ str(time))
            except:
                pass

            print('\nRead file > ', file_url, '\n')
            files = urllib.request.urlopen(file_url)
            text = ''
            for f in files:
                decoded = f.decode('utf-8')
                text += decoded
                print(decoded)

            # write file log
            hashurl = hashlib.md5(file_url.encode())

            with open('log/' + time + '/' + domain + '-' + hashurl.hexdigest() + '.txt', 'a') as logFile:
                logFile.write(file_url + '\n\n')
                logFile.write('written at : ' + str(datetime.datetime.now()) + '\n\n')
                logFile.write('-----------------------------------------------------\n\n')
                logFile.write(res)
                logFile.write('=====================================================\n\n')
                logFile.write(text)
                logFile.close()

        except:
            web = requests.get(file_url)
            soup = BeautifulSoup(web.txt)
            try:
                with open('log/' + time + '/' + domain + '-' + hashurl.hexdigest() + '.txt', 'a') as logFile:
                    logFile.write(file_url + '\n\n')
                    logFile.write('written at : ' + str(datetime.datetime.now()) + '\n\n')
                    logFile.write('-----------------------------------------------------\n\n')
                    logFile.write(res)
                    logFile.write('=====================================================\n\n')
                    logFile.write(soup.get_text())
                    logFile.close()
            except IOError:
                print('Unble to read file > ', file_url)
                print(IOError)

    def list_file(self):
        """
        print all the file log (history from search)
        """

        directory = []
        x = PrettyTable()
        x.field_names = ["No","Folder", "File"]
        for i in os.listdir('log/'):
            if os.path.isdir('log/' + i):
                directory.append(i)

        if len(directory) > 0:
            no = 0
            for i in directory:
                no += 1
                # list the file
                for f in os.listdir('log/' + i + '/'):
                    x.add_row([no, i, f])
                    self.local_file.append('log/' + i + '/' + f)
        else:
            print('there is no file')

        return x

    def url_filter(self, url):
        """
        get real domain name from random url
        """
        res = url.split("://")[1].split('/')[0]
        final_string = res
        return final_string

    def help(self):
        string = """1. search [ keyword ]\n2. readfile-url [ index url ]\n3. list-file\n4. readfile-local\n5. exit\n6. help
        """
        print(string)

    def read_local(self):
        """
        read result from google dork
        """

        print(self.list_file())

        # get input spesific file from user

        nmr = int(input("\nindex file > "))
        selected_file = self.local_file[nmr - 1]

        #check os type

        if platform.system() == "Windows":
            os.system("notepad " + selected_file)
        elif platform.system() == "Linux":
            os.system("nano " + selected_file)
        else:

            # if os is not detected this program will print on the terminal

            with open(self.local_file[nmr - 1], 'r') as files:
                print(files.read())
                files.close()
    def start(self):
        """
        To start sunglasses use this method on your main file
        """
        print('1. search [ keyword ]')
        print('2. readfile-url [ index url ]')
        print('3. list-file')
        print('4. readfile-local')
        print('5. exit')
        print('6. help\n\n')

        # remove .google-cookie
        try:
            os.remove('.google-cookie')
        except:
            pass

        running = True
        while running:
            #listen for command
            ask = str(input('\ninput > '))

            if ask.split(" ")[0] == "search":
                #clear screen
                self.clear_screen()

                keyword = self.keyword_parser(ask.split(' '))
                print('You search for : ', keyword)
                result = self.search_url(keyword)
                print('\nResult : {} sites \n'.format(result))

            elif ask.split(" ")[0] == "readfile-url":
                self.clear_screen()
                self.read_file(ask.split(' ')[1])
            elif ask == "list-file":
                self.clear_screen()
                print(self.list_file())

            elif ask == "readfile-local":
                self.clear_screen()
                self.read_local()

            elif ask == "exit":
                print('Bye ^_^')
                running = False
            elif ask == "help":
                self.help()
            else:
                print('Unknown method')

if __name__ != '__main__':
    module = ModuleCode()