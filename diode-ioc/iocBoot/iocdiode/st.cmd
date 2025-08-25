#!../../bin/linux-x86_64/diode

#- SPDX-FileCopyrightText: 2005 Argonne National Laboratory
#-
#- SPDX-License-Identifier: EPICS

#- You may have to change diode to something else
#- everywhere it appears in this file

< envPaths

epicsEnvSet("STREAM_PROTOCOL_PATH", "${TOP}/db/")

## Register all support components
dbLoadDatabase "../../dbd/diode.dbd"
diode_registerRecordDeviceDriver(pdbbase) 

## Load record instances
#dbLoadRecords("../../db/diode.db","user=iocadm")

drvAsynIPPortConfigure("KEYSIGHT", "172.30.85.75:5024")


dbLoadRecords("../../db/diode-ioc.db")
iocInit()

## Start any sequence programs
#seq sncdiode,"user=iocadm"
