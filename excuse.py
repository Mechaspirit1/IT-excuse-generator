#Because all IT workers are assholes, might as well emrbrace it ! 
from random import choice

def basic_generation(art, adj, con, act, prp, col, sol):
    excuse  =   f"{choice(art)} {choice(adj)} {choice(con)} {choice(act)} {choice(prp)} {choice(col)}. {choice(sol)}."
    return excuse

articles    =   ["The", "A"]

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
        "Domain", "Tenent", "Kernel",
        "Documentation", "SSH", "Telnet",
        "Binaries", "Scripts", "Containers",
        "Orchestrator", "Regex", "Build system",
        "Ticket", "VPN", "UML diagram",
        "Circuit", "Power Supply", "Shell",
        "Compiler", "Assembler", "Interpreter",
        "Filesystem", "Hardware", "Cluster",
        "Observability stack", "Logs", "Init system",
        "Modem", "Router", "NFS server",
        "Deamon", "VLAN", "Certificate",
        "Security Policy", "Access token", "Active directory",
        "Firmware", "Cron job", "Parser",
        "Git repository", "Microservice", "Dependencies",
        "Endpoints", "HTTP request", "User permissions",
        "User roles", "RBAC", "Priviledge escalation",
        "Authentication", "Authotization", "AI Agent",
        "Agentic", "Machine learning", "Large language model",
        "Neural network", "Generative AI", "Tensor cores",
        "Data center", "Mainframe", "Critical systems",
        "Graphics card", "Chipset", "Expansion slots",
        "Server rack", "Supercomputer", "Microcode",
        "Storage", "Antivirus", "Threat detector",
        "Infraestructure", "TCP/IP Layer", "Communications protocol",
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
        "hardware failure", "a broken update", "mallicious activity", 
        "threat actors", "misconfiguration", "layer 8 issues",
        "PEBKAC errors", "ID-10-t errors", "missing dependencies",
        "mandatory password rotation", "vendor lock-in", "a kernel panic",
        "packet loss", "SMART errors", "bad blocks",
        "lose SATA cables", "UPS failure", "API rate limits",
        "management intervention", "trashing of the flow of data"
        ]

solution    =   [
        "Rotate drivers to previous working version",
        "Turn it on and off again",
        "Pull power cable from the wall",
        "Run sudo rm -rf / --no-preserve-root",
        "Delete boot partition and try again",
        "Consult documentation",
        "Open a ticket with manufacturer"
        ]

#print(len(concepts))
#print(len(adjectives))
print(basic_generation(articles, adjectives, concepts, actions, prepositions, conditional, solution))
