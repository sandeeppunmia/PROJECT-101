import os
import shutil
import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload(self,file_from,file_to):
        print(file_to)
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            print(files)
            for file_name in files:
                local_path = os.path.join(root,file_name)
                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to,relative_path)
                with open(local_path,'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))
            
def main():
    access_token = 'sl.AwO3n1mie3GsEINtlXl2MuJuA6q4iIyhn9ddKin8ikrM90bhZ_sI2nVTOCK-aY9qwBGkm95hPFLwsouqGP1U_uim6b3g7Fio7WIbWv57C0Ja-w5sh1xYzevihm6TDRhIWjU93Ow'
    transferData = TransferData(access_token)
    file_from = str(input("Enter the folder path to transfer"))
    file_to = input("Enter the full path to uload to dropbox")
    transferData.upload(file_from,file_to)
    print("File has been moved")

main()