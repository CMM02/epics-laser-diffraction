# SPDX-FileCopyrightText: 2003 Argonne National Laboratory
#
# SPDX-License-Identifier: EPICS

TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = laser
# laser.dbd will be created and installed
DBD += laser.dbd

# laser.dbd will be made up from these files:
laser_DBD += base.dbd
laser_DBD += asyn.dbd
laser_DBD += stream-base.dbd
laser_DBD += drvAsynIPPort.dbd

laser_LIBS += stream
laser_LIBS += asyn

# Include dbd files from all support applications:
#laser_DBD += xxx.dbd

# Add all the support libraries needed by this IOC
#laser_LIBS += xxx

# laser_registerRecordDeviceDriver.cpp derives from laser.dbd
laser_SRCS += laser_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
laser_SRCS_DEFAULT += laserMain.cpp
laser_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#laser_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
laser_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

