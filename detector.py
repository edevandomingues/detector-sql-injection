# Detector v2.3 - ULTIMA - Agora vai!
print("=== DETECTOR v2.3 - ULTIMATE ===")
print("Digite 'sair' para fechar\n")

while True:
    codigo = input("Cole o codigo para analisar: ")
    if codigo.lower() == "sair":
        break

    # deixa tudo minusculo e troca aspa estranha
    c = codigo.lower().replace("’", "'").replace("‘", "'")

    # REGRAS SIMPLES QUE PEGAM TUDO
    if "drop table" in c or "delete from" in c or "--" in c:
        print("--> 🚨 VULNERABILIDADE! Comando perigoso!")
    elif "or" in c and ("=" in c and "'" in c):
        print(f"--> 🚨 VULNERABILIDADE! Classico SQL Injection! Detectado: or + ' + =")
    elif "1=1" in c or "'='" in c or "'1'='1'" in c or "or'1'" in c.replace(" ", ""):
        print("--> 🚨 VULNERABILIDADE! Padrao 1=1 detectado!")
    else:
        print("--> ✅ Codigo parece seguro.")
    
    print("-" * 30)