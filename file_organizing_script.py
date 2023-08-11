'''
Original Folder Structure:
    multilabel
        -02
            - merged
                - mask00_abdominal_wall.png
                - mask00_colon.png
                ...
            - image00.png
            - image01.png
            ...
            - mask00_abdominal_wall.png
            - mask00_colon.png
            ...
        -03
        .
        .
        .
        -31

        
Organized Folder Structure:
    organized
        - image0
            - images
                - image0.png
            - masks
                - mask0_abdominal_wall.png
                - mask0_colon.png
                ...
        - image1
        ...
        - image1430

'''


import os
import shutil

if not os.path.exists('organized'):
    os.makedirs('organized')
else:
    shutil.rmtree(os.path.join(os.getcwd(), 'organized'))
    os.makedirs('organized')
rootdir = os.getcwd()
os.chdir('.\multilabel') 
dirs = os.listdir()
dirs.remove('.directory')

total_count = 0
for folder_name in dirs:
    source_folder = rootdir + f'\multilabel\{folder_name}'
    annotation_folder = rootdir + f'\multilabel\{folder_name}\merged'
    destination_folder = rootdir + '\organized'
    images = [f for f in os.listdir(source_folder) if f.lower().endswith('.png')]
    annotations = [f for f in os.listdir(annotation_folder) if f.lower().endswith('.png')]
    for image in images:
        if image.startswith('image'):
            original_count = image.split('.')[0].replace("image", "")
            total_count += 1
            new_file_name = f'image{total_count}.png'

            os.chdir(rootdir+'.\organized')
            os.makedirs(f'image{total_count}')
            os.chdir(rootdir+f'.\organized\image{total_count}')
            os.makedirs(f'images')
            os.makedirs(f'masks')

            source_file_path = os.path.join(source_folder, image)
            destination_file_path = os.path.join(destination_folder + f'\image{total_count}\images', new_file_name) 
            shutil.copy(source_file_path, destination_file_path)

            for mask_file in annotations:
                mask_name_split = mask_file.split('_')
                mask_count = mask_name_split[0].replace("mask", "")
                if original_count == mask_count:
                    new_file_name = f"mask{total_count}_{mask_name_split[1].split('.')[0]}.png"

                    source_file_path = os.path.join(source_folder, mask_file)
                    destination_file_path = os.path.join(destination_folder + f'\image{total_count}\masks', new_file_name) 
                    shutil.copy(source_file_path, destination_file_path)            
print(total_count)