#!../../bin/linux-x86_64/laser

#- SPDX-FileCopyrightText: 2005 Argonne National Laboratory
#-
#- SPDX-License-Identifier: EPICS

#- You may have to change laser to something else
#- everywhere it appears in this file

#< envPaths

## Register all support components
dbLoadDatabase "../../dbd/laser.dbd"
laser_registerRecordDeviceDriver(pdbbase) 

## Load record instances
#dbLoadRecords("../../db/laser.db","user=iocadm")

iocInit()

## Start any sequence programs
#seq snclaser,"user=iocadm"
