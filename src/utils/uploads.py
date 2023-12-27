from datetime import datetime
import settings
import os
from flask import flash, current_app


def upload_image(image, user = None, post = None, comment = None):     
    """Uploads a file to storage and replace existing file in given table

    Args:
        image (_type_): _description_
        user (_type_, optional): _description_. Defaults to None.
        post (_type_, optional): _description_. Defaults to None.
        comment (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: name of the file 
    """
    file_date = datetime.now().strftime("%Y%H%M%S")  
    
    if image.filename != "":
    
        new_image_name = file_date + "_" + image.filename
        
        file_path, _ = os.path.split(current_app.config['UPLOADS_FOLDER'])
        file_path = os.path.join(file_path, new_image_name)

        file_path, file_extension = os.path.splitext(file_path)
        
        if file_extension in current_app.config['UPLOAD_EXTENSIONS']:
            if user:
                check_existing(user.profileimg)
            elif post:
                check_existing(post.media)
            elif comment: check_existing(comment.media)

            image.save(os.path.join(current_app.config['UPLOADS_FOLDER'], new_image_name))

            return new_image_name
            
        else:
            print(f"Format {file_extension} is not supported")
   
    def check_existing(column_name):
        """Check if exist a file in the column and replace for the new file

        Args:
            column_name (_type_): name of the column that contains image filename
        """
        if column_name != "":
            try:
                os.remove(os.path.join(current_app.config['UPLOADS_FOLDER'], column_name))
                    
            except FileNotFoundError as file_not_found:
                print("File not found in " + file_path + ". " + str(file_not_found))

            except Exception as ex:
                print("Exception: " + str(ex))

       