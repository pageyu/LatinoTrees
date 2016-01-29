# cross section DB
# units in pb
#
# References			
#	A	https://twiki.cern.ch/twiki/bin/view/CMS/StandardModelCrossSectionsat13TeV		
#	B	https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO		
#	C	https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt1314TeV		
#	D	https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec		
#	E	https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns		
#	F	https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR3		
#	G	https://twiki.cern.ch/twiki/bin/view/CMS/GenXsecTaskForce		
#	H	http://arxiv.org/pdf/1307.7403v1.pdf		
#	I	https://twiki.cern.ch/twiki/bin/viewauth/CMS/HowToGenXSecAnalyzer		
#	J	http://cms.cern.ch/iCMS/jsp/openfile.jsp?tp=draft&files=AN2015_099_v8.pdf
#	K	https://twiki.cern.ch/twiki/bin/view/CMS/HiggsWW13TeVProductionMassScan (powheg numbers)
#	L	https://twiki.cern.ch/twiki/bin/view/CMS/HiggsWW13TeVProduction (powheg numbers)
#       M       https://twiki.cern.ch/twiki/bin/view/CMS/DMAnalysis
#       N       MCM
#	X	Unknown! - Cross section not yet there
#       	

## QCD
samples['QCD_Pt-15to20_MuEnrichedPt5']                .extend( ['xsec=1273190000',    'kfact=1.000',            'ref=N'] )
samples['QCD_Pt-20toInf_MuEnrichedPt15']              .extend( ['xsec=720648000',     'kfact=1.000',            'ref=N'] )
samples['QCD_Pt-15to20_EMEnriched']                   .extend( ['xsec=1273000000',    'kfact=1.000',            'ref=N'] )
samples['QCD_Pt-20to30_EMEnriched']                   .extend( ['xsec=557600000',     'kfact=1.000',            'ref=N'] )
samples['QCD_Pt-30to50_EMEnriched']                   .extend( ['xsec=136000000',     'kfact=1.000',            'ref=N'] )
samples['QCD_Pt-50to80_EMEnriched']                   .extend( ['xsec=19800000',      'kfact=1.000',            'ref=N'] )
samples['QCD_Pt-30toInf_DoubleEMEnriched']            .extend( ['xsec=162060000',     'kfact=1.000',            'ref=N'] )

## VVV
samples['WWW']            .extend( ['xsec=0.18331',     'kfact=1.000',            'ref=H'] )
samples['WWZ']            .extend( ['xsec=0.16510',     'kfact=1.000',            'ref=E'] )
samples['WZZ']            .extend( ['xsec=0.05565',     'kfact=1.000',            'ref=E'] )
samples['ZZZ']            .extend( ['xsec=0.01398',     'kfact=1.000',            'ref=E'] )

# Wjets
samples['WJetsToLNu']                	.extend( ['xsec=61526.7',     'kfact=1.000',		'ref=E'] )

# WW 
samples['WWTo2L2Nu']	             	.extend( ['xsec=12.178',     'kfact=1.000',		'ref=E'] )		
samples['WWToLNuQQ']	             	.extend( ['xsec=49.997',     'kfact=1.000',		'ref=E'] )	
samples['WWToLNuQQext']	             	.extend( ['xsec=49.997',     'kfact=1.000',		'ref=E'] )
samples['WWTo4Q'] 	             	.extend( ['xsec=51.723',     'kfact=1.000',		'ref=E'] )
samples['GluGluWWTo2L2Nu_MCFM']      	.extend( ['xsec=0.8436',      'kfact=1.000',		'ref=E'] ) # 2*3.974*0.1086*.1086*9 --> 2 is a k-factor, 3.974 comes from the comment on the qqWW samples in reference E
samples['GluGluWWTo2L2NuHiggs_MCFM'] 	.extend( ['xsec=1.3633',      'kfact=1.000',		'ref=X'] ) # 2*0.6817 --> 2 is the same k-factor, 0.6817 is 0.07574*9, first number comes from MCFM, 9 is the lepton combinations
samples['WWTo2L2NuHerwigPS']	        .extend( ['xsec=12.178',     'kfact=1.000',		'ref=E'] )		

# tt
samples['TTTo2L2Nu'] 	             	.extend( ['xsec=87.31',     	'kfact=1.000',		'ref=B'] )		
	
# ggH,HWW
samples['GluGluHToWWTo2L2Nu_Mlarge']  	.extend( ['xsec=0.6818',     	'kfact=1.000',		'ref=X'] ) # 10GeV Higgs width 30.21(powheg)*0.215*0.108*0.108*9	

samples['GluGluHToWWTo2L2Nu_alternative_M120']  .extend( ['xsec=0.9818',     	'kfact=1.000',		'ref=CF'] ) 
samples['GluGluHToWWTo2L2Nu_alternative_M125']  .extend( ['xsec=0.9913',      	'kfact=1.000',		'ref=CF'] ) 
samples['GluGluHToWWTo2L2Nu_alternative_M130']  .extend( ['xsec=0.9081',     	'kfact=1.000',		'ref=X'] ) # 28.55(powheg)*0.303*0.108*0.108*9

samples['GluGluHToWWTo2L2Nu_M115']  	.extend( ['xsec=0.3128',     	'kfact=1.000',		'ref=KF'] ) # 34.69*0.0859*0.108*0.108*9  
samples['GluGluHToWWTo2L2Nu_M120']  	.extend( ['xsec=0.4768',     	'kfact=1.000',		'ref=KF'] ) # 32.21*0.141*0.108*0.108*9  
samples['GluGluHToWWTo2L2Nu_M124']      .extend( ['xsec=0.6353',     	'kfact=1.000',		'ref=KF'] ) # 30.41*0.199*0.108*0.108*9  
samples['GluGluHToWWTo2L2Nu_M125']      .extend( ['xsec=0.9913',      	'kfact=1.000',		'ref=CF'] ) # 43.92*0.215*0.108*0.108*9 Higgs LHC value
samples['GluGluHToWWTo2L2Nu_M126']      .extend( ['xsec=0.7171',     	'kfact=1.000',		'ref=KF'] ) # 29.57*0.231*0.108*0.108*9      
samples['GluGluHToWWTo2L2Nu_M130']      .extend( ['xsec=0.8906',     	'kfact=1.000',		'ref=KF'] ) # 28.00*0.303*0.108*0.108*9       
samples['GluGluHToWWTo2L2Nu_M135']      .extend( ['xsec=1.1006',     	'kfact=1.000',		'ref=KF'] ) # 26.21*0.400*0.108*0.108*9       
samples['GluGluHToWWTo2L2Nu_M140']      .extend( ['xsec=1.2938',     	'kfact=1.000',		'ref=KF'] ) # 24.60*0.501*0.108*0.108*9        
samples['GluGluHToWWTo2L2Nu_M145']      .extend( ['xsec=1.4594',     	'kfact=1.000',		'ref=KF'] ) # 23.17*0.600*0.108*0.108*9      
samples['GluGluHToWWTo2L2Nu_M150']      .extend( ['xsec=1.6001',     	'kfact=1.000',		'ref=KF'] ) # 21.90*0.696*0.108*0.108*9        
samples['GluGluHToWWTo2L2Nu_M155']      .extend( ['xsec=1.7409',     	'kfact=1.000',		'ref=KF'] ) # 20.86*0.795*0.108*0.108*9    
samples['GluGluHToWWTo2L2Nu_M160']      .extend( ['xsec=1.9102',     	'kfact=1.000',		'ref=KF'] ) # 20.04*0.908*0.108*0.108*9      
samples['GluGluHToWWTo2L2Nu_M165']      .extend( ['xsec=1.8966',     	'kfact=1.000',		'ref=KF'] ) # 18.82*0.960*0.108*0.108*9  
samples['GluGluHToWWTo2L2Nu_M170']      .extend( ['xsec=1.8104',     	'kfact=1.000',		'ref=KF'] ) # 17.89*0.964*0.108*0.108*9    
samples['GluGluHToWWTo2L2Nu_M175']      .extend( ['xsec=1.7147',     	'kfact=1.000',		'ref=KF'] ) # 17.05*0.958*0.108*0.108*9       
samples['GluGluHToWWTo2L2Nu_M190']      .extend( ['xsec=1.2187',     	'kfact=1.000',		'ref=KF'] ) # 14.77*0.786*0.108*0.108*9          
samples['GluGluHToWWTo2L2Nu_M200']      .extend( ['xsec=1.0548',     	'kfact=1.000',		'ref=KF'] ) # 13.56*0.741*0.108*0.108*9            
samples['GluGluHToWWTo2L2Nu_M210']      .extend( ['xsec=0.9639',     	'kfact=1.000',		'ref=KF'] ) # 12.70*0.723*0.108*0.108*9           
samples['GluGluHToWWTo2L2Nu_M230']      .extend( ['xsec=0.8332',     	'kfact=1.000',		'ref=KF'] ) # 11.21*0.708*0.108*0.108*9              
samples['GluGluHToWWTo2L2Nu_M250']      .extend( ['xsec=0.7270',     	'kfact=1.000',		'ref=KF'] ) # 9.88*0.701*0.108*0.108*9   
samples['GluGluHToWWTo2L2Nu_M270']      .extend( ['xsec=0.6483',     	'kfact=1.000',		'ref=KF'] ) # 8.86*0.697*0.108*0.108*9   
samples['GluGluHToWWTo2L2Nu_M300']      .extend( ['xsec=0.5731',     	'kfact=1.000',		'ref=KF'] ) # 7.89*0.692*0.108*0.108*9    
samples['GluGluHToWWTo2L2Nu_M350']      .extend( ['xsec=0.5698',     	'kfact=1.000',		'ref=KF'] ) # 8.03*0.676*0.108*0.108*9      
samples['GluGluHToWWTo2L2Nu_M400']      .extend( ['xsec=0.4360',     	'kfact=1.000',		'ref=KF'] ) # 7.136*0.582*0.108*0.108*9   
samples['GluGluHToWWTo2L2Nu_M450']      .extend( ['xsec=0.2926',     	'kfact=1.000',		'ref=KF'] ) # 5.059*0.551*0.108*0.108*9     
samples['GluGluHToWWTo2L2Nu_M500']      .extend( ['xsec=0.1926',     	'kfact=1.000',		'ref=KF'] ) # 3.360*0.546*0.108*0.108*9    
samples['GluGluHToWWTo2L2Nu_M600']      .extend( ['xsec=0.8599',     	'kfact=1.000',		'ref=KF'] ) # 1.468*0.558*0.108*0.108*9      
samples['GluGluHToWWTo2L2Nu_M650']      .extend( ['xsec=0.0593',     	'kfact=1.000',		'ref=KF'] ) # 0.994*0.568*0.108*0.108*9  
samples['GluGluHToWWTo2L2Nu_M700']      .extend( ['xsec=0.0416',     	'kfact=1.000',		'ref=KF'] ) # 0.687*0.577*0.108*0.108*9    
samples['GluGluHToWWTo2L2Nu_M800']      .extend( ['xsec=0.0218',     	'kfact=1.000',		'ref=KF'] ) # 0.3493*0.594*0.108*0.108*9     
samples['GluGluHToWWTo2L2Nu_M900']      .extend( ['xsec=0.0123',     	'kfact=1.000',		'ref=KF'] ) # 0.1920*0.609*0.108*0.108*9     
samples['GluGluHToWWTo2L2Nu_M1000']     .extend( ['xsec=0.0073',     	'kfact=1.000',		'ref=KF'] ) # 0.1128*0.621*0.108*0.108*9        

samples['GluGluHToWWTo2L2NuAMCNLO_M125']  .extend( ['xsec=0.9913',      	'kfact=1.000',		'ref=CF'] ) 
samples['GluGluHToWWTo2L2NuPowheg_M125']  .extend( ['xsec=0.9913',      	'kfact=1.000',		'ref=CF'] ) 
samples['GluGluHToWWTo2L2NuHerwigPS_M125'] .extend( ['xsec=0.9913',      	'kfact=1.000',		'ref=CF'] ) 

samples['GluGluHToWWToLNuQQ_M650']      .extend( ['xsec=0.1259',     	'kfact=1.000',		'ref=LF'] ) # 1.0149*0.568*0.108*3*0.6741     
samples['GluGluHToWWToLNuQQ_M1000']     .extend( ['xsec=0.0029',     	'kfact=1.000',		'ref=LF'] ) # 0.11877*0.1128*0.108*3*0.6741     

# W-H
samples['HWminusJ_HToWW_M120']       	.extend( ['xsec=0.0866',     	'kfact=1.000',		'ref=EF'] ) # 0.614 * 0.141
samples['HWminusJ_HToWW_M125']  	.extend( ['xsec=0.1160',     	'kfact=1.000',		'ref=EF'] ) # 0.539 * 0.215
samples['HWminusJ_HToWW_M130'] 		.extend( ['xsec=0.1430',     	'kfact=1.000',		'ref=EF'] ) # 0.472* 0.303

# W+H
samples['HWplusJ_HToWW_M120']          	.extend( ['xsec=0.1350',       'kfact=1.000',	       	'ref=EF'] ) # 0.956 * 0.141
samples['HWplusJ_HToWW_M125']          	.extend( ['xsec=0.1810',       'kfact=1.000',	       	'ref=EF'] ) # 0.842 * 0.215
samples['HWplusJ_HToWW_M130']          	.extend( ['xsec=0.2250',       'kfact=1.000',	       	'ref=EF'] ) # 0.743 * 0.303

# ZH
samples['HZJ_HToWW_M120']  	       	.extend( ['xsec=0.121',       	'kfact=1.000',	      	'ref=EF'] ) # 0.855 * 0.141
samples['HZJ_HToWW_M125']  	       	.extend( ['xsec=0.187',       	'kfact=1.000',	      	'ref=EF'] ) # 0.8696* 0.215
samples['HZJ_HToWW_M130']  	       	.extend( ['xsec=0.202',       	'kfact=1.000',	      	'ref=EF'] ) # 0.667* 0.303

# VBF
samples['VBFHToWWTo2L2Nu_alternative_M120']    .extend( ['xsec=0.0579',       	'kfact=1.000',	       	'ref=EF'] ) # 3.91 *  0.141*0.108*0.108*9
samples['VBFHToWWTo2L2Nu_alternative_M125']    .extend( ['xsec=0.0846',		'kfact=1.000',	   	'ref=EF'] ) # 3.75 * 0.215*0.108*0.108*9
samples['VBFHToWWTo2L2Nu_alternative_M130']    .extend( ['xsec=0.1148',        	'kfact=1.000',	       	'ref=EF'] ) # 3.61 *  0.303*0.108*0.108*9

samples['VBFHToWWTo2L2Nu_M115']   	.extend( ['xsec=0.0369',	'kfact=1.000',	   	'ref=EF'] ) # 4.09*0.0859*0.108*0.108*9  
samples['VBFHToWWTo2L2Nu_M124']   	.extend( ['xsec=0.0794',	'kfact=1.000',	   	'ref=EF'] ) # 3.80*0.199*0.108*0.108*9  
samples['VBFHToWWTo2L2Nu_M125']   	.extend( ['xsec=0.0846',	'kfact=1.000',	   	'ref=EF'] ) # 3.75*0.215*0.108*0.108*9
samples['VBFHToWWTo2L2Nu_M126']   	.extend( ['xsec=0.0907',     	'kfact=1.000',		'ref=KF'] ) # 3.74*0.231*0.108*0.108*9       
samples['VBFHToWWTo2L2Nu_M130']   	.extend( ['xsec=0.1151',     	'kfact=1.000',		'ref=KF'] ) # 3.62*0.303*0.108*0.108*9     
samples['VBFHToWWTo2L2Nu_M135']         .extend( ['xsec=0.1465',     	'kfact=1.000',		'ref=KF'] ) # 3.49*0.400*0.108*0.108*9       
samples['VBFHToWWTo2L2Nu_M140']      	.extend( ['xsec=0.1772',     	'kfact=1.000',		'ref=KF'] ) # 3.37*0.501*0.108*0.108*9      
samples['VBFHToWWTo2L2Nu_M150']         .extend( ['xsec=0.2301',     	'kfact=1.000',		'ref=KF'] ) # 3.15*0.696*0.108*0.108*9        
samples['VBFHToWWTo2L2Nu_M155']         .extend( ['xsec=0.2553',    	'kfact=1.000',		'ref=KF'] ) # 3.06*0.795*0.108*0.108*9 
samples['VBFHToWWTo2L2Nu_M160']         .extend( ['xsec=0.2859',     	'kfact=1.000',		'ref=KF'] ) # 3.00*0.908*0.108*0.108*9     
samples['VBFHToWWTo2L2Nu_M175']         .extend( ['xsec=0.2715',     	'kfact=1.000',		'ref=KF'] ) # 2.70*0.958*0.108*0.108*9        
samples['VBFHToWWTo2L2Nu_M180']      	.extend( ['xsec=0.2563',     	'kfact=1.000',		'ref=KF'] ) # 2.62*0.932*0.108*0.108*9        
samples['VBFHToWWTo2L2Nu_M190']         .extend( ['xsec=0.2013',     	'kfact=1.000',		'ref=KF'] ) # 2.44*0.786*0.108*0.108*9 
samples['VBFHToWWTo2L2Nu_M200']     	.extend( ['xsec=0.1781',     	'kfact=1.000',		'ref=KF'] ) # 2.29*0.741*0.108*0.108*9    
samples['VBFHToWWTo2L2Nu_M210']     	.extend( ['xsec=0.1655',     	'kfact=1.000',		'ref=KF'] ) # 2.18*0.723*0.108*0.108*9       
samples['VBFHToWWTo2L2Nu_M230']     	.extend( ['xsec=0.1412',     	'kfact=1.000',		'ref=KF'] ) # 1.9*0.708*0.108*0.108*9         
samples['VBFHToWWTo2L2Nu_M300']     	.extend( ['xsec=0.0960',     	'kfact=1.000',		'ref=KF'] ) # 1.322*0.692*0.108*0.108*9      
samples['VBFHToWWTo2L2Nu_M650']     	.extend( ['xsec=0.0189',     	'kfact=1.000',		'ref=KF'] ) # 0.317*0.568*0.108*0.108*9       
samples['VBFHToWWTo2L2Nu_M800']     	.extend( ['xsec=0.0189',     	'kfact=1.000',		'ref=KF'] ) # 0.200*0.594*0.108*0.108*9      

samples['VBFHToWWTo2L2NuPowheg_M125'] 	.extend( ['xsec=0.0846',	'kfact=1.000',	   	'ref=EF'] ) # 3.75*0.215*0.108*0.108*9
samples['VBFHToWWTo2L2NuAMCNLO_M125'] 	.extend( ['xsec=0.0846',	'kfact=1.000',	   	'ref=EF'] ) # 3.75*0.215*0.108*0.108*9

samples['VBFHToWWToNuQQ_M450']         	.extend( ['xsec=0.0031',     	'kfact=1.000',		'ref=LF'] ) # 0.685*0.551*0.108*3*0.6741   
samples['VBFHToWWToNuQQ_M1000']         .extend( ['xsec=0.0082',     	'kfact=1.000',		'ref=LF'] ) # 0.125*0.1128*0.108*3*0.6741   

# VBS
samples['WpWpJJ_EWK_QCD']   		.extend( ['xsec=0.05004',	'kfact=1.000',	   	'ref=I'] )
samples['WpWpJJ_EWK']   		.extend( ['xsec=0.02526',	'kfact=1.000',	   	'ref=I'] )
samples['WpWpJJ_QCD']   		.extend( ['xsec=0.02474',	'kfact=1.000',	   	'ref=I'] )
samples['WpWmJJ_EWK_QCD_noTop']   	.extend( ['xsec=2.66300',	'kfact=1.000',	   	'ref=I'] )
samples['WpWmJJ_EWK_noTop']   		.extend( ['xsec=0.35000',	'kfact=1.000',	   	'ref=X'] )
samples['WpWmJJ_QCD_noTop']   		.extend( ['xsec=2.42300',	'kfact=1.000',	   	'ref=I'] )
samples['WpWmJJ_EWK_QCD_noTop_noHiggs'] .extend( ['xsec=2.65000',	'kfact=1.000',	   	'ref=X'] )
samples['WpWmJJ_EWK'] 			.extend( ['xsec=0.55000',	'kfact=1.000',	   	'ref=X'] )
samples['TWJ']   			.extend( ['xsec=0.28000',	'kfact=1.000',	   	'ref=X'] )
samples['WLLJJToLNu_M-60_EWK_QCD']   	.extend( ['xsec=0.50000',	'kfact=1.000',	   	'ref=I'] )
samples['WLLJJToLNu_M-60_EWK']   	.extend( ['xsec=0.04634',	'kfact=1.000',	   	'ref=I'] )
samples['WLLJJToLNu_M-60_QCD']   	.extend( ['xsec=0.49480',	'kfact=1.000',	   	'ref=I'] )
samples['WLLJJToLNu_M-4to60_EWK_QCD']  	.extend( ['xsec=0.50490',	'kfact=1.000',	   	'ref=I'] )
samples['WZJJ_EWK_QCD']   		.extend( ['xsec=0.48910',	'kfact=1.000',	   	'ref=I'] )
samples['WZJJ_EWK']   			.extend( ['xsec=0.03900',	'kfact=1.000',	   	'ref=X'] )
samples['WZJJ_QCD']   			.extend( ['xsec=0.45850',	'kfact=1.000',	   	'ref=I'] )
samples['WW_DoubleScattering']   	.extend( ['xsec=1.61400',	'kfact=1.000',	   	'ref=X'] )
samples['DY2JetsToLL']   		.extend( ['xsec=333.300',	'kfact=1.000',	   	'ref=I'] )
samples['WGJJ']   			.extend( ['xsec=0.00000',	'kfact=1.000',	   	'ref=X'] )

# ttDM
samples['ttDM0001scalar0010'] .extend( ['xsec=19.59'         , 'kfact=1.000', 'ref=J'] )
#samples['ttDM0001scalar0020'] .extend( ['xsec=10.48'         , 'kfact=1.000', 'ref=J'] )
samples['ttDM0001scalar0050'] .extend( ['xsec=2.941'         , 'kfact=1.000', 'ref=J'] )
samples['ttDM0001scalar0100'] .extend( ['xsec=0.6723'        , 'kfact=1.000', 'ref=J'] )
samples['ttDM0001scalar0200'] .extend( ['xsec=0.09327'       , 'kfact=1.000', 'ref=J'] )
samples['ttDM0001scalar0300'] .extend( ['xsec=0.0295'        , 'kfact=1.000', 'ref=J'] ) 
samples['ttDM0001scalar0500'] .extend( ['xsec=0.00518'       , 'kfact=1.000', 'ref=J'] )  
#samples['ttDM0001scalar1000'] .extend( ['xsec=0.0003687'     , 'kfact=1.000', 'ref=J'] ) 
#samples['ttDM0001scalar2000'] .extend( ['xsec=0.00001034'    , 'kfact=1.000', 'ref=J'] )  
#samples['ttDM0001scalar5000'] .extend( ['xsec=0.0000000617'  , 'kfact=1.000', 'ref=J'] )
samples['ttDM0010scalar0010'] .extend( ['xsec=0.09487'       , 'kfact=1.000', 'ref=J'] ) 
#samples['ttDM0010scalar0015'] .extend( ['xsec=0.1202'        , 'kfact=1.000', 'ref=J'] )
samples['ttDM0010scalar0050'] .extend( ['xsec=2.942'         , 'kfact=1.000', 'ref=J'] )  
samples['ttDM0010scalar0100'] .extend( ['xsec=0.6732'        , 'kfact=1.000', 'ref=J'] ) 
#samples['ttDM0010scalar5000'] .extend( ['xsec=0.00000006138' , 'kfact=1.000', 'ref=J'] )
#samples['ttDM0050scalar0010'] .extend( ['xsec=0.001906'      , 'kfact=1.000', 'ref=J'] ) 
samples['ttDM0050scalar0050'] .extend( ['xsec=0.002329'      , 'kfact=1.000', 'ref=J'] )  
#samples['ttDM0050scalar0095'] .extend( ['xsec=0.006558'      , 'kfact=1.000', 'ref=J'] ) 
samples['ttDM0050scalar0200'] .extend( ['xsec=0.09224'       , 'kfact=1.000', 'ref=J'] )  
samples['ttDM0050scalar0300'] .extend( ['xsec=0.02901'       , 'kfact=1.000', 'ref=J'] )  
#samples['ttDM0050scalar5000'] .extend( ['xsec=0.00000005616' , 'kfact=1.000', 'ref=J'] )
#samples['ttDM0150scalar0010'] .extend( ['xsec=0.00008634'    , 'kfact=1.000', 'ref=J'] )  
samples['ttDM0150scalar0200'] .extend( ['xsec=0.00013'       , 'kfact=1.000', 'ref=J'] ) 
#samples['ttDM0150scalar0295'] .extend( ['xsec=0.000394'      , 'kfact=1.000', 'ref=J'] )  
#samples['ttDM0150scalar0500'] .extend( ['xsec=0.003754'      , 'kfact=1.000', 'ref=J'] ) 
#samples['ttDM0150scalar5000'] .extend( ['xsec=0.00000004162' , 'kfact=1.000', 'ref=J'] )
#samples['ttDM0500scalar0010'] .extend( ['xsec=0.0000007356'  , 'kfact=1.000', 'ref=J'] )  
samples['ttDM0500scalar0500'] .extend( ['xsec=0.0000009894'  , 'kfact=1.000', 'ref=J'] ) 
#samples['ttDM0500scalar0995'] .extend( ['xsec=0.0000073'     , 'kfact=1.000', 'ref=J'] )
#samples['ttDM0500scalar2000'] .extend( ['xsec=0.000005808'   , 'kfact=1.000', 'ref=J'] )  
#samples['ttDM0500scalar5000'] .extend( ['xsec=0.000001048'   , 'kfact=1.000', 'ref=J'] )  
#samples['ttDM1000scalar0010'] .extend( ['xsec=0.000000006607', 'kfact=1.000', 'ref=J'] )  
#samples['ttDM1000scalar1000'] .extend( ['xsec=0.000000009433', 'kfact=1.000', 'ref=J'] )
#samples['ttDM1000scalar1995'] .extend( ['xsec=0.0000001108'  , 'kfact=1.000', 'ref=J'] )
#samples['ttDM1000scalar2000'] .extend( ['xsec=0.0000000017'  , 'kfact=1.000', 'ref=J'] )

samples['ttDM0001pseudo0010'] .extend( ['xsec=0.4409'        , 'kfact=1.000', 'ref=J'] )
samples['ttDM0001pseudo0020'] .extend( ['xsec=0.3992'        , 'kfact=1.000', 'ref=J'] )
samples['ttDM0001pseudo0050'] .extend( ['xsec=0.3032'        , 'kfact=1.000', 'ref=J'] )
samples['ttDM0001pseudo0100'] .extend( ['xsec=0.1909'        , 'kfact=1.000', 'ref=J'] )
samples['ttDM0001pseudo0200'] .extend( ['xsec=0.0836'        , 'kfact=1.000', 'ref=J'] )
#samples['ttDM0001pseudo0300'] .extend( ['xsec=0.03999'       , 'kfact=1.000', 'ref=J'] )
samples['ttDM0001pseudo0500'] .extend( ['xsec=0.005408'      , 'kfact=1.000', 'ref=J'] )
#samples['ttDM0001pseudo1000'] .extend( ['xsec=0.0003973'     , 'kfact=1.000', 'ref=J'] )
#samples['ttDM0001pseudo2000'] .extend( ['xsec=0.00001087'    , 'kfact=1.000', 'ref=J'] )
#samples['ttDM0001pseudo5000'] .extend( ['xsec=0.00000007022' , 'kfact=1.000', 'ref=J'] )
#samples['ttDM0010pseudo0010'] .extend( ['xsec=0.01499'       , 'kfact=1.000', 'ref=J'] )
#samples['ttDM0010pseudo0015'] .extend( ['xsec=0.3034'        , 'kfact=1.000', 'ref=J'] )
#samplesttDM0010pseudo0050'] .extend( ['xsec=0.1901'        , 'kfact=1.000', 'ref=J'] )
samples['ttDM0010pseudo0100'] .extend( ['xsec=0.00000007023' , 'kfact=1.000', 'ref=J'] ) 
#samples['ttDM0010pseudo5000'] .extend( ['xsec=0.01863'       , 'kfact=1.000', 'ref=J'] )
#samples['ttDM0050pseudo0010'] .extend( ['xsec=0.002444'      , 'kfact=1.000', 'ref=J'] )
#samples['ttDM0050pseudo0050'] .extend( ['xsec=0.002979'      , 'kfact=1.000', 'ref=J'] )
#samples['ttDM0050pseudo0095'] .extend( ['xsec=0.08382'       , 'kfact=1.000', 'ref=J'] )
samples['ttDM0050pseudo0200'] .extend( ['xsec=0.03989'       , 'kfact=1.000', 'ref=J'] )
#samples['ttDM0050pseudo0300'] .extend( ['xsec=0.00000006831' , 'kfact=1.000', 'ref=J'] ) 
#samples['ttDM0050pseudo5000'] .extend( ['xsec=0.01067'       , 'kfact=1.000', 'ref=J'] )
#samples['ttDM0150pseudo0010'] .extend( ['xsec=0.0002364'     , 'kfact=1.000', 'ref=J'] )
samples['ttDM0150pseudo0200'] .extend( ['xsec=0.0004124'     , 'kfact=1.000', 'ref=J'] )
#samples['ttDM0150pseudo0295'] .extend( ['xsec=0.004611'      , 'kfact=1.000', 'ref=J'] )
samples['ttDM0150pseudo0500'] .extend( ['xsec=0.000000057'   , 'kfact=1.000', 'ref=J'] )
#samples['ttDM0150pseudo5000'] .extend( ['xsec=0.003365'      , 'kfact=1.000', 'ref=J'] )
#samples['ttDM0500pseudo0010'] .extend( ['xsec=0.000002279'   , 'kfact=1.000', 'ref=J'] )
#samples['ttDM0500pseudo0500'] .extend( ['xsec=0.000003275'   , 'kfact=1.000', 'ref=J'] )
#samples['ttDM0500pseudo0995'] .extend( ['xsec=0.000007611'   , 'kfact=1.000', 'ref=J'] )
#samples['ttDM0500pseudo2000'] .extend( ['xsec=0.00000001867' , 'kfact=1.000', 'ref=J'] ) 
#samples['ttDM0500pseudo5000'] .extend( ['xsec=0.00006171'    , 'kfact=1.000', 'ref=J'] )
#samples['ttDM1000pseudo0010'] .extend( ['xsec=0.000000026'   , 'kfact=1.000', 'ref=J'] )
#samples['ttDM1000pseudo1000'] .extend( ['xsec=0.00000003933' , 'kfact=1.000', 'ref=J'] ) 
#samples['ttDM1000pseudo1995'] .extend( ['xsec=0.000000003536', 'kfact=1.000', 'ref=J'] ) 
#samples['ttDM1000pseudo2000'] .extend( ['xsec=0.000001103'   , 'kfact=1.000', 'ref=J'] )  

## monoHiggs
samples['monoH_2HDM_MZp-600_MA0-300']  .extend( ['xsec=0.004901329',	'kfact=1.000',	   	'ref=M'] ) #0.046690*9*(0.108)^2
samples['monoH_2HDM_MZp-800_MA0-300']  .extend( ['xsec=0.005431458',	'kfact=1.000',	   	'ref=M'] ) #0.051740*9*(0.108)^2
samples['monoH_2HDM_MZp-1000_MA0-300'] .extend( ['xsec=0.004405843',	'kfact=1.000',	   	'ref=M'] ) #0.041970*9*(0.108)^2
samples['monoH_2HDM_MZp-1200_MA0-300'] .extend( ['xsec=0.003334038',	'kfact=1.000',	   	'ref=M'] ) #0.031760*9*(0.108)^2
samples['monoH_2HDM_MZp-1400_MA0-300'] .extend( ['xsec=0.002473235',	'kfact=1.000',	   	'ref=M'] ) #0.023560*9*(0.108)^2
samples['monoH_2HDM_MZp-1700_MA0-300'] .extend( ['xsec=0.001585138',	'kfact=1.000',	   	'ref=M'] ) #0.015100*9*(0.108)^2
samples['monoH_2HDM_MZp-2000_MA0-300'] .extend( ['xsec=0.001021836',	'kfact=1.000',	   	'ref=M'] ) #0.009734*9*(0.108)^2
samples['monoH_2HDM_MZp-2500_MA0-300'] .extend( ['xsec=0.000510183',	'kfact=1.000',	   	'ref=M'] ) #0.004860*9*(0.108)^2
