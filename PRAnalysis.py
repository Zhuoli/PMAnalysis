# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import DataLoadAndClean 
from ProjectClass import *

#Test
# Given a list of reachable PMS and traffic log, read and clean it 
PRTraffic,KPTraffic = DataLoadAndClean.readAndClean();

# set up a task for this project
#Project 
projectDir = 'DevelopmentEnvironment4AAoP'
projectURL='https://projects.massmutual.com/projects/development environment for aaop and the tameb adapter'
developmentEnvironment4AAoP = ProjectAnalysis(projectDir,projectURL,PRTraffic,KPTraffic)
#Project 
projectDir = 'AveksaUpgrade'
projectURL='https://projects.massmutual.com/projects/aveksa upgrade t-04049'
aveksaUpprade = ProjectAnalysis(projectDir,projectURL,PRTraffic,KPTraffic)
#Project 
projectDir = 'KnowledgeEcoSystem2'
projectURL='https://projects.massmutual.com/projects/Knowledge EcoSystem 2'
KnowledgeEcoSystem2 = ProjectAnalysis(projectDir,projectURL,PRTraffic,KPTraffic)
#Project 
projectDir = 'CustomerCommunicationFrameworkandConsolidationtoxPression'
projectURL='https://projects.massmutual.com/projects/Customer Communication Framework and Consolidation to xPression'
CustomerCommunicationFrameworkandConsolidationtoxPression = ProjectAnalysis(projectDir,projectURL,PRTraffic,KPTraffic)

#Project 
projectDir = 'FieldTechnologyChargeback'
projectURL='https://projects.massmutual.com/projects/Field%20Technology%20Chargeback'
FieldTechnologyChargeback = ProjectAnalysis(projectDir,projectURL,PRTraffic,KPTraffic)

#Project 
projectDir = 'KnowledgePortalRestructure-Design'
projectURL='https://projects.massmutual.com/projects/Knowledge%20Portal%20Restructure-%20Design'
KnowledgePortalRestructure = ProjectAnalysis(projectDir,projectURL,PRTraffic,KPTraffic)

#Project 
projectDir = 'CoolGenConversion'
projectURL='https://projects.massmutual.com/projects/CoolGen%20Conversion'
CoolGenConversion = ProjectAnalysis(projectDir,projectURL,PRTraffic,KPTraffic)

#Project 
projectDir = 'SBI_Technology'
projectURL='https://projects.massmutual.com/projects/SBI_Technology'
SBI_Technology = ProjectAnalysis(projectDir,projectURL,PRTraffic,KPTraffic)

#Project 
projectDir = 'FieldMobileApplication '
projectURL='https://projects.massmutual.com/projects/Field%20Mobile%20Application'
FieldMobileApplication = ProjectAnalysis(projectDir,projectURL,PRTraffic,KPTraffic)

#Project 
projectDir = 'Cancelled__ProofOfTechnology-DataWareHouseBI'
projectURL='https://projects.massmutual.com/projects/Proof%20Of%20Technology%20-%20Data%20WarehouseBI%20Enablement'
FieldMobileApplication = ProjectAnalysis(projectDir,projectURL,PRTraffic,KPTraffic)

#Project 
projectDir = 'Cancelled__ElectronicPayments'
projectURL='https://projects.massmutual.com/projects/Electronic%20Payments%20-%20WireACH'
FieldMobileApplication = ProjectAnalysis(projectDir,projectURL,PRTraffic,KPTraffic)

#Project 
projectDir = 'Cancelled__PalmJuvenileStatus'
projectURL='https://projects.massmutual.com/projects/Palm%20Juvenile%20Status'
FieldMobileApplication = ProjectAnalysis(projectDir,projectURL,PRTraffic,KPTraffic)

#Project 
projectDir = 'Cancelled__Varonis5.8Upgrade'
projectURL='https://projects.massmutual.com/projects/Varonis%205.8%20Upgrade'
FieldMobileApplication = ProjectAnalysis(projectDir,projectURL,PRTraffic,KPTraffic)


################################### Added Projects #####################################
#Project 
projectDir = 'Cancelled__BlankFromAutomatedDistribution'
projectURL='https://projects.massmutual.com/projects/Blank%20Form%20Automated%20Distribution'
FieldMobileApplication = ProjectAnalysis(projectDir,projectURL,PRTraffic,KPTraffic)


#Project 
projectDir = 'PMToolEnhancement'
projectURL='https://projects.massmutual.com/projects/PM%20Tool%20Enhancement'
FieldMobileApplication = ProjectAnalysis(projectDir,projectURL,PRTraffic,KPTraffic)


#Project 
projectDir = 'AnnuityWorkflowMigration2Citrix'
projectURL='https://projects.massmutual.com/projects/Annuity%20Workflow%20migration%20to%20Citrix'
FieldMobileApplication = ProjectAnalysis(projectDir,projectURL,PRTraffic,KPTraffic)


#Project 
projectDir = 'SolutionModelingTool'
projectURL='https://projects.massmutual.com/projects/Solution%20Modeling%20Tool'
FieldMobileApplication = ProjectAnalysis(projectDir,projectURL,PRTraffic,KPTraffic)

#Project 
projectDir = 'DisableSplitTunneling'
projectURL='https://projects.massmutual.com/projects/Disable%20Split%20Tunneling'
FieldMobileApplication = ProjectAnalysis(projectDir,projectURL,PRTraffic,KPTraffic)

#Project 
projectDir = 'ImplementNetworkAccessControls'
projectURL='https://projects.massmutual.com/projects/Implement%20Network%20Access%20Controls%20(NAC)'
FieldMobileApplication = ProjectAnalysis(projectDir,projectURL,PRTraffic,KPTraffic)

#Project 
projectDir = 'ClaimsPlatformReplacement'
projectURL='https://projects.massmutual.com/projects/Claims%20Platform%20Replacement'
FieldMobileApplication = ProjectAnalysis(projectDir,projectURL,PRTraffic,KPTraffic)

#Project 
projectDir = 'EBPPDay2Items'
projectURL='https://projects.massmutual.com/projects/EBPP%20Day%202%20Items'
FieldMobileApplication = ProjectAnalysis(projectDir,projectURL,PRTraffic,KPTraffic)

#Project 
projectDir = 'MacAsAStandardForTheField'
projectURL='https://projects.massmutual.com/projects/MAC%20as%20a%20Standard%20for%20the%20Field'
FieldMobileApplication = ProjectAnalysis(projectDir,projectURL,PRTraffic,KPTraffic)

#Project 
projectDir = 'BoxCloudFileSharing'
projectURL='https://projects.massmutual.com/projects/Box%20Cloud%20File%20Sharing'
FieldMobileApplication = ProjectAnalysis(projectDir,projectURL,PRTraffic,KPTraffic)

#Project 
projectDir = 'DPMRelease2'
projectURL='https://projects.massmutual.com/projects/DPM%20Release%202'
FieldMobileApplication = ProjectAnalysis(projectDir,projectURL,PRTraffic,KPTraffic)

#Project 
projectDir = 'AcordStandardsUpdate'
projectURL='https://projects.massmutual.com/projects/Acord%20Standards%20Update'
FieldMobileApplication = ProjectAnalysis(projectDir,projectURL,PRTraffic,KPTraffic)