from ophyd import PVPositioner, EpicsSignal, EpicsSignalRO, EpicsMotor, Device
from bluesky.callbacks.mpl_plotting import LivePlot
from ophyd.status import Status
from ophyd import Component as Cpt
from bluesky.plans import scan, count
from bluesky import RunEngine
import bluesky.plan_stubs as bps
from bluesky.callbacks import LiveTable
from time import sleep

class Laser(PVPositioner):
    setpoint = Cpt(EpicsSignal, ':CYCLE')
    readback = Cpt(EpicsSignalRO, ':RBK')
    done = Cpt(EpicsSignalRO, ':DONE')
    done_value = 1

class Motor(Device):
    rotation = Cpt(EpicsMotor, ':ROT')
    tilt = Cpt(EpicsMotor, ':TILT')
    trans = Cpt(EpicsMotor, ':TRANS')
    
class Picoammeter(Device):
    readback = Cpt(EpicsSignal, ':rdCur')
    readRange = Cpt(EpicsSignalRO, ':rdCRng')
    setRange = Cpt(EpicsSignal, ':setCRng')

RE = RunEngine()

laserTest = Laser('laser', name="laserTest")
laserTest.wait_for_connection()
smaract = Motor('GRATING', name="smaract")
smaract.wait_for_connection()
meter = Picoammeter('Diode', name = "meter")
meter.wait_for_connection()

token = RE.subscribe(LiveTable(["meter_readback"]))

from databroker import Broker
db = Broker.named('temp')
RE.subscribe(db.insert)
scan_data, = RE(scan([meter.readback], smaract.rotation, -50000000, 50000000, 2000), LivePlot('meter_readback', 'smaract_rotation'))

header = db[scan_data]
wavelength = 650e-9

data = header.table()
time = data.time
rbk = data.meter_readback
rot = data.smaract_rotation

import pandas as pd
df = pd.DataFrame()
df['time'] = time
df['readback'] = rbk
df['angle'] = rot

df.to_csv('run_5.csv', index=False)

import numpy as np
import matplotlib.pyplot as plot
from scipy.signal import find_peaks

temp_rbk = rbk
    
peaks, _ = find_peaks(temp_rbk, prominence=2e-6)
plot.plot(rot/1e6, rbk, label = 'current')

pk_vals = [rbk[idx] for idx in peaks]
rot_vals = [rot[idx]/1e6 for idx in peaks]

plot.scatter(rot_vals, pk_vals, marker='x', color='red', label='peaks') 
plot.xlabel("Rotation [Deg]")
plot.ylabel("Current [A]")
plot.legend()

plot.savefig('run_5.png', format='png')

thetas = list(rot[peaks])
center = peaks[2]
center_theta = rot[center]
dtheta = []

for i in [0,1,3,4]:
    dtheta.append(abs((thetas[i] - center_theta) / 1e6))

m = [2,1,1,2]
grating_density = abs(1/(wavelength*(m/np.sin(dtheta))))

np.savetxt('grating_5.csv', grating_density)