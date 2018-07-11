#Botnet Synthetisizer

This application generates botnet traffic attack for cooperative (smart) vertical scanning of 
a target machine. Its only purpose is to support research and validation on related attacks 
detection mechanisms. 

Specifically, it was tested on Snort detection rule-based engine and portscan preprocessor.

Features:
 1. rate control 
 2. protocol selection (TCP or UDP)
 3. ports interval definition (including gap) 
 4. port interval sweeping policy (in-sequence, random, overlapping)

It was implemented based on nmap tool using python multithreading. Its use for mounting
real-world attacks is very limited since does not fully implement the necessary functionalities.
Beware, any malicious use of this application is beyound the objectives and falls outside our 
liabilities. 
This is an alpha release.
