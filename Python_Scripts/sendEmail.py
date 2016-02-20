import sys
import requests

# Used to import the functions for sending emails and getting the email dictionary
from mailGunClient import *
from emailDictionary import *

# ------------------------------------------------------------------------------

# sendEmail.py

# This script is used for two things. The first is to fill up my inbox with 
# impressive looking emails in case someone is reading over my shoulder. The
# next is so that I can ping off emails from the command line.

# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# String constants to be printed to console.

ERROR_WRONG_NUM_COMMAND_LINE_ARGS = "\nError, wrong number of command line arguments.\n"
ERROR_INVALID_RECIPIENT = "\nError, invalid recipient.\n"
ERROR_INVALID_COMMAND_TYPE = "\nError, invalid command type.\n"

SUCCESS_MAIL_SENT = "\nSuccess, message sent\n"

# ------------------------------------------------------------------------------
# Integer constants.

ERROR_CODE = 1                          # So 0 is not returned on error.
NUM_NECCESSARY_COMMAND_LINE_ARGS = 3    # Filename, command type and email address.
NUM_NECCESSARY_COMMAND_LINE_ARGS_SEND_MAIL = 4
RECIPIENT_INDEX = 2                     
MESSAGE_INDEX = 3
COMMAND_TYPE_INDEX = 1
EMAIL_FROM = 2
EMAIL_CONTENTS = 1
EMAIL_SUBJECT = 0

# ------------------------------------------------------------------------------
# List of email addresses to be accessed. The dictionary keys are passed to
# the program on the command line.

# emailAddresses = {}

commandTypeOptions = {'SendMail' : 'SendMail', 
                      'BusyAndImportant' : 'BusyAndImportant',
                      'CallMe' : 'CallMe'}

single_email_subject = 'Command Line Email'
single_email_from = 'jamescollerton@live.co.uk'

# ------------------------------------------------------------------------------
# Functions

# Gets the command line arguments and checks to make sure there are two.
def getCommandLineArgs():
    
    commandLineArgs = sys.argv

    if(len(commandLineArgs) < NUM_NECCESSARY_COMMAND_LINE_ARGS):
        print(ERROR_WRONG_NUM_COMMAND_LINE_ARGS)
        sys.exit(ERROR_CODE)

    return(commandLineArgs) 

# Used to get what type of command we want to run from the command line.
def getCommandTypeFromCommandLineArgs(commandLineArgs):

    commandType = commandLineArgs[COMMAND_TYPE_INDEX]

    if commandType in commandTypeOptions:
        return(commandType)
    else:
        print(ERROR_INVALID_COMMAND_TYPE)
        sys.exit(ERROR_CODE)

# Functions for sending a single email
def sendMailFunctions(commandLineArgs, emailAddresses):

    checkNumberOfCommandLineArgs(commandLineArgs)
    recipient = getRecipientFromCommandLineArgs(commandLineArgs, emailAddresses)
    message = getMessageFromCommandLineArgs(commandLineArgs)
    sendEmail(recipient, message, single_email_subject, single_email_from)
    print(SUCCESS_MAIL_SENT)

def checkNumberOfCommandLineArgs(commandLineArgs):

    if(len(commandLineArgs) != NUM_NECCESSARY_COMMAND_LINE_ARGS_SEND_MAIL):
        print(ERROR_WRONG_NUM_COMMAND_LINE_ARGS)
        sys.exit(ERROR_CODE)

# Gets recipient from command line, then checks it's in the emails array.
def getRecipientFromCommandLineArgs(commandLineArgs, emailAddresses):

    recipient = commandLineArgs[RECIPIENT_INDEX]
    
    if recipient in emailAddresses:
        return(emailAddresses[recipient])
    else:
        print(ERROR_INVALID_RECIPIENT)
        sys.exit(ERROR_CODE)

# Finds the message from the command line.
def getMessageFromCommandLineArgs(commandLineArgs):

    message = commandLineArgs[MESSAGE_INDEX]

    return(message)

# Functions for sending enough emails to fill up your inbox.
def busyAndImportantFunctions(commandLineArgs, emailAddresses):

    recipient = getRecipientFromCommandLineArgs(commandLineArgs, emailAddresses)
    emailList = getEmailListFromTxtFile()
    for email in emailList:
        sendEmail(recipient, email[EMAIL_CONTENTS], email[EMAIL_SUBJECT], email[EMAIL_FROM])

# Gets the emails from the txt file, splits it up and then sends it back as an array
def getEmailListFromTxtFile():

    subjectEmailArray = []

    with open('../bin/busyAndImportantEmails.txt', 'r') as content_file:
        content = content_file.read()

    emailsWithSubjects = content.split('||')

    for email in emailsWithSubjects:
        subjectEmailArray.append(email.split('|'))

    return(subjectEmailArray)

# ------------------------------------------------------------------------------
# Main function.

# Gets the command line arguments and runs some checks, finds the recipient from
# the command line arguments, finds the message text from the command line args
# and then sends a mail using that info.

def main():

    commandLineArgs = getCommandLineArgs()
    emailAddresses = getEmailDictionary()
    commandType = getCommandTypeFromCommandLineArgs(commandLineArgs)

    if(commandType == commandTypeOptions['SendMail']):
        sendMailFunctions(commandLineArgs, emailAddresses)
    elif(commandType == commandTypeOptions['BusyAndImportant']):
        busyAndImportantFunctions(commandLineArgs, emailAddresses)

if __name__ == "__main__":
    main()
