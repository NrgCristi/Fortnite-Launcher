import psutil
import sys
import crayons

def get_colored_box(color, text):

    return f'{color("[")}{text}{color("]")}'

async def get_other_clients():

    log.debug('Looking for other running clients...')

    clients = []

    
            

    log.debug(f'Found {len(clients)} clients.')

    return clients

async def wait_for_game_spawn(process: psutil.Process, ignore: list):

    log.debug(f'Waiting for game to spawn...')

    while True:
        if process.is_running() == False:
            
        
                    
                




    

    
   

    

   

            print('Select a valid option! Try again\n')
            continue
        break

    webbrowser.open_new_tab(choosen_url)

    print(choosen_url)
    if user_logged == '1':
        print('An epic games page should be opened in your web brower. Paste the authorizationCode here:')
    
        print('An epic games page should be opened in your web brower. Login on the required account and then paste the authorizationCode here:')
    
    user_code = await aioconsole.ainput('> ')

    code = user_code.strip(' ')

    if code in ['cancel', 'c']:
        log.debug('add_account flow stopped. User cancelled')
        print('Account add cancelled')
        

    if len(code) != 32:
        log.debug('add_account flow stopped. The code from the user was invalid.')
        print(f'Failed account add. The code\'s lenght is invalid. A valid authorization code is 32 characters long.')
        

    

    auth_request = await Auth.authorization_code_auth(code)

    

        

        

        
        

        

        
            

        

        

    
        
        
        

async def remove_account():

    log.debug('remove_account flow started.')

    
    print(crayons.red('Remove Account', bold=True))

    while True:

        account_list = list(auths.keys())
        countlist = []
        count = 0

        for account in account_list:
            count += 1
            countlist.append(count)
            print(f'{get_colored_box(crayons.red, str(count))} {account}')

        print(f'{get_colored_box(crayons.green, "C")} Cancel\n')


        user_selection = await aioconsole.ainput(f'Select an account: ')

        try:
            user_selection.strip(' ')

            if user_selection.lower() in ['c', 'cancel']:
                print(crayons.red('Account remove cancelled.'))
                log.debug('remove_account flow cancelled by user.')
                

            if int(user_selection) not in countlist:
                print(crayons.red('Invalid selection\n'))
                continue

            
                break
        except:
            print(crayons.red('Select a valid option\n'))
            continue



    

        

        
            

        
        
        
    
    

        
        

        

            
            
           

            

                

                
                    

               
                
                

        

            
            print('Removing account from auths.json file anyway.')

            

            
                

            log.debug('remove_account flow failed successfully. Authentication failed but removed from auths.json anyways')

            print('Account removed.') # task failed successfully
            

    
async def launch_game(exchange_code: str, launch_command: str):

    log.debug('Launching game...')

    fortnite_path = configuration['fortnite_path']
    executable_args = launch_command
    additional_args = configuration["commandline_arguments"]

    log.debug('Manifest downloaded and processed correctly, preparing command line arguments')

    args = [
        executable_args,
        '-AUTH_LOGIN=unused',
        f'-AUTH_PASSWORD={exchange_code}',
        '-AUTH_TYPE=exchangecode',
        '-epicapp=Fortnite',
        '-epicenv=Prod',
        '-EpicPortal',
    ]

    for i in additional_args:
        if i.startswith('-'):
            args.append(i)

    ignore_list = await get_other_clients()

    log.debug(f'Starting FortniteLauncher.exe with args {args}...')

    FortniteLauncher = subprocess.Popen([f'{fortnite_path}/FortniteGame/Binaries/Win64/FortniteLauncher.exe'] + args, cwd=f'{fortnite_path}/FortniteGame/Binaries/Win64/', stdout=subprocess.DEVNULL)
    process = psutil.Process(pid = FortniteLauncher.pid)

    wait_spawn = await wait_for_game_spawn(process, ignore_list)

    if wait_spawn == True:

        log.debug('Game launched correctly.')
        

    

        log.debug('Game did\'nt launch.')
        


async def start():

    if '--debug' in sys.argv:
        coloredlogs.install(
            level='DEBUG'
        )

    while True:

        

        print(f'\n{crayons.cyan("Fortnite Launcher", bold=True)} | {crayons.white(f"Beta v{v}", bold=True)}\n')

        try:
            configuration = json.load(open('config.json', 'r', encoding = 'utf-8'))
        except Exception as e:
            print(f'An error ocurred loading config.json file. {e}')
            await aioconsole.ainput('Press ENTER to exit')

        try:
            auths = json.load(open('auths.json', 'r', encoding = 'utf-8'))
        except Exception as e:
            print(f'An error ocurred loading auths.json file. {e}')
            await aioconsole.ainput('Press ENTER to exit')

        account_list = list(auths.keys())
        countlist = []
        count = 0

        for account in account_list:
            count += 1
            countlist.append(count)
            print(f'{get_colored_box(crayons.green, str(count))} {account}')

        print(f'\n{get_colored_box(crayons.blue, "A")} Add an account')
        print(f'{get_colored_box(crayons.blue, "R")} Remove an account\n')
        print(f'{get_colored_box(crayons.red, "X")} Exit\n')

        user_selection = await aioconsole.ainput(f'Select an option: ')

        try:
            user_selection.strip(' ')

            if user_selection.lower() == 'x':
                exit()

            if user_selection.lower() == 'a':
                await add_account()
                continue

            if user_selection.lower() == 'r':
                if len(account_list) == 0:
                    print('There is no accounts to remove!\n')
                    continue
                
                
                    await remove_account()
                    continue

            if int(user_selection) not in countlist:
                print(crayons.red('Invalid selection\n'))
                continue

        except:
            print(crayons.red('Select a valid option\n'))
            continue

        selected_account = int(user_selection) - 1

        game_folder = configuration['fortnite_path']

        

            

            
                

            
            

            

                

                
                

                

                
                    

               

                

                    
                   

                    
                        

                    
                        
                    

                    


