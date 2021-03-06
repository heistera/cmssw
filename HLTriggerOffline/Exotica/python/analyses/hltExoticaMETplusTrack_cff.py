import FWCore.ParameterSet.Config as cms

METplusTrackPSet = cms.PSet(
    hltPathsToCheck = cms.vstring(
        #"HLT_MET75_IsoTrk50_v",       # 2015-6 proposal
        #"HLT_MET90_IsoTrk50_v",       # 2015-6 proposal
        #"HLT_MET60_IsoTrk35_Loose_v", # 2016-6 proposal
        "HLT_MET105_IsoTrk50_v",       # 2017 proposal
        "HLT_MET120_IsoTrk50_v"        # 2017 proposal
    ),
    recPFMETLabel = cms.InputTag("pfMet"),
    #recMETLabel   = cms.InputTag("hltPFMETProducer"),
    genMETLabel   = cms.InputTag("genMetTrue"),
    recMuonLabel  = cms.InputTag("muons"),
    recElecLabel  = cms.InputTag("gedGsfElectrons"),
    #recTrackLabel = cms.InputTag("generalTracks"),
    #hltMETLabel   = cms.InputTag("hltMetClean"),                    
    l1METLabel    = cms.InputTag("l1extraParticles","MET"),   
    # -- Analysis specific cuts
    minCandidates = cms.uint32(1),
    # -- Analysis specific binnings
    parametersTurnOn = cms.vdouble(   0,  10,  20,  30,  40,  50,  60,  70,   80,  90,
                                    100, 110, 120, 130, 140, 150, 160, 170,  180, 190,
                                    200, 210, 220, 230, 240, 250, 260, 270,  280, 290,
                                    300, 310, 320, 330, 340, 350, 360, 370,  380, 390,
                                    400
                                  ),
    parametersTurnOnSumEt = cms.vdouble(   0,  10,  20,  30,  40,  50,  60,  70,   80,  90,
                                         100, 110, 120, 130, 140, 150, 160, 170,  180, 190,
                                         200, 210, 220, 230, 240, 250, 260, 270,  280, 290,
                                         300, 310, 320, 330, 340, 350, 360, 370,  380, 390,
                                         400
                                       ),
    dropPt2 = cms.bool(True),
    dropPt3 = cms.bool(True),
)

