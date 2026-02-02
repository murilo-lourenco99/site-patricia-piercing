import os

CAMINHO_HTML = 'paginas/catalogo.html'
PASTA_PRODUTOS = 'produtos'

def limpar_texto(texto):
    return texto.replace('-', ' ').strip()

def gerar_html_joia(arquivo):
    partes = arquivo.rsplit('.', 1)[0].split('_')
    # Padrao: Categoria_Nome_Preco
    cat = limpar_texto(partes[0]).capitalize() if len(partes) >= 3 else "Joia"
    nome = limpar_texto(partes[1]).title() if len(partes) >= 3 else limpar_texto(partes[0]).title()
    preco = partes[-1]

    return f"""
    <div class="product-card">
        <img src="../{PASTA_PRODUTOS}/{arquivo}" class="img-produto" alt="{nome}">
        <div class="info-produto">
            <span class="categoria-tag">{cat}</span>
            <h3 class="nome-joia">{nome}</h3>
            <p class="preco-joia">R$ {preco}</p>
        </div>
    </div>"""

def atualizar():
    arquivos = [f for f in os.listdir(PASTA_PRODUTOS) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    cards_html = [gerar_html_joia(f) for f in arquivos]

    with open(CAMINHO_HTML, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    try:
        marcador_ini = '<div id="container-catalogo" class="product-grid">'
        marcador_fim = '</div>'
        
        p1 = conteudo.split(marcador_ini)[0]
        p2 = conteudo.split(marcador_ini)[1].split(marcador_fim, 1)[1]
        
        with open(CAMINHO_HTML, 'w', encoding='utf-8') as f:
            f.write(p1 + marcador_ini + "\n".join(cards_html) + marcador_fim + p2)
        print(f"✅ Catálogo de Joias atualizado ({len(cards_html)} itens).")
    except:
        print("Erro nos marcadores do catalogo.html")

if __name__ == "__main__":
    atualizar()