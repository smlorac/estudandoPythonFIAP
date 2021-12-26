import platform

print("Distribuição do SO: ", platform.platform())
print("Nome do SO: ", platform.system())
print("Versão do SO: ", platform.release())
print("Arquitetura: ", platform.architecture())
print("Nome do computador: ", platform.node())
print("Tipo de máquina: ", platform.machine())
print("Processador: ", platform.processor())
print("Versão do Python: ", platform.python_version())