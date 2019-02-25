from onvif import ONVIFCamera
import zeep

mycam = ONVIFCamera('192.168.15.44', 80, 'admin', 'Supervisor', 'C:/Users/profe/AppData/Local/Programs/Python/Python37/Lib/site-packages/wsdl')

def zeep_pythonvalue(self, xmlvalue):
	return xmlvalue

zeep.xsd.simple.AnySimpleType.pythonvalue = zeep_pythonvalue

#Получение токенов сервисов
print ('Токены сервисов')
media_service = mycam.create_media_service()
print (media_service.GetProfiles())

#Получение пределов координат PTZ, а также узанём, поддерживает ли камера absolute move
#и способна ли камера устанавливать значение фокуса вручную
print ('Получение информации о камере')
ptz_service = mycam.create_ptz_service()
print (ptz_service.GetNodes())

#Получаем значение координат камеры, а также значение фокуса
print('Координаты камеры, значение фокуса камеры')
print(ptz_service.GetStatus('protoken_1'))