#!/usr/bin/env python3
"""
火影忍者主题网站图片下载脚本
使用免费API生成占位图片
"""

import os
import requests
from PIL import Image, ImageDraw, ImageFont
import urllib.parse

def create_placeholder_image(text, size=(400, 400), color1='#ff6b00', color2='#ff9500'):
    """创建占位图片"""
    img = Image.new('RGB', size, color1)
    draw = ImageDraw.Draw(img)
    
    # 创建渐变背景
    for i in range(size[1]):
        r1, g1, b1 = tuple(int(color1[1:][i:i+2], 16) for i in (0, 2, 4))
        r2, g2, b2 = tuple(int(color2[1:][i:i+2], 16) for i in (0, 2, 4))
        
        r = int(r1 + (r2 - r1) * i / size[1])
        g = int(g1 + (g2 - g1) * i / size[1])
        b = int(b1 + (b2 - b1) * i / size[1])
        
        draw.line([(0, i), (size[0], i)], fill=(r, g, b))
    
    # 添加文字
    try:
        font_large = ImageFont.truetype("arial.ttf", 60)
        font_small = ImageFont.truetype("arial.ttf", 20)
    except:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # 绘制主文字
    bbox = draw.textbbox((0, 0), text, font=font_large)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    draw.text(((size[0] - text_width) // 2, (size[1] - text_height) // 2 - 50), 
              text, fill='white', font=font_large)
    
    # 绘制副标题
    subtitle = "火影忍者主题网站"
    bbox = draw.textbbox((0, 0), subtitle, font=font_small)
    text_width = bbox[2] - bbox[0]
    
    draw.text(((size[0] - text_width) // 2, (size[1]) // 2 + 50), 
              subtitle, fill='white', font=font_small)
    
    return img

def download_placeholder_images():
    """下载占位图片"""
    images_dir = 'images'
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)
    
    # 定义图片配置
    image_configs = {
        'naruto.jpg': ('🦊 鸣人', '#ff6b00', '#ff9500'),
        'sasuke.jpg': ('⚡ 佐助', '#000080', '#4169e1'),
        'itachi-featured.jpg': ('🔥 鼬', '#8b0000', '#ff0000'),
        'hashirama.jpg': ('🌳 柱间', '#228b22', '#32cd32'),
        'tobirama.jpg': ('🌊 扉间', '#00bfff', '#0099cc'),
        'hiruzen.jpg': ('🐒 日斩', '#8b4513', '#daa520'),
        'minato.jpg': ('⚡ 水门', '#ffff00', '#ffd700'),
        'tsunade.jpg': ('💎 纲手', '#9370db', '#8a2be2'),
        'kakashi.jpg': ('⚡ 卡卡西', '#708090', '#a9a9a9'),
        'ninja-world-map.jpg': ('🗺️ 忍界', '#8b4513', '#daa520'),
        'konoha-logo.png': ('🍃 木叶', '#228b22', '#32cd32'),
        'akatsuki-symbol.png': ('☁️ 晓', '#8b0000', '#ff0000'),
        'rasengan.gif': ('🌀 螺旋丸', '#ff6b00', '#ff9500'),
        'chidori.gif': ('⚡ 千鸟', '#9370db', '#8a2be2'),
        'fire-country.jpg': ('🔥 火之国', '#ff6b00', '#ff9500'),
        'wind-country.jpg': ('🌪️ 风之国', '#ffff00', '#ffd700'),
        'water-country.jpg': ('🌊 水之国', '#00bfff', '#0099cc'),
        'earth-country.jpg': ('🗻 土之国', '#8b4513', '#a0522d'),
        'lightning-country.jpg': ('⚡ 雷之国', '#9370db', '#8a2be2'),
    }
    
    # 生成图片
    for filename, (text, color1, color2) in image_configs.items():
        print(f"正在生成 {filename}...")
        
        # 创建图片
        img = create_placeholder_image(text, color1=color1, color2=color2)
        
        # 保存图片
        filepath = os.path.join(images_dir, filename)
        img.save(filepath)
        print(f"✅ 已保存: {filepath}")
    
    print("\n🎉 所有占位图片已生成完成！")
    print("📁 图片保存在 images/ 文件夹中")
    print("🌐 现在可以在浏览器中查看完整的网站效果了！")

def download_from_placeholder_api():
    """从占位图片API下载图片"""
    images_dir = 'images'
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)
    
    # 使用 picsum.photos 生成占位图片
    api_configs = {
        'naruto.jpg': 'https://picsum.photos/400/400?random=1',
        'sasuke.jpg': 'https://picsum.photos/400/400?random=2',
        'itachi-featured.jpg': 'https://picsum.photos/800/600?random=3',
        'ninja-world-map.jpg': 'https://picsum.photos/1200/800?random=4',
        'hashirama.jpg': 'https://picsum.photos/400/400?random=5',
        'tobirama.jpg': 'https://picsum.photos/400/400?random=6',
        'hiruzen.jpg': 'https://picsum.photos/400/400?random=7',
        'minato.jpg': 'https://picsum.photos/400/400?random=8',
        'tsunade.jpg': 'https://picsum.photos/400/400?random=9',
        'kakashi.jpg': 'https://picsum.photos/400/400?random=10',
    }
    
    for filename, url in api_configs.items():
        try:
            print(f"正在下载 {filename}...")
            response = requests.get(url)
            response.raise_for_status()
            
            filepath = os.path.join(images_dir, filename)
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            print(f"✅ 已下载: {filepath}")
            
        except requests.RequestException as e:
            print(f"❌ 下载失败 {filename}: {e}")

if __name__ == "__main__":
    print("🍃 火影忍者主题网站图片生成器 🍃")
    print("=" * 50)
    
    try:
        # 首先尝试生成自定义占位图片
        download_placeholder_images()
        
    except ImportError:
        print("❌ 缺少PIL库，尝试使用在线API下载...")
        try:
            download_from_placeholder_api()
        except ImportError:
            print("❌ 缺少requests库")
            print("💡 请运行: pip install Pillow requests")
    
    except Exception as e:
        print(f"❌ 生成图片时出错: {e}")
        print("💡 请检查Python环境和权限设置")