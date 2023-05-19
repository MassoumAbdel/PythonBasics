import yaml

print('Prep steps: Loading the data to the current file...')
# please have your username and password  in config file
config_file = "config.yaml" # or you could give the full path of file
                    # example ../../data/config.yaml
with open(config_file,'r') as file:
     credentials = yaml.safe_load(file)

# print(credentials)
# print(credentials['username'])
# print(credentials['password'])
# print(credentials['host'])



print(credentials)

uname = credentials['username']
pword = credentials['password']
url = credentials['host']

print(' ****** Testing case started ***********')
print(f'Open the website: {url}')
print(f'Enter the user name {uname}')
print(f'Enter the password {pword}')
print(f'Click on Login button')
print('--------')
print(f'Main page opened !!!!')




