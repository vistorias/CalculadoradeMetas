import streamlit as st

def calcular_meta(valor_mensal, indicadores):
    pesos = {
        'Produção': 0.15,
        'Ticket Médio': 0.15,
        'Despesas': 0.15,
        'Satisfação Cliente': 0.275,
        'Pesquisa Clima': 0.0688,
        'Turnover': 0.0688,
        'ABS': 0.0688,
        'Treinamento': 0.0688
    }

    total_trimestral = valor_mensal * 3
    total_recebido = total_trimestral

    for mes in range(3):
        for indicador in pesos.keys():
            if not indicadores[mes][indicador]:
                total_recebido -= valor_mensal * pesos[indicador]
    
    return total_recebido

# Interface no Streamlit
st.title("📊 Calculadora de Metas Trimestrais")

valor_mensal = st.number_input("Digite o valor mensal da meta:", min_value=0.0, step=100.0)

meses = ["Janeiro", "Fevereiro", "Março"]
indicadores = ["Produção", "Ticket Médio", "Despesas", "Satisfação Cliente", "Pesquisa Clima", "Turnover", "ABS", "Treinamento"]

checkboxes = []
for mes in meses:
    st.subheader(mes)
    check_mes = {}
    for indicador in indicadores:
        check_mes[indicador] = st.checkbox(f"{indicador} ({mes})", value=True)
    checkboxes.append(check_mes)

if st.button("Calcular"):
    resultado = calcular_meta(valor_mensal, checkboxes)
    st.success(f"💰 Valor final da meta trimestral: R$ {resultado:.2f}")