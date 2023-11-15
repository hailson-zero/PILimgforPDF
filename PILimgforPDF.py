import os
import sys
from PIL import Image
import glob
from natsort import os_sorted

def PILimagforPDF(img_path):
    fse = sys.getfilesystemencoding()

    pdf_path = os.path.join(img_path,'pdf_files')
    print(pdf_path + '\n')
    if pdf_path not in glob.glob(os.path.join(img_path,'*')):
        try: 
            os.mkdir(pdf_path)
        except:
            print('The directory is invalid! \nRestart the program and try again.')

    manga_path = os_sorted(glob.glob(os.path.join(img_path,'*')))
    for folder in manga_path:
        check = False
        if pdf_path in folder:
            continue

        name = folder.split('\\')[-1]
        pdf_name = os.path.join(pdf_path, name + '.pdf')
        new_name = name.replace('[','(')
        new_name = new_name.replace(']',')')
        if new_name != name:
            name = new_name
            new_path = os.path.join('\\'.join(folder.split('\\')[:-1]), name)
            os.rename(folder, new_path)
            folder = new_path
            pdf_name = os.path.join(pdf_path, name + '.pdf')
        
        if pdf_name in glob.glob(os.path.join(pdf_path,'*')):
            check = True
            continue

        images = []
        img_dir = os.path.join(folder,'*')
        print(name)
        img_files = os_sorted(glob.glob(u'{}'.format(img_dir)))
        for img_file in img_files:
            if img_file.endswith(('.jpg', '.JPG', '.jpeg', '.png', '.PNG', '.gif', '.webp')):
                try:
                    images.append(Image.open(img_file).convert("RGB"))
                except:
                    print ('Unable to convert this file:' + img_file)
            else:
                print ('Unable to convert this file:' + img_file)
                    
        if check == True:
            continue
        if images:
            images[0].save(pdf_name, save_all=True, append_images=images[1:])
    return   

manga_path = input('Enter the Directory: ')
PILimagforPDF(manga_path)
input('Complete\nPress enter to close')