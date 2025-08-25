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

drvAsynIPPortConfigure("STAGE", "172.30.85.55:5000")

epicsEnvSet("STREAM_PROTOCOL_PATH", "${TOP}/gratingApp/Db/grating.proto")


iocInit()

## Start any sequence programs
#seq sncgrating,"user=iocadm"
