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

PROD_IOC = grating
# grating.dbd will be created and installed
DBD += grating.dbd

# grating.dbd will be made up from these files:
grating_DBD += base.dbd

# Include dbd files from all support applications:
#grating_DBD += xxx.dbd

# Add all the support libraries needed by this IOC
#grating_LIBS += xxx

# grating_registerRecordDeviceDriver.cpp derives from grating.dbd
grating_SRCS += grating_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
grating_SRCS_DEFAULT += gratingMain.cpp
grating_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#grating_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link QSRV (pvAccess Server) if available
ifdef EPICS_QSRV_MAJOR_VERSION
    ps_LIBS += qsrv
    ps_LIBS += $(EPICS_BASE_PVA_CORE_LIBS)
    ps_DBD += PVAServerRegister.dbd
    ps_DBD += qsrv.dbd
endif

# Finally link to the EPICS Base libraries
grating_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

