import streamlit as st
from datetime import datetime
from pathlib import Path

st.set_page_config(
    page_title="CiberImpacto | Check-Up Digital",
    page_icon="🛡️",
    layout="centered"
)

PRIMARY = "#1482FF"
BLUE = "#0A62FF"
LIGHT_BLUE = "#40BDF9"
TURQUOISE = "#12E9CA"
DARK = "#061426"
TEXT = "#0B1626"

st.markdown(
    f"""
    <style>
        .stApp {{
            background: #F4FAFF;
            color: {TEXT};
        }}

        h1, h2, h3, h4, p, label, span, div {{
            font-family: Arial, Helvetica, sans-serif;
        }}

        .hero {{
            background: linear-gradient(135deg, {BLUE}, {PRIMARY} 55%, {TURQUOISE});
            padding: 30px;
            border-radius: 26px;
            color: white;
            margin-bottom: 24px;
            box-shadow: 0 14px 35px rgba(10, 98, 255, 0.25);
        }}

        .hero h1 {{
            color: white;
            font-size: 34px;
            line-height: 1.12;
            margin-bottom: 8px;
        }}

        .hero p {{
            color: #EFFFFF;
            font-size: 17px;
            margin-bottom: 0;
        }}

        .top-badge {{
            display: inline-block;
            background: rgba(255,255,255,0.20);
            border: 1px solid rgba(255,255,255,0.35);
            padding: 7px 13px;
            border-radius: 999px;
            font-weight: 700;
            margin-bottom: 14px;
        }}

        .section-title {{
            color: {BLUE};
            font-size: 24px;
            font-weight: 800;
            margin: 18px 0 10px 0;
        }}

        .question-box {{
            background: white;
            color: {TEXT};
            padding: 18px 20px;
            border-radius: 18px;
            border-left: 8px solid {PRIMARY};
            box-shadow: 0 8px 24px rgba(5, 35, 80, 0.08);
            margin: 18px 0 8px 0;
        }}

        .question-box strong {{
            color: {BLUE};
            font-size: 17px;
        }}

        .question-box p {{
            color: {TEXT};
            margin: 6px 0 0 0;
            font-size: 16px;
        }}

        .ransom-box {{
            background: linear-gradient(135deg, #061426, #2B0B16);
            color: white;
            padding: 24px;
            border-radius: 22px;
            border: 1px solid rgba(255,255,255,0.14);
            box-shadow: 0 14px 35px rgba(43, 11, 22, 0.28);
            margin: 18px 0 14px 0;
        }}

        .ransom-box h2 {{
            color: white;
            margin-top: 0;
            font-size: 24px;
        }}

        .ransom-alert {{
            background: rgba(255,255,255,0.09);
            border: 1px solid rgba(255,255,255,0.18);
            border-left: 7px solid #FF4D4D;
            padding: 16px;
            border-radius: 16px;
            margin-top: 14px;
        }}

        .ransom-alert strong {{
            color: #FFFFFF;
            font-size: 17px;
        }}

        .ransom-alert p {{
            color: #F4F7FA;
            font-size: 15px;
            margin: 8px 0 0 0;
        }}

        .safe-note {{
            background: #EFFFFB;
            color: #083526;
            border-left: 7px solid {TURQUOISE};
            padding: 15px 18px;
            border-radius: 16px;
            box-shadow: 0 8px 20px rgba(5, 35, 80, 0.06);
            margin: 10px 0 20px 0;
        }}

        .safe-note strong {{
            color: {BLUE};
        }}

        .result-box {{
            padding: 24px;
            border-radius: 22px;
            color: {TEXT};
            background: white;
            box-shadow: 0 12px 30px rgba(5,35,80,0.12);
            border-top: 8px solid {PRIMARY};
            margin-top: 20px;
        }}

        .stButton > button {{
            background: linear-gradient(90deg, {PRIMARY}, {TURQUOISE});
            color: #001020;
            border: none;
            border-radius: 999px;
            padding: 13px 24px;
            font-weight: 800;
            width: 100%;
        }}

        .stDownloadButton > button {{
            background: {BLUE};
            color: white;
            border: none;
            border-radius: 999px;
            padding: 12px 22px;
            font-weight: 800;
        }}

        div[data-testid="stSelectbox"] label {{
            display: none;
        }}

        .cta-link {{
            display: inline-block;
            margin-top: 12px;
            background: linear-gradient(90deg, {PRIMARY}, {TURQUOISE});
            color: #001020 !important;
            text-decoration: none;
            padding: 12px 18px;
            border-radius: 999px;
            font-weight: 800;
        }}

        .footer {{
            text-align: center;
            color: #5B6B7A;
            font-size: 13px;
            margin-top: 26px;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

logo_path = Path("logo_ciberimpacto.png")
if logo_path.exists():
    st.image(str(logo_path), width=210)
else:
    st.markdown("### CiberImpacto")

st.markdown(
    """
    <div class="hero">
        <div class="top-badge">🛡️ Check-Up Digital</div>
        <h1>Na ótica do utilizador: sabe identificar um ataque informático?</h1>
        <p>Veja uma simulação segura de ransomware e responda a 6 situações do dia a dia.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="section-title">Simulação segura: ransomware</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="ransom-box">
        <h2>⚠️ Os seus ficheiros foram bloqueados</h2>
        <div class="ransom-alert">
            <strong>Mensagem no ecrã:</strong>
            <p>“Todos os seus documentos foram encriptados. Para recuperar o acesso, pague nas próximas 24 horas. Não contacte a informática.”</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

acao_ransomware = st.selectbox(
    "O que faria primeiro nesta situação?",
    [
        "Selecionar resposta",
        "Pagava rapidamente para recuperar os ficheiros",
        "Tentava abrir vários ficheiros para confirmar o problema",
        "Desligava a ligação à rede e reportava de imediato ao responsável interno",
        "Ignorava a mensagem e continuava a trabalhar",
    ],
    key="simulacao_ransomware"
)

if acao_ransomware != "Selecionar resposta":
    if acao_ransomware == "Desligava a ligação à rede e reportava de imediato ao responsável interno":
        st.success("Resposta recomendada: isolar o equipamento da rede e reportar de imediato.")
    else:
        st.error("Atenção: esta ação pode aumentar o impacto do ataque ou atrasar a resposta.")

    st.markdown(
        """
        <div class="safe-note">
            <strong>Lição prática:</strong><br>
            Não pague, não tente resolver sozinho e não continue a usar o equipamento. Desligue a ligação à Internet/rede, avise rapidamente o responsável interno ou fornecedor de informática e siga o procedimento da empresa.
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('<div class="section-title">Check-up rápido</div>', unsafe_allow_html=True)
st.info("Responda às situações como se estivesse no seu dia de trabalho. O resultado aparece no final.")

perguntas = [
    {
        "tema": "Phishing",
        "pergunta": "Imagine que está a trabalhar e recebe um email urgente a pedir para clicar num link e validar a sua password. O que faz?",
        "opcoes": [
            "Selecionar resposta",
            "Clico no link para resolver rapidamente",
            "Respondo ao email a pedir confirmação",
            "Verifico o remetente e reporto internamente",
        ],
        "correta": "Verifico o remetente e reporto internamente",
        "explicacao": "Perante emails urgentes, deve validar o remetente e reportar internamente antes de clicar."
    },
    {
        "tema": "Passwords",
        "pergunta": "Qual destas passwords é mais segura?",
        "opcoes": [
            "Selecionar resposta",
            "Empresa2026",
            "Ciber123",
            "Rio!Azul77#Porta",
        ],
        "correta": "Rio!Azul77#Porta",
        "explicacao": "Passwords longas, únicas e difíceis de adivinhar são mais seguras."
    },
    {
        "tema": "Anexos perigosos",
        "pergunta": "Recebe uma fatura de uma empresa desconhecida com o ficheiro Fatura.exe. O que faz?",
        "opcoes": [
            "Selecionar resposta",
            "Abro para confirmar",
            "Envio para outro colega abrir",
            "Reporto como suspeito e não abro",
        ],
        "correta": "Reporto como suspeito e não abro",
        "explicacao": "Ficheiros .exe podem conter malware ou ransomware."
    },
    {
        "tema": "MFA",
        "pergunta": "A empresa usa autenticação multifator nas contas principais?",
        "opcoes": [
            "Selecionar resposta",
            "Sim, nas contas importantes",
            "Não",
            "Não sei",
        ],
        "correta": "Sim, nas contas importantes",
        "explicacao": "A autenticação multifator reduz o risco de acesso indevido às contas."
    },
    {
        "tema": "Formação",
        "pergunta": "Os colaboradores recebem sensibilização em cibersegurança?",
        "opcoes": [
            "Selecionar resposta",
            "Sim, regularmente",
            "Só uma vez",
            "Nunca",
        ],
        "correta": "Sim, regularmente",
        "explicacao": "A sensibilização regular ajuda a reduzir o erro humano."
    },
    {
        "tema": "Incidentes",
        "pergunta": "Um colaborador perde o portátil da empresa. O que deve acontecer?",
        "opcoes": [
            "Selecionar resposta",
            "Esperar para ver se aparece",
            "Reportar de imediato e bloquear acessos",
            "Não fazer nada se tiver password",
        ],
        "correta": "Reportar de imediato e bloquear acessos",
        "explicacao": "A rapidez no reporte permite bloquear acessos e reduzir danos."
    },
]

respostas = []
for i, item in enumerate(perguntas, start=1):
    st.markdown(
        f"""
        <div class="question-box">
            <strong>Pergunta {i} · {item['tema']}</strong>
            <p>{item['pergunta']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    resposta = st.selectbox(
        f"Pergunta {i}",
        item["opcoes"],
        key=f"pergunta_{i}",
        label_visibility="collapsed"
    )
    respostas.append({
        "tema": item["tema"],
        "pergunta": item["pergunta"],
        "resposta": resposta,
        "correta": item["correta"],
        "explicacao": item["explicacao"],
        "respondida": resposta != "Selecionar resposta",
        "certa": resposta == item["correta"],
    })

st.markdown("---")

if st.button("Ver resultado do check-up"):
    nao_respondidas = [r for r in respostas if not r["respondida"]]

    if nao_respondidas:
        st.warning("Responda a todas as perguntas antes de ver o resultado.")
    else:
        total = len(respostas)
        certas = sum(1 for r in respostas if r["certa"])
        percentagem = round((certas / total) * 100)

        if percentagem >= 85:
            nivel = "Baixo"
            recomendacao = "Manter sensibilização regular e simulações periódicas."
        elif percentagem >= 60:
            nivel = "Médio"
            recomendacao = "Realizar uma sessão prática de sensibilização em cibersegurança."
        elif percentagem >= 35:
            nivel = "Alto"
            recomendacao = "Implementar formação de 4h ou 10h em Cibersegurança na Ótica do Utilizador."
        else:
            nivel = "Crítico"
            recomendacao = "Atuar com urgência: diagnóstico, formação e plano de ação."

        st.markdown(
            f"""
            <div class="result-box">
                <h2>Resultado: Risco {nivel}</h2>
                <h3>{certas}/{total} respostas corretas · {percentagem}%</h3>
                <p><strong>Recomendação CiberImpacto:</strong> {recomendacao}</p>
                <p>Para saber mais sobre formação e sensibilização em cibersegurança, visite o site da CiberImpacto.</p>
                <a class="cta-link" href="https://www.ciberimpacto.pt" target="_blank">Visitar site da CiberImpacto</a>
            </div>
            """,
            unsafe_allow_html=True
        )

        temas_melhorar = [r["tema"] for r in respostas if not r["certa"]]
        if temas_melhorar:
            st.error("Temas a melhorar: " + ", ".join(temas_melhorar))
        else:
            st.success("Excelente resultado. A empresa demonstra boas práticas nos temas avaliados.")

        with st.expander("Ver correção das respostas"):
            for r in respostas:
                if r["certa"]:
                    st.success(f"{r['tema']}: resposta correta.")
                else:
                    st.warning(f"{r['tema']}: resposta recomendada — {r['correta']}")
                st.caption(r["explicacao"])

        data = datetime.now().strftime("%d/%m/%Y %H:%M")
        relatorio = f"""
CIBERIMPACTO - CHECK-UP DIGITAL

Data: {data}
Resultado: Risco {nivel}
Pontuação: {certas}/{total}
Percentagem: {percentagem}%

Recomendação:
{recomendacao}

Temas a melhorar:
{', '.join(temas_melhorar) if temas_melhorar else 'Sem fragilidades relevantes identificadas neste check-up.'}

Próximo passo sugerido:
Agendar uma sessão de sensibilização em cibersegurança com a CiberImpacto.

Site CiberImpacto:
https://www.ciberimpacto.pt
"""
        st.download_button(
            "Descarregar relatório",
            data=relatorio,
            file_name="relatorio_checkup_digital_ciberimpacto.txt",
            mime="text/plain"
        )

st.markdown(
    """
    <div class="footer">
        CiberImpacto – Formação e Eventos | Capacitar pessoas. Proteger organizações.<br>
        <a href="https://www.ciberimpacto.pt" target="_blank">www.ciberimpacto.pt</a>
    </div>
    """,
    unsafe_allow_html=True
)
