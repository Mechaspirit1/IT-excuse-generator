#!/usr/bin/env python3
#Because all IT workers are assholes, might as well embrace it !
import argparse
from random import choice

def basic_mode(adj, con, act, prp, col, sol):
    phrase = f"The {choice(adj)} {choice(con)} {choice(act)} {choice(prp)} {choice(col)}. {choice(sol)}."
    return phrase

def template_mode(adj, con, act, col, sol):
    template    =   [
            f"Due to {choice(col)}, the {choice(adj)} {choice(con)} is experiencing some downtime. I'll warn you when it comes back.",
            f"The {choice(adj)} {choice(con)} is being updated, until that's over there's nothing i can do.",
            f"Have you tried to {choice(sol)} ?",
            f"Ah yes, the {choice(con)} {choice(act)}. We're working on it.",
            f"{choice(sol)}. That usually works.",
            f"We have been experiencing some {choice(adj)} {choice(col)}, we're trying to fix it on our end.",
            f"Maybe your {choice(adj)} {choice(con)} {choice(act)}. Try talking to support.",
            f"That sounds like a classic case of {choice(adj)} {choice(col)}. Try to {choice(sol)}.",
            f"The {choice(adj)} {choice(con)} is going through some routine maintenance, sorry about that.",
            ]
    return choice(template)

#Probably an overly complicated way of doing this but it ensures that every adjective is unique
def chaos_mode(adj, con, adj_ammount):
    string = ' '
    string_store = ' '
    loop = 0

    while True:
        f_string = (choice(adj) + ' ')
        if f_string not in string_store:
            string += f_string
            string_store += f_string
            loop+=1
        else:
            continue
        if loop == adj_ammount:
            break
    return f"{string}{choice(con)}"

def bofh_mode(adj, con, act, col, sol):
    templates   =    [
        f"The {choice(con)} is functioning perfectly. Have you considered that you may be the issue?",
        f"Your {choice(con)} {choice(act)} after detecting {choice(col)}. This was done for everyone's safety.",
        f"The {choice(adj)} {choice(con)} is refusing to cooperate with you specifically.",
        f"I fixed it five minutes ago. Whatever you're seeing now is a brand new problem.",
        f"The {choice(con)} has entered self-defense mode after detecting excessive user interaction.",
        f"Your ticket has been marked as 'Works on my machine.'",
        f"I'm afraid the {choice(con)} has become self-aware and no longer respects management.",
        f"The issue was escalated, laughed at, and then closed.",
        f"The {choice(adj)} {choice(con)} has been quarantined until it forgets what you did to it.",
        f"The problem disappeared the moment I walked over. I'm charging this one to morale.",
        f"The {choice(con)} is busy processing more important requests.",
        f"We've determined that replacing the user would be more cost-effective than replacing the hardware.",
        f"Please stop clicking random buttons. The {choice(con)} is becoming frightened.",
        f"The {choice(con)} is operating within specification. Your expectations are not.",
        f"The {choice(adj)} {choice(con)} rebooted out of self-preservation.",
        f"I could explain the problem, but then I'd have to explain networking.",
        f"The problem has been isolated. Please stop interacting with it.",
        f"The {choice(con)} has been promoted to management and no longer performs useful work.",
        f"Unfortunately, the {choice(con)} has inherited the same configuration strategy as the rest of the department.",
        f"The {choice(con)} appears to be allergic to your workflow.",
        ]
    return choice(templates)

def main():
    adjectives  =   [
            "Distributed", "Virtualized", "Legacy",
            "Web-based", "Generative", "Future-proof",
            "Stable", "Redundant", "Zero-trust",
            "Physical", "Electronic", "Self-hosted",
            "Cloud-based", "Object oriented", "Functional",
            "High-availability", "Procedural", "Cutting-edge",
            "Multimedia", "Automated", "Proprietary",
            "Open-source", "Source-available", "Hybrid",
            "Scalable", "Wireless", "Embedded",
            "Compact", "Up-to-date", "Interactive",
            "Asynchronous", "Encrypted"
            ]

    concepts    =   [
            "Computer", "Network", "Server",
            "Cloud", "Virtual Machine", "Application",
            "Text editor", "Operating system", "Internet",
            "VPS", "Hypervisor", "Service provider",
            "Architecture", "Memory", "CPU",
            "Motherboard", "Database", "IDE",
            "Environment", "Back end", "Terminal",
            "Cooling system", "Client", "Package Manager",
            "Package", "RJ45", "Serial cable",
            "Domain", "Tenant", "Kernel",
            "Documentation", "SSH", "Telnet",
            "Binaries", "Scripts", "Containers",
            "Orchestrator", "Regex", "Build system",
            "Ticket", "VPN", "UML diagram",
            "Circuit", "Power Supply", "Shell",
            "Compiler", "Assembler", "Interpreter",
            "File-system", "Hardware", "Cluster",
            "Observability stack", "Logs", "Init system",
            "Modem", "Router", "NFS server",
            "Daemon", "VLAN", "Certificate",
            "Security Policy", "Access token", "Active directory",
            "Firmware", "Cron job", "Parser",
            "Git repository", "Micro-service", "Dependencies",
            "Endpoints", "HTTP request", "User permissions",
            "User roles", "RBAC", "Privilege escalation",
            "Authentication", "Authorization", "AI Agent",
            "Agentic model", "Machine learning model", "Large language model",
            "Neural network", "Generative AI", "Tensor cores",
            "Data center", "Mainframe", "Critical systems",
            "Graphics card", "Chipset", "Expansion slots",
            "Server rack", "Supercomputer", "Microcode",
            "Storage", "Antivirus", "Threat detector",
            "Infrastructure", "TCP/IP Layer", "Communications protocol",
            "BIOS", "UEFI", "Instruction set",
            "IOT devices"
            ]

    actions   =   [
            "rebooted", "was reinitialized", "desynchronized",
            "corrupted", "fragmented", "broke down",
            "underflowed", "failed", "overheated",
            "went offline", "disconnected", "was invalidated",
            "was unassigned", "expired", "locked down",
            "closed", "timed out", "was removed"
            ]

    prepositions    =   [
            "due to", "because of", "owing to",
            "on account of"
            ]

    conditional =   [
            "solar flares", "power outages", "gamma radiation",
            "a buffer overflow", "poor airflow", "deprecated drivers",
            "glitches", "undocumented bugs", "clock skew",
            "insufficient resource allocation", "systemd failures", "race conditions",
            "hardware failure", "a broken update", "malicious activity", 
            "threat actors", "misconfiguration", "layer 8 issues",
            "PEBKAC errors", "ID-10-t errors", "missing dependencies",
            "mandatory password rotation", "vendor lock-in", "a kernel panic",
            "packet loss", "SMART errors", "bad blocks",
            "loose SATA cables", "UPS failure", "API rate limits",
            "management intervention", "trashing of the flow of data"
            ]

    solution    =   [
            "Rotate the drivers to previous working version",
            "Turn it on and off again",
            "Pull the power cable from the wall",
            "Run sudo rm -rf / --no-preserve-root",
            "Run while :; do mkdir x && cd x; done",
            "Delete the boot partition and try again",
            "Consult the documentation",
            "Open a ticket with the manufacturer",
            "Re-install the operating system",
            "Compile a new kernel",
            "Defrag the disk",
            "Call 1 (800) 328-3425",
            "Disasemble the unit and put it back together",
            "Escalate issue to a superior"
            ]

    parser = argparse.ArgumentParser(description="IT excuse generator | \033]8;;https://github.com/Mechaspirit1\033\\A tool by Pablo Loschi (Mechaspirit1)\033]8;;\033\\")

    parser.add_argument("-b", "--basic", action="store_true", help="Generates a basic, randomized string of nonsense. Default if no argument is passed")
    parser.add_argument("-t", "--template", action="store_true", help="Chooses from a list of templates and randomizes their contents")
    parser.add_argument("-c", "--chaos", type=int, metavar="N", choices=range(2, 31), help="Generates a nonsensical tech concpet based on the ammount of adjectives passed as input (2-30)")
    parser.add_argument("-o", "--bofh", action="store_true", help="Chooses from a list of templates written in a manner that resembles classic BOFH (Bastard operator from hell) style excuses")
    parser.add_argument("-v", "--version", action="store_true", help="Displays version number")

    args = parser.parse_args()
    
    if args.template:
        print(template_mode(adjectives, concepts, actions, conditional, solution))
    elif args.chaos is not None:
        print(chaos_mode(adjectives, concepts, args.chaos))
    elif args.bofh:
       print(bofh_mode(adjectives, concepts, actions, conditional, solution))
    elif args.version:
        print("excuse version 1.0.0 written in python 3.14.6")
    else:
        args = args.basic
        print(basic_mode(adjectives, concepts, actions, prepositions, conditional, solution))

if __name__ == "__main__":
    main()
