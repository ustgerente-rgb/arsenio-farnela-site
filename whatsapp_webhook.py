#!/usr/bin/env python3
"""
Script para enviar notificações de formulário para WhatsApp
Usa a API do Twilio ou alternativa simples
"""

import os
import json
from datetime import datetime

# Configuração
WHATSAPP_NUMBER = "+258864476821"  # Seu número
WEBHOOK_URL = os.environ.get("WEBHOOK_URL", "")

def format_form_message(form_data):
    """Formata os dados do formulário em uma mensagem legível"""
    message = f"""
📋 *NOVO AGENDAMENTO*

👤 *Nome:* {form_data.get('nome', 'N/A')}
📧 *E-mail:* {form_data.get('email', 'N/A')}
📱 *Telefone:* {form_data.get('telefone', 'N/A')}

⚖️ *Serviço:* {form_data.get('servico', 'N/A')}
📍 *Local:* {form_data.get('local', 'N/A')}
💬 *Tipo:* {form_data.get('tipo_atendimento', 'N/A')}

📝 *Descrição:*
{form_data.get('descricao', 'N/A')}

⏰ *Data:* {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
    """.strip()
    return message

def send_to_whatsapp(message):
    """Envia mensagem para WhatsApp"""
    try:
        # Opção 1: Usar Twilio (requer configuração)
        # from twilio.rest import Client
        # client = Client(account_sid, auth_token)
        # client.messages.create(
        #     from_="whatsapp:+14155552671",
        #     body=message,
        #     to=f"whatsapp:{WHATSAPP_NUMBER}"
        # )
        
        # Opção 2: Usar API simples (placeholder)
        print(f"[WhatsApp] Mensagem enviada para {WHATSAPP_NUMBER}")
        print(f"Conteúdo:\n{message}")
        return True
    except Exception as e:
        print(f"Erro ao enviar: {e}")
        return False

if __name__ == "__main__":
    # Exemplo de teste
    test_data = {
        "nome": "João Silva",
        "email": "joao@example.com",
        "telefone": "+258123456789",
        "servico": "Direito Comercial",
        "local": "Maputo",
        "tipo_atendimento": "Online",
        "descricao": "Preciso de consultoria sobre contrato"
    }
    
    message = format_form_message(test_data)
    send_to_whatsapp(message)
