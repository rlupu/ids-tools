#Botnet Synthetisizer
This application generates botnet traffic attack for cooperative (smart) vertical scanning of 
a target machine. Its only purpose is to support research, validation on related attacks 
detection mechanisms and for pentesting activities. 

Specifically, it was tested on Snort detection rule-based engine and portscan preprocessor.

Features:
 1. rate control 
 2. protocol selection (TCP or UDP)
 3. ports interval definition (including gap) 
 4. port interval sweeping policy (in-sequence, random, overlapping)

It was implemented based on nmap tool using python multithreading. Its use for mounting
real-world attacks is very limited since does not fully implement the necessary functionalities.
Beware, any malicious use of this application is beyond the objectives and falls outside our 
liabilities. 
This is an alpha release.


#Snort rules sampler
snort_rules_sampler.py application randomly select (upon an uniform distribution) uncommented rules from the snort rules database 
(default /etc/snort/rules/). The size of the rules sample must be specified as argument (see the help info). Since some snort 
rules are multi-line defined, the sample size yielded could be slightly different.

Latest tests achieved on databases with over 30,000 rules. 


