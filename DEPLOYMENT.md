# Guia de Deployment - Site Arsénio Farnela

## 🚀 Opções de Hospedagem Permanente

---

## 1️⃣ NETLIFY (Recomendado - Mais Fácil)

### Vantagens
- ✅ Gratuito com plano generoso
- ✅ Deploy automático
- ✅ SSL/HTTPS incluído
- ✅ CDN global
- ✅ Suporte a domínio customizado

### Passo a Passo

#### 1. Preparar Repositório GitHub

```bash
# Inicializar git (se não estiver)
cd /home/ubuntu/arsenio_farnela_site
git init
git add .
git commit -m "Initial commit: Site Arsénio Farnela"

# Criar repositório no GitHub
# https://github.com/new
# Nome: arsenio_farnela_site
# Descrição: Site institucional para Arsénio Farnela, Advogado

# Adicionar remote
git remote add origin https://github.com/SEU_USUARIO/arsenio_farnela_site.git
git branch -M main
git push -u origin main
```

#### 2. Conectar ao Netlify

1. Acesse https://app.netlify.com
2. Clique em "Add new site" → "Import an existing project"
3. Selecione GitHub
4. Autorize Netlify
5. Selecione o repositório `arsenio_farnela_site`
6. Configure:
   - **Build command:** (deixe vazio)
   - **Publish directory:** `.` (ponto)
7. Clique em "Deploy site"

#### 3. Configurar Domínio Customizado

1. Em Netlify, vá em "Site settings" → "Domain management"
2. Clique em "Add custom domain"
3. Digite seu domínio (ex: arseniofarnela.com)
4. Configure DNS no seu registrador:
   ```
   CNAME: seu-site.netlify.app
   ```
5. Aguarde propagação (até 48h)

#### 4. Ativar HTTPS

1. Em Netlify, vá em "Domain management" → "HTTPS"
2. Clique em "Verify DNS configuration"
3. Aguarde certificado ser gerado automaticamente

---

## 2️⃣ VERCEL

### Vantagens
- ✅ Extremamente rápido
- ✅ Gratuito
- ✅ Otimização automática
- ✅ Analytics incluído

### Passo a Passo

1. Acesse https://vercel.com/new
2. Clique em "Import Git Repository"
3. Conecte sua conta GitHub
4. Selecione `arsenio_farnela_site`
5. Clique em "Deploy"
6. Após deploy, configure domínio em "Settings" → "Domains"

---

## 3️⃣ GITHUB PAGES (Gratuito)

### Vantagens
- ✅ Totalmente gratuito
- ✅ Integrado com GitHub
- ✅ Sem limite de bandwidth

### Desvantagens
- ❌ Sem suporte a backend
- ❌ Domínio padrão: username.github.io

### Passo a Passo

1. Faça push do repositório para GitHub
2. Vá em Settings → Pages
3. Selecione "Deploy from a branch"
4. Branch: `main`
5. Folder: `/ (root)`
6. Clique em "Save"
7. Site estará em: `https://username.github.io/arsenio_farnela_site`

---

## 4️⃣ SERVIDOR PRÓPRIO (VPS/Dedicado)

### Recomendado para
- Controle total
- Domínio próprio
- Possível backend futuro

### Requisitos
- VPS com Linux (Ubuntu 20.04+)
- Domínio registrado
- Conhecimento básico de servidor

### Instalação com Nginx

```bash
# 1. Conectar ao servidor
ssh root@seu_servidor_ip

# 2. Atualizar sistema
apt update && apt upgrade -y

# 3. Instalar Nginx
apt install nginx -y

# 4. Criar diretório do site
mkdir -p /var/www/arsenio_farnela_site
cd /var/www/arsenio_farnela_site

# 5. Fazer upload dos arquivos (do seu computador)
# scp -r /home/ubuntu/arsenio_farnela_site/* root@seu_servidor_ip:/var/www/arsenio_farnela_site/

# 6. Configurar permissões
chown -R www-data:www-data /var/www/arsenio_farnela_site
chmod -R 755 /var/www/arsenio_farnela_site

# 7. Criar arquivo de configuração Nginx
cat > /etc/nginx/sites-available/arsenio_farnela << 'EOF'
server {
    listen 80;
    server_name arseniofarnela.com www.arseniofarnela.com;
    
    root /var/www/arsenio_farnela_site;
    index index.html;
    
    location / {
        try_files $uri $uri/ =404;
    }
    
    # Cache estático
    location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
EOF

# 8. Ativar site
ln -s /etc/nginx/sites-available/arsenio_farnela /etc/nginx/sites-enabled/
rm /etc/nginx/sites-enabled/default

# 9. Testar configuração
nginx -t

# 10. Reiniciar Nginx
systemctl restart nginx

# 11. Instalar SSL com Let's Encrypt
apt install certbot python3-certbot-nginx -y
certbot --nginx -d arseniofarnela.com -d www.arseniofarnela.com

# 12. Configurar renovação automática
systemctl enable certbot.timer
systemctl start certbot.timer
```

### Configurar DNS

No seu registrador de domínio:

```
A Record: arseniofarnela.com → seu_servidor_ip
A Record: www.arseniofarnela.com → seu_servidor_ip
```

---

## 5️⃣ CLOUDFLARE PAGES

### Vantagens
- ✅ Gratuito
- ✅ CDN global
- ✅ Proteção DDoS
- ✅ Analytics

### Passo a Passo

1. Acesse https://pages.cloudflare.com
2. Clique em "Create a project"
3. Conecte GitHub
4. Selecione repositório
5. Configure:
   - **Build command:** (deixe vazio)
   - **Build output directory:** `.`
6. Deploy automático
7. Configure domínio em "Custom domain"

---

## 📋 Checklist de Deployment

### Antes de Publicar

- [ ] Testar em navegadores (Chrome, Firefox, Safari, Edge)
- [ ] Testar responsividade (mobile, tablet, desktop)
- [ ] Verificar links internos e externos
- [ ] Testar formulário
- [ ] Verificar logo carrega corretamente
- [ ] Testar velocidade (https://pagespeed.web.dev)

### Após Publicar

- [ ] Ativar HTTPS
- [ ] Configurar redirecionamento HTTP → HTTPS
- [ ] Registrar em Google Search Console
- [ ] Registrar em Bing Webmaster Tools
- [ ] Adicionar Google Analytics
- [ ] Configurar backups automáticos
- [ ] Monitorar uptime

---

## 🔐 Segurança Pós-Deployment

### Headers de Segurança (Nginx)

```nginx
add_header X-Content-Type-Options "nosniff" always;
add_header X-Frame-Options "DENY" always;
add_header X-XSS-Protection "1; mode=block" always;
add_header Referrer-Policy "no-referrer-when-downgrade" always;
add_header Permissions-Policy "geolocation=(), microphone=(), camera=()" always;
```

### Firewall

```bash
# UFW (Uncomplicated Firewall)
ufw allow 22/tcp    # SSH
ufw allow 80/tcp    # HTTP
ufw allow 443/tcp   # HTTPS
ufw enable
```

---

## 📊 Monitorar Performance

### Google PageSpeed Insights
https://pagespeed.web.dev

### GTmetrix
https://gtmetrix.com

### Lighthouse (Chrome DevTools)
- Abra DevTools (F12)
- Vá em "Lighthouse"
- Clique em "Analyze page load"

---

## 🔄 Atualizar Site

### Com Netlify/Vercel/GitHub Pages

```bash
# Fazer alterações localmente
# Editar index.html, etc.

# Fazer commit
git add .
git commit -m "Atualizar conteúdo"

# Push para GitHub
git push origin main

# Deploy automático! ✨
```

### Com Servidor Próprio

```bash
# Fazer alterações localmente
# Fazer commit
git add .
git commit -m "Atualizar conteúdo"

# SSH para servidor
ssh root@seu_servidor_ip

# Atualizar arquivos
cd /var/www/arsenio_farnela_site
git pull origin main

# Ou fazer upload manual
# scp -r /home/ubuntu/arsenio_farnela_site/* root@seu_servidor_ip:/var/www/arsenio_farnela_site/
```

---

## 💰 Custos Estimados

| Opção | Custo Mensal | Domínio | SSL | Notas |
|-------|-------------|---------|-----|-------|
| Netlify | Gratuito | ~$12/ano | ✅ Incluído | Melhor para começar |
| Vercel | Gratuito | ~$12/ano | ✅ Incluído | Muito rápido |
| GitHub Pages | Gratuito | ~$12/ano | ✅ Incluído | Simples |
| VPS (DigitalOcean) | $5-10 | ~$12/ano | Gratuito (Let's Encrypt) | Controle total |
| Servidor Dedicado | $50+ | ~$12/ano | Gratuito | Alto desempenho |

---

## 🆘 Troubleshooting

### Site não carrega
- Verifique se DNS está propagado (https://dnschecker.org)
- Verifique permissões de arquivo
- Verifique logs do servidor

### Logo não aparece
- Verifique se arquivo `assets/logo.jpg` existe
- Verifique caminho relativo: `assets/logo.jpg`
- Limpe cache (Ctrl+Shift+Delete)

### Formulário não funciona
- Formulário atual é apenas frontend
- Implemente backend para processar dados
- Use Formspree ou EmailJS como alternativa

### Site lento
- Comprima imagens
- Ative cache do navegador
- Use CDN
- Minimize CSS/JavaScript

---

## 📞 Suporte

Para dúvidas sobre deployment:
- Netlify: https://docs.netlify.com
- Vercel: https://vercel.com/docs
- GitHub Pages: https://pages.github.com
- Nginx: https://nginx.org/en/docs

---

**Última atualização:** 28 de Fevereiro de 2026
