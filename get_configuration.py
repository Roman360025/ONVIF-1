from onvif import ONVIFCamera
import zeep

#Подключаемся к устройству
mycam = ONVIFCamera('192.168.15.42', 80, 'login', 'password', 'C:/Users/profe/AppData/Local/Programs/Python/Python37/Lib/site-packages/wsdl')

def zeep_pythonvalue(self, xmlvalue):
	return xmlvalue

zeep.xsd.simple.AnySimpleType.pythonvalue = zeep_pythonvalue

#Создаём сервис media
media = mycam.create_media_service()
#Создаём сервис PTZ
ptz = mycam.create_ptz_service()

#Получаем токены сервисов первого профайла
media_profile = media.GetProfiles()[0]
print(media_profile)
print()

# Проверим, отдаёт ли камера свои координаты PTZ
print('координаты PTZ')
print(ptz.GetStatus( media_profile.token))


