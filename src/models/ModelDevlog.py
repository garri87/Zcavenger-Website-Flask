from entities.Devlog import Devlog

from datetime import datetime

import os

class ModelDevlog():
    
    @classmethod
    def create_devlog(self,db,title,text,media):
        try:

            createdate = datetime.now()
            
            fileDate = createdate.strftime("%Y%H%M%S")
            
            if media.filename is not '':
                mediaName = fileDate + "_" + media.filename
                media.save("src/uploads/"+mediaName)
            else:
                mediaName = None
                
            devlog = Devlog(title,text,mediaName)
            
            db.session.add(devlog)
            db.session.commit()
                         
            return devlog
            
        except Exception as ex:
            raise Exception(ex)