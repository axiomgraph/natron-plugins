# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named Ls_nail_GLExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from Ls_nail_GLExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.Ls_nail_GL"

def getLabel():
    return "Ls_nail_GL"

def getVersion():
    return 1.0

def getIconPath():
    return "Ls_nail_GL.png"

def getGrouping():
    return "Community/GLSL/Distort"

def getPluginDescription():
    return "Warp an area of the Source and Mask to follow a track.\n( http://youtube.com/watch?v=GOQAAb9NqAM )"

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group
    lastNode.setColor(0.07451, 0.5686, 0.4863)

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "Controls")
    param = lastNode.createStringParam("sep01", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep01 = param
    del param

    param = lastNode.createStringParam("sep02", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep02 = param
    del param

    param = lastNode.createSeparatorParam("PASTE_TRACKS", "Paste tracks here")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.PASTE_TRACKS = param
    del param

    param = lastNode.createStringParam("sep03", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep03 = param
    del param

    param = lastNode.createStringParam("sep04", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep04 = param
    del param

    param = lastNode.createDouble2DParam("Shadertoy1_2paramValueVec20", "Nail from : ")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueVec20 = param
    del param

    param = lastNode.createStringParam("sep05", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep05 = param
    del param

    param = lastNode.createDouble2DParam("Shadertoy1_2paramValueVec21", "Nail to : ")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueVec21 = param
    del param

    param = lastNode.createStringParam("sep06", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep06 = param
    del param

    param = lastNode.createStringParam("sep07", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep07 = param
    del param

    param = lastNode.createSeparatorParam("MANUAL_TRACK", "Manual track")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.MANUAL_TRACK = param
    del param

    param = lastNode.createStringParam("sep08", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep08 = param
    del param

    param = lastNode.createStringParam("sep09", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep09 = param
    del param

    param = lastNode.createDoubleParam("offsetX", "Offset x : ")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(-2048, 0)
    param.setDisplayMaximum(2048, 0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    param.setValue(111, 0)
    lastNode.offsetX = param
    del param

    param = lastNode.createStringParam("sep10", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep10 = param
    del param

    param = lastNode.createDoubleParam("offsetY", "Offset x : ")
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(-2048, 0)
    param.setDisplayMaximum(2048, 0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.offsetY = param
    del param

    param = lastNode.createStringParam("sep11", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep11 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy1_2paramValueBool3", "Tracks are pixels : ")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueBool3 = param
    del param

    param = lastNode.createStringParam("sep12", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep12 = param
    del param

    param = lastNode.createStringParam("sep13", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep13 = param
    del param

    param = lastNode.createSeparatorParam("AMOUNT", "Amount")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.AMOUNT = param
    del param

    param = lastNode.createStringParam("sep14", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep14 = param
    del param

    param = lastNode.createStringParam("sep15", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep15 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat4", "Extra push : ")
    param.setDisplayMinimum(-300, 0)
    param.setDisplayMaximum(300, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat4 = param
    del param

    param = lastNode.createStringParam("sep16", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep16 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat5", "Nail strength : ")
    param.setDisplayMinimum(-300, 0)
    param.setDisplayMaximum(300, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat5 = param
    del param

    param = lastNode.createStringParam("sep17", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep17 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat6", "Edge swoop : ")
    param.setMinimum(0, 0)
    param.setMaximum(1, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(0.7, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat6 = param
    del param

    param = lastNode.createStringParam("sep18", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep18 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy1_2paramValueBool7", "Matte is target : ")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueBool7 = param
    del param

    param = lastNode.createStringParam("sep19", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep19 = param
    del param

    param = lastNode.createStringParam("sep20", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep20 = param
    del param

    param = lastNode.createSeparatorParam("OVERLAY", "Overlay")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.OVERLAY = param
    del param

    param = lastNode.createStringParam("sep21", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep21 = param
    del param

    param = lastNode.createStringParam("sep22", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep22 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy1_2paramValueBool8", "Overlay : ")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueBool8 = param
    del param

    param = lastNode.createStringParam("sep23", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep23 = param
    del param

    param = lastNode.createColorParam("Shadertoy1_2paramValueVec39", "Nail area tint : ", False)
    param.setDefaultValue(0.33, 0)
    param.restoreDefaultValue(0)
    param.setDefaultValue(0.27, 1)
    param.restoreDefaultValue(1)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueVec39 = param
    del param

    param = lastNode.createStringParam("sep24", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep24 = param
    del param

    param = lastNode.createStringParam("sep25", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep25 = param
    del param

    lastNode.Credits = lastNode.createPageParam("Credits", "Credits")
    param = lastNode.createStringParam("sep101", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep101 = param
    del param

    param = lastNode.createStringParam("sep102", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep102 = param
    del param

    param = lastNode.createSeparatorParam("NAME", "Ls_nail_GL v1.0")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.NAME = param
    del param

    param = lastNode.createStringParam("sep103", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep103 = param
    del param

    param = lastNode.createStringParam("sep104", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep104 = param
    del param

    param = lastNode.createSeparatorParam("LINE01", "")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.LINE01 = param
    del param

    param = lastNode.createStringParam("sep105", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep105 = param
    del param

    param = lastNode.createStringParam("sep106", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep106 = param
    del param

    param = lastNode.createSeparatorParam("FR", "ShaderToy 0.8.8")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.FR = param
    del param

    param = lastNode.createStringParam("sep107", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep107 = param
    del param

    param = lastNode.createStringParam("sep108", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep108 = param
    del param

    param = lastNode.createSeparatorParam("CONVERSION", " (Fabrice Fernandez - 2018)")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.CONVERSION = param
    del param

    param = lastNode.createStringParam("sep109", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep109 = param
    del param

    param = lastNode.createStringParam("sep110", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep110 = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Credits', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output2"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output2")
    lastNode.setPosition(4139, 4048)
    lastNode.setSize(80, 44)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput2 = lastNode

    del lastNode
    # End of node "Output2"

    # Start of node "Source"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Source")
    lastNode.setLabel("Source")
    lastNode.setPosition(4139, 3645)
    lastNode.setSize(80, 44)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupSource = lastNode

    del lastNode
    # End of node "Source"

    # Start of node "Shadertoy1_2"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("Shadertoy1_2")
    lastNode.setLabel("Shadertoy1_2")
    lastNode.setPosition(4139, 3881)
    lastNode.setSize(80, 44)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupShadertoy1_2 = lastNode

    param = lastNode.getParam("paramValueVec20")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        del param

    param = lastNode.getParam("paramValueVec21")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        del param

    param = lastNode.getParam("paramValueVec22")
    if param is not None:
        param.setValue(111, 0)
        param.setValue(0, 1)
        del param

    param = lastNode.getParam("paramValueBool3")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramValueFloat4")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramValueFloat5")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramValueFloat6")
    if param is not None:
        param.setValue(0.7, 0)
        del param

    param = lastNode.getParam("paramValueBool7")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramValueBool8")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramValueVec39")
    if param is not None:
        param.setValue(0.33, 0)
        param.setValue(0.27, 1)
        param.setValue(0, 2)
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("//\n//\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//                        MM.                          .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                     MM.  .MMMM        MMMMMMM    MMM.  .MM\n//                    MM.  .MMM           MMMMMM     MMM.  .MM\n//                   MM.  .MmM              MMMM      MMM.  .MM\n//                  MM.  .MMM                 MM       MMM.  .MM\n//                 MM.  .MMM                   M        MMM.  .MM\n//                MM.  .MMM                              MMM.  .MM\n//                 MM.  .MMM                            MMM.  .MM\n//                  MM.  .MMM       M                  MMM.  .MM\n//                   MM.  .MMM      MM                MMM.  .MM\n//                    MM.  .MMM     MMM              MMM.  .MM\n//                     MM.  .MMM    MMMM            MMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                        MM.                          .MM\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//\n//\n//\n//\n// Adaptation pour Natron par F. Fernandez\n// Code original : Ls_nail Matchbox pour Autodesk Flame\n\n// Adapted to Natron by F.Fernandez\n// Original code : Ls_nail Matchbox for Autodesk Flame\n\n// iChannel0: Source, filter = linear, wrap = clamp\n// iChannel1: Mask, filter = linear, wrap = clamp\n// iChannel2: Nail Mask, filter=nearest, wrap=clamp\n// BBox: iChannel0\n\n// Transforms the area inside the nail matte by the difference between two tracks\n// Use to stick down floating CG, by nailing from a track on the CG to a track on the BG\n// lewis@lewissaunders.com\n// TODO:\n//  o Anti-aliased overlay\n//  o Rotate, scale, shear?\n//  o Better filtering probably.  Not sure if EWA would work because no dFdx?\n\n\n\nuniform vec2 trackfrom = vec2(0.0,0.0); // Nail from : (Nail this point...)\nuniform vec2 trackto = vec2(0.0,0.0); // Nail to : (...to this point)\nuniform vec2 offset = vec2(0.0,0.0); // Offset : (offset)\n\nuniform bool tracksarepixels = true; // Tracks are pixels : \n\nuniform float extra = 1.0; // Extra push : \nuniform float amount = 1.0; // Nail strength : \nuniform float edgeswoop = 0.7; // Edge swoop : \n\nuniform bool matteistarget = true; // Matte is target, not source : \n\n\nuniform bool overlay = false; // Overlay : (overlay)\n\nuniform vec3 areatint = vec3(0.33,0.27,0.0);\n\nfloat distanceToSegment(vec2 p0, vec2 p1, vec2 p) {\n\tvec2 v = p1 - p0;\n\tvec2 w = p - p0;\n\tfloat c1 = dot(w, v);\n\tfloat c2 = dot(v, v);\n\n\tif(c1 <= 0.0)\n\t\treturn length(p0 - p);\n\tif(c2 <= c1)\n\t\treturn length(p1 - p);\n\n\tfloat b = c1 / c2;\n\tvec2 pb = p0 + b * v;\n\treturn length(pb - p);\n}\n\nvoid mainImage( out vec4 fragColor, in vec2 fragCoord )\n{\n\tvec2 res = vec2(iResolution.x, iResolution.y);\n\tvec2 coords = fragCoord.xy / res;\n\n\tvec2 diff = trackto - trackfrom + offset;\n\tdiff *= extra;\n\tdiff *= amount;\n\n\tif(tracksarepixels) {\n\t\tdiff /= res;\n\t}\n\n\tfloat coeff = 0.0;\n\tif(matteistarget) {\n\t\tcoeff = texture2D(iChannel2, coords).b;\n\t} else {\n\t\tcoeff = texture2D(iChannel2, coords - diff).b;\n\t}\n\tcoeff = mix(coeff, smoothstep(0.0, 1.0, coeff), edgeswoop);\n\tdiff *= coeff;\n\n\tvec2 q = coords - diff;\n\n\tvec3 o = texture2D(iChannel0, q).rgb;\n\tfloat m = texture2D(iChannel1, q).b;\n\n\tif(overlay) {\n\t\tvec2 trackfromp = trackfrom;\n\t\tvec2 tracktop = trackto;\n\t\tvec2 offsetp = offset;\n\t\tvec2 coordsp = coords * res;\n\n\t\tif(!tracksarepixels) {\n\t\t\ttrackfromp *= res;\n\t\t\ttracktop *= res;\n\t\t\toffsetp *= res;\n\t\t}\n\n\t\tif(length(coordsp - trackfromp) < 5.0)\n\t\t\to = vec3(0.8, 0.2, 0.2);\n\n\t\tif(length(coordsp - tracktop) < 5.0)\n\t\t\to = vec3(0.2, 0.8, 0.2);\n\n\t\tif(length(offsetp) > 0.0) {\n\t\t\tif(length(coordsp - (tracktop + offsetp)) < 5.0) {\n\t\t\t\to = vec3(0.2, 0.2, 0.8);\n\t\t\t}\n\t\t}\n\n\t\tif(distanceToSegment(trackfromp, tracktop + offsetp, coordsp) < 1.0) {\n\t\t\tif(mod(length(trackfromp - coordsp), 8.0) < 4.0) {\n\t\t\t\to = vec3(0.4, 0.4, 0.8);\n\t\t\t}\n\t\t}\n\t\to += coeff * areatint;\n\t}\n\n\tfragColor = vec4(o, m);\n}\n")
        del param

    param = lastNode.getParam("mipmap0")
    if param is not None:
        param.set("linear")
        del param

    param = lastNode.getParam("wrap0")
    if param is not None:
        param.set("clamp")
        del param

    param = lastNode.getParam("inputLabel0")
    if param is not None:
        param.setValue("Source")
        del param

    param = lastNode.getParam("mipmap1")
    if param is not None:
        param.set("linear")
        del param

    param = lastNode.getParam("wrap1")
    if param is not None:
        param.set("clamp")
        del param

    param = lastNode.getParam("inputLabel1")
    if param is not None:
        param.setValue("Mask")
        del param

    param = lastNode.getParam("mipmap2")
    if param is not None:
        param.set("nearest")
        del param

    param = lastNode.getParam("inputLabel2")
    if param is not None:
        param.setValue("Nail Mask")
        del param

    param = lastNode.getParam("inputEnable3")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("iChannel0")
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("mouseParams")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramCount")
    if param is not None:
        param.setValue(10, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("vec2")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("trackfrom")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("Nail from :")
        del param

    param = lastNode.getParam("paramHint0")
    if param is not None:
        param.setValue("Nail this point...")
        del param

    param = lastNode.getParam("paramType1")
    if param is not None:
        param.set("vec2")
        del param

    param = lastNode.getParam("paramName1")
    if param is not None:
        param.setValue("trackto")
        del param

    param = lastNode.getParam("paramLabel1")
    if param is not None:
        param.setValue("Nail to :")
        del param

    param = lastNode.getParam("paramHint1")
    if param is not None:
        param.setValue("...to this point")
        del param

    param = lastNode.getParam("paramType2")
    if param is not None:
        param.set("vec2")
        del param

    param = lastNode.getParam("paramName2")
    if param is not None:
        param.setValue("offset")
        del param

    param = lastNode.getParam("paramLabel2")
    if param is not None:
        param.setValue("Offset :")
        del param

    param = lastNode.getParam("paramHint2")
    if param is not None:
        param.setValue("offset")
        del param

    param = lastNode.getParam("paramType3")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName3")
    if param is not None:
        param.setValue("tracksarepixels")
        del param

    param = lastNode.getParam("paramLabel3")
    if param is not None:
        param.setValue("Tracks are pixels :")
        del param

    param = lastNode.getParam("paramDefaultBool3")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramType4")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName4")
    if param is not None:
        param.setValue("extra")
        del param

    param = lastNode.getParam("paramLabel4")
    if param is not None:
        param.setValue("Extra push :")
        del param

    param = lastNode.getParam("paramDefaultFloat4")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramType5")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName5")
    if param is not None:
        param.setValue("amount")
        del param

    param = lastNode.getParam("paramLabel5")
    if param is not None:
        param.setValue("Nail strength :")
        del param

    param = lastNode.getParam("paramDefaultFloat5")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramType6")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName6")
    if param is not None:
        param.setValue("edgeswoop")
        del param

    param = lastNode.getParam("paramLabel6")
    if param is not None:
        param.setValue("Edge swoop :")
        del param

    param = lastNode.getParam("paramDefaultFloat6")
    if param is not None:
        param.setValue(0.7, 0)
        del param

    param = lastNode.getParam("paramType7")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName7")
    if param is not None:
        param.setValue("matteistarget")
        del param

    param = lastNode.getParam("paramLabel7")
    if param is not None:
        param.setValue("Matte is target")
        del param

    param = lastNode.getParam("paramDefaultBool7")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramType8")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName8")
    if param is not None:
        param.setValue("overlay")
        del param

    param = lastNode.getParam("paramLabel8")
    if param is not None:
        param.setValue("Overlay :")
        del param

    param = lastNode.getParam("paramHint8")
    if param is not None:
        param.setValue("overlay")
        del param

    param = lastNode.getParam("paramType9")
    if param is not None:
        param.set("vec3")
        del param

    param = lastNode.getParam("paramName9")
    if param is not None:
        param.setValue("areatint")
        del param

    param = lastNode.getParam("paramLabel9")
    if param is not None:
        param.setValue("areatint")
        del param

    param = lastNode.getParam("paramDefaultVec39")
    if param is not None:
        param.setValue(0.33, 0)
        param.setValue(0.27, 1)
        del param

    del lastNode
    # End of node "Shadertoy1_2"

    # Start of node "Mask"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Mask")
    lastNode.setLabel("Mask")
    lastNode.setPosition(4296, 3757)
    lastNode.setSize(80, 44)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupMask = lastNode

    del lastNode
    # End of node "Mask"

    # Start of node "Nail_mask"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Nail_mask")
    lastNode.setLabel("Nail mask")
    lastNode.setPosition(3997, 3746)
    lastNode.setSize(80, 44)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupNail_mask = lastNode

    del lastNode
    # End of node "Nail_mask"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput2.connectInput(0, groupShadertoy1_2)
    groupShadertoy1_2.connectInput(0, groupSource)
    groupShadertoy1_2.connectInput(1, groupMask)
    groupShadertoy1_2.connectInput(2, groupNail_mask)

    param = groupShadertoy1_2.getParam("paramValueVec20")
    group.getParam("Shadertoy1_2paramValueVec20").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueVec21")
    group.getParam("Shadertoy1_2paramValueVec21").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueVec22")
    param.setExpression("thisGroup.offsetX.get()", False, 0)
    param.setExpression("thisGroup.offsetY.get()", False, 1)
    del param
    param = groupShadertoy1_2.getParam("paramValueBool3")
    group.getParam("Shadertoy1_2paramValueBool3").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueFloat4")
    group.getParam("Shadertoy1_2paramValueFloat4").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueFloat5")
    group.getParam("Shadertoy1_2paramValueFloat5").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueFloat6")
    group.getParam("Shadertoy1_2paramValueFloat6").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueBool7")
    group.getParam("Shadertoy1_2paramValueBool7").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueBool8")
    group.getParam("Shadertoy1_2paramValueBool8").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueVec39")
    group.getParam("Shadertoy1_2paramValueVec39").setAsAlias(param)
    del param

    try:
        extModule = sys.modules["Ls_nail_GLExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
