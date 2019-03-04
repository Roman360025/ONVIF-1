from onvif import ONVIFCamera
import zeep
from time import sleep

#Подключаемся к устройству
mycam = ONVIFCamera('192.168.15.55', 8999, 'login', 'password', 'C:/Users/profe/AppData/Local/Programs/Python/Python37/Lib/site-packages/wsdl')

#Без кода ниже программа не работает 
def zeep_pythonvalue(self, xmlvalue):
    return xmlvalue

zeep.xsd.simple.AnySimpleType.pythonvalue = zeep_pythonvalue

#Создаём сервис media
media = mycam.create_media_service()
#Создаём сервис PTZ
ptz = mycam.create_ptz_service()

#Получаем необходимые токены
media_profile = media.GetProfiles()[0]

#Получаем текущий статус PTZ
status = ptz.GetStatus({'ProfileToken': media_profile.token})

#Создаём объект, через который будем осуществлять движение камеры
request = ptz.create_type('ContinuousMove')
request.ProfileToken = media_profile.token
request.Velocity = status.Position

def continuous_move(timeout):
    #Начинаем continuous move
    ptz.ContinuousMove(request)
    # Ждём нужное количество времени
    sleep(timeout)
    # По истечении времени прекращаем Continuous move
    ptz.Stop(media_profile.token)

def move_tilt(velocity, timeout):
    request.Velocity.PanTilt.x = 0.0
    request.Velocity.PanTilt.y = velocity
    continuous_move(timeout)

def move_pan(velocity, timeout):
    request.Velocity.PanTilt.x = velocity
    request.Velocity.PanTilt.y = 0.0
    continuous_move(timeout)

def zoom(velocity, timeout):
    request.Velocity.Zoom.x = velocity
    continuous_move(timeout)

#Укажем необходимые данные для осуществления Continuous move
# Уменьшим zoom
zoom(-1, 2)

# Движение вправо
move_pan(-1, 2)

# Движение влево
move_pan(1, 2)

# Движение вверх
move_tilt(-1, 2)

# Движение вниз
move_tilt(1, 2)






