# IT excuse generator
A technical jargon (bullshit) generator aimed at IT support, sysadmins, programmers, engineers and so on.
Need a quick excuse as to why you're behind your deadlines ? Maybe your oh-so-beloved coworkers are having
trouble connecting to the corporate VPN. Is someone pestering you in teams about a ticket you didn't even
bother to read ? Fret not ! This simple script is sure to fool all but the most minimally tech literate
corporate drone !


Inspired by experiences at my last internship with Microsoft administration (glad that's over),
where i coincidentally became acquainted with BOFH (Bastard operator from hell) stories, which i would never
have heard of otherwise because i am nowhere near old enough to remember them at their peak, 
and other funny tales and personal experiences from greybeards that have been messing around with
UNIX boxes and Windows NT/Domain services since before i was in diapers.

# Installation
Since this one has no external dependencies, installation is pretty straight forward.

```bash 
git clone https://github.com/Mechaspirit1/IT-excuse-generator && cd IT-excuse-generator
chmod +x excuse.py && mv excuse.py excuse
sudo mv excuse /usr/local/bin
``` 
# Functionality
Currently there are four available modes of generation, which are detailed in the help session.

Running ```excuse -h``` or ```excuse --help``` outputs the following: 

```bash
usage: excuse.py [-h] [-b] [-t] [-c N] [-o]

IT excuse generator | A tool by Pablo Loschi (Mechaspirit1)

options:
  -h, --help      show this help message and exit
  -b, --basic     Generates a basic, randomized string of nonsense. Default if no argument is passed
  -t, --template  Chooses from a list of templates and randomizes their contents
  -c, --chaos N   Generates a nonsensical tech concpet based on the ammount of adjectives passed as input (2-30)
  -o, --bofh      Chooses from a list of templates written in a manner that resembles classic BOFH (Bastard operator from hell) style excuses
  -v, --version   Displays version number
```

Pairs well with ```cowsay```

```bash
$ excuse -t | cowsay
 _______________________________________
/ Due to poor airflow, the Up-to-date   \
| Data center is experiencing some      |
| downtime. I'll warn you when it comes |
\ back.                                 /
 ---------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

# Disclaimer
This is for entertainment purposes only, but if you end up actually using this irl send me a screenshot :^)

# License
[MIT](https://choosealicense.com/licenses/mit/)

