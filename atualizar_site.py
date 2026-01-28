import os

CAMINHO_HTML = 'paginas/catalogo.html'
PASTA_PRODUTOS = 'produtos'
PASTA_PERFURACOES = 'perfuracoes'

def limpar_texto(texto):
    return texto.replace('-', ' ').strip()

def gerar_html_card(arquivo, pasta, eh_perfuracao=False):
    partes = arquivo.rsplit('.', 1)[0].split('_')
    if eh_perfuracao:
        nome = limpar_texto(partes[0]).title()
        feedback = limpar_texto(partes[1]) if len(partes) > 1 else "Amei o resultado!"
        info = f'<p class="feedback-cliente">{feedback}</p>'
    else:
        cat = limpar_texto(partes[0]).capitalize() if len(partes) >= 3 else "Joia"
        nome = limpar_texto(partes[1]).title() if len(partes) >= 3 else limpar_texto(partes[0]).title()
        preco = partes[-1]
        info = f'<span class="categoria-tag">{cat}</span><p class="preco-joia">R$ {preco}</p>'

    return f"""
    <div class="product-card">
        <img src="../{pasta}/{arquivo}" class="img-produto" alt="{nome}">
        <div class="info-produto">
            <h3 class="nome-joia">{nome}</h3>
            {info}
        </div>
    </div>"""

def atualizar():
    l_joias = [f for f in os.listdir(PASTA_PRODUTOS) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    l_perfs = [f for f in os.listdir(PASTA_PERFURACOES) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    html_joias = "".join([gerar_html_card(f, PASTA_PRODUTOS) for f in l_joias])
    html_perfs = "".join([gerar_html_card(f, PASTA_PERFURACOES, True) for f in l_perfs])

    with open(CAMINHO_HTML, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    # Injeção nos containers
    try:
        j_ini, p_ini, fim = '<div id="container-catalogo" class="product-grid">', '<div id="container-perfuracoes" class="product-grid" style="display: none;">', '</div>'
        conteudo = conteudo.split(j_ini)[0] + j_ini + html_joias + fim + conteudo.split(j_ini)[1].split(fim, 1)[1]
        conteudo = conteudo.split(p_ini)[0] + p_ini + html_perfs + fim + conteudo.split(p_ini)[1].split(fim, 1)[1]
        
        with open(CAMINHO_HTML, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        print("✅ Catálogo atualizado com sucesso!")
    except:
        print("❌ Erro: Verifique os IDs no arquivo catalogo.html")

if __name__ == "__main__":
    atualizar()