from datetime import datetime
import settings
import os

def upload_profile_img(user=None,new_profileimg=None):
    now = datetime.now()                
    file_date = now.strftime("%Y%H%M%S")  
    if new_profileimg.filename != "":
        new_profileimg_name = file_date + "_" + new_profileimg.filename
        
        file_path, file_extension = os.path.splitext(os.path.join(settings.UPLOADS_FOLDER, new_profileimg_name))
        
        if file_extension in settings.UPLOAD_EXTENSIONS:
            if user:
                if user.profileimg != "":
                    os.remove(os.path.join(file_path, user.profileimg))
                    user.profileimg = new_profileimg_name   
                new_profileimg.save(file_path + new_profileimg_name)

            else:
                new_profileimg.save(file_path + new_profileimg_name)

                return new_profileimg_name
            
        else:
            print(f"Format {file_extension} is not supported")
       