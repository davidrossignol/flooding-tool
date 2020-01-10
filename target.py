import os
import IP2Location

class Target():
    def __init__(self, host, port=0):
        self.host = host
        self.port = port
        self.shortInfo = []
        self.allInfo = []
        self.ip2locInfo = []

    def isAlive(self):
        res = os.system("ping -c 1 " + self.host)
        if res == 0:
            print("Host %s is up!" % (self.host))
            return True
        else:
            print("Host %s is down!" % (self.host))
            return False

    def getInformation(self):
        ip2loc = IP2Location.IP2Location()
        ip2loc.open("data/IP-COUNTRY-REGION-CITY-LATITUDE-LONGITUDE-ZIPCODE-TIMEZONE-ISP-DOMAIN-NETSPEED-AREACODE-WEATHER-MOBILE-ELEVATION-USAGETYPE-SAMPLE.BIN")
        rec = ip2loc.get_all(self.host)
        
        self.ip2locInfo = rec

    def displayShortInfo(self):
        if self.ip2locInfo == []:
            self.getInformation()
            print("Country: %s " % self.ip2locInfo.country_short)
            print("Region: %s " % self.ip2locInfo.region)
            print("Timezone: %s " % self.ip2locInfo.timezone)
        else:
            print("Country: %s " % self.ip2locInfo.country_short)
            print("Region: %s " % self.ip2locInfo.region)
            print("Timezone: %s " % self.ip2locInfo.timezone)
        