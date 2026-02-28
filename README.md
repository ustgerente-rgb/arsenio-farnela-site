# Site Institucional - Arsénio Farnela

## 📋 Descrição do Projeto

Site institucional profissional para **Arsénio Farnela**, Advogado, Docente Universitário e Agente Oficial de Propriedade Industrial. O site apresenta serviços jurídicos, informações de contacto, tabela de preços e formulário de agendamento de consultas.

**URL do Site:** [Será preenchida com domínio permanente]

---

## 📁 Estrutura do Projeto

```
arsenio_farnela_site/
├── index.html                 # Página principal (HTML + CSS + JS)
├── assets/
│   └── logo.jpg              # Logo QUID JURIS MOZ
├── css/                       # Pasta para CSS externo (futuro)
├── js/                        # Pasta para JavaScript externo (futuro)
├── README.md                  # Este arquivo
├── DEPLOYMENT.md              # Guia de deployment
└── .gitignore                 # Arquivo para controle de versão
```

---

## 🎯 Funcionalidades

### Seções Principais

1. **Header/Hero Section**
   - Logo QUID JURIS MOZ
   - Título e subtítulo profissional
   - Call-to-action "Agendar Consulta"

2. **Sobre**
   - Breve biografia e experiência profissional

3. **Serviços**
   - 5 áreas de prática jurídica em cards
   - Descrições concisas de cada serviço

4. **Áreas de Atendimento**
   - Maputo (atendimento online)
   - Manica (Chimoio, Manica, Guro - presencial e online)
   - Online (videoconferência)

5. **Consultas e Preços**
   - Inscrição QUID JURIS: 5.000 MT
   - Mensalidade: 3.500 MT
   - Consulta Online: 1.500 MT
   - Consulta Presencial (Manica): 3.500 MT

6. **Agendamento de Consulta**
   - Formulário com validação
   - Seleção dinâmica de tipo de atendimento
   - Restrição: presencial apenas para Manica/Chimoio/Guro

7. **Contactos**
   - E-mail: arseniofarnela@gmail.com
   - Emola: 864486821
   - M-Pesa: 855484877

---

## 🎨 Design e Responsividade

### Paleta de Cores
- **Azul Profissional:** #0A4D8C
- **Dourado Destaque:** #C9A24A
- **Fundo Claro:** #f8f9fa
- **Branco:** #fff

### Responsividade
- ✅ Desktop (1200px+)
- ✅ Tablet (768px - 1199px)
- ✅ Mobile (até 767px)

### Tipografia
- Font Stack: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Inter', Arial, sans-serif
- Tamanhos fluidos com `clamp()` para escalabilidade

---

## ⚙️ Funcionalidades JavaScript

### Controle Dinâmico de Atendimento

```javascript
function updateAttendanceOptions() {
  const location = document.getElementById('location').value;
  const presencialOption = document.getElementById('presencial-option');
  
  // Presencial disponível apenas para Manica, Chimoio e Guro
  if (location === 'manica' || location === 'chimoio' || location === 'guro') {
    presencialOption.style.display = 'block';
  } else {
    presencialOption.style.display = 'none';
    if (document.getElementById('attendance').value === 'presencial') {
      document.getElementById('attendance').value = 'online';
    }
  }
}
```

### Scroll Suave

```javascript
document.getElementById('booking').scrollIntoView({behavior: 'smooth'})
```

---

## 🚀 Deployment

### Opção 1: Hospedagem Estática (Recomendado)

#### Netlify
1. Faça fork do repositório ou upload dos arquivos
2. Conecte ao Netlify
3. Build command: (deixe em branco - site estático)
4. Publish directory: `.` (raiz)

#### Vercel
1. Importe o repositório
2. Vercel detectará automaticamente como site estático
3. Deploy automático em cada push

#### GitHub Pages
1. Faça push para repositório GitHub
2. Vá em Settings > Pages
3. Selecione branch `main` como source
4. Site estará disponível em `https://username.github.io/arsenio_farnela_site`

### Opção 2: Servidor Próprio

```bash
# Copiar arquivos para servidor
scp -r arsenio_farnela_site/ user@server:/var/www/

# Configurar Nginx
server {
    listen 80;
    server_name arseniofarnela.com;
    root /var/www/arsenio_farnela_site;
    index index.html;
}

# Configurar SSL com Let's Encrypt
sudo certbot certonly --webroot -w /var/www/arsenio_farnela_site -d arseniofarnela.com
```

### Opção 3: Servidor Local (Desenvolvimento)

```bash
# Python 3
python3 -m http.server 8000

# Node.js
npx http-server

# PHP
php -S localhost:8000
```

---

## 📝 Edição e Manutenção

### Editar Conteúdo

Abra `index.html` em um editor de texto e procure pelas seções:

```html
<!-- Editar nome -->
<h1>Arsénio Farnela</h1>

<!-- Editar descrição -->
<p class="subtitle">Advogado, Docente Universitário...</p>

<!-- Editar serviços -->
<div class="service-card">
  <h3>Nome do Serviço</h3>
  <p>Descrição do serviço</p>
</div>

<!-- Editar preços -->
<div class="price">5.000 <span class="currency">MT</span></div>

<!-- Editar contactos -->
<a href="mailto:email@example.com">email@example.com</a>
```

### Editar Estilos

Os estilos estão dentro da tag `<style>` no `index.html`. Para modificar:

1. **Cores:** Procure por `#0A4D8C` (azul) ou `#C9A24A` (dourado)
2. **Fontes:** Procure por `font-family`
3. **Espaçamento:** Procure por `padding` e `margin`
4. **Responsividade:** Procure por `@media`

---

## 🔒 Segurança

### Recomendações

1. **HTTPS Obrigatório**
   - Use certificado SSL/TLS
   - Redirecione HTTP para HTTPS

2. **Headers de Segurança**
   ```
   X-Content-Type-Options: nosniff
   X-Frame-Options: DENY
   X-XSS-Protection: 1; mode=block
   ```

3. **Política de Privacidade**
   - Adicione página de política de privacidade
   - Implemente LGPD/GDPR se necessário

4. **Formulário**
   - Valide dados no servidor
   - Implemente CAPTCHA se receber spam
   - Use endpoint seguro para processar formulários

---

## 📧 Processamento de Formulários

### Backend Necessário

O formulário atual é apenas frontend. Para processar submissions:

#### Opção 1: Formspree
```html
<form action="https://formspree.io/f/YOUR_ID" method="POST">
  <!-- campos do formulário -->
</form>
```

#### Opção 2: EmailJS
```javascript
emailjs.init('YOUR_PUBLIC_KEY');
document.querySelector('form').addEventListener('submit', function(e) {
  e.preventDefault();
  emailjs.sendForm('service_id', 'template_id', this);
});
```

#### Opção 3: Backend Customizado
Implemente um servidor Node.js/Python para processar e enviar emails.

---

## 🔧 Troubleshooting

### Logo não aparece
- Verifique se o arquivo está em `assets/logo.jpg`
- Verifique permissões do arquivo
- Limpe cache do navegador (Ctrl+Shift+Delete)

### Formulário não funciona
- O formulário atual não envia dados - implemente backend
- Verifique console do navegador (F12) para erros

### Site não responsivo
- Verifique se `<meta name="viewport">` está no `<head>`
- Teste em diferentes tamanhos de tela
- Use DevTools do navegador (F12)

### Presencial não aparece para Manica
- Verifique se JavaScript está habilitado
- Abra console (F12) e procure por erros
- Teste seleção de Manica/Chimoio/Guro

---

## 📱 SEO e Metadados

### Meta Tags Incluídas
- `charset`: UTF-8
- `viewport`: Responsividade
- `description`: Descrição para buscadores
- `theme-color`: Cor do navegador

### Melhorias Recomendadas
1. Adicione `robots.txt`
2. Crie `sitemap.xml`
3. Registre em Google Search Console
4. Adicione Schema.org markup
5. Otimize imagens (compressão)

---

## 📞 Suporte e Atualizações

### Histórico de Versões

**v1.0 (28/02/2026)**
- Lançamento inicial
- Logo QUID JURIS
- Seção de contactos
- Restrição de presencial para Maputo

### Próximas Melhorias
- [ ] Backend para processamento de formulários
- [ ] Integração com sistema de pagamento
- [ ] Blog/Artigos jurídicos
- [ ] Chat ao vivo
- [ ] Agendamento automático
- [ ] Galeria de fotos
- [ ] Depoimentos de clientes

---

## 📄 Licença

© 2026 Arsénio Farnela — Todos os direitos reservados

---

## 📞 Contacto

**E-mail:** arseniofarnela@gmail.com  
**Emola:** 864486821  
**M-Pesa:** 855484877

---

**Última atualização:** 28 de Fevereiro de 2026
