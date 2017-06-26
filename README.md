# ids-tools
snort_rules_sampler.py application randomly select (upon an uniform distribution) uncommented rules from the snort rules database 
(default /etc/snort/rules/). The size of the rules sample must be specified as argument (see the help info). Since some snort 
rules are multi-line defined, the sample size yielded could be slightly different.
