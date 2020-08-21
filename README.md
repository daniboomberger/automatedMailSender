# Automated Mail Sender

This project was created as I deleted multiple accounts with an similar mail body so I thought why not to create an automated mail sender. Maybe there will be more but it's just an functional project so we will see soon....

## How does the program work
Create an json file with your E-Mail list and the provide the needed properties.
Attention --> json should start at 0 (maybe will be more dynamic in some time...) 
The Json layout is actually static and cannot be changed for now but the mail count that can be sent is set to 100
```json
{
    "0": {
        "subject": "subject",
        "receiver": "test@mail.com",
        "name": "Name",
        "formal": "Dear"
    }
}
```
As second create an text file with your template mail message
Attention --> variables need an dollar sign ($) infront of them
This is just some example it's dynamically modular
```
$formal $name

I would like to delete my data and my data

Best regards,
My Name
```


