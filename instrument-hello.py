import visa
import sys

def main():
  instrument_address = getInstrumentAddress()
  rm = visa.ResourceManager('@py')
  instrument = rm.open_resource("TCPIP::{ip}".format(ip = instrument_address))
  identification = instrument.query("*IDN?")
  instrument.write("*WAI");

  parseAndPrintIdentification(identification)

def getInstrumentAddress():
  if len(sys.argv) != 2:
    print("instrument address missing")  
    sys.exit(1)
  return sys.argv[1]

def parseAndPrintIdentification(identification):
  manufacturer, model, serial, firmware = identification.split(',')
  print("Manufacturer:      {}".format(manufacturer))
  print("Device type:       {}".format(model))
  print("Serial number:     {}".format(serial))
  print("Firmware version:  {}".format(firmware))

if __name__ == '__main__':
  main()
