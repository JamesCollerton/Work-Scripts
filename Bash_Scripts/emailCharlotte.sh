# ------------------------------------------------------------------------------

# emailCharlotte.sh

# This script is used so I can ping off a quick email to Charlotte from the
# command line. It takes an argument of the email body.

# ------------------------------------------------------------------------------

python ../Python_Scripts/sendEmail.py SendMail MeGmail "$@"
