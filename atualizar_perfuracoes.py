import os

CAMINHO_HTML = 'paginas/perfuracoes.html'
PASTA_PERFURACOES = 'perfuracoes'

def limpar_texto(texto):
    return texto.replace('-', ' ').strip()

def gerar_html_feedback(arquivo):
    partes = arquivo.rsplit('.', 1)[0].split('_')
    nome_furo = limpar_texto(partes[0]).title()
    feedback = limpar_texto(partes[1]) if len(partes) > 1 else "Trabalho realizado com excelência."

    return f"""
    <div class="product-card">
        <img src="../{PASTA_PERFURACOES}/{arquivo}" class="img-produto" alt="{nome_furo}">
        <div class="info-produto">
            <h3 class="nome-joia">{nome_furo}</h3>
            <p class="feedback-cliente">{feedback}</p>
        </div>
    </div>"""

def atualizar():
    if not os.path.exists(PASTA_PERFURACOES):
        print(f"Erro: Pasta {PASTA_PERFURACOES} não encontrada.")
        return

    arquivos = [f for f in os.listdir(PASTA_PERFURACOES) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    cards_html = [gerar_html_feedback(f) for f in arquivos]

    with open(CAMINHO_HTML, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    try:
        marcador_ini = '<div id="container-perfuracoes" class="product-grid">'
        marcador_fim = '</div>'
        
        parte_inicial = conteudo.split(marcador_ini)[0]
        parte_final = conteudo.split(marcador_ini)[1].split(marcador_fim, 1)[1]
        
        novo_conteudo = parte_inicial + marcador_ini + "\n".join(cards_html) + marcador_fim + parte_final

        with open(CAMINHO_HTML, 'w', encoding='utf-8') as f:
            f.write(novo_conteudo)
        print(f"✅ Sucesso! {len(cards_html)} Feedbacks atualizados em perfuracoes.html")
    except Exception as e:
        print(f"Erro ao processar o HTML: {e}")

if __name__ == "__main__":
    atualizar()