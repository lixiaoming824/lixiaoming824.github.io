#!/usr/bin/env python3
"""
简单的图片生成器 - 不依赖外部库
"""

import os
import base64
from io import BytesIO

def create_svg_placeholder(text, width=400, height=400, bg_color='#ff6b00', text_color='white'):
    """创建SVG占位图片"""
    svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:{bg_color};stop-opacity:1" />
            <stop offset="100%" style="stop-color:{bg_color}88;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="100%" height="100%" fill="url(#grad)"/>
    <text x="50%" y="45%" text-anchor="middle" font-family="Arial" font-size="36" fill="{text_color}" font-weight="bold">
        {text}
    </text>
    <text x="50%" y="65%" text-anchor="middle" font-family="Arial" font-size="16" fill="{text_color}">
        火影忍者主题网站
    </text>
</svg>'''
    return svg_content

def generate_placeholder_images():
    """生成占位图片"""
    images_dir = 'images'
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)
    
    # 图片配置
    image_configs = {
        'naruto.jpg': ('🦊 鸣人', '#ff6b00'),
        'sasuke.jpg': ('⚡ 佐助', '#000080'),
        'itachi-featured.jpg': ('🔥 鼬', '#8b0000'),
        'hashirama.jpg': ('🌳 柱间', '#228b22'),
        'tobirama.jpg': ('🌊 扉间', '#00bfff'),
        'hiruzen.jpg': ('🐒 日斩', '#8b4513'),
        'minato.jpg': ('⚡ 水门', '#ffff00'),
        'tsunade.jpg': ('💎 纲手', '#9370db'),
        'kakashi.jpg': ('⚡ 卡卡西', '#708090'),
        'ninja-world-map.jpg': ('🗺️ 忍界', '#8b4513'),
        'konoha-logo.png': ('🍃 木叶', '#228b22'),
        'akatsuki-symbol.png': ('☁️ 晓', '#8b0000'),
        'rasengan.gif': ('🌀 螺旋丸', '#ff6b00'),
        'chidori.gif': ('⚡ 千鸟', '#9370db'),
        'fire-country.jpg': ('🔥 火之国', '#ff6b00'),
        'wind-country.jpg': ('🌪️ 风之国', '#ffff00'),
        'water-country.jpg': ('🌊 水之国', '#00bfff'),
        'earth-country.jpg': ('🗻 土之国', '#8b4513'),
        'lightning-country.jpg': ('⚡ 雷之国', '#9370db'),
        'naruto-small.jpg': ('🦊', '#ff6b00'),
        'sasuke-small.jpg': ('⚡', '#000080'),
        'sakura-small.jpg': ('🌸', '#ff69b4'),
        'kakashi-small.jpg': ('⚡', '#708090'),
        'pain-small.jpg': ('👁️', '#8b0000'),
        'itachi-small.jpg': ('🔥', '#8b0000'),
        'characters-bg.jpg': ('忍者列传', '#ff6b00'),
        'world-bg.jpg': ('世界探秘', '#00cc66'),
        'jutsu-bg.jpg': ('忍术卷轴', '#8a2be2'),
        'moments-bg.jpg': ('经典瞬间', '#ffd700'),
    }
    
    # 生成SVG图片
    for filename, (text, color) in image_configs.items():
        print(f"正在生成 {filename}...")
        
        # 根据文件名调整尺寸
        if 'small' in filename:
            width, height = 100, 100
        elif 'bg' in filename:
            width, height = 800, 600
        elif 'map' in filename:
            width, height = 1200, 800
        elif 'featured' in filename:
            width, height = 600, 800
        else:
            width, height = 400, 400
            
        svg_content = create_svg_placeholder(text, width, height, color)
        
        # 保存为SVG文件
        svg_filename = filename.replace('.jpg', '.svg').replace('.png', '.svg').replace('.gif', '.svg')
        filepath = os.path.join(images_dir, svg_filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        
        print(f"✅ 已保存: {filepath}")
    
    print("\n🎉 所有占位图片已生成完成！")
    print("📁 图片保存在 images/ 文件夹中")
    print("💡 生成的是SVG格式，浏览器可以直接显示")

if __name__ == "__main__":
    print("🍃 火影忍者主题网站图片生成器 🍃")
    print("=" * 50)
    
    try:
        generate_placeholder_images()
    except Exception as e:
        print(f"❌ 生成图片时出错: {e}")
        print("💡 请检查文件夹权限")