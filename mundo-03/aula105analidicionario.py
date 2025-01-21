def notas(*n, sit=False):
    r = {}
    r["Total"] = len(n)
    r["Maior"] = max(n)
    r["Menor"] = min(n)
    r["Média"] = sum(n)/len(n)
    if sit:
        if r["Média"] >= 7:
            r["Situação"] = "Boa"
        elif r["Média"] >= 5:
            r["Situação"] = "Razoável"
        else:
            r["Situação"] = "Ruim"
    return r


resp = notas(10, 5, 2, 3, 9, sit=True)
print(resp)
