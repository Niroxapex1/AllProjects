import os
import shutil
import stat
def remove_readonly(func, path):
    # Change the file to writable and then reattempt the removal
    os.chmod(path, stat.S_IWRITE)
    
    
outer_list = []

directory_path = "C:\\Users\\Nirox\\Desktop\\Projects"
file_list = os.listdir(directory_path)

for outer in file_list:
    if outer.find('.py') != -1:
        file_list.remove(outer)
for i in file_list:
    innerfile = os.listdir('C:\\Users\\Nirox\\Desktop\\Projects\\'+i)
    for j in innerfile:
        if j.find('.git') != -1:
            shutil.rmtree('C:\\Users\\Nirox\\Desktop\\Projects\\'+i+'\\'+'.git',onerror=remove_readonly)
   




