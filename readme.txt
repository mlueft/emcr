Description
-----------
This project wants to build a console application to read and write embroidery cards.

Usage
-----
emco.py -cr -p 

-c           card reader:
                  vikant - Vikandbox
-p           port

-d           Clear card
-l           Load content from card.
-s           Save content to card.
-f           Data folder. Content of this folder is stored to card.
                          Content of the card is stored to this folder.

Supported Card readers
----------------------
* Vikandbox with serial connection

Supported Cards
---------------
* Vikant card Type I

Why
---
After repairing a death Brother PE-180D I have got from Ebay I bought a Serial vikant
box. Unfortunately It was damaged too. The card reader didn't recognize the memory 
chip on the card. To get an idea what was going on I analyzed the traffic on the com port
and wrote a card reader emuation. Finally I brought everything back to life. 

Embroidery cards are a dying technology and knowledge about it is at risc to get lost.
There is no software running on linux.
There is no software running in the console.

An open software to write and read the cards is my attempt to preserve the knowledge
and to extend the live of this technology.