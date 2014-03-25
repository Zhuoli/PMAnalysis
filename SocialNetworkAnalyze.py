from EmailCommunication.EmailCommunicationDraw import *
from EmailCommunication.EmailAnimation import *
#run

def drawEmailCommunication(projectName):
    members = getMembersName(projectName)
    senders,cleand = cleanData(cleaned_data,TeamMembers=members)
    EcoS2R = getProjectS2R(senders,members,cleand)
    print 'EcoS2R: ',EcoS2R
    drawEmail(EcoS2R)
 
    
drawEmailCommunication('KnowledgeEcoSystem2');
clean4gephi('KnowledgeEcoSystem2')
#addTimeInterval()