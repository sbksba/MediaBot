from module.Config_tools import ConfigSectionMap
from module.Notification import notification_media

if __name__=="__main__":
    media = ConfigSectionMap("MEDIABOT")['media']
    notification_media(media+"/Serie")
