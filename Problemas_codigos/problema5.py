import pandas as pd

rl_procedimento_cid = open('sigtap-simplificado/rl_procedimento_cid.txt', 'r', encoding='UTF-8')
rl_procedimento_cid = rl_procedimento_cid.readlines()
tab_rl_procedimento_cid = []

for d in rl_procedimento_cid:
    dados = []
    co_procedimento = d[1:10].strip()  # Lê 10 digitos da primeira linha e para, não printa o resto
    co_cid = d[10:14].strip()
    st_principal = d[14].strip()
    dt_competencia = d[15:].strip()
    
    dados.append(co_procedimento)
    dados.append(co_cid)
    dados.append(st_principal)
    dados.append(dt_competencia)

tab_rl_procedimento_cid.append(dados)
tab_rl_procedimento_pd = pd.DataFrame(tab_rl_procedimento_cid, columns=['CO_PROCEDIMENTO','CO_CID','ST_PRINCIPAL','DT_COMPETENCIA'])
tab_rl_procedimento_pd.head()
