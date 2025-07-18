#!/usr/bin/env python3
"""
创建更加真实的火影主题SVG图片
"""

import os

def create_naruto_svg():
    """创建鸣人头像SVG"""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <!-- 头发渐变 -->
        <linearGradient id="hairGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#FFD700;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#FFA500;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#FF8C00;stop-opacity:1" />
        </linearGradient>
        
        <!-- 皮肤渐变 -->
        <linearGradient id="skinGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#FDBCB4;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#F4A460;stop-opacity:1" />
        </linearGradient>
        
        <!-- 衣服渐变 -->
        <linearGradient id="clothGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#FF6B00;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#FF4500;stop-opacity:1" />
        </linearGradient>
        
        <!-- 阴影 -->
        <filter id="shadow">
            <feDropShadow dx="2" dy="2" stdDeviation="3" flood-color="#000" flood-opacity="0.3"/>
        </filter>
    </defs>
    
    <!-- 背景 -->
    <circle cx="200" cy="200" r="190" fill="url(#clothGrad)" filter="url(#shadow)"/>
    
    <!-- 头部 -->
    <ellipse cx="200" cy="180" rx="80" ry="90" fill="url(#skinGrad)"/>
    
    <!-- 头发 -->
    <path d="M 120 120 Q 200 80 280 120 Q 270 100 200 85 Q 130 100 120 120" fill="url(#hairGrad)"/>
    <path d="M 140 110 Q 180 95 200 100 Q 220 95 260 110" fill="url(#hairGrad)"/>
    
    <!-- 护额 -->
    <rect x="130" y="130" width="140" height="25" fill="#4169E1" stroke="#000080" stroke-width="2"/>
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
    
    <!-- 胡须纹 -->
    <path d="M 145 185 L 165 180" stroke="#000" stroke-width="2" fill="none"/>
    <path d="M 145 195 L 165 190" stroke="#000" stroke-width="2" fill="none"/>
    <path d="M 145 205 L 165 200" stroke="#000" stroke-width="2" fill="none"/>
    
    <path d="M 235 180 L 255 185" stroke="#000" stroke-width="2" fill="none"/>
    <path d="M 235 190 L 255 195" stroke="#000" stroke-width="2" fill="none"/>
    <path d="M 235 200 L 255 205" stroke="#000" stroke-width="2" fill="none"/>
    
    <!-- 鼻子 -->
    <path d="M 200 185 L 195 195 L 205 195 Z" fill="#E6B89C"/>
    
    <!-- 嘴巴 -->
    <path d="M 190 210 Q 200 220 210 210" stroke="#000" stroke-width="2" fill="none"/>
    
    <!-- 衣领 -->
    <path d="M 120 270 Q 200 260 280 270 L 280 400 L 120 400 Z" fill="url(#clothGrad)"/>
    
    <!-- 项链 -->
    <circle cx="200" cy="285" r="8" fill="#DC143C"/>
    
    <!-- 文字 -->
    <text x="200" y="350" text-anchor="middle" font-family="Arial" font-size="24" font-weight="bold" fill="#FFF">
        鸣人
    </text>
</svg>'''

def create_sasuke_svg():
    """创建佐助头像SVG"""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <!-- 头发渐变 -->
        <linearGradient id="darkHair" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#000080;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#191970;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#000000;stop-opacity:1" />
        </linearGradient>
        
        <!-- 皮肤渐变 -->
        <linearGradient id="paleSkin" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#F5DEB3;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#DDD;stop-opacity:1" />
        </linearGradient>
        
        <!-- 衣服渐变 -->
        <linearGradient id="darkCloth" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#000080;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#000040;stop-opacity:1" />
        </linearGradient>
        
        <!-- 写轮眼渐变 -->
        <radialGradient id="sharingan" cx="50%" cy="50%" r="50%">
            <stop offset="0%" style="stop-color:#FF0000;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#8B0000;stop-opacity:1" />
        </radialGradient>
        
        <filter id="shadow">
            <feDropShadow dx="2" dy="2" stdDeviation="3" flood-color="#000" flood-opacity="0.5"/>
        </filter>
    </defs>
    
    <!-- 背景 -->
    <circle cx="200" cy="200" r="190" fill="url(#darkCloth)" filter="url(#shadow)"/>
    
    <!-- 头部 -->
    <ellipse cx="200" cy="180" rx="80" ry="90" fill="url(#paleSkin)"/>
    
    <!-- 头发 -->
    <path d="M 120 120 Q 200 70 280 120 Q 270 90 200 75 Q 130 90 120 120" fill="url(#darkHair)"/>
    <path d="M 140 110 Q 180 85 200 90 Q 220 85 260 110" fill="url(#darkHair)"/>
    <path d="M 180 100 Q 200 95 220 100 Q 210 110 200 105 Q 190 110 180 100" fill="url(#darkHair)"/>
    
    <!-- 护额 -->
    <rect x="130" y="130" width="140" height="25" fill="#4169E1" stroke="#000080" stroke-width="2"/>
    <path d="M 160 142 L 240 142" stroke="#C0C0C0" stroke-width="3"/>
    
    <!-- 写轮眼 -->
    <circle cx="175" cy="170" r="15" fill="url(#sharingan)"/>
    <circle cx="225" cy="170" r="15" fill="url(#sharingan)"/>
    
    <!-- 写轮眼图案 -->
    <circle cx="175" cy="170" r="8" fill="#000"/>
    <circle cx="225" cy="170" r="8" fill="#000"/>
    
    <!-- 写轮眼勾玉 -->
    <path d="M 175 162 Q 170 167 175 172 Q 180 167 175 162" fill="#FF0000"/>
    <path d="M 183 167 Q 178 172 183 177 Q 188 172 183 167" fill="#FF0000"/>
    <path d="M 167 167 Q 162 172 167 177 Q 172 172 167 167" fill="#FF0000"/>
    
    <path d="M 225 162 Q 220 167 225 172 Q 230 167 225 162" fill="#FF0000"/>
    <path d="M 233 167 Q 228 172 233 177 Q 238 172 233 167" fill="#FF0000"/>
    <path d="M 217 167 Q 212 172 217 177 Q 222 172 217 167" fill="#FF0000"/>
    
    <!-- 鼻子 -->
    <path d="M 200 185 L 195 195 L 205 195 Z" fill="#E6B89C"/>
    
    <!-- 嘴巴 -->
    <path d="M 190 210 Q 200 205 210 210" stroke="#000" stroke-width="2" fill="none"/>
    
    <!-- 衣领 -->
    <path d="M 120 270 Q 200 260 280 270 L 280 400 L 120 400 Z" fill="url(#darkCloth)"/>
    
    <!-- 宇智波家徽 -->
    <circle cx="200" cy="290" r="15" fill="#FF0000"/>
    <path d="M 200 280 Q 190 285 200 295 Q 210 285 200 280" fill="#FFF"/>
    
    <!-- 文字 -->
    <text x="200" y="350" text-anchor="middle" font-family="Arial" font-size="24" font-weight="bold" fill="#FFF">
        佐助
    </text>
</svg>'''

def create_itachi_svg():
    """创建鼬头像SVG"""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="600" height="800" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <!-- 头发渐变 -->
        <linearGradient id="itachiHair" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#2F2F2F;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#1C1C1C;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#000000;stop-opacity:1" />
        </linearGradient>
        
        <!-- 皮肤渐变 -->
        <linearGradient id="itachiSkin" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#F5DEB3;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#E6D3B7;stop-opacity:1" />
        </linearGradient>
        
        <!-- 晓组织斗篷 -->
        <linearGradient id="akatsukiCloak" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#8B0000;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#B22222;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#800000;stop-opacity:1" />
        </linearGradient>
        
        <!-- 万花筒写轮眼 -->
        <radialGradient id="mangekyou" cx="50%" cy="50%" r="50%">
            <stop offset="0%" style="stop-color:#FF0000;stop-opacity:1" />
            <stop offset="70%" style="stop-color:#DC143C;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#8B0000;stop-opacity:1" />
        </radialGradient>
        
        <filter id="glow">
            <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
            <feMerge> 
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
        
        <filter id="shadow">
            <feDropShadow dx="3" dy="3" stdDeviation="5" flood-color="#000" flood-opacity="0.4"/>
        </filter>
    </defs>
    
    <!-- 背景 -->
    <rect width="600" height="800" fill="url(#akatsukiCloak)"/>
    
    <!-- 云朵图案 -->
    <g opacity="0.3">
        <ellipse cx="100" cy="100" rx="30" ry="15" fill="#FFF"/>
        <ellipse cx="90" cy="90" rx="20" ry="12" fill="#FFF"/>
        <ellipse cx="110" cy="85" rx="25" ry="10" fill="#FFF"/>
        
        <ellipse cx="500" cy="150" rx="35" ry="18" fill="#FFF"/>
        <ellipse cx="485" cy="140" rx="25" ry="15" fill="#FFF"/>
        <ellipse cx="515" cy="135" rx="30" ry="12" fill="#FFF"/>
        
        <ellipse cx="150" cy="700" rx="40" ry="20" fill="#FFF"/>
        <ellipse cx="130" cy="690" rx="30" ry="15" fill="#FFF"/>
        <ellipse cx="170" cy="685" rx="35" ry="18" fill="#FFF"/>
    </g>
    
    <!-- 身体轮廓 -->
    <path d="M 200 500 Q 300 480 400 500 L 450 800 L 150 800 Z" fill="url(#akatsukiCloak)" filter="url(#shadow)"/>
    
    <!-- 头部 -->
    <ellipse cx="300" cy="280" rx="90" ry="100" fill="url(#itachiSkin)"/>
    
    <!-- 头发 -->
    <path d="M 200 200 Q 300 150 400 200 Q 390 170 300 155 Q 210 170 200 200" fill="url(#itachiHair)"/>
    <path d="M 220 190 Q 280 165 300 170 Q 320 165 380 190" fill="url(#itachiHair)"/>
    
    <!-- 长发 -->
    <path d="M 210 250 Q 200 350 220 450 Q 240 400 250 350" fill="url(#itachiHair)"/>
    <path d="M 390 250 Q 400 350 380 450 Q 360 400 350 350" fill="url(#itachiHair)"/>
    
    <!-- 护额 -->
    <rect x="220" y="230" width="160" height="30" fill="#4169E1" stroke="#000080" stroke-width="2"/>
    <path d="M 240 245 L 360 245" stroke="#C0C0C0" stroke-width="4"/>
    
    <!-- 额头上的划痕 -->
    <path d="M 270 245 L 330 245" stroke="#8B0000" stroke-width="3"/>
    
    <!-- 万花筒写轮眼 -->
    <circle cx="270" cy="270" r="20" fill="url(#mangekyou)" filter="url(#glow)"/>
    <circle cx="330" cy="270" r="20" fill="url(#mangekyou)" filter="url(#glow)"/>
    
    <!-- 万花筒图案 -->
    <circle cx="270" cy="270" r="12" fill="#000"/>
    <circle cx="330" cy="270" r="12" fill="#000"/>
    
    <!-- 复杂的万花筒图案 -->
    <g fill="#FF0000">
        <!-- 左眼 -->
        <path d="M 270 258 Q 265 265 270 272 Q 275 265 270 258"/>
        <path d="M 278 265 Q 275 270 278 275 Q 283 270 278 265"/>
        <path d="M 262 265 Q 257 270 262 275 Q 267 270 262 265"/>
        <path d="M 270 275 Q 275 280 270 285 Q 265 280 270 275"/>
        
        <!-- 右眼 -->
        <path d="M 330 258 Q 325 265 330 272 Q 335 265 330 258"/>
        <path d="M 338 265 Q 335 270 338 275 Q 343 270 338 265"/>
        <path d="M 322 265 Q 317 270 322 275 Q 327 270 322 265"/>
        <path d="M 330 275 Q 335 280 330 285 Q 325 280 330 275"/>
    </g>
    
    <!-- 泪槽线 -->
    <path d="M 260 285 Q 265 320 270 350" stroke="#8B0000" stroke-width="3" fill="none"/>
    <path d="M 340 285 Q 335 320 330 350" stroke="#8B0000" stroke-width="3" fill="none"/>
    
    <!-- 鼻子 -->
    <path d="M 300 295 L 295 305 L 305 305 Z" fill="#E6B89C"/>
    
    <!-- 嘴巴 -->
    <path d="M 290 320 Q 300 315 310 320" stroke="#000" stroke-width="2" fill="none"/>
    
    <!-- 项链 -->
    <circle cx="300" cy="380" r="8" fill="#FFD700"/>
    
    <!-- 文字 -->
    <text x="300" y="600" text-anchor="middle" font-family="Arial" font-size="32" font-weight="bold" fill="#FFF">
        宇智波鼬
    </text>
    
    <text x="300" y="650" text-anchor="middle" font-family="Arial" font-size="18" fill="#FFF" opacity="0.8">
        "原谅我，佐助..."
    </text>
</svg>'''

def create_konoha_logo_svg():
    """创建木叶标志SVG"""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <!-- 叶子渐变 -->
        <linearGradient id="leafGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#32CD32;stop-opacity:1" />
            <stop offset="30%" style="stop-color:#228B22;stop-opacity:1" />
            <stop offset="70%" style="stop-color:#006400;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#013220;stop-opacity:1" />
        </linearGradient>
        
        <!-- 阴影 -->
        <filter id="leafShadow">
            <feDropShadow dx="2" dy="2" stdDeviation="2" flood-color="#000" flood-opacity="0.3"/>
        </filter>
    </defs>
    
    <!-- 背景圆 -->
    <circle cx="100" cy="100" r="95" fill="#FFF" stroke="#228B22" stroke-width="10"/>
    
    <!-- 主叶子 -->
    <path d="M 100 30 Q 70 60 80 100 Q 90 120 100 110 Q 110 120 120 100 Q 130 60 100 30" 
          fill="url(#leafGrad)" filter="url(#leafShadow)"/>
    
    <!-- 叶脉 -->
    <path d="M 100 35 Q 95 65 100 105" stroke="#013220" stroke-width="3" fill="none"/>
    <path d="M 100 50 Q 85 70 95 85" stroke="#013220" stroke-width="2" fill="none"/>
    <path d="M 100 50 Q 115 70 105 85" stroke="#013220" stroke-width="2" fill="none"/>
    <path d="M 100 70 Q 90 85 95 95" stroke="#013220" stroke-width="1" fill="none"/>
    <path d="M 100 70 Q 110 85 105 95" stroke="#013220" stroke-width="1" fill="none"/>
    
    <!-- 火焰装饰 -->
    <g opacity="0.7">
        <path d="M 50 150 Q 60 130 70 150 Q 80 130 90 150" 
              fill="#FF6B00" stroke="#FF4500" stroke-width="1"/>
        <path d="M 110 150 Q 120 130 130 150 Q 140 130 150 150" 
              fill="#FF6B00" stroke="#FF4500" stroke-width="1"/>
    </g>
    
    <!-- 文字 -->
    <text x="100" y="180" text-anchor="middle" font-family="Arial" font-size="14" 
          font-weight="bold" fill="#228B22">木叶隐村</text>
</svg>'''

def create_rasengan_svg():
    """创建螺旋丸SVG"""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <!-- 螺旋丸渐变 -->
        <radialGradient id="rasenganGrad" cx="50%" cy="50%" r="50%">
            <stop offset="0%" style="stop-color:#87CEEB;stop-opacity:1" />
            <stop offset="30%" style="stop-color:#00BFFF;stop-opacity:1" />
            <stop offset="70%" style="stop-color:#1E90FF;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#0000FF;stop-opacity:1" />
        </radialGradient>
        
        <!-- 能量波纹 -->
        <radialGradient id="energyGrad" cx="50%" cy="50%" r="50%">
            <stop offset="0%" style="stop-color:#FFF;stop-opacity:0.8" />
            <stop offset="50%" style="stop-color:#87CEEB;stop-opacity:0.6" />
            <stop offset="100%" style="stop-color:#1E90FF;stop-opacity:0.2" />
        </radialGradient>
        
        <!-- 发光效果 -->
        <filter id="glow">
            <feGaussianBlur stdDeviation="4" result="coloredBlur"/>
            <feMerge> 
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
        
        <!-- 动画 -->
        <animateTransform id="spin" attributeName="transform" type="rotate" 
                         values="0 200 200;360 200 200" dur="2s" repeatCount="indefinite"/>
    </defs>
    
    <!-- 背景 -->
    <rect width="400" height="400" fill="#000"/>
    
    <!-- 能量波纹 -->
    <g opacity="0.6">
        <circle cx="200" cy="200" r="180" fill="none" stroke="#00BFFF" stroke-width="2" opacity="0.3">
            <animate attributeName="r" values="180;220;180" dur="2s" repeatCount="indefinite"/>
            <animate attributeName="opacity" values="0.3;0.1;0.3" dur="2s" repeatCount="indefinite"/>
        </circle>
        <circle cx="200" cy="200" r="150" fill="none" stroke="#87CEEB" stroke-width="2" opacity="0.4">
            <animate attributeName="r" values="150;190;150" dur="1.5s" repeatCount="indefinite"/>
            <animate attributeName="opacity" values="0.4;0.2;0.4" dur="1.5s" repeatCount="indefinite"/>
        </circle>
        <circle cx="200" cy="200" r="120" fill="none" stroke="#1E90FF" stroke-width="2" opacity="0.5">
            <animate attributeName="r" values="120;160;120" dur="1s" repeatCount="indefinite"/>
            <animate attributeName="opacity" values="0.5;0.3;0.5" dur="1s" repeatCount="indefinite"/>
        </circle>
    </g>
    
    <!-- 主体螺旋丸 -->
    <g filter="url(#glow)">
        <circle cx="200" cy="200" r="80" fill="url(#rasenganGrad)"/>
        
        <!-- 螺旋纹理 -->
        <g>
            <animateTransform attributeName="transform" type="rotate" 
                             values="0 200 200;360 200 200" dur="1s" repeatCount="indefinite"/>
            
            <!-- 内螺旋 -->
            <path d="M 200 140 Q 240 160 220 200 Q 180 240 200 220 Q 240 180 200 200 Q 160 160 200 140" 
                  fill="none" stroke="#FFF" stroke-width="4" opacity="0.8"/>
            
            <!-- 外螺旋 -->
            <path d="M 200 120 Q 260 150 240 200 Q 160 250 200 230 Q 260 170 200 200 Q 140 150 200 120" 
                  fill="none" stroke="#87CEEB" stroke-width="3" opacity="0.6"/>
            
            <!-- 小螺旋 -->
            <path d="M 200 160 Q 220 180 200 200 Q 180 220 200 200 Q 220 180 200 160" 
                  fill="none" stroke="#FFF" stroke-width="2" opacity="0.9"/>
        </g>
        
        <!-- 中心光点 -->
        <circle cx="200" cy="200" r="10" fill="#FFF" opacity="0.9">
            <animate attributeName="opacity" values="0.9;0.5;0.9" dur="0.5s" repeatCount="indefinite"/>
        </circle>
    </g>
    
    <!-- 手掌轮廓 -->
    <g opacity="0.7">
        <ellipse cx="200" cy="320" rx="60" ry="30" fill="url(#energyGrad)" transform="rotate(-10 200 320)"/>
        <rect x="170" y="300" width="60" height="40" fill="url(#energyGrad)" rx="20"/>
        
        <!-- 手指 -->
        <ellipse cx="150" cy="310" rx="8" ry="20" fill="url(#energyGrad)" transform="rotate(-20 150 310)"/>
        <ellipse cx="170" cy="290" rx="8" ry="25" fill="url(#energyGrad)" transform="rotate(-10 170 290)"/>
        <ellipse cx="190" cy="285" rx="8" ry="28" fill="url(#energyGrad)"/>
        <ellipse cx="210" cy="290" rx="8" ry="25" fill="url(#energyGrad)" transform="rotate(10 210 290)"/>
        <ellipse cx="230" cy="310" rx="8" ry="20" fill="url(#energyGrad)" transform="rotate(20 230 310)"/>
    </g>
    
    <!-- 文字 -->
    <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="24" 
          font-weight="bold" fill="#00BFFF">螺旋丸</text>
</svg>'''

def create_world_map_svg():
    """创建忍者世界地图SVG"""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="1200" height="800" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <!-- 地形渐变 -->
        <linearGradient id="landGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#8FBC8F;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#9ACD32;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#6B8E23;stop-opacity:1" />
        </linearGradient>
        
        <!-- 海洋渐变 -->
        <linearGradient id="seaGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#4682B4;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#5F9EA0;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#2F4F4F;stop-opacity:1" />
        </linearGradient>
        
        <!-- 山脉渐变 -->
        <linearGradient id="mountainGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#A0522D;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#8B4513;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#654321;stop-opacity:1" />
        </linearGradient>
        
        <!-- 沙漠渐变 -->
        <linearGradient id="desertGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#F4A460;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#DAA520;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#B8860B;stop-opacity:1" />
        </linearGradient>
        
        <!-- 阴影 -->
        <filter id="shadow">
            <feDropShadow dx="2" dy="2" stdDeviation="3" flood-color="#000" flood-opacity="0.3"/>
        </filter>
    </defs>
    
    <!-- 海洋背景 -->
    <rect width="1200" height="800" fill="url(#seaGrad)"/>
    
    <!-- 波浪效果 -->
    <g opacity="0.3">
        <path d="M 0 100 Q 100 80 200 100 Q 300 120 400 100 Q 500 80 600 100 Q 700 120 800 100 Q 900 80 1000 100 Q 1100 120 1200 100 L 1200 0 L 0 0 Z" 
              fill="#6495ED"/>
        <path d="M 0 700 Q 100 720 200 700 Q 300 680 400 700 Q 500 720 600 700 Q 700 680 800 700 Q 900 720 1000 700 Q 1100 680 1200 700 L 1200 800 L 0 800 Z" 
              fill="#6495ED"/>
    </g>
    
    <!-- 火之国 -->
    <path d="M 400 200 Q 500 150 600 200 Q 650 250 600 300 Q 550 350 500 300 Q 450 250 400 200" 
          fill="url(#landGrad)" filter="url(#shadow)"/>
    
    <!-- 木叶村 -->
    <circle cx="500" cy="250" r="15" fill="#228B22" filter="url(#shadow)"/>
    <text x="520" y="255" font-family="Arial" font-size="14" font-weight="bold" fill="#000">木叶隐村</text>
    
    <!-- 风之国 -->
    <path d="M 200 400 Q 300 350 400 400 Q 450 450 400 500 Q 350 550 300 500 Q 250 450 200 400" 
          fill="url(#desertGrad)" filter="url(#shadow)"/>
    
    <!-- 砂隐村 -->
    <circle cx="300" cy="450" r="12" fill="#DAA520" filter="url(#shadow)"/>
    <text x="320" y="455" font-family="Arial" font-size="12" font-weight="bold" fill="#000">砂隐村</text>
    
    <!-- 水之国 -->
    <ellipse cx="800" cy="200" rx="80" ry="60" fill="url(#landGrad)" filter="url(#shadow)"/>
    
    <!-- 雾隐村 -->
    <circle cx="800" cy="200" r="10" fill="#5F9EA0" filter="url(#shadow)"/>
    <text x="820" y="205" font-family="Arial" font-size="12" font-weight="bold" fill="#000">雾隐村</text>
    
    <!-- 土之国 -->
    <path d="M 150 200 Q 250 150 350 200 Q 300 250 250 300 Q 200 250 150 200" 
          fill="url(#mountainGrad)" filter="url(#shadow)"/>
    
    <!-- 岩隐村 -->
    <circle cx="250" cy="225" r="12" fill="#8B4513" filter="url(#shadow)"/>
    <text x="270" y="230" font-family="Arial" font-size="12" font-weight="bold" fill="#000">岩隐村</text>
    
    <!-- 雷之国 -->
    <path d="M 700 100 Q 800 50 900 100 Q 850 150 800 200 Q 750 150 700 100" 
          fill="url(#mountainGrad)" filter="url(#shadow)"/>
    
    <!-- 云隐村 -->
    <circle cx="800" cy="125" r="12" fill="#9370DB" filter="url(#shadow)"/>
    <text x="820" y="130" font-family="Arial" font-size="12" font-weight="bold" fill="#000">云隐村</text>
    
    <!-- 终结之谷 -->
    <path d="M 650 300 Q 680 280 710 300 Q 680 320 650 300" fill="#4682B4" filter="url(#shadow)"/>
    <text x="730" y="305" font-family="Arial" font-size="11" font-weight="bold" fill="#000">终结之谷</text>
    
    <!-- 山脉 -->
    <path d="M 0 300 Q 50 250 100 300 Q 150 250 200 300 Q 250 250 300 300" 
          fill="none" stroke="url(#mountainGrad)" stroke-width="8" opacity="0.7"/>
    
    <path d="M 900 300 Q 950 250 1000 300 Q 1050 250 1100 300 Q 1150 250 1200 300" 
          fill="none" stroke="url(#mountainGrad)" stroke-width="8" opacity="0.7"/>
    
    <!-- 标题 -->
    <text x="600" y="50" text-anchor="middle" font-family="Arial" font-size="32" 
          font-weight="bold" fill="#000" filter="url(#shadow)">忍者世界地图</text>
    
    <!-- 图例 -->
    <g transform="translate(50, 600)">
        <rect x="0" y="0" width="200" height="150" fill="#FFF" fill-opacity="0.8" 
              stroke="#000" stroke-width="2" rx="10"/>
        <text x="100" y="20" text-anchor="middle" font-family="Arial" font-size="14" 
              font-weight="bold" fill="#000">图例</text>
        
        <circle cx="20" cy="40" r="8" fill="#228B22"/>
        <text x="35" y="45" font-family="Arial" font-size="12" fill="#000">忍者村</text>
        
        <rect x="10" y="55" width="16" height="10" fill="url(#landGrad)"/>
        <text x="35" y="65" font-family="Arial" font-size="12" fill="#000">陆地</text>
        
        <rect x="10" y="75" width="16" height="10" fill="url(#seaGrad)"/>
        <text x="35" y="85" font-family="Arial" font-size="12" fill="#000">海洋</text>
        
        <rect x="10" y="95" width="16" height="10" fill="url(#mountainGrad)"/>
        <text x="35" y="105" font-family="Arial" font-size="12" fill="#000">山脉</text>
        
        <rect x="10" y="115" width="16" height="10" fill="url(#desertGrad)"/>
        <text x="35" y="125" font-family="Arial" font-size="12" fill="#000">沙漠</text>
    </g>
</svg>'''

def generate_all_realistic_svgs():
    """生成所有真实感SVG图片"""
    images_dir = 'images'
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)
    
    # 图片配置
    svg_creators = {
        'naruto.svg': create_naruto_svg,
        'sasuke.svg': create_sasuke_svg, 
        'itachi-featured.svg': create_itachi_svg,
        'konoha-logo.svg': create_konoha_logo_svg,
        'rasengan.svg': create_rasengan_svg,
        'ninja-world-map.svg': create_world_map_svg,
    }
    
    for filename, creator_func in svg_creators.items():
        print(f"正在生成真实感图片: {filename}...")
        
        svg_content = creator_func()
        filepath = os.path.join(images_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        
        print(f"✅ 已保存: {filepath}")
    
    print("\n🎉 所有真实感SVG图片已生成完成！")
    print("🎨 这些图片包含了:")
    print("  - 详细的角色设计（面部特征、服装、特殊能力）")
    print("  - 动画效果（旋转、发光、波纹）")
    print("  - 渐变和阴影效果")
    print("  - 符合火影风格的配色")
    print("📁 图片保存在 images/ 文件夹中")

if __name__ == "__main__":
    print("🎨 火影忍者真实感SVG图片生成器 🎨")
    print("=" * 50)
    
    try:
        generate_all_realistic_svgs()
    except Exception as e:
        print(f"❌ 生成图片时出错: {e}")
        print("💡 请检查文件夹权限")