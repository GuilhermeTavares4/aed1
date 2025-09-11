def tira_tags(html):
    texto_final = ""
    pode_adicionar = True
    i = 0
    while i < len(html):
        if html[i] == "<":
            pode_adicionar = False

        if html[i] == ">":
            pode_adicionar = True
        else:
            if pode_adicionar:
                texto_final += html[i]
        i += 1
    return texto_final


html = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Document</title></head><body><h1>jaiogjoiajgriaoe</h1><h3>agiorgjioagja    </h3><div>fodase 123</div></body></html>'
        
print(tira_tags(html))