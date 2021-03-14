import pyexiv2
import _caesarHandler

class _modifyEXIF:
    def __init__(self,str):
        self.metadata = pyexiv2.ImageMetadata(str)
        self.metadata.read()

    def ModifyTime(self,datetime):

        tag1=self.metadata['Exif.Image.DateTime']

        tag2=self.metadata['Exif.Photo.DateTimeOriginal']

        tag3=self.metadata['Exif.Photo.DateTimeDigitized']

        print tag1.raw_value
        print tag2.raw_value
        print tag3.raw_value

        tag1.raw_value=datetime
        tag2.raw_value=datetime
        tag3.raw_value=datetime

        self.metadata.write()

    def ModifyGps(self,gps):

        lon=self.metadata['Exif.GPSInfo.GPSLongitude']
        lonref=self.metadata['Exif.GPSInfo.GPSLongitudeRef']
        lat=self.metadata['Exif.GPSInfo.GPSLatitude']
        latref = self.metadata['Exif.GPSInfo.GPSLatitudeRef']

        gpslist=gps.split(",")

        if gpslist[0]<0:
            lonref.raw_value = 'W'
        else:
            lonref.raw_value = 'E'
        if gpslist[1] < 0:
            latref.raw_value = 'S'
        else:
            latref.raw_value = 'N'

        lat.raw_value=self.ConvertToCoordinate(float(gpslist[0]))
        lon.raw_value=self.ConvertToCoordinate(float(gpslist[1]))

            #lon.raw_value=str(_caesarHandler.encryptOrdecrypt(str(self.ConvertToCoordinate(float(gpslist[1]))),'encrypt',key))

        self.metadata.write()
        #print lon.raw_value
        #print lonref.raw_value
        #print lat.raw_value
        #print latref.raw_value

    def ConvertToCoordinate(self,gps):
        gpsCoordinate=''
        gps*=3600*10000

        try:
            seconds = int(gps / 10000)
            minutes = int(gps % 10000)
        except:
            seconds = 0.0

        try:
            minutes/=60
            degrees = int(minutes % 10000)
            minutes = int(minutes / 10000)
        except:
            minutes = 0.0

        degrees/=60

        gpsCoordinate = str(degrees)+'/10000 '+str(minutes)+'/1 '+str(seconds)+'/1'
        #print gpsCoordinate

        return gpsCoordinate

    def ModifyModel(self, model):

        tag1 = self.metadata['Exif.Image.Model']

        print tag1.raw_value

        tag1.raw_value = model

        self.metadata.write()

    def ModifyMake(self, make):
        tag1 = self.metadata['Exif.Image.Make']

        print tag1.raw_value

        tag1.raw_value = make

        self.metadata.write()