# rohdeschwarz-plaground
Playground for scripts dealing with various Rohde &amp; Schwarz instruments.

## References
 * PyVISA [Documentation](http://pyvisa.readthedocs.io/en/latest/), [Code](https://github.com/pyvisa/pyvisa)
 * PyVISA-py [Documentation](http://pyvisa-py.readthedocs.io/en/latest/), [Code](https://github.com/pyvisa/pyvisa-py)
 * [R&S HMO1002 Series Digital Oscilloscope SCPI Programmers Manual](https://cdn.rohde-schwarz.com/pws/dl_downloads/dl_common_library/dl_manuals/gb_1/h/hmo1002_1202/HMO1002_1202_SCPI_ProgrammersManual_en_01.pdf)
 * [R&S HMP Series Power Supply SCPI Programmers Manual](https://cdn.rohde-schwarz.com/pws/dl_downloads/dl_common_library/dl_manuals/gb_1/h/hmp_serie/HMP_SCPI_ProgrammersManual_en_01.pdf)
 * [R&S HMC8012 Digital Multimeter SCPI Programmers Manual](https://cdn.rohde-schwarz.com/pws/dl_downloads/dl_common_library/dl_manuals/gb_1/h/hmc8012_1/HMC8012_SCPI_ProgrammersManual_en_01.pdf)

## Programs
 * `instrument-hello.sh` 
   * Shell script getting the device identification using telnet
   * Used SCPI commands: 
     * `*IDN?`
 * `instrument-hello.py`
   * Get and print the device identification using PyVISA and PyVISA-py
   * Used SCPI commands: i
     * `*IDN?`
     * `*WAI`
 * `hmo1002-screenshot.py`
   * Obtain and safe a screen shot in PNG format from a Rohde & Schwarz HMO1002 oscilloscope using PyVISA and PyVISA-py
   * Used SCPI commands: i
     * `*IDN?` 
     * `*WAI`
     * `HCOPY:FORMAT PNG`
     * `HCOPY:DATA?`
