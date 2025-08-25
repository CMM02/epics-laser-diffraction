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

PROD_IOC = diode
# diode.dbd will be created and installed
DBD += diode.dbd

diode_DBD += base.dbd
diode_DBD += stream-base.dbd
diode_DBD += asyn.dbd
diode_DBD += drvAsynIPPort.dbd


# diode.dbd will be made up from these files:
diode_DBD += base.dbd

# Include dbd files from all support applications:
#diode_DBD += xxx.dbd

# Add all the support libraries needed by this IOC
#diode_LIBS += xxx
diode_LIBS += stream
diode_LIBS += asyn

# diode_registerRecordDeviceDriver.cpp derives from diode.dbd
diode_SRCS += diode_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
diode_SRCS_DEFAULT += diodeMain.cpp
diode_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#diode_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link QSRV (pvAccess Server) if available
ifdef EPICS_QSRV_MAJOR_VERSION
    ps_LIBS += qsrv
    ps_LIBS += $(EPICS_BASE_PVA_CORE_LIBS)
    ps_DBD += PVAServerRegister.dbd
    ps_DBD += qsrv.dbd
endif

# Finally link to the EPICS Base libraries
diode_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

