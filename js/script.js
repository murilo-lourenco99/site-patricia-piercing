// WhatsApp
function contactarVendedor(nome) {
    const fone = "5511982540314";
    const msg = encodeURIComponent(`Olá Patrícia! Tenho interesse na joia: ${nome}`);
    window.open(`https://wa.me/${fone}?text=${msg}`, '_blank');
}

// Filtro
function filtrar(cat) {
    const cards = document.querySelectorAll('.product-card');
    cards.forEach(card => {
        card.style.display = (cat === 'todos' || card.dataset.category === cat) ? 'flex' : 'none';
    });
    // Estilo do botão ativo
    document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');
}

// Ano Automático
document.addEventListener("DOMContentLoaded", () => {
    const p = document.querySelector(".main-footer p");
    if(p) p.innerHTML = `&copy; ${new Date().getFullYear()} Patrícia Lourenço`;
});