import dns.resolver


# Basic user interface header
print(r"""
                                                                  _     _
        / ___| ___ _ __ __ _| | __| | ___  ___  _____   _____ _ __|___  |
       | |  _ / _ \ '__/ _` | |/ _` |/ _ \/ __|/ _ \ \ / / _ \ '_ \  / /
       | |_| |  __/ | | (_| | | (_| | (_) \__ \  __/\ V /  __/ | | |/ /
        \____|\___|_|  \__,_|_|\__,_|\___/|___/\___| \_/ \___|_| |_/_/
                                                                                     """)

print("\n******************************************************************************")
print("\n* Copyright of Geraldoseven7, 2025                                           *")
print("\n* https://github.com/Geraldoseven7                                           *")
print("\n******************************************************************************")


res = dns.resolver.Resolver()

file = open("/home/robot/Documents/PC/DnsBrute/DnsBrute/wordlist.txt", 'r')
subdomains = file.read().splitlines()

target = input("Enter your target: ")

for subdomain in subdomains:
	try:
		sub_target = subdomain + '.' + target
		result = res.resolve(sub_target, "A")
		for ip in result:

			print(sub_target, "->", ip)
	except:
		pass
