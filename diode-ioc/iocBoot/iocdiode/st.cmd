#!../../bin/linux-x86_64/diode

#- SPDX-FileCopyrightText: 2005 Argonne National Laboratory
#-
#- SPDX-License-Identifier: EPICS

#- You may have to change diode to something else
#- everywhere it appears in this file

#< envPaths

## Register all support components
dbLoadDatabase "../../dbd/diode.dbd"
diode_registerRecordDeviceDriver(pdbbase) 

## Load record instances
#dbLoadRecords("../../db/diode.db","user=iocadm")

iocInit()

## Start any sequence programs
#seq sncdiode,"user=iocadm"
