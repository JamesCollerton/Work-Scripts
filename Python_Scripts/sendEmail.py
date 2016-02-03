import sys
import requests

# ------------------------------------------------------------------------------
# String constants to be printed to console.

ERROR_WRONG_NUM_COMMAND_LINE_ARGS = "\nError, wrong number of command line arguments.\n"
ERROR_INVALID_RECIPIENT = "\nError, invalid recipient.\n"
ERROR_INVALID_COMMAND_TYPE = "\nError, invalid command type.\n"

SUCCESS_MAIL_SENT = "\nSuccess, message sent\n"

# ------------------------------------------------------------------------------
# Integer constants.

ERROR_CODE = 1
NUM_NECCESSARY_COMMAND_LINE_ARGS = 4
RECIPIENT_INDEX = 2
MESSAGE_INDEX = 3
COMMAND_TYPE_INDEX = 1

# ------------------------------------------------------------------------------
# List of email addresses to be accessed. The dictionary keys are passed to
# the program on the command line.

emailAddresses = {'MeWork' : 'James.Collerton@thorogood.com',
                  'CharlotteWork' : 'Charlotte.Emms@phgroup.com',
                  'MeLive' : 'JamesCollerton@live.co.uk',
                  'MeGmail' : 'jc1175@my.bristol.ac.uk'}

commandTypeOptions = {'SendMail' : 'SendMail', 
                      'BusyAndImportant' : 'BusyAndImportant',
                      'CallMe' : 'CallMe'}

# ------------------------------------------------------------------------------
# Functions

# Gets the command line arguments and checks to make sure there are two.
def getCommandLineArgs():
    
    commandLineArgs = sys.argv

    if(len(commandLineArgs) != NUM_NECCESSARY_COMMAND_LINE_ARGS):
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

def sendMailFunctions(commandLineArgs):

    recipient = getRecipientFromCommandLineArgs(commandLineArgs)
    message = getMessageFromCommandLineArgs(commandLineArgs)
    sendEmail(recipient, message)
    print(SUCCESS_MAIL_SENT)

# Gets recipient from command line, then checks it's in the emails array.
def getRecipientFromCommandLineArgs(commandLineArgs):

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

def busyAndImportantFunctions(commandLineArgs):

    recipient = getRecipientFromCommandLineArgs

# Sends an email using Mail-Gun. Pretty standard set up from the website.
def sendEmail(recipient, message):

    key = 'key-17a8bba64262bd0139ac29b6d77e6f58'
    sandbox = 'sandbox03d7770e45654ce5a58c47f7f8a49647.mailgun.org'

    request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
    request = requests.post(request_url, auth=('api', key), data={
        'from': 'jamescollerton@live.co.uk',
        'to': recipient,
        'subject': 'Check request!',
        'text': message
    })

# ------------------------------------------------------------------------------
# Main function.

# Gets the command line arguments and runs some checks, finds the recipient from
# the command line arguments, finds the message text from the command line args
# and then sends a mail using that info.

def main():

    commandLineArgs = getCommandLineArgs()
    commandType = getCommandTypeFromCommandLineArgs(commandLineArgs)

    if(commandType == commandTypeOptions['SendMail']):
        sendMailFunctions(commandLineArgs)
    else if(commandType == commandTypeOptions['BusyAndImportant']):
        busyAndImportantFunctions(commandLineArgs)

if __name__ == "__main__":
    main()
