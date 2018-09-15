# twilio-itsoktoben

Available on Docker Hub:

`docker pull ianauger/twilio-itsoktobenew`

This is a pretty basic Python app which uses the Twilio API to send a text reassuring you that yes, it's okay to be new.

It does require a list of environment variables to work:

- TWILIO_SID: your Twilio account SID
- TWILIO_TOKEN: the API secret token
- TWILIO_TN: the telephone number on Twilio's network sending the SMS
- DEST_TN: the telephone number the SMS is being sent to

For obvious reasons, I really didn't want to hard code in my own API information or phone numbers.  :)

Points for improvement:

- May try using the Alpine image for Python -- when built, this image actually turns out to be nearly a gig, with most of that just being the base image.
