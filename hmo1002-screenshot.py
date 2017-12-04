import visa
import sys

def main():
  instrument_address = getInstrumentAddress()
  rm = visa.ResourceManager('@py')
  instrument = rm.open_resource("TCPIP::{ip}".format(ip = instrument_address))
  print(instrument.query("*IDN?"))
  instrument.write("*WAI");

  instrument.write("HCOPY:FORMAT PNG")
  instrument.write("HCOPY:DATA?")
  screenshot = instrument.read_raw()
  header_length = 2 + int(screenshot[1:2])
  
  f = open('screenshot.png', 'wb')
  f.write(screenshot[header_length:])
  f.close()

  instrument.close()

def getInstrumentAddress():
  if len(sys.argv) != 2:
    print("instrument address missing")  
    sys.exit(1)
  return sys.argv[1]

if __name__ == '__main__':
  main()
