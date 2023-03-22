import os
import shutil

def delete_extra_folders():
    
    num_of_extra_folders= 0
    for root, dirname, filenames in os.walk('/kaggle/input'):
    #print(os.path.join(dirname, filename))
        for dir in dirname:
            if (dir=='extra' or dir=='Extra'):
                num_of_extra_folders = num_of_extra_folders+1
                file_path = os.path.join(root,dir)
                if os.path.exists(file_path):
                    shutil.rmtree(file_path)  
    return num_of_extra_folders