from onvif import ONVIFCamera
import zeep
from time import sleep

#Подключаемся к устройству
mycam = ONVIFCamera('192.168.15.42', 80, 'login', 'password', 'C:/Users/profe/AppData/Local/Programs/Python/Python37/Lib/site-packages/wsdl')

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

#Создаём объект, через который будет передавать координаты камере
requesta = ptz.create_type('AbsoluteMove')
requesta.ProfileToken = media_profile.token
requesta.Position = status.Position

# Передаём координаты камере
requesta.Position.PanTilt.x = -1.0
requesta.Position.PanTilt.y = 1.0
requesta.Position.Zoom.x = 1.0
ptz.AbsoluteMove(requesta)
sleep(2)

#Выводим на экран текущие координаты камеры для проверки правильности перемещения
print ('Pan: ', status.Position.PanTilt.x)
print ('Tilt: ', status.Position.PanTilt.y)
print ('Zoom: ', status.Position.Zoom.x)



