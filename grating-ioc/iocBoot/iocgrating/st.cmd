#!../../bin/linux-x86_64/grating

#- SPDX-FileCopyrightText: 2005 Argonne National Laboratory
#-
#- SPDX-License-Identifier: EPICS

#- You may have to change grating to something else
#- everywhere it appears in this file

< envPaths

## Register all support components
dbLoadDatabase "../../dbd/grating.dbd"
grating_registerRecordDeviceDriver(pdbbase) 

## Load record instances
dbLoadRecords("../../gratingApp/Db/grating.db","user=iocadm")

# Configure controller
drvAsynIPPortConfigure("STAGE", "172.30.85.55:5000", 0, 0, 0)

# smarActMCSCreateController(const char *motorPortName, const char *ioPortName, int numAxes, double movingPollPeriod, double idlePollPeriod);
smarActMCSCreateController("STAGE_MOTOR", "STAGE", 3, 0.02, 1.0, 0)


# Controller port, axis number, controller channel
# smarActMCSCreateAxis(const char *motorPortName, int axisNumber, int channel)
smarActMCSCreateAxis("STAGE_MOTOR", 0, 0)
smarActMCSCreateAxis("STAGE_MOTOR", 1, 1)
smarActMCSCreateAxis("STAGE_MOTOR", 2, 2)



iocInit()

## Start any sequence programs
#seq sncgrating,"user=iocadm"
