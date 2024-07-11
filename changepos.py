import os
import shutil
import stat
def remove_readonly(func, path):
    # Change the file to writable and then reattempt the removal
    os.chmod(path, stat.S_IWRITE)
    
    
outer_list = []

directory_path = "C:\\Users\\Nirox\\Desktop\\Projects"
file_list = os.listdir(directory_path)
#if there was any .py file remove them from directory
for outer in file_list:
    if outer.find('.py') != -1:
        file_list.remove(outer)
#pick all existing files in the directory of another directory
for i in file_list:
    innerfile = os.listdir(i)
    for j in innerfile:
        print(j)
        shutil.move(f'{i}/{j}',directory_path)





