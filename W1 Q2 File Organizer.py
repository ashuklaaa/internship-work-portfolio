import os
import shutil

directory='./'

file_types={
    "images":[".jpg",".jpeg",".png",".gif"],
    "documents":[".pdf",".docx",".txt"],
    "videos":[".mp4",".mkv",".flv"],
    "audio":[".mp3",".wav"],
    "archives":[".zip",".tar",".rar"],
    "spreadsheets":[".xls",".xlsx",".csv"]
}
def create_folders(base_dir,folders):
    for folder in folders:
        folder_path=os.path.join(base_dir,folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

def organise_files_by_type(base_dir,file_types):
    for filename in os.listdir(base_dir):
        file_path=os.path.join(base_dir,filename)

        if os.path.isdir(file_path):
            continue
        
        file_ext=os.path.splitext(filename)[1].lower()
        for folder,extensions in file_types.items():
            if file_ext in extensions:
                target_folder= os.path.join(base_dir,folder)
                shutil.move(file_path,target_folder)
                print(f"Moved (filename) to (folder)")
                break

create_folders(directory,file_types.keys())
organise_files_by_type(directory,file_types)



    

