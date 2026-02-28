# Guia de Manutenção - Site Arsénio Farnela

## 📋 Tarefas Rotineiras

### Semanal
- [ ] Verificar se o site está online (uptime)
- [ ] Revisar formulários de contacto (se implementado backend)
- [ ] Verificar erros no console do navegador (F12)

### Mensal
- [ ] Revisar analytics (Google Analytics)
- [ ] Verificar performance (PageSpeed Insights)
- [ ] Atualizar conteúdo se necessário
- [ ] Fazer backup dos arquivos

### Trimestral
- [ ] Revisar e atualizar preços
- [ ] Verificar links internos e externos
- [ ] Atualizar informações de contacto
- [ ] Revisar SEO

### Anual
- [ ] Renovar domínio
- [ ] Renovar certificado SSL (automático com Let's Encrypt)
- [ ] Revisar design e UX
- [ ] Atualizar ano no footer

---

## 🔧 Como Editar o Site

### Editar Texto e Conteúdo

1. Abra o arquivo `index.html` em um editor de texto
2. Procure pelo conteúdo que deseja editar
3. Faça as alterações
4. Salve o arquivo
5. Faça upload para o servidor ou faça push para GitHub

**Exemplo: Editar e-mail**

```html
<!-- Antes -->
<a href="mailto:arseniofarnela@gmail.com">arseniofarnela@gmail.com</a>

<!-- Depois -->
<a href="mailto:newemail@example.com">newemail@example.com</a>
```

### Editar Preços

```html
<!-- Localizar a seção "Consultas e Preços" -->
<div class="pricing-card">
  <h3>Consulta Online</h3>
  <p class="currency">Videoconferência</p>
  <div class="price">1.500 <span class="currency">MT</span></div>
</div>

<!-- Mudar 1.500 para o novo valor -->
<div class="price">2.000 <span class="currency">MT</span></div>
```

### Editar Serviços

```html
<!-- Localizar a seção "Serviços" -->
<div class="service-card">
  <h3>Direito Comercial</h3>
  <p>Contratos, constituição de sociedades, compliance e consultoria empresarial.</p>
</div>

<!-- Editar título ou descrição -->
<div class="service-card">
  <h3>Novo Serviço</h3>
  <p>Nova descrição do serviço.</p>
</div>
```

### Editar Cores

```css
/* Localizar a seção de estilos */
/* Azul principal */
color: #0A4D8C;

/* Dourado destaque */
background: #C9A24A;

/* Mudar para novas cores */
color: #1a5fa3;  /* novo azul */
background: #d4b860;  /* novo dourado */
```

### Editar Logo

1. Prepare uma nova imagem (recomendado: 200x200px, PNG ou JPG)
2. Salve como `logo.jpg` em `assets/`
3. Substitua o arquivo existente
4. Faça upload para o servidor

---

## 🖼️ Adicionar Imagens

### Estrutura Recomendada

```
assets/
├── logo.jpg              # Logo principal
├── images/
│   ├── hero-bg.jpg      # Background do header
│   ├── service-1.jpg    # Ícones de serviços
│   └── testimonial-1.jpg # Fotos de clientes
└── icons/
    ├── phone.svg
    ├── email.svg
    └── location.svg
```

### Adicionar Imagem no HTML

```html
<!-- Adicionar imagem em uma seção -->
<img src="assets/images/minha-imagem.jpg" alt="Descrição da imagem">

<!-- Com estilo -->
<img src="assets/images/minha-imagem.jpg" alt="Descrição" style="max-width: 100%; height: auto;">
```

### Otimizar Imagens

```bash
# Comprimir JPEG
convert input.jpg -quality 80 output.jpg

# Converter para WebP (mais eficiente)
cwebp input.jpg -o output.webp

# Redimensionar
convert input.jpg -resize 800x600 output.jpg
```

---

## 🔗 Adicionar Novas Seções

### Template para Nova Seção

```html
<!-- Adicionar antes do footer -->
<section class="nova-secao">
  <h2>Título da Seção</h2>
  <div class="conteudo">
    <!-- Seu conteúdo aqui -->
  </div>
</section>
```

### Exemplo: Adicionar Seção de Blog

```html
<section class="blog-section">
  <h2>Artigos Jurídicos</h2>
  <div class="blog-grid">
    <article class="blog-card">
      <h3>Título do Artigo</h3>
      <p class="date">28 de Fevereiro de 2026</p>
      <p>Resumo do artigo...</p>
      <a href="artigo1.html">Ler mais</a>
    </article>
  </div>
</section>
```

---

## 📱 Testar Responsividade

### No Navegador (Chrome/Firefox)

1. Abra o site
2. Pressione `F12` (DevTools)
3. Clique no ícone de dispositivo (mobile)
4. Teste em diferentes tamanhos:
   - Mobile: 320px, 375px, 425px
   - Tablet: 768px, 1024px
   - Desktop: 1200px+

### Tamanhos Padrão

```
Mobile:     320px - 767px
Tablet:     768px - 1023px
Desktop:    1024px+
```

---

## 🐛 Corrigir Bugs Comuns

### Logo não aparece
```html
<!-- Verificar caminho -->
<img src="assets/logo.jpg" alt="Logo">

<!-- Se não funcionar, tentar -->
<img src="./assets/logo.jpg" alt="Logo">
```

### Formulário não funciona
- O formulário atual é apenas frontend
- Para enviar dados, implemente backend
- Use serviço como Formspree: https://formspree.io

### Site não responsivo
- Verificar se `<meta name="viewport">` existe
- Limpar cache do navegador
- Testar em incógnito

### Presencial não aparece para Manica
- Abrir Console (F12)
- Verificar se há erros JavaScript
- Testar seleção de Manica

---

## 📊 Monitorar Performance

### Ferramentas Recomendadas

1. **Google PageSpeed Insights**
   - https://pagespeed.web.dev
   - Mede velocidade e SEO

2. **GTmetrix**
   - https://gtmetrix.com
   - Análise detalhada de performance

3. **Google Analytics**
   - https://analytics.google.com
   - Rastreia visitantes e comportamento

4. **Google Search Console**
   - https://search.google.com/search-console
   - Monitora presença em buscadores

### Metas de Performance

- Tempo de carregamento: < 3 segundos
- Lighthouse Score: > 90
- Mobile Score: > 85

---

## 🔐 Segurança

### Checklist de Segurança

- [ ] HTTPS ativado (cadeado verde)
- [ ] Certificado SSL válido
- [ ] Sem avisos de segurança no navegador
- [ ] Sem conteúdo misto (HTTP + HTTPS)
- [ ] Headers de segurança configurados

### Monitorar Segurança

```bash
# Verificar certificado SSL
openssl s_client -connect arseniofarnela.com:443

# Verificar headers de segurança
curl -I https://arseniofarnela.com
```

---

## 🔄 Fazer Backup

### Backup Manual

```bash
# Criar arquivo compactado
tar -czf backup_site_$(date +%Y%m%d).tar.gz /var/www/arsenio_farnela_site/

# Fazer download
scp root@servidor:/root/backup_site_*.tar.gz ~/backups/
```

### Backup Automático (Linux)

```bash
# Criar script de backup
cat > /usr/local/bin/backup_site.sh << 'EOF'
#!/bin/bash
BACKUP_DIR="/backups"
SITE_DIR="/var/www/arsenio_farnela_site"
DATE=$(date +%Y%m%d_%H%M%S)

mkdir -p $BACKUP_DIR
tar -czf $BACKUP_DIR/site_$DATE.tar.gz $SITE_DIR

# Manter apenas últimos 7 backups
find $BACKUP_DIR -name "site_*.tar.gz" -mtime +7 -delete
EOF

# Tornar executável
chmod +x /usr/local/bin/backup_site.sh

# Agendar com cron (diário às 2 da manhã)
echo "0 2 * * * /usr/local/bin/backup_site.sh" | crontab -
```

---

## 📝 Atualizar Documentação

### Quando Atualizar

- [ ] Após adicionar nova seção
- [ ] Após mudar preços
- [ ] Após adicionar novo serviço
- [ ] Após alterar informações de contacto
- [ ] Após fazer deploy

### Como Atualizar

1. Edite este arquivo (MAINTENANCE.md)
2. Adicione data da atualização
3. Descreva as alterações
4. Faça commit e push

---

## 📞 Suporte Técnico

### Problemas Comuns

| Problema | Solução |
|----------|---------|
| Site não carrega | Verificar DNS, verificar servidor |
| Imagens não aparecem | Verificar caminho, verificar permissões |
| Formulário não funciona | Implementar backend, usar Formspree |
| Site lento | Comprimir imagens, ativar cache |
| Erro 404 | Verificar links, verificar estrutura |

### Recursos Úteis

- MDN Web Docs: https://developer.mozilla.org
- W3Schools: https://www.w3schools.com
- Stack Overflow: https://stackoverflow.com
- CSS-Tricks: https://css-tricks.com

---

## 📋 Changelog

### v1.0 (28/02/2026)
- Lançamento inicial
- Logo QUID JURIS
- Seção de contactos
- Restrição de presencial para Maputo
- Documentação completa

---

## 🎯 Próximas Melhorias

- [ ] Backend para processamento de formulários
- [ ] Sistema de agendamento integrado
- [ ] Blog com artigos jurídicos
- [ ] Chat ao vivo
- [ ] Integração com redes sociais
- [ ] Galeria de fotos
- [ ] Depoimentos de clientes
- [ ] Sistema de pagamento online

---

**Última atualização:** 28 de Fevereiro de 2026

**Próxima revisão recomendada:** 28 de Março de 2026
