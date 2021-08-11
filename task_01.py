import os

dic_01 = ["my_project", "settings", "mainapp", "adminapp", "authapp"]
dir_path = os.path.join(dic_01[0])
if not os.path.exists(dir_path):
    os.mkdir(dir_path)
os.chdir(dir_path)
for i in range(1, len(dic_01)):
    if not os.path.exists(dic_01[i]):
        os.makedirs(dic_01[i])
