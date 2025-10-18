def valida_ip(ip):
    nums = ip.split(".")
    if len(nums) != 4:
        return False
    if int(nums[0]) < 1 or int(nums[0]) > 255:
        return False
    for num in nums[1:]:
        if int(num) < 0 or int(num) > 255:
            return False
        
    return True


def read_ips(arq_ips):
    with open(caminho + arq_ips, 'r') as arq:
        ips = arq.read()
        ips = ips.splitlines()
    gera_arquivos_ips(ips)


def gera_arquivos_ips(ips):
    with open(caminho + '14-ips_validos', 'w') as arq:
        texto_arq = ""
        ips_validos = filter(valida_ip, ips)
        for ip in ips_validos:
            texto_arq += ip
            texto_arq += "\n"
        arq.write(texto_arq)

    with open(caminho + '14-ips_invalidos', 'w') as arq:
        texto_arq = ""
        ips_invalidos = filter(lambda i: not valida_ip(i), ips)
        for ip in ips_invalidos:
            texto_arq += ip
            texto_arq += "\n"
        arq.write(texto_arq)


caminho = "txt/"
list_ips = []
read_ips('14-ips.txt')