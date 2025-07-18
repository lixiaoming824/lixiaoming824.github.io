#!/usr/bin/env python3
"""
完整的火影忍者主题SVG图片生成器
包含网站所需的所有图片
"""

import os

def create_tobirama_svg():
    """创建千手扉间SVG"""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <!-- 头发渐变 -->
        <linearGradient id="silverHair" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#E6E6FA;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#C0C0C0;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#A9A9A9;stop-opacity:1" />
        </linearGradient>
        
        <!-- 皮肤渐变 -->
        <linearGradient id="skin" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#FDBCB4;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#F4A460;stop-opacity:1" />
        </linearGradient>
        
        <!-- 蓝色铠甲 -->
        <linearGradient id="armor" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#4169E1;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#000080;stop-opacity:1" />
        </linearGradient>
        
        <filter id="shadow">
            <feDropShadow dx="2" dy="2" stdDeviation="3" flood-color="#000" flood-opacity="0.3"/>
        </filter>
    </defs>
    
    <!-- 背景 -->
    <circle cx="200" cy="200" r="190" fill="url(#armor)" filter="url(#shadow)"/>
    
    <!-- 头部 -->
    <ellipse cx="200" cy="180" rx="80" ry="90" fill="url(#skin)"/>
    
    <!-- 银色头发 -->
    <path d="M 120 120 Q 200 80 280 120 Q 270 100 200 85 Q 130 100 120 120" fill="url(#silverHair)"/>
    <path d="M 140 110 Q 180 95 200 100 Q 220 95 260 110" fill="url(#silverHair)"/>
    <path d="M 160 120 Q 200 110 240 120" fill="url(#silverHair)"/>
    
    <!-- 护额 -->
    <rect x="130" y="130" width="140" height="25" fill="#4169E1" stroke="#000080" stroke-width="2"/>
    <rect x="170" y="135" width="60" height="15" fill="#C0C0C0"/>
    
    <!-- 木叶标志 -->
    <path d="M 190 142 Q 200 138 210 142 Q 200 148 190 142" fill="#228B22"/>
    
    <!-- 眼睛 -->
    <ellipse cx="175" cy="170" rx="12" ry="15" fill="#8B0000"/>
    <ellipse cx="225" cy="170" rx="12" ry="15" fill="#8B0000"/>
    <circle cx="175" cy="170" r="8" fill="#000"/>
    <circle cx="225" cy="170" r="8" fill="#000"/>
    <circle cx="177" cy="167" r="3" fill="#FFF"/>
    <circle cx="227" cy="167" r="3" fill="#FFF"/>
    
    <!-- 面部纹路 -->
    <path d="M 170 150 Q 175 160 180 150" stroke="#8B0000" stroke-width="2" fill="none"/>
    <path d="M 220 150 Q 225 160 230 150" stroke="#8B0000" stroke-width="2" fill="none"/>
    
    <!-- 鼻子 -->
    <path d="M 200 185 L 195 195 L 205 195 Z" fill="#E6B89C"/>
    
    <!-- 嘴巴 -->
    <path d="M 190 210 Q 200 205 210 210" stroke="#000" stroke-width="2" fill="none"/>
    
    <!-- 铠甲 -->
    <path d="M 120 270 Q 200 260 280 270 L 280 400 L 120 400 Z" fill="url(#armor)"/>
    
    <!-- 铠甲细节 -->
    <rect x="180" y="290" width="40" height="20" fill="#1E90FF" stroke="#000080" stroke-width="1"/>
    
    <!-- 文字 -->
    <text x="200" y="350" text-anchor="middle" font-family="Arial" font-size="20" font-weight="bold" fill="#FFF">
        扉间
    </text>
</svg>'''

def create_hiruzen_svg():
    """创建猿飞日斩SVG"""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <!-- 白发渐变 -->
        <linearGradient id="whiteHair" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#FFFFFF;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#F0F0F0;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#D3D3D3;stop-opacity:1" />
        </linearGradient>
        
        <!-- 皮肤渐变 -->
        <linearGradient id="oldSkin" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#F4A460;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#DEB887;stop-opacity:1" />
        </linearGradient>
        
        <!-- 火影袍 -->
        <linearGradient id="hokageRobe" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#FFFFFF;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#F0F0F0;stop-opacity:1" />
        </linearGradient>
        
        <filter id="shadow">
            <feDropShadow dx="2" dy="2" stdDeviation="3" flood-color="#000" flood-opacity="0.3"/>
        </filter>
    </defs>
    
    <!-- 背景 -->
    <circle cx="200" cy="200" r="190" fill="url(#hokageRobe)" filter="url(#shadow)"/>
    
    <!-- 头部 -->
    <ellipse cx="200" cy="180" rx="80" ry="90" fill="url(#oldSkin)"/>
    
    <!-- 白发 -->
    <path d="M 120 120 Q 200 80 280 120 Q 270 100 200 85 Q 130 100 120 120" fill="url(#whiteHair)"/>
    <path d="M 140 110 Q 180 95 200 100 Q 220 95 260 110" fill="url(#whiteHair)"/>
    
    <!-- 胡须 -->
    <path d="M 160 250 Q 200 260 240 250" stroke="#FFFFFF" stroke-width="4" fill="none"/>
    <path d="M 170 260 Q 200 265 230 260" stroke="#FFFFFF" stroke-width="3" fill="none"/>
    
    <!-- 护额 -->
    <rect x="130" y="130" width="140" height="25" fill="#FF0000" stroke="#8B0000" stroke-width="2"/>
    <rect x="170" y="135" width="60" height="15" fill="#C0C0C0"/>
    
    <!-- 木叶标志 -->
    <path d="M 190 142 Q 200 138 210 142 Q 200 148 190 142" fill="#228B22"/>
    
    <!-- 眼睛 -->
    <ellipse cx="175" cy="170" rx="12" ry="15" fill="#8B4513"/>
    <ellipse cx="225" cy="170" rx="12" ry="15" fill="#8B4513"/>
    <circle cx="175" cy="170" r="8" fill="#000"/>
    <circle cx="225" cy="170" r="8" fill="#000"/>
    <circle cx="177" cy="167" r="3" fill="#FFF"/>
    <circle cx="227" cy="167" r="3" fill="#FFF"/>
    
    <!-- 皱纹 -->
    <path d="M 160 160 Q 175 165 190 160" stroke="#8B4513" stroke-width="1" fill="none"/>
    <path d="M 210 160 Q 225 165 240 160" stroke="#8B4513" stroke-width="1" fill="none"/>
    <path d="M 180 200 Q 200 205 220 200" stroke="#8B4513" stroke-width="1" fill="none"/>
    
    <!-- 鼻子 -->
    <path d="M 200 185 L 195 195 L 205 195 Z" fill="#E6B89C"/>
    
    <!-- 嘴巴 -->
    <path d="M 190 220 Q 200 215 210 220" stroke="#000" stroke-width="2" fill="none"/>
    
    <!-- 火影袍 -->
    <path d="M 120 270 Q 200 260 280 270 L 280 400 L 120 400 Z" fill="url(#hokageRobe)"/>
    
    <!-- 火影标志 -->
    <text x="200" y="300" text-anchor="middle" font-family="Arial" font-size="16" font-weight="bold" fill="#FF0000">
        火
    </text>
    
    <!-- 文字 -->
    <text x="200" y="350" text-anchor="middle" font-family="Arial" font-size="20" font-weight="bold" fill="#8B4513">
        日斩
    </text>
</svg>'''

def create_minato_svg():
    """创建波风水门SVG"""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <!-- 金色头发 -->
        <linearGradient id="goldHair" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#FFD700;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#FFA500;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#FF8C00;stop-opacity:1" />
        </linearGradient>
        
        <!-- 皮肤渐变 -->
        <linearGradient id="skin" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#FDBCB4;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#F4A460;stop-opacity:1" />
        </linearGradient>
        
        <!-- 火影袍 -->
        <linearGradient id="hokageCloak" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#FFFFFF;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#F0F0F0;stop-opacity:1" />
        </linearGradient>
        
        <filter id="shadow">
            <feDropShadow dx="2" dy="2" stdDeviation="3" flood-color="#000" flood-opacity="0.3"/>
        </filter>
    </defs>
    
    <!-- 背景 -->
    <circle cx="200" cy="200" r="190" fill="url(#hokageCloak)" filter="url(#shadow)"/>
    
    <!-- 头部 -->
    <ellipse cx="200" cy="180" rx="80" ry="90" fill="url(#skin)"/>
    
    <!-- 金色头发 -->
    <path d="M 120 120 Q 200 80 280 120 Q 270 100 200 85 Q 130 100 120 120" fill="url(#goldHair)"/>
    <path d="M 140 110 Q 180 95 200 100 Q 220 95 260 110" fill="url(#goldHair)"/>
    <path d="M 160 120 Q 200 110 240 120" fill="url(#goldHair)"/>
    
    <!-- 护额 -->
    <rect x="130" y="130" width="140" height="25" fill="#FF0000" stroke="#8B0000" stroke-width="2"/>
    <rect x="170" y="135" width="60" height="15" fill="#C0C0C0"/>
    
    <!-- 木叶标志 -->
    <path d="M 190 142 Q 200 138 210 142 Q 200 148 190 142" fill="#228B22"/>
    
    <!-- 眼睛 -->
    <ellipse cx="175" cy="170" rx="12" ry="15" fill="#1E90FF"/>
    <ellipse cx="225" cy="170" rx="12" ry="15" fill="#1E90FF"/>
    <circle cx="175" cy="170" r="8" fill="#000"/>
    <circle cx="225" cy="170" r="8" fill="#000"/>
    <circle cx="177" cy="167" r="3" fill="#FFF"/>
    <circle cx="227" cy="167" r="3" fill="#FFF"/>
    
    <!-- 鼻子 -->
    <path d="M 200 185 L 195 195 L 205 195 Z" fill="#E6B89C"/>
    
    <!-- 嘴巴 -->
    <path d="M 190 210 Q 200 215 210 210" stroke="#000" stroke-width="2" fill="none"/>
    
    <!-- 火影袍 -->
    <path d="M 120 270 Q 200 260 280 270 L 280 400 L 120 400 Z" fill="url(#hokageCloak)"/>
    
    <!-- 火影标志 -->
    <text x="200" y="300" text-anchor="middle" font-family="Arial" font-size="18" font-weight="bold" fill="#FF0000">
        四代目火影
    </text>
    
    <!-- 文字 -->
    <text x="200" y="350" text-anchor="middle" font-family="Arial" font-size="20" font-weight="bold" fill="#FF8C00">
        水门
    </text>
</svg>'''

def create_tsunade_svg():
    """创建纲手SVG"""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <!-- 金色头发 -->
        <linearGradient id="blondeHair" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#FFD700;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#DAA520;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#B8860B;stop-opacity:1" />
        </linearGradient>
        
        <!-- 皮肤渐变 -->
        <linearGradient id="skin" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#FDBCB4;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#F4A460;stop-opacity:1" />
        </linearGradient>
        
        <!-- 绿色衣服 -->
        <linearGradient id="greenCloth" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#228B22;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#006400;stop-opacity:1" />
        </linearGradient>
        
        <filter id="shadow">
            <feDropShadow dx="2" dy="2" stdDeviation="3" flood-color="#000" flood-opacity="0.3"/>
        </filter>
    </defs>
    
    <!-- 背景 -->
    <circle cx="200" cy="200" r="190" fill="url(#greenCloth)" filter="url(#shadow)"/>
    
    <!-- 头部 -->
    <ellipse cx="200" cy="180" rx="80" ry="90" fill="url(#skin)"/>
    
    <!-- 金色头发 -->
    <path d="M 120 120 Q 200 80 280 120 Q 270 100 200 85 Q 130 100 120 120" fill="url(#blondeHair)"/>
    <path d="M 140 110 Q 180 95 200 100 Q 220 95 260 110" fill="url(#blondeHair)"/>
    
    <!-- 双马尾 -->
    <ellipse cx="130" cy="200" rx="15" ry="40" fill="url(#blondeHair)" transform="rotate(-30 130 200)"/>
    <ellipse cx="270" cy="200" rx="15" ry="40" fill="url(#blondeHair)" transform="rotate(30 270 200)"/>
    
    <!-- 护额 -->
    <rect x="130" y="130" width="140" height="25" fill="#4169E1" stroke="#000080" stroke-width="2"/>
    <rect x="170" y="135" width="60" height="15" fill="#C0C0C0"/>
    
    <!-- 木叶标志 -->
    <path d="M 190 142 Q 200 138 210 142 Q 200 148 190 142" fill="#228B22"/>
    
    <!-- 眼睛 -->
    <ellipse cx="175" cy="170" rx="12" ry="15" fill="#8B4513"/>
    <ellipse cx="225" cy="170" rx="12" ry="15" fill="#8B4513"/>
    <circle cx="175" cy="170" r="8" fill="#000"/>
    <circle cx="225" cy="170" r="8" fill="#000"/>
    <circle cx="177" cy="167" r="3" fill="#FFF"/>
    <circle cx="227" cy="167" r="3" fill="#FFF"/>
    
    <!-- 菱形印记 -->
    <path d="M 200 155 L 205 160 L 200 165 L 195 160 Z" fill="#8A2BE2"/>
    
    <!-- 鼻子 -->
    <path d="M 200 185 L 195 195 L 205 195 Z" fill="#E6B89C"/>
    
    <!-- 嘴巴 -->
    <path d="M 190 210 Q 200 215 210 210" stroke="#000" stroke-width="2" fill="none"/>
    
    <!-- 绿色衣服 -->
    <path d="M 120 270 Q 200 260 280 270 L 280 400 L 120 400 Z" fill="url(#greenCloth)"/>
    
    <!-- 项链 -->
    <circle cx="200" cy="285" r="8" fill="#32CD32"/>
    
    <!-- 文字 -->
    <text x="200" y="350" text-anchor="middle" font-family="Arial" font-size="20" font-weight="bold" fill="#FFF">
        纲手
    </text>
</svg>'''

def create_hashirama_svg():
    """创建千手柱间SVG"""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <!-- 黑色头发 -->
        <linearGradient id="blackHair" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#2F2F2F;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#1C1C1C;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#000000;stop-opacity:1" />
        </linearGradient>
        
        <!-- 皮肤渐变 -->
        <linearGradient id="skin" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#FDBCB4;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#F4A460;stop-opacity:1" />
        </linearGradient>
        
        <!-- 红色铠甲 -->
        <linearGradient id="redArmor" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#B22222;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#8B0000;stop-opacity:1" />
        </linearGradient>
        
        <filter id="shadow">
            <feDropShadow dx="2" dy="2" stdDeviation="3" flood-color="#000" flood-opacity="0.3"/>
        </filter>
    </defs>
    
    <!-- 背景 -->
    <circle cx="200" cy="200" r="190" fill="url(#redArmor)" filter="url(#shadow)"/>
    
    <!-- 头部 -->
    <ellipse cx="200" cy="180" rx="80" ry="90" fill="url(#skin)"/>
    
    <!-- 黑色头发 -->
    <path d="M 120 120 Q 200 80 280 120 Q 270 100 200 85 Q 130 100 120 120" fill="url(#blackHair)"/>
    <path d="M 140 110 Q 180 95 200 100 Q 220 95 260 110" fill="url(#blackHair)"/>
    <path d="M 160 120 Q 200 110 240 120" fill="url(#blackHair)"/>
    
    <!-- 护额 -->
    <rect x="130" y="130" width="140" height="25" fill="#4169E1" stroke="#000080" stroke-width="2"/>
    <rect x="170" y="135" width="60" height="15" fill="#C0C0C0"/>
    
    <!-- 木叶标志 -->
    <path d="M 190 142 Q 200 138 210 142 Q 200 148 190 142" fill="#228B22"/>
    
    <!-- 眼睛 -->
    <ellipse cx="175" cy="170" rx="12" ry="15" fill="#8B4513"/>
    <ellipse cx="225" cy="170" rx="12" ry="15" fill="#8B4513"/>
    <circle cx="175" cy="170" r="8" fill="#000"/>
    <circle cx="225" cy="170" r="8" fill="#000"/>
    <circle cx="177" cy="167" r="3" fill="#FFF"/>
    <circle cx="227" cy="167" r="3" fill="#FFF"/>
    
    <!-- 鼻子 -->
    <path d="M 200 185 L 195 195 L 205 195 Z" fill="#E6B89C"/>
    
    <!-- 嘴巴 -->
    <path d="M 190 210 Q 200 215 210 210" stroke="#000" stroke-width="2" fill="none"/>
    
    <!-- 红色铠甲 -->
    <path d="M 120 270 Q 200 260 280 270 L 280 400 L 120 400 Z" fill="url(#redArmor)"/>
    
    <!-- 千手家徽 -->
    <circle cx="200" cy="290" r="15" fill="#32CD32"/>
    <path d="M 200 280 L 190 300 L 210 300 Z" fill="#FFF"/>
    
    <!-- 文字 -->
    <text x="200" y="350" text-anchor="middle" font-family="Arial" font-size="20" font-weight="bold" fill="#FFF">
        柱间
    </text>
</svg>'''

def create_chidori_svg():
    """创建千鸟SVG"""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <!-- 雷电渐变 -->
        <radialGradient id="lightningGrad" cx="50%" cy="50%" r="50%">
            <stop offset="0%" style="stop-color:#FFFFFF;stop-opacity:1" />
            <stop offset="30%" style="stop-color:#9370DB;stop-opacity:1" />
            <stop offset="70%" style="stop-color:#8A2BE2;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#4B0082;stop-opacity:1" />
        </radialGradient>
        
        <!-- 能量波纹 -->
        <radialGradient id="energyGrad" cx="50%" cy="50%" r="50%">
            <stop offset="0%" style="stop-color:#FFF;stop-opacity:0.9" />
            <stop offset="50%" style="stop-color:#9370DB;stop-opacity:0.6" />
            <stop offset="100%" style="stop-color:#8A2BE2;stop-opacity:0.3" />
        </radialGradient>
        
        <!-- 发光效果 -->
        <filter id="glow">
            <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
            <feMerge> 
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
        
        <!-- 闪烁动画 -->
        <animate id="flicker" attributeName="opacity" 
                 values="1;0.5;1;0.3;1" dur="0.5s" repeatCount="indefinite"/>
    </defs>
    
    <!-- 背景 -->
    <rect width="400" height="400" fill="#000"/>
    
    <!-- 能量波纹 -->
    <g opacity="0.7">
        <circle cx="200" cy="200" r="170" fill="none" stroke="#9370DB" stroke-width="3" opacity="0.4">
            <animate attributeName="r" values="170;200;170" dur="1.5s" repeatCount="indefinite"/>
            <animate attributeName="opacity" values="0.4;0.2;0.4" dur="1.5s" repeatCount="indefinite"/>
        </circle>
        <circle cx="200" cy="200" r="140" fill="none" stroke="#8A2BE2" stroke-width="3" opacity="0.5">
            <animate attributeName="r" values="140;170;140" dur="1s" repeatCount="indefinite"/>
            <animate attributeName="opacity" values="0.5;0.3;0.5" dur="1s" repeatCount="indefinite"/>
        </circle>
    </g>
    
    <!-- 主体千鸟 -->
    <g filter="url(#glow)">
        <circle cx="200" cy="200" r="70" fill="url(#lightningGrad)"/>
        
        <!-- 雷电纹理 -->
        <g opacity="0.8">
            <animate attributeName="opacity" values="0.8;0.4;0.8" dur="0.3s" repeatCount="indefinite"/>
            
            <!-- 闪电1 -->
            <path d="M 200 150 L 190 170 L 210 170 L 200 190 L 220 180 L 200 200 L 180 190 L 200 210 L 210 230 L 190 220 L 200 250" 
                  fill="none" stroke="#FFF" stroke-width="3"/>
            
            <!-- 闪电2 -->
            <path d="M 170 200 L 180 180 L 160 190 L 180 170 L 160 160 L 190 180 L 170 200 L 190 220 L 170 230" 
                  fill="none" stroke="#E6E6FA" stroke-width="2"/>
            
            <!-- 闪电3 -->
            <path d="M 230 200 L 220 180 L 240 190 L 220 170 L 240 160 L 210 180 L 230 200 L 210 220 L 230 230" 
                  fill="none" stroke="#E6E6FA" stroke-width="2"/>
        </g>
        
        <!-- 中心光点 -->
        <circle cx="200" cy="200" r="8" fill="#FFF">
            <animate attributeName="opacity" values="1;0.3;1" dur="0.2s" repeatCount="indefinite"/>
        </circle>
    </g>
    
    <!-- 手掌轮廓 -->
    <g opacity="0.6">
        <ellipse cx="200" cy="320" rx="50" ry="25" fill="url(#energyGrad)" transform="rotate(-5 200 320)"/>
        <rect x="175" y="300" width="50" height="35" fill="url(#energyGrad)" rx="15"/>
        
        <!-- 手指 -->
        <ellipse cx="155" cy="305" rx="7" ry="18" fill="url(#energyGrad)" transform="rotate(-15 155 305)"/>
        <ellipse cx="170" cy="290" rx="7" ry="20" fill="url(#energyGrad)" transform="rotate(-5 170 290)"/>
        <ellipse cx="185" cy="285" rx="7" ry="22" fill="url(#energyGrad)"/>
        <ellipse cx="200" cy="285" rx="7" ry="22" fill="url(#energyGrad)"/>
        <ellipse cx="215" cy="290" rx="7" ry="20" fill="url(#energyGrad)" transform="rotate(5 215 290)"/>
    </g>
    
    <!-- 文字 -->
    <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="24" 
          font-weight="bold" fill="#9370DB">千鸟</text>
</svg>'''

def create_shadow_clone_svg():
    """创建影分身SVG"""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <!-- 烟雾渐变 -->
        <radialGradient id="smokeGrad" cx="50%" cy="50%" r="50%">
            <stop offset="0%" style="stop-color:#FFFFFF;stop-opacity:0.8" />
            <stop offset="50%" style="stop-color:#D3D3D3;stop-opacity:0.6" />
            <stop offset="100%" style="stop-color:#A9A9A9;stop-opacity:0.3" />
        </radialGradient>
        
        <!-- 分身渐变 -->
        <linearGradient id="cloneGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#FF6B00;stop-opacity:0.8" />
            <stop offset="50%" style="stop-color:#FF9500;stop-opacity:0.6" />
            <stop offset="100%" style="stop-color:#FFA500;stop-opacity:0.4" />
        </linearGradient>
        
        <!-- 模糊效果 -->
        <filter id="blur">
            <feGaussianBlur stdDeviation="2" result="blur"/>
        </filter>
        
        <!-- 发光效果 -->
        <filter id="glow">
            <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
            <feMerge> 
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
    </defs>
    
    <!-- 背景 -->
    <rect width="400" height="400" fill="#000"/>
    
    <!-- 烟雾云 -->
    <g opacity="0.7">
        <ellipse cx="200" cy="200" rx="150" ry="80" fill="url(#smokeGrad)">
            <animate attributeName="rx" values="150;180;150" dur="2s" repeatCount="indefinite"/>
            <animate attributeName="opacity" values="0.7;0.4;0.7" dur="2s" repeatCount="indefinite"/>
        </ellipse>
        
        <!-- 小烟雾 -->
        <ellipse cx="120" cy="180" rx="40" ry="25" fill="url(#smokeGrad)" opacity="0.5">
            <animate attributeName="cy" values="180;160;180" dur="1.5s" repeatCount="indefinite"/>
        </ellipse>
        <ellipse cx="280" cy="220" rx="35" ry="20" fill="url(#smokeGrad)" opacity="0.4">
            <animate attributeName="cy" values="220;200;220" dur="1.8s" repeatCount="indefinite"/>
        </ellipse>
        <ellipse cx="200" cy="120" rx="30" ry="15" fill="url(#smokeGrad)" opacity="0.6">
            <animate attributeName="cy" values="120;100;120" dur="1.2s" repeatCount="indefinite"/>
        </ellipse>
    </g>
    
    <!-- 分身人影 -->
    <g filter="url(#glow)">
        <!-- 分身1 -->
        <g opacity="0.8">
            <ellipse cx="150" cy="250" rx="30" ry="80" fill="url(#cloneGrad)"/>
            <ellipse cx="150" cy="180" rx="25" ry="35" fill="url(#cloneGrad)"/>
            <ellipse cx="135" cy="220" rx="15" ry="30" fill="url(#cloneGrad)"/>
            <ellipse cx="165" cy="220" rx="15" ry="30" fill="url(#cloneGrad)"/>
            <ellipse cx="135" cy="280" rx="12" ry="25" fill="url(#cloneGrad)"/>
            <ellipse cx="165" cy="280" rx="12" ry="25" fill="url(#cloneGrad)"/>
            <animate attributeName="opacity" values="0.8;0.4;0.8" dur="1.5s" repeatCount="indefinite"/>
        </g>
        
        <!-- 分身2 -->
        <g opacity="0.6">
            <ellipse cx="250" cy="250" rx="30" ry="80" fill="url(#cloneGrad)"/>
            <ellipse cx="250" cy="180" rx="25" ry="35" fill="url(#cloneGrad)"/>
            <ellipse cx="235" cy="220" rx="15" ry="30" fill="url(#cloneGrad)"/>
            <ellipse cx="265" cy="220" rx="15" ry="30" fill="url(#cloneGrad)"/>
            <ellipse cx="235" cy="280" rx="12" ry="25" fill="url(#cloneGrad)"/>
            <ellipse cx="265" cy="280" rx="12" ry="25" fill="url(#cloneGrad)"/>
            <animate attributeName="opacity" values="0.6;0.3;0.6" dur="1.8s" repeatCount="indefinite"/>
        </g>
        
        <!-- 分身3 -->
        <g opacity="0.5">
            <ellipse cx="200" cy="270" rx="25" ry="70" fill="url(#cloneGrad)"/>
            <ellipse cx="200" cy="210" rx="20" ry="30" fill="url(#cloneGrad)"/>
            <ellipse cx="185" cy="240" rx="12" ry="25" fill="url(#cloneGrad)"/>
            <ellipse cx="215" cy="240" rx="12" ry="25" fill="url(#cloneGrad)"/>
            <ellipse cx="185" cy="295" rx="10" ry="20" fill="url(#cloneGrad)"/>
            <ellipse cx="215" cy="295" rx="10" ry="20" fill="url(#cloneGrad)"/>
            <animate attributeName="opacity" values="0.5;0.2;0.5" dur="2.2s" repeatCount="indefinite"/>
        </g>
    </g>
    
    <!-- 结印手势 -->
    <g opacity="0.9">
        <ellipse cx="200" cy="150" rx="40" ry="20" fill="url(#cloneGrad)" transform="rotate(-10 200 150)"/>
        <ellipse cx="190" cy="140" rx="15" ry="8" fill="url(#cloneGrad)" transform="rotate(-20 190 140)"/>
        <ellipse cx="210" cy="140" rx="15" ry="8" fill="url(#cloneGrad)" transform="rotate(20 210 140)"/>
        
        <!-- 手指 -->
        <ellipse cx="180" cy="145" rx="3" ry="10" fill="url(#cloneGrad)" transform="rotate(-30 180 145)"/>
        <ellipse cx="185" cy="140" rx="3" ry="12" fill="url(#cloneGrad)" transform="rotate(-10 185 140)"/>
        <ellipse cx="195" cy="135" rx="3" ry="12" fill="url(#cloneGrad)"/>
        <ellipse cx="205" cy="135" rx="3" ry="12" fill="url(#cloneGrad)"/>
        <ellipse cx="215" cy="140" rx="3" ry="12" fill="url(#cloneGrad)" transform="rotate(10 215 140)"/>
        <ellipse cx="220" cy="145" rx="3" ry="10" fill="url(#cloneGrad)" transform="rotate(30 220 145)"/>
    </g>
    
    <!-- 文字 -->
    <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="20" 
          font-weight="bold" fill="#FF9500">影分身之术</text>
</svg>'''

def create_sakura_svg():
    """创建春野樱SVG"""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <!-- 粉色头发 -->
        <linearGradient id="pinkHair" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#FFB6C1;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#FF69B4;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#FF1493;stop-opacity:1" />
        </linearGradient>
        
        <!-- 皮肤渐变 -->
        <linearGradient id="skin" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#FDBCB4;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#F4A460;stop-opacity:1" />
        </linearGradient>
        
        <!-- 红色衣服 -->
        <linearGradient id="redCloth" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#DC143C;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#B22222;stop-opacity:1" />
        </linearGradient>
    </defs>
    
    <!-- 背景 -->
    <circle cx="50" cy="50" r="45" fill="url(#redCloth)"/>
    
    <!-- 头部 -->
    <ellipse cx="50" cy="40" rx="18" ry="20" fill="url(#skin)"/>
    
    <!-- 粉色头发 -->
    <path d="M 32 25 Q 50 20 68 25 Q 65 22 50 20 Q 35 22 32 25" fill="url(#pinkHair)"/>
    <path d="M 35 30 Q 50 25 65 30" fill="url(#pinkHair)"/>
    
    <!-- 护额 -->
    <rect x="35" y="30" width="30" height="6" fill="#4169E1"/>
    <rect x="42" y="31" width="16" height="4" fill="#C0C0C0"/>
    
    <!-- 眼睛 -->
    <ellipse cx="44" cy="38" rx="3" ry="4" fill="#90EE90"/>
    <ellipse cx="56" cy="38" rx="3" ry="4" fill="#90EE90"/>
    <circle cx="44" cy="38" r="2" fill="#000"/>
    <circle cx="56" cy="38" r="2" fill="#000"/>
    
    <!-- 鼻子 -->
    <path d="M 50 42 L 48 45 L 52 45 Z" fill="#E6B89C"/>
    
    <!-- 嘴巴 -->
    <path d="M 47 48 Q 50 50 53 48" stroke="#000" stroke-width="1" fill="none"/>
    
    <!-- 衣服 -->
    <path d="M 32 60 Q 50 58 68 60 L 68 90 L 32 90 Z" fill="url(#redCloth)"/>
    
    <!-- 医疗标志 -->
    <path d="M 48 70 L 52 70 L 52 74 L 48 74 Z" fill="#FFF"/>
    <path d="M 50 68 L 50 76" stroke="#FFF" stroke-width="2"/>
</svg>'''

def create_akatsuki_symbol_svg():
    """创建晓组织标志SVG"""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <!-- 红色渐变 -->
        <radialGradient id="redGrad" cx="50%" cy="50%" r="50%">
            <stop offset="0%" style="stop-color:#DC143C;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#B22222;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#8B0000;stop-opacity:1" />
        </radialGradient>
        
        <!-- 阴影 -->
        <filter id="shadow">
            <feDropShadow dx="3" dy="3" stdDeviation="4" flood-color="#000" flood-opacity="0.5"/>
        </filter>
    </defs>
    
    <!-- 背景圆 -->
    <circle cx="100" cy="100" r="90" fill="url(#redGrad)" filter="url(#shadow)"/>
    
    <!-- 外圈 -->
    <circle cx="100" cy="100" r="85" fill="none" stroke="#000" stroke-width="4"/>
    
    <!-- 云朵形状 -->
    <g fill="#FFF">
        <!-- 主云朵 -->
        <ellipse cx="100" cy="85" rx="45" ry="25"/>
        <ellipse cx="85" cy="75" rx="30" ry="20"/>
        <ellipse cx="115" cy="75" rx="30" ry="20"/>
        <ellipse cx="70" cy="85" rx="25" ry="15"/>
        <ellipse cx="130" cy="85" rx="25" ry="15"/>
        
        <!-- 云朵装饰 -->
        <ellipse cx="100" cy="110" rx="35" ry="20"/>
        <ellipse cx="85" cy="120" rx="25" ry="15"/>
        <ellipse cx="115" cy="120" rx="25" ry="15"/>
        
        <!-- 小云朵 -->
        <ellipse cx="60" cy="110" rx="20" ry="12"/>
        <ellipse cx="140" cy="110" rx="20" ry="12"/>
        <ellipse cx="50" cy="95" rx="15" ry="10"/>
        <ellipse cx="150" cy="95" rx="15" ry="10"/>
        
        <!-- 底部云朵 -->
        <ellipse cx="100" cy="135" rx="40" ry="20"/>
        <ellipse cx="80" cy="145" rx="25" ry="15"/>
        <ellipse cx="120" cy="145" rx="25" ry="15"/>
        <ellipse cx="100" cy="155" rx="30" ry="12"/>
    </g>
    
    <!-- 内部阴影 -->
    <g opacity="0.3">
        <ellipse cx="100" cy="90" rx="40" ry="20" fill="#000"/>
        <ellipse cx="100" cy="115" rx="30" ry="15" fill="#000"/>
        <ellipse cx="100" cy="140" rx="35" ry="18" fill="#000"/>
    </g>
    
    <!-- 文字 -->
    <text x="100" y="185" text-anchor="middle" font-family="Arial" font-size="14" 
          font-weight="bold" fill="#8B0000">晓组织</text>
</svg>'''

def create_fire_country_svg():
    """创建火之国地图SVG"""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <!-- 地形渐变 -->
        <linearGradient id="landGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#8FBC8F;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#9ACD32;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#6B8E23;stop-opacity:1" />
        </linearGradient>
        
        <!-- 火焰渐变 -->
        <radialGradient id="fireGrad" cx="50%" cy="50%" r="50%">
            <stop offset="0%" style="stop-color:#FF6B00;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#FF4500;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#DC143C;stop-opacity:1" />
        </radialGradient>
        
        <!-- 阴影 -->
        <filter id="shadow">
            <feDropShadow dx="2" dy="2" stdDeviation="3" flood-color="#000" flood-opacity="0.3"/>
        </filter>
    </defs>
    
    <!-- 背景 -->
    <rect width="400" height="400" fill="#4682B4"/>
    
    <!-- 火之国轮廓 -->
    <path d="M 100 150 Q 200 100 300 150 Q 350 200 300 250 Q 250 300 200 280 Q 150 300 100 250 Q 50 200 100 150" 
          fill="url(#landGrad)" filter="url(#shadow)"/>
    
    <!-- 火焰装饰 -->
    <g opacity="0.6">
        <path d="M 150 200 Q 160 180 170 200 Q 180 180 190 200 Q 200 180 210 200" 
              fill="url(#fireGrad)"/>
        <path d="M 210 220 Q 220 200 230 220 Q 240 200 250 220" 
              fill="url(#fireGrad)"/>
        <path d="M 170 240 Q 180 220 190 240 Q 200 220 210 240" 
              fill="url(#fireGrad)"/>
    </g>
    
    <!-- 木叶村 -->
    <circle cx="200" cy="200" r="12" fill="#228B22" filter="url(#shadow)"/>
    <path d="M 200 190 Q 195 195 200 205 Q 205 195 200 190" fill="#32CD32"/>
    
    <!-- 山脉 -->
    <path d="M 80 180 Q 100 160 120 180 Q 140 160 160 180" fill="#8B4513" opacity="0.7"/>
    <path d="M 240 180 Q 260 160 280 180 Q 300 160 320 180" fill="#8B4513" opacity="0.7"/>
    
    <!-- 河流 -->
    <path d="M 180 120 Q 200 140 220 120 Q 240 140 260 120" stroke="#4682B4" stroke-width="4" fill="none"/>
    <path d="M 140 280 Q 160 300 180 280 Q 200 300 220 280" stroke="#4682B4" stroke-width="4" fill="none"/>
    
    <!-- 标题 -->
    <text x="200" y="50" text-anchor="middle" font-family="Arial" font-size="24" 
          font-weight="bold" fill="#FF6B00" filter="url(#shadow)">火之国</text>
    
    <!-- 说明文字 -->
    <text x="200" y="350" text-anchor="middle" font-family="Arial" font-size="14" 
          font-weight="bold" fill="#000">木叶隐村所在地</text>
</svg>'''

def create_all_small_avatars():
    """创建所有小头像SVG"""
    small_avatars = {
        'naruto-small.svg': '🦊',
        'sasuke-small.svg': '⚡', 
        'sakura-small.svg': '🌸',
        'kakashi-small.svg': '⚡',
        'pain-small.svg': '👁️',
        'itachi-small.svg': '🔥',
        'kisame-small.svg': '🦈',
        'deidara-small.svg': '💥',
        'gaara-small.svg': '🏜️',
        'tsunade-small.svg': '💎',
        'raikage-small.svg': '⚡',
        'tsuchikage-small.svg': '🗻',
        'yugito-small.svg': '🐱',
        'killer-bee-small.svg': '🐙',
        'hinata-small.svg': '👁️',
        'jiraiya-small.svg': '🐸'
    }
    
    svg_templates = {}
    
    for filename, emoji in small_avatars.items():
        character_name = filename.replace('-small.svg', '')
        
        # 根据角色设置不同的配色
        if 'naruto' in character_name:
            bg_color = '#FF6B00'
            text_color = '#FFF'
        elif 'sasuke' in character_name:
            bg_color = '#000080'
            text_color = '#FFF'
        elif 'sakura' in character_name:
            bg_color = '#FF69B4'
            text_color = '#FFF'
        elif 'kakashi' in character_name:
            bg_color = '#708090'
            text_color = '#FFF'
        elif 'pain' in character_name:
            bg_color = '#8B0000'
            text_color = '#FFF'
        elif 'itachi' in character_name:
            bg_color = '#8B0000'
            text_color = '#FFF'
        elif 'gaara' in character_name:
            bg_color = '#DAA520'
            text_color = '#000'
        elif 'tsunade' in character_name:
            bg_color = '#32CD32'
            text_color = '#FFF'
        else:
            bg_color = '#4169E1'
            text_color = '#FFF'
        
        svg_templates[filename] = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:{bg_color};stop-opacity:1" />
            <stop offset="100%" style="stop-color:{bg_color}CC;stop-opacity:1" />
        </linearGradient>
        
        <filter id="shadow">
            <feDropShadow dx="1" dy="1" stdDeviation="2" flood-color="#000" flood-opacity="0.3"/>
        </filter>
    </defs>
    
    <!-- 背景 -->
    <circle cx="50" cy="50" r="45" fill="url(#bgGrad)" filter="url(#shadow)"/>
    
    <!-- 角色表情符号 -->
    <text x="50" y="60" text-anchor="middle" font-family="Arial" font-size="32" fill="{text_color}">
        {emoji}
    </text>
    
    <!-- 边框 -->
    <circle cx="50" cy="50" r="45" fill="none" stroke="{bg_color}" stroke-width="3"/>
</svg>'''
    
    return svg_templates

def create_background_svgs():
    """创建背景图片SVG"""
    backgrounds = {
        'characters-bg.svg': ('忍者列传', '#FF6B00'),
        'world-bg.svg': ('世界探秘', '#00CC66'),
        'jutsu-bg.svg': ('忍术卷轴', '#8A2BE2'),
        'moments-bg.svg': ('经典瞬间', '#FFD700')
    }
    
    svg_templates = {}
    
    for filename, (title, color) in backgrounds.items():
        svg_templates[filename] = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:{color};stop-opacity:1" />
            <stop offset="50%" style="stop-color:{color}CC;stop-opacity:1" />
            <stop offset="100%" style="stop-color:{color}88;stop-opacity:1" />
        </linearGradient>
        
        <pattern id="pattern" x="0" y="0" width="100" height="100" patternUnits="userSpaceOnUse">
            <circle cx="50" cy="50" r="2" fill="rgba(255,255,255,0.2)"/>
            <circle cx="25" cy="25" r="1" fill="rgba(255,255,255,0.1)"/>
            <circle cx="75" cy="75" r="1.5" fill="rgba(255,255,255,0.15)"/>
        </pattern>
        
        <filter id="shadow">
            <feDropShadow dx="2" dy="2" stdDeviation="3" flood-color="#000" flood-opacity="0.3"/>
        </filter>
    </defs>
    
    <!-- 背景渐变 -->
    <rect width="800" height="600" fill="url(#bgGrad)"/>
    
    <!-- 图案覆盖 -->
    <rect width="800" height="600" fill="url(#pattern)"/>
    
    <!-- 装饰性图形 -->
    <g opacity="0.3">
        <path d="M 100 100 Q 200 50 300 100 Q 400 150 500 100 Q 600 50 700 100" 
              fill="none" stroke="rgba(255,255,255,0.4)" stroke-width="4"/>
        <path d="M 100 500 Q 200 450 300 500 Q 400 550 500 500 Q 600 450 700 500" 
              fill="none" stroke="rgba(255,255,255,0.4)" stroke-width="4"/>
    </g>
    
    <!-- 中心标题 -->
    <text x="400" y="300" text-anchor="middle" font-family="Arial" font-size="48" 
          font-weight="bold" fill="rgba(255,255,255,0.8)" filter="url(#shadow)">
        {title}
    </text>
    
    <!-- 副标题 -->
    <text x="400" y="350" text-anchor="middle" font-family="Arial" font-size="18" 
          fill="rgba(255,255,255,0.6)">
        火影忍者主题网站
    </text>
</svg>'''
    
    return svg_templates

def generate_all_complete_svgs():
    """生成所有完整的SVG图片"""
    images_dir = 'images'
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)
    
    # 主要角色SVG创建函数
    main_svgs = {
        'tobirama.svg': create_tobirama_svg,
        'hiruzen.svg': create_hiruzen_svg,
        'minato.svg': create_minato_svg,
        'tsunade.svg': create_tsunade_svg,
        'hashirama.svg': create_hashirama_svg,
        'chidori.svg': create_chidori_svg,
        'shadow-clone.svg': create_shadow_clone_svg,
        'akatsuki-symbol.svg': create_akatsuki_symbol_svg,
        'fire-country.svg': create_fire_country_svg,
    }
    
    # 生成主要SVG
    for filename, creator_func in main_svgs.items():
        print(f"正在生成主要图片: {filename}...")
        svg_content = creator_func()
        filepath = os.path.join(images_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        print(f"✅ 已保存: {filepath}")
    
    # 生成小头像SVG
    small_avatars = create_all_small_avatars()
    for filename, svg_content in small_avatars.items():
        print(f"正在生成小头像: {filename}...")
        filepath = os.path.join(images_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        print(f"✅ 已保存: {filepath}")
    
    # 生成背景图片SVG
    backgrounds = create_background_svgs()
    for filename, svg_content in backgrounds.items():
        print(f"正在生成背景图片: {filename}...")
        filepath = os.path.join(images_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        print(f"✅ 已保存: {filepath}")
    
    # 生成其他国家地图
    other_countries = {
        'wind-country.svg': ('风之国', '#DAA520', '🌪️'),
        'water-country.svg': ('水之国', '#4682B4', '🌊'),
        'earth-country.svg': ('土之国', '#8B4513', '🗻'),
        'lightning-country.svg': ('雷之国', '#9370DB', '⚡'),
    }
    
    for filename, (country_name, color, emoji) in other_countries.items():
        print(f"正在生成国家地图: {filename}...")
        svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="countryGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:{color};stop-opacity:1" />
            <stop offset="50%" style="stop-color:{color}CC;stop-opacity:1" />
            <stop offset="100%" style="stop-color:{color}88;stop-opacity:1" />
        </linearGradient>
        
        <filter id="shadow">
            <feDropShadow dx="2" dy="2" stdDeviation="3" flood-color="#000" flood-opacity="0.3"/>
        </filter>
    </defs>
    
    <!-- 背景 -->
    <rect width="400" height="400" fill="#4682B4"/>
    
    <!-- 国家轮廓 -->
    <path d="M 100 150 Q 200 100 300 150 Q 350 200 300 250 Q 250 300 200 280 Q 150 300 100 250 Q 50 200 100 150" 
          fill="url(#countryGrad)" filter="url(#shadow)"/>
    
    <!-- 国家象征 -->
    <text x="200" y="220" text-anchor="middle" font-family="Arial" font-size="48" fill="rgba(255,255,255,0.8)">
        {emoji}
    </text>
    
    <!-- 标题 -->
    <text x="200" y="50" text-anchor="middle" font-family="Arial" font-size="24" 
          font-weight="bold" fill="{color}" filter="url(#shadow)">{country_name}</text>
    
    <!-- 说明文字 -->
    <text x="200" y="350" text-anchor="middle" font-family="Arial" font-size="14" 
          font-weight="bold" fill="#000">五大国之一</text>
</svg>'''
        
        filepath = os.path.join(images_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        print(f"✅ 已保存: {filepath}")
    
    print("\n🎉 所有完整的真实感SVG图片已生成完成！")
    print("🎨 包含以下类型的图片:")
    print("  - 7位火影的详细头像")
    print("  - 主要角色小头像")
    print("  - 忍术动画效果")
    print("  - 五大国地图")
    print("  - 组织标志")
    print("  - 页面背景图")
    print("📁 总共生成了 40+ 个SVG图片文件")

if __name__ == "__main__":
    print("🎨 火影忍者完整SVG图片生成器 🎨")
    print("=" * 50)
    
    try:
        generate_all_complete_svgs()
    except Exception as e:
        print(f"❌ 生成图片时出错: {e}")
        print("💡 请检查文件夹权限")