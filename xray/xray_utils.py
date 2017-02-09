import os, numpy as np
from matplotlib import pyplot as plt

def lambda_keV_to_nm(lambda_keV):
  '''Change the unit of wavelength from keV to nm.

  :param float lambda_keV: the wavelength in keV unit.
  :returns: the wavelength in nm unit.
  '''
  return 1.2398 / lambda_keV

def lambda_keV_to_angstrom(lambda_keV):
  '''Change the unit of wavelength from keV to angstrom.

  :param float lambda_keV: the wavelength in keV unit.
  :returns: the wavelength in angstrom unit.
  '''
  return 12.398 / lambda_keV

def lambda_nm_to_keV(lambda_nm):
  '''Change the unit of wavelength from nm to keV.

  :param float lambda_nm: the wavelength in nm unit.
  :returns: the wavelength in keV unit.
  '''
  return 1.2398 / lambda_nm

def lambda_angstrom_to_keV(lambda_angstrom):
  '''Change the unit of wavelength from angstrom to keV.

  :param float lambda_angstrom: the wavelength in angstrom unit.
  :returns: the wavelength in keV unit.
  '''
  return 12.398 / lambda_angstrom

def plot_xray_trans(mat='Al', ts=[1.0], rho=1.0, unit='keV', energy_lim=(1, 100), legfmt='%.1f', display=False):
  '''Plot the transmitted intensity of a X-ray beam through a given material.
  
  :param string mat: A string representing the material (e.g. 'Al')
  :param list ts: a list of thickness values of the material in mm ([1.0] by default)
  :param float rho: density of the material in g/cm^3 (1.0 by default)
  :param string unit: unit for the energy column (keV by default)
  :param tuple energy_lim: energy bounds in the plot (1, 100 by default)
  :param bool display: display or save an image of the plot (False by default)
  '''
  path = os.path.dirname(__file__)
  print path
  mu_rho = np.genfromtxt(os.path.join(path, 'data', mat + '.txt'), usecols = (0, 1), comments='#')
  energy = mu_rho[:,0]
  if unit == 'MeV':
    energy *= 1000
  legstr = '%%s %s mm' % legfmt
  for t in ts:
    # apply Beer-Lambert
    trans = 100*np.exp(-mu_rho[:,1]*rho*t/10)
    plt.plot(energy, trans, '-', linewidth=3, markersize=10, label=legstr % (mat, t))
  plt.xlim(energy_lim)
  plt.grid()
  plt.legend(loc='upper left')
  plt.xlabel('Photon Energy (keV)')
  plt.ylabel(r'Transmission $I/I_0$ (%)')
  if display:
    plt.show()
  else:
    plt.savefig('xray_trans_' + mat + '.png')
