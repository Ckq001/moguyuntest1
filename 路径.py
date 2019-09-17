import os

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, 'config.ini')
print (proDir)
print (configPath)