#!/usr/bin/env python3

"""
Extract subdomains from https://subdomainfinder.c99.nl/index.php
Why? No access to API
"""

import argparse
import requests
import re
import os

parser = argparse.ArgumentParser(
    description='This tool extracts subdomains from c99.nl API'
)
parser.add_argument(
    '-d', '--domain', required=True,
    help='Domain to extract its subdomains '
)
parser.add_argument(
    '-o', '--output', required=False,
    help='Optional output text file'
)

args = parser.parse_args()
domain = args.domain
output = args.output

if output is None:
    output = False
else:
    output = output if '/' in output else os.getcwd() + '/' + output

url = 'https://subdomainfinder.c99.nl/index.php'
data = {
    "CSRF1001916923901630": "breach101721828", "CSRF1083936598279085": "burglar108154104",  "CSRF1067688052058917": "subnet_ip108883961", "CSRF1092594774484847": "drudge104079447", "CSRF1015282408545270": "hack105745452", "CSRF1012220801901055": "malware108280103", "CSRF1016458212661252": "addict105855134", "CSRF1035633125145602": "pirating109499365", "CSRF1069420069821804": "spammer108789039", "CSRF1102167832295501": "stalker106586596", "CSRF1079129295658785": "stalker110230215", "CSRF1068628521338614": "tech109612967", "CSRF1089597530982755": "hack100266877", "CSRF1103398787336263": "cracker105264482", "CSRF1105982712837506": "phishing104541331", "CSRF1061454295670378": "intrusion101376104", "CSRF1005424587883139": "counterfeiter105708780", "CSRF1006522558048882": "ipv4109770757", "CSRF1008029336941873": "tech106270001", "CSRF1004204481395128": "CSRF100218525", "CSRF1052504557599956": "spammer103449316", "CSRF1005996292956933": "network109367504", "CSRF1006235369195523": "identitytheft107405739", "CSRF1018306035582601": "hack109696431", "CSRF1022945241721948": "hacking104519114", "CSRF1083137977276912": "cyberspace103064266", "CSRF1095180337257817": "ipv4104924137", "CSRF1089500203509430": "pirating101853687", "CSRF1073944206927736": "hack105178350", "CSRF1014169354197328": "phisher102054566", "CSRF1003776417543564": "phisher107504169", "CSRF1067991438626924": "identitytheft109864202", "CSRF1043738465410709": "tenant106986218", "CSRF1082833135563301": "subnet_ip105767118", "CSRF1045772835637755": "CSRF103248068", "CSRF1071340627709913": "firewall100779759", "CSRF1056418537637442": "cyber100979021", "CSRF1066835625309172": "counterfeiter110905638", "CSRF1034574906997915": "malware100908325", "CSRF1078542347007207": "cyber102793084", "CSRF1071008542766482": "spy108438716", "CSRF9843427068797932": "programmer104789312", "jn": "JS aan, T aangeroepen, CSRF aangepast", "domain": domain, "lol-stop-reverse-engineering-my-source-and-buy-an-api-key": "895bb11f63f6be3048b9e27411803f77180bf975", "scan_subdomains": "", "privatequery": "on"}
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
req = requests.post(url, data=data, headers=header)
match = re.findall("<a class='link' target='_blank' href='//(.*?)'>", req.text)
# match = set(match)
subdomains = set()
for d in match:
    if d not in subdomains:
        print(d)
        subdomains.add(d)

if output:
    with open(output, 'w') as writer:
        writer.write('\n'.join(subdomains))

    output = '.'.join(output.split('.')[:-1])+'_ip.txt'
    match = re.findall("<a class='link' target='_blank' href='/geoip.php\?ip=(.*?)'>", req.text)
    ips = set()
    for ip in match:
        if ip not in ips and ip != 'none':
            ips.add(ip)

    with open(output, 'w') as writer:
        writer.write('\n'.join(ips))
