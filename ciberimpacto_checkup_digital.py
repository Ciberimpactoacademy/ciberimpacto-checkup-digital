
import streamlit as st
from datetime import datetime
from pathlib import Path
import pandas as pd

st.set_page_config(
    page_title="CiberImpacto | Check-Up Digital",
    page_icon="🛡️",
    layout="centered"
)

PRIMARY = "#1482FF"
BLUE = "#0A62FF"
LIGHT_BLUE = "#40BDF9"
TURQUOISE = "#12E9CA"
WHITE = "#FFFFFF"

st.markdown(
    f"""
    <style>
        .stApp {{
            background: linear-gradient(135deg, #07111F 0%, #0A1F44 45%, #062B3F 100%);
            color: {WHITE};
        }}

        section[data-testid="stSidebar"] {{
            background: #061426;
        }}

        h1, h2, h3, h4, p, label, span, div {{
            font-family: Arial, Helvetica, sans-serif;
        }}

        .main-card {{
            background: rgba(255, 255, 255, 0.08);
            padding: 28px;
            border-radius: 24px;
            border: 1px solid rgba(255,255,255,0.14);
            box-shadow: 0 18px 50px rgba(0,0,0,0.25);
            margin-bottom: 20px;
        }}

        .hero-title {{
            font-size: 38px;
            line-height: 1.1;
            font-weight: 800;
            color: {WHITE};
            margin-bottom: 10px;
        }}

        .hero-subtitle {{
            font-size: 18px;
            color: #D9F7FF;
            margin-bottom: 10px;
        }}

        .badge {{
            display: inline-block;
            padding: 8px 14px;
            border-radius: 999px;
            background: linear-gradient(90deg, {PRIMARY}, {TURQUOISE});
            color: #001020;
            font-weight: 700;
            margin-bottom: 18px;
        }}

        .small-text {{
            color: #BFD8E8;
            font-size: 14px;
        }}

        .result-card {{
            padding: 24px;
            border-radius: 22px;
            margin-top: 22px;
            color: #001020;
            font-weight: 600;
        }}

        .risk-low {{
            background: linear-gradient(135deg, #12E9CA, #B8FFF4);
        }}

        .risk-medium {{
            background: linear-gradient(135deg, #FFD166, #FFF1BD);
        }}

        .risk-high {{
            background: linear-gradient(135deg, #FF9F1C, #FFD6A3);
        }}

        .risk-critical {{
            background: linear-gradient(135deg, #FF4D6D, #FFC2CC);
        }}

        .stButton > button {{
            background: linear-gradient(90deg, {PRIMARY}, {TURQUOISE});
            color: #001020;
            border: none;
            border-radius: 999px;
            padding: 12px 22px;
            font-weight: 800;
        }}

        .stDownloadButton > button {{
            background: linear-gradient(90deg, {TURQUOISE}, {LIGHT_BLUE});
            color: #001020;
            border: none;
            border-radius: 999px;
            padding: 12px 22px;
            font-weight: 800;
        }}

        div[data-testid="stRadio"] label {{
            background: rgba(255,255,255,0.07);
            padding: 10px 12px;
            border-radius: 12px;
            margin-bottom: 6px;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

logo_path = Path("logo_ciberimpacto.png")

with st.sidebar:
    if logo_path.exists():
        st.image(str(logo_path), use_container_width=True)
    else:
        st.markdown("## CiberImpacto")
        st.caption("Para mostrar o logótipo, coloque o ficheiro logo_ciberimpacto.png no GitHub.")

    st.markdown("---")
    st.markdown("### Check-Up Digital")
    st.write("Diagnóstico rápido para empresas.")
    st.markdown("**Duração:** 2 a 3 minutos")
    st.markdown("**Resultado:** imediato")

st.markdown(
    """
    <div class="main-card">
        <div class="badge">🛡️ CiberImpacto Check-Up Digital</div>
        <div class="hero-title">A sua empresa está preparada para um ataque informático?</div>
        <div class="hero-subtitle">
            Responda a 8 perguntas rápidas e descubra o nível de exposição da sua empresa.
        </div>
        <p class="small-text">
            Ferramenta prática de sensibilização para phishing, passwords, ransomware e fuga de dados.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

with st.form("checkup_form"):
    st.markdown("## 1. Dados da empresa")

    col1, col2 = st.columns(2)
    with col1:
        empresa = st.text_input("Nome da empresa")
        nome = st.text_input("Nome do responsável")
    with col2:
        email = st.text_input("Email")
        colaboradores = st.selectbox(
            "N.º de colaboradores",
            ["Até 10", "11 a 50", "51 a 250", "Mais de 250"]
        )

    st.markdown("## 2. Check-up rápido")

    perguntas = [
        {
            "q": "1. Recebe um email urgente a pedir para clicar num link e validar a password. O que faz?",
            "options": [
                "Clico no link para resolver rapidamente",
                "Respondo ao email a pedir confirmação",
                "Verifico o remetente e reporto internamente",
                "Reencaminho para os colegas"
            ],
            "correct": "Verifico o remetente e reporto internamente",
            "theme": "Phishing"
        },
        {
            "q": "2. Qual destas passwords é mais segura?",
            "options": [
                "Empresa2026",
                "Ciber123",
                "NomeDaEmpresa@2026",
                "Rio!Azul77#Porta"
            ],
            "correct": "Rio!Azul77#Porta",
            "theme": "Passwords"
        },
        {
            "q": "3. Recebe uma fatura de uma empresa desconhecida com o ficheiro Fatura.exe. O que faz?",
            "options": [
                "Abro para confirmar",
                "Envio para outro colega abrir",
                "Reporto como suspeito e não abro",
                "Guardo no computador"
            ],
            "correct": "Reporto como suspeito e não abro",
            "theme": "Malware"
        },
        {
            "q": "4. A empresa usa autenticação multifator MFA?",
            "options": [
                "Sim, em contas importantes",
                "Não",
                "Não sei",
                "Só em alguns computadores"
            ],
            "correct": "Sim, em contas importantes",
            "theme": "MFA"
        },
        {
            "q": "5. Os colaboradores recebem sensibilização em cibersegurança?",
            "options": [
                "Sim, regularmente",
                "Só uma vez",
                "Nunca",
                "Não sei"
            ],
            "correct": "Sim, regularmente",
            "theme": "Sensibilização"
        },
        {
            "q": "6. Existe procedimento para reportar incidentes?",
            "options": [
                "Sim, claro e comunicado",
                "Existe, mas poucos conhecem",
                "Não existe",
                "Não sei"
            ],
            "correct": "Sim, claro e comunicado",
            "theme": "Incidentes"
        },
        {
            "q": "7. A empresa realiza backups regulares?",
            "options": [
                "Sim, com testes de recuperação",
                "Sim, mas sem testes",
                "Não",
                "Não sei"
            ],
            "correct": "Sim, com testes de recuperação",
            "theme": "Backups"
        },
        {
            "q": "8. Um colaborador perde o portátil da empresa. O que deve acontecer?",
            "options": [
                "Esperar para ver se aparece",
                "Reportar de imediato e bloquear acessos",
                "Comprar outro equipamento",
                "Não fazer nada se tiver password"
            ],
            "correct": "Reportar de imediato e bloquear acessos",
            "theme": "Resposta a incidentes"
        }
    ]

    respostas = []
    for item in perguntas:
        resposta = st.radio(item["q"], item["options"], key=item["q"])
        respostas.append({
            "Pergunta": item["q"],
            "Tema": item["theme"],
            "Resposta": resposta,
            "Correta": item["correct"],
            "Certo": resposta == item["correct"]
        })

    submitted = st.form_submit_button("Ver resultado")

if submitted:
    total = len(respostas)
    certos = sum(1 for r in respostas if r["Certo"])
    percentagem = round((certos / total) * 100)

    if percentagem >= 85:
        nivel = "Baixo"
        css_class = "risk-low"
        mensagem = "A empresa demonstra boas práticas, mas deve manter sensibilização regular."
        recomendacao = "Reforçar campanhas periódicas e simulações de phishing."
    elif percentagem >= 60:
        nivel = "Médio"
        css_class = "risk-medium"
        mensagem = "Existem boas práticas, mas também fragilidades que podem ser exploradas."
        recomendacao = "Recomenda-se uma sessão prática de sensibilização em cibersegurança."
    elif percentagem >= 35:
        nivel = "Alto"
        css_class = "risk-high"
        mensagem = "A empresa apresenta exposição relevante a riscos digitais."
        recomendacao = "Recomenda-se formação de 4h ou 10h em Cibersegurança na Ótica do Utilizador."
    else:
        nivel = "Crítico"
        css_class = "risk-critical"
        mensagem = "A empresa pode estar muito exposta a phishing, malware e fuga de dados."
        recomendacao = "Recomenda-se intervenção urgente com diagnóstico, formação e plano de ação."

    st.markdown(
        f"""
        <div class="result-card {css_class}">
            <h2>Resultado: Risco {nivel}</h2>
            <h3>{percentagem}% de boas práticas identificadas</h3>
            <p>{mensagem}</p>
            <p><strong>Recomendação:</strong> {recomendacao}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    df = pd.DataFrame(respostas)
    temas_a_melhorar = df[df["Certo"] == False]["Tema"].tolist()

    if temas_a_melhorar:
        st.warning("Temas a melhorar: " + ", ".join(temas_a_melhorar))
    else:
        st.success("Excelente resultado. A empresa demonstrou boas práticas nos temas avaliados.")

    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    relatorio = f"""
CIBERIMPACTO - CHECK-UP DIGITAL

Data: {data}
Empresa: {empresa}
Responsável: {nome}
Email: {email}
N.º de colaboradores: {colaboradores}

Resultado global: Risco {nivel}
Pontuação: {certos}/{total}
Percentagem: {percentagem}%

Resumo:
{mensagem}

Recomendação:
{recomendacao}

Temas a melhorar:
{", ".join(temas_a_melhorar) if temas_a_melhorar else "Sem fragilidades relevantes identificadas neste check-up."}

Próximo passo sugerido:
Agendar uma sessão de sensibilização em cibersegurança com a CiberImpacto.
"""

    st.download_button(
        "Descarregar relatório",
        data=relatorio,
        file_name="relatorio_checkup_digital_ciberimpacto.txt",
        mime="text/plain"
    )

    csv = df.to_csv(index=False).encode("utf-8-sig")
    st.download_button(
        "Descarregar respostas em CSV",
        data=csv,
        file_name="respostas_checkup_digital.csv",
        mime="text/csv"
    )

    st.markdown("## Quer uma proposta?")
    st.info("Envie este relatório para catia.verissimo@ciberimpacto.pt ou use-o como base para contacto comercial.")

st.markdown(
    """
    <br>
    <p class="small-text" style="text-align:center;">
        CiberImpacto – Formação e Eventos | Capacitar pessoas. Proteger organizações.
    </p>
    """,
    unsafe_allow_html=True
)
