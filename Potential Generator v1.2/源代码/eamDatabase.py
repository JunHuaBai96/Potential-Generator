#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python version of the code Zhou04_create_v2.f
original author: X. W. Zhou, xzhou@sandia.gov
based on updates by: Lucas Hale lucas.hale@nist.gov
written by: Germain Clavier g.m.g.c.clavier@tue.nl

This file contains atom attributes for the EAM model and alloy combination. The
original file is EAM_code. It is designed to be used with create_eam.py script.
To add new contribution, just add new AtType instances.
"""

import math

class AtType:
    def __init__(
        self,
        name,
        re,
        fe,
        rhoe,
        rhos,
        alpha,
        beta,
        A,
        B,
        cai,
        ramda,
        Fi0,
        Fi1,
        Fi2,
        Fi3,
        Fm0,
        Fm1,
        Fm2,
        Fm3,
        fnn,
        Fn,
        ielement,
        amass,
        Fm4,
        beta1,
        ramda1,
        rhol,
        rhoh,
    ):
        self.name = name
        self.re = re
        self.fe = fe
        self.rhoe = rhoe
        self.rhos = rhos
        self.alpha = alpha
        self.beta = beta
        self.A = A
        self.B = B
        self.cai = cai
        self.ramda = ramda
        self.Fi0 = Fi0
        self.Fi1 = Fi1
        self.Fi2 = Fi2
        self.Fi3 = Fi3
        self.Fm0 = Fm0
        self.Fm1 = Fm1
        self.Fm2 = Fm2
        self.Fm3 = Fm3
        self.fnn = fnn
        self.Fn = Fn
        self.ielement = ielement
        self.amass = amass
        self.Fm4 = Fm4
        self.beta1 = beta1
        self.ramda1 = ramda1
        self.rhol = rhol
        self.rhoh = rhoh
        self.blat = math.sqrt(2.0) * self.re
        self.rhoin = self.rhol * self.rhoe
        self.rhoout = self.rhoh * self.rhoe

    def __repr__(self):
        output = """{}:
        re = {}; fe = {}
        rhoe = {}; rhos = {};
        alpha = {}; beta = {};
        A = {}; B = {}
        cai = {}; ramda = {}
        Fi0 = {}; Fi1 = {}; Fi2 = {}; Fi3 = {}
        Fm0 = {}; Fm1 = {}; Fm2 = {}; Fm3 = {}; Fm4 = {}
        fnn = {}; Fn = {}
        ielement = {}; amass = {}
        beta1 = {}; ramda1 = {}
        rhol = {}; rhoh = {}
        blat = {}; rhoin = {}; rhoout = {}"""
        return output.format(
            self.name,
            self.re,
            self.fe,
            self.rhoe,
            self.rhos,
            self.alpha,
            self.beta,
            self.A,
            self.B,
            self.cai,
            self.ramda,
            self.Fi0,
            self.Fi1,
            self.Fi2,
            self.Fi3,
            self.Fm0,
            self.Fm1,
            self.Fm2,
            self.Fm3,
            self.Fm4,
            self.fnn,
            self.Fn,
            self.ielement,
            self.amass,
            self.beta1,
            self.ramda1,
            self.rhol,
            self.rhoh,
            self.blat,
            self.rhoin,
            self.rhoout,
        )


Database = {}
Database["Cu"] = AtType(
    "Cu",           # Name
    2.556162,       # re
    1.554485,       # fe
    21.175871,      # rhoe
    21.175395,      # rhos
    8.127620,       # alpha
    4.334731,       # beta
    0.396620,       # A
    0.548085,       # B
    0.308782,       # cai
    0.756515,       # ramda
    -2.170269,      # Fi0
    -0.263788,      # Fi1
    1.088878,       # Fi2
    -0.817603,      # Fi3
    -2.19,          # Fm0
    0.00,           # Fm1
    0.561830,       # Fm2
    -2.100595,      # Fm3
    0.310490,       # fnn
    -2.186568,      # Fn
    29,             # ielement
    63.546,         # amass
    -2.100595,      # Fm4
    4.334731,       # beta1
    0.756515,       # ramda1
    0.85,           # rhol
    1.15,           # rhoh
)
Database["Ag"] = AtType(
    "Ag",
    2.891814,
    1.106232,
    14.604100,
    14.604144,
    9.132010,
    4.870405,
    0.277758,
    0.419611,
    0.339710,
    0.750758,
    -1.729364,
    -0.255882,
    0.912050,
    -0.561432,
    -1.75,
    0.00,
    0.744561,
    -1.150650,
    0.783924,
    -1.748423,
    47,
    107.8682,
    -1.150650,
    4.870405,
    0.750758,
    0.85,
    1.15,
)
Database["Au"] = AtType(
    "Au",
    2.885034,
    1.529021,
    19.991632,
    19.991509,
    9.516052,
    5.075228,
    0.229762,
    0.356666,
    0.356570,
    0.748798,
    -2.937772,
    -0.500288,
    1.601954,
    -0.835530,
    -2.98,
    0.00,
    1.706587,
    -1.134778,
    1.021095,
    -2.978815,
    79,
    196.96654,
    -1.134778,
    5.075228,
    0.748798,
    0.85,
    1.15,
)
Database["Ni"] = AtType(
    "Ni",
    2.488746,
    2.007018,
    27.562015,
    27.562031,
    8.383453,
    4.471175,
    0.429046,
    0.633531,
    0.443599,
    0.820658,
    -2.693513,
    -0.076445,
    0.241442,
    -2.375626,
    -2.70,
    0.00,
    0.265390,
    -0.152856,
    0.445470,
    -2.7,
    28,
    58.6934,
    -0.152856,
    4.471175,
    0.820658,
    0.85,
    1.15,
)
Database["Pd"] = AtType(
    "Pd",
    2.750897,
    1.595417,
    21.335246,
    21.940073,
    8.697397,
    4.638612,
    0.406763,
    0.598880,
    0.397263,
    0.754799,
    -2.321006,
    -0.473983,
    1.615343,
    -0.231681,
    -2.36,
    0.00,
    1.481742,
    -1.675615,
    1.130000,
    -2.352753,
    46,
    106.42,
    -1.675615,
    4.638612,
    0.754799,
    0.85,
    1.15,
)
Database["Pt"] = AtType(
    "Pt",
    2.771916,
    2.336509,
    33.367564,
    35.205357,
    7.105782,
    3.789750,
    0.556398,
    0.696037,
    0.385255,
    0.770510,
    -1.455568,
    -2.149952,
    0.528491,
    1.222875,
    -4.17,
    0.00,
    3.010561,
    -2.420128,
    1.450000,
    -4.145597,
    78,
    195.08,
    -2.420128,
    3.789750,
    0.770510,
    0.25,
    1.15,
)
Database["Al"] = AtType(
    "Al",
    2.863924,
    1.403115,
    20.418205,
    23.195740,
    6.613165,
    3.527021,
    0.314873,
    0.365551,
    0.379846,
    0.759692,
    -2.807602,
    -0.301435,
    1.258562,
    -1.247604,
    -2.83,
    0.00,
    0.622245,
    -2.488244,
    0.785902,
    -2.824528,
    13,
    26.981539,
    -2.488244,
    3.527021,
    0.759692,
    0.85,
    1.15,
)
Database["Pb"] = AtType(
    "Pb",
    3.499723,
    0.647872,
    8.450154,
    8.450063,
    9.121799,
    5.212457,
    0.161219,
    0.236884,
    0.250805,
    0.764955,
    -1.422370,
    -0.210107,
    0.682886,
    -0.529378,
    -1.44,
    0.00,
    0.702726,
    -0.538766,
    0.935380,
    -1.439436,
    82,
    207.2,
    -0.538766,
    5.212457,
    0.764955,
    0.85,
    1.15,
)
Database["Fe"] = AtType(
    "Fe",
    2.481987,
    1.885957,
    20.041463,
    20.041463,
    9.818270,
    5.236411,
    0.392811,
    0.646243,
    0.170306,
    0.340613,
    -2.534992,
    -0.059605,
    0.193065,
    -2.282322,
    -2.54,
    0.00,
    0.200269,
    -0.148770,
    0.391750,
    -2.539945,
    26,
    55.847,
    -0.148770,
    5.236411,
    0.340613,
    0.85,
    1.15,
)
Database["Mo"] = AtType(
    "Mo",
    2.728100,
    2.723710,
    29.354065,
    29.354065,
    8.393531,
    4.476550,
    0.708787,
    1.120373,
    0.137640,
    0.275280,
    -3.692913,
    -0.178812,
    0.380450,
    -3.133650,
    -3.71,
    0.00,
    0.875874,
    0.776222,
    0.790879,
    -3.712093,
    42,
    95.94,
    0.776222,
    4.476550,
    0.275280,
    0.85,
    1.15,
)
Database["Ta"] = AtType(
    "Ta",
    2.860082,
    3.086341,
    33.787168,
    33.787168,
    8.489528,
    4.527748,
    0.611679,
    1.032101,
    0.176977,
    0.353954,
    -5.103845,
    -0.405524,
    1.112997,
    -3.585325,
    -5.14,
    0.00,
    1.640098,
    0.221375,
    0.848843,
    -5.141526,
    73,
    180.9479,
    0.221375,
    4.527748,
    0.353954,
    0.85,
    1.15,
)
Database["W"] = AtType(
    "W",
    2.740840,
    3.487340,
    37.234847,
    37.234847,
    8.900114,
    4.746728,
    0.882435,
    1.394592,
    0.139209,
    0.278417,
    -4.946281,
    -0.148818,
    0.365057,
    -4.432406,
    -4.96,
    0.00,
    0.661935,
    0.348147,
    0.582714,
    -4.961306,
    74,
    183.84,
    0.348147,
    4.746728,
    0.278417,
    0.85,
    1.15,
)
Database["Mg"] = AtType(
    "Mg",
    3.196291,
    0.544323,
    7.132600,
    7.132600,
    10.228708,
    5.455311,
    0.137518,
    0.225930,
    0.5,
    1.0,
    -0.896473,
    -0.044291,
    0.162232,
    -0.689950,
    -0.90,
    0.00,
    0.122838,
    -0.226010,
    0.431425,
    -0.899702,
    12,
    24.305,
    -0.226010,
    5.455311,
    1.0,
    0.85,
    1.15,
)
Database["Co"] = AtType(
    "Co",
    2.505979,
    1.975299,
    27.206789,
    27.206789,
    8.679625,
    4.629134,
    0.421378,
    0.640107,
    0.5,
    1.0,
    -2.541799,
    -0.219415,
    0.733381,
    -1.589003,
    -2.56,
    0.00,
    0.705845,
    -0.687140,
    0.694608,
    -2.559307,
    27,
    58.9332,
    -0.687140,
    4.629134,
    1.0,
    0.85,
    1.15,
)
Database["Ti"] = AtType(
    "Ti",
    2.933872,
    1.863200,
    25.565138,
    25.565138,
    8.775431,
    4.680230,
    0.373601,
    0.570968,
    0.5,
    1.0,
    -3.203773,
    -0.198262,
    0.683779,
    -2.321732,
    -3.22,
    0.00,
    0.608587,
    -0.750710,
    0.558572,
    -3.219176,
    22,
    47.88,
    -0.750710,
    4.680230,
    1.0,
    0.85,
    1.15,
)
Database["Zr"] = AtType(
    "Zr",
    3.199978,
    2.230909,
    30.879991,
    30.879991,
    8.559190,
    4.564902,
    0.424667,
    0.640054,
    0.5,
    1.0,
    -4.485793,
    -0.293129,
    0.990148,
    -3.202516,
    -4.51,
    0.00,
    0.928602,
    -0.981870,
    0.597133,
    -4.509025,
    40,
    91.224,
    -0.981870,
    4.564902,
    1.0,
    0.85,
    1.15,
)
Database["Cr"] = AtType(
    "Cr",
    2.493879,
1.793835,
17.641302,
19.60545,
8.604593,
7.170494,
1.551848,
1.827556,
0.18533,
0.277995,
-2.022754,
0.039608,
-0.183611,
-2.245972,
-2.02,
0.00,
-0.056517,
0.439144,
0.456,
-2.020038,
24,
51.9961,
0.439144,
7.170494,
0.277995,
0.85,
1.15,
)
Database["V"] = AtType(
    "V",
    2.594662,
2.523567, 
27.724393,
27.724393,
7.515860,
4.908879,
0.631438,
0.886485,
0.185170,
0.419307,
-3.352734,
-0.254664,
0.640819,
-2.830487,
-3.380243,
0,
1.242772,
0.134111,
0.635059,
-3.365898,
23,
50.94,
0.134111,
4.908879,
0.419307,
0.85,
1.15
)