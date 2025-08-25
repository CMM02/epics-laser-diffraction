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

# Link QSRV (pvAccess Server) if available
ifdef EPICS_QSRV_MAJOR_VERSION
    ps_LIBS += qsrv
    ps_LIBS += $(EPICS_BASE_PVA_CORE_LIBS)
    ps_DBD += PVAServerRegister.dbd
    ps_DBD += qsrv.dbd
endif

# Finally link to the EPICS Base libraries
laser_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

