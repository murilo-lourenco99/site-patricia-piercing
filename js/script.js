// WhatsApp
function contactarVendedor(nome) {
    const fone = "5511982540314";
    const msg = encodeURIComponent(`Olá Patrícia! Tenho interesse na joia: ${nome}`);
    window.open(`https://wa.me/${fone}?text=${msg}`, '_blank');
}