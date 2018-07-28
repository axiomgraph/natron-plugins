# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named Barrel_Blur_Chroma_GLExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from Barrel_Blur_Chroma_GLExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.Barrel_Blur_Chroma_GL"

def getLabel():
    return "Barrel_Blur_Chroma_GL"

def getVersion():
    return 1

def getIconPath():
    return "Barrel_Blur_Chroma_GL.png"

def getGrouping():
    return "Community/GLSL/Blur"

def getPluginDescription():
    return "Barrel chroma blur effect."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group
    lastNode.setColor(0.8314, 0.4863, 0.1373)

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

    param = lastNode.createSeparatorParam("SETUP", "Setup")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.SETUP = param
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

    param = lastNode.createDoubleParam("Shadertoy1paramValueFloat0", "Barrel : ")
    param.setMinimum(0, 0)
    param.setMaximum(100, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(50, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("Distorsion amount")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1paramValueFloat0 = param
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

    param = lastNode.createDoubleParam("Shadertoy1paramValueFloat1", "Chromatic Aberration : ")
    param.setMinimum(0, 0)
    param.setMaximum(200, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(10, 0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("Chromatic Aberration amount")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1paramValueFloat1 = param
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

    param = lastNode.createIntParam("Shadertoy1paramValueInt2", "Iterations : ")
    param.setMinimum(1, 0)
    param.setDisplayMinimum(1, 0)
    param.setDisplayMaximum(50, 0)
    param.setDefaultValue(10, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("Iterations number")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1paramValueInt2 = param
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

    param = lastNode.createSeparatorParam("line101", "Barrel_Blur_Chroma_GL v1.0")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line101 = param
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

    param = lastNode.createSeparatorParam("line102", "")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line102 = param
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

    param = lastNode.createSeparatorParam("conversion", " (Fabrice Fernandez - 2017)")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.conversion = param
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

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output2")
    lastNode.setPosition(4139, 3997)
    lastNode.setSize(90, 33)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "Source"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Source")
    lastNode.setLabel("Source")
    lastNode.setPosition(4139, 3698)
    lastNode.setSize(90, 33)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupSource = lastNode

    del lastNode
    # End of node "Source"

    # Start of node "Shadertoy1"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("Shadertoy1")
    lastNode.setLabel("Shadertoy1")
    lastNode.setPosition(4139, 3847)
    lastNode.setSize(90, 36)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupShadertoy1 = lastNode

    param = lastNode.getParam("paramValueFloat0")
    if param is not None:
        param.setValue(50, 0)
        del param

    param = lastNode.getParam("paramValueFloat1")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramValueInt2")
    if param is not None:
        param.setValue(10, 0)
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("// https://www.shadertoy.com/view/XssGz8\n\n// Simulates Chromatic Aberration by linearly interpolating blur-weights from red to green to blue.\n// Original idea by Kusma: https://github.com/kusma/vlee/blob/master/data/postprocess.fx\n\n// iChannel0: Source, filter=linear, wrap=clamp\n// BBox: iChannel0\n\nuniform float max_distort_px = 50.; // Barrel (Distortion amount in pixels), min=0., max=100.\nuniform float min_distort_factor = -0.5; // Chromatic Aberration (Relative distortion of the red channel), min=0., max=2.\nuniform int num_iter = 7; // Iterations : (iterations number)\n\n// To the extent possible under law,\n// the author has waived all copyright and related or neighboring rights to this work.\n\nfloat remap( float t, float a, float b ) {\n\treturn clamp( (t - a) / (b - a), 0.0, 1.0 );\n}\nvec2 remap( vec2 t, vec2 a, vec2 b ) {\n\treturn clamp( (t - a) / (b - a), 0.0, 1.0 );\n}\n\n//float linterp( float t ) {\n//\treturn clamp( 1.0 - abs( 2.0*t - 1.0 ), 0.0, 1.0 );\n//\n\n\n//note: input [0;1]\nvec3 spectrum_offset_rgb( float t )\n{\n    //note: optimisation from https://twitter.com/Stubbesaurus/status/818847844790575104\n    //t = 3.0 * t - 0.5;\n\t//vec3 ret = clamp( vec3(1.0-t, 1.0-abs(t-1.0), t-1.0), 0.0, 1.0);\n    float t0 = 3.0 * t - 1.5;\n\tvec3 ret = clamp( vec3( -t0, 1.0-abs(t0), t0), 0.0, 1.0);\n\n    //note: old crappy code\n\t//vec3 ret;\n\t//float lo = step(t,0.5);\n\t//float hi = 1.0-lo;\n\t//float w = linterp( remap( t, 1.0/6.0, 5.0/6.0 ) );\n\t//ret = vec3(lo,1.0,hi) * vec3(1.0-w, w, 1.0-w);\n    \n    return ret;\n\t//return smoothstep( vec3(0.0), vec3(1.0), ret );\n    //return pow( ret, vec3(1.0/2.2) );\n\n}\n\n/*\nconst float gamma = 2.2;\nvec3 lin2srgb( vec3 c )\n{\n    return pow( c, vec3(gamma) );\n}\nvec3 srgb2lin( vec3 c )\n{\n    return pow( c, vec3(1.0/gamma));\n}\n*/\n\n\nvec3 yCgCo2rgb(vec3 ycc)\n{\n    float R = ycc.x - ycc.y + ycc.z;\n\tfloat G = ycc.x + ycc.y;\n\tfloat B = ycc.x - ycc.y - ycc.z;\n    return vec3(R,G,B);\n}\n\nvec3 spectrum_offset_ycgco( float t )\n{\n\t//vec3 ygo = vec3( 1.0, 1.5*t, 0.0 ); //green-pink\n    //vec3 ygo = vec3( 1.0, -1.5*t, 0.0 ); //green-purple\n    vec3 ygo = vec3( 1.0, 0.0, -1.25*t ); //cyan-orange\n    //vec3 ygo = vec3( 1.0, 0.0, 1.5*t ); //brownyello-blue\n    return yCgCo2rgb( ygo );\n}\n\nvec3 yuv2rgb( vec3 yuv )\n{\n    vec3 rgb;\n    rgb.r = yuv.x + yuv.z * 1.13983;\n    rgb.g = yuv.x + dot( vec2(-0.39465, -0.58060), yuv.yz );\n    rgb.b = yuv.x + yuv.y * 2.03211;\n    return rgb;\n}\n\n\n// ====\n\n//note: from https://www.shadertoy.com/view/XslGz8\nvec2 radialdistort(vec2 coord, vec2 amt)\n{\n\tvec2 cc = coord - 0.5;\n\treturn coord + 2.0 * cc * amt;\n}\n\n// Given a vec2 in [-1,+1], generate a texture coord in [0,+1]\nvec2 barrelDistortion( vec2 p, vec2 amt )\n{\n    p = 2.0 * p - 1.0;\n\n    /*\n    const float maxBarrelPower = 5.0;\n\t//note: http://glsl.heroku.com/e#3290.7 , copied from Little Grasshopper\n    float theta  = atan(p.y, p.x);\n    vec2 radius = vec2( length(p) );\n    radius = pow(radius, 1.0 + maxBarrelPower * amt);\n    p.x = radius.x * cos(theta);\n    p.y = radius.y * sin(theta);\n\n\t/*/\n    // much faster version\n    //const float maxBarrelPower = 5.0;\n    //float radius = length(p);\n    float maxBarrelPower = sqrt(5.0);\n    float radius = dot(p,p); //faster but doesn\'t match above accurately\n    p *= pow(vec2(radius), maxBarrelPower * amt);\n\t/* */\n\n    return p * 0.5 + 0.5;\n}\n\n//note: from https://www.shadertoy.com/view/MlSXR3\nvec2 brownConradyDistortion(vec2 uv, float dist)\n{\n    uv = uv * 2.0 - 1.0;\n    // positive values of K1 give barrel distortion, negative give pincushion\n    float barrelDistortion1 = 0.1 * dist; // K1 in text books\n    float barrelDistortion2 = -0.025 * dist; // K2 in text books\n\n    float r2 = dot(uv,uv);\n    uv *= 1.0 + barrelDistortion1 * r2 + barrelDistortion2 * r2 * r2;\n    //uv *= 1.0 + barrelDistortion1 * r2;\n    \n    // tangential distortion (due to off center lens elements)\n    // is not modeled in this function, but if it was, the terms would go here\n    return uv * 0.5 + 0.5;\n}\n\nvec2 distort( vec2 uv, float t, vec2 min_distort, vec2 max_distort )\n{\n    vec2 dist = mix( min_distort, max_distort, t );\n    //return radialdistort( uv, 2.0 * dist );\n    //return barrelDistortion( uv, 1.75 * dist ); //distortion at center\n    return brownConradyDistortion( uv, 75.0 * dist.x );\n}\n\n// ====\n\nvec3 spectrum_offset_yuv( float t )\n{\n\t//vec3 yuv = vec3( 1.0, 3.0*t, 0.0 ); //purple-green\n    //vec3 yuv = vec3( 1.0, 0.0, 2.0*t ); //purple-green\n    vec3 yuv = vec3( 1.0, 0.0, -1.0*t ); //cyan-orange\n    //vec3 yuv = vec3( 1.0, -0.75*t, 0.0 ); //brownyello-blue\n    return yuv2rgb( yuv );\n}\n\nvec3 spectrum_offset( float t )\n{\n  \treturn spectrum_offset_rgb( t );\n   \t//return srgb2lin( spectrum_offset_rgb( t ) );\n    //return lin2srgb( spectrum_offset_rgb( t ) );\n\n    //return spectrum_offset_ycgco( t );\n    //return spectrum_offset_yuv( t );\n}\n\n// ====\n\nfloat nrand( vec2 n )\n{\n\treturn fract(sin(dot(n.xy, vec2(12.9898, 78.233)))* 43758.5453);\n}\n\nvec3 render( vec2 uv )\n{\n    //#define DEBUG\n    #if defined( DEBUG )\n    if ( uv.x > 0.7 && uv.y > 0.7 )\n    {\n        float d = length( vec2(0.77)- uv );\n        d = min( d, length( vec2(0.82)- uv ) );\n        d = min( d, length( vec2(0.875)- uv ) );      \n        return vec3( step( d, 0.025) );\n    }\n    #endif\n    \n    return texture( iChannel0, uv ).rgb;\n}\n\nvoid mainImage( out vec4 fragColor, in vec2 fragCoord )\n{\t\n\tvec2 uv = fragCoord.xy/iResolution.xy;\n\n    /*\n    if ( uv.x > 0.7 &&  uv.y < 0.2 )\n    {\n        vec2 luv = remap( uv, vec2(0.7,0.0), vec2(1.0, 0.2) );\n        vec3 c;\n        c.r = step( luv.x, 1.0/3.0);\n        c.g = step( 1.0/3.0, luv.x )*step(luv.x, 2.0/3.0);\n        c.b = step( 2.0/3.0, luv.x );\n        c *= 0.4;\n        \n        vec3 rgb = spectrum_offset_rgb( luv.x );\n        c += step( abs(rgb-luv.yyy), vec3(0.0125) );\n\n        if ( uv.y > 0.20125 )\n        {\n            c = spectrum_offset( luv.x );\n            if ( uv.y < 0.21 )\n                c = vec3(0.0);\n                \n        }\n        \n        fragColor.rgb = c;\n        return;\n    }\n    */\n    \n\tvec2 max_distort = vec2(max_distort_px) * iRenderScale.xy / iResolution.xy;\n    vec2 min_distort = (1.+min_distort_factor) * max_distort;\n\n    //vec2 oversiz = vec2(1.0);\n    vec2 oversiz = distort( vec2(1.0), 1.0, min_distort, max_distort );\n    uv = remap( uv, 1.0-oversiz, oversiz );\n    \n    //debug oversiz\n    //vec2 distuv = distort( uv, 1.0, max_distort );\n    //if ( abs(distuv.x-0.5)>0.5 || abs(distuv.y-0.5)>0.5)\n    //{\n    //    fragColor = vec4( 1.0, 0.0, 0.0, 1.0 ); return;\n    //}\n    \n\n    float stepsiz = 1.0 / (float(num_iter)-1.0);\n    float rnd = nrand( uv + fract(iTime) );\n    float t = rnd * stepsiz;\n    \n    vec3 sumcol = vec3(0.0);\n\tvec3 sumw = vec3(0.0);\n\tfor ( int i=0; i<num_iter; ++i )\n\t{\n\t\tvec3 w = spectrum_offset( t );\n\t\tsumw += w;\n        vec2 uvd = distort(uv, t, min_distort, max_distort ); //TODO: move out of loop\n\t\tsumcol += w * render( uvd );\n        t += stepsiz;\n\t}\n    sumcol.rgb /= sumw;\n    \n    vec3 outcol = sumcol.rgb;\n    //outcol = lin2srgb( outcol );\n    outcol += rnd/255.0;\n    \n\tfragColor = vec4( outcol, 1.0);\n}\n")
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

    param = lastNode.getParam("inputEnable1")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable2")
    if param is not None:
        param.setValue(False)
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
        param.setValue(3, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("max_distort_px")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("Barrel")
        del param

    param = lastNode.getParam("paramHint0")
    if param is not None:
        param.setValue("Distortion amount in pixels")
        del param

    param = lastNode.getParam("paramDefaultFloat0")
    if param is not None:
        param.setValue(49.99999999999999, 0)
        del param

    param = lastNode.getParam("paramMinFloat0")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat0")
    if param is not None:
        param.setValue(99.99999999999999, 0)
        del param

    param = lastNode.getParam("paramType1")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName1")
    if param is not None:
        param.setValue("min_distort_factor")
        del param

    param = lastNode.getParam("paramLabel1")
    if param is not None:
        param.setValue("Chromatic Aberration")
        del param

    param = lastNode.getParam("paramHint1")
    if param is not None:
        param.setValue("Relative distortion of the red channel")
        del param

    param = lastNode.getParam("paramDefaultFloat1")
    if param is not None:
        param.setValue(-0.5, 0)
        del param

    param = lastNode.getParam("paramMinFloat1")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat1")
    if param is not None:
        param.setValue(2, 0)
        del param

    param = lastNode.getParam("paramType2")
    if param is not None:
        param.set("int")
        del param

    param = lastNode.getParam("paramName2")
    if param is not None:
        param.setValue("num_iter")
        del param

    param = lastNode.getParam("paramLabel2")
    if param is not None:
        param.setValue("Iterations :")
        del param

    param = lastNode.getParam("paramHint2")
    if param is not None:
        param.setValue("iterations number")
        del param

    param = lastNode.getParam("paramDefaultInt2")
    if param is not None:
        param.setValue(7, 0)
        del param

    del lastNode
    # End of node "Shadertoy1"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput1.connectInput(0, groupShadertoy1)
    groupShadertoy1.connectInput(0, groupSource)

    param = groupShadertoy1.getParam("paramValueFloat0")
    group.getParam("Shadertoy1paramValueFloat0").setAsAlias(param)
    del param
    param = groupShadertoy1.getParam("paramValueFloat1")
    group.getParam("Shadertoy1paramValueFloat1").setAsAlias(param)
    del param
    param = groupShadertoy1.getParam("paramValueInt2")
    group.getParam("Shadertoy1paramValueInt2").setAsAlias(param)
    del param

    try:
        extModule = sys.modules["Barrel_Blur_Chroma_GLExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
