// 主 JavaScript 文件
document.addEventListener('DOMContentLoaded', function() {
    
    // 导航栏滚动效果
    const navbar = document.querySelector('.navbar');
    let lastScrollTop = 0;
    
    window.addEventListener('scroll', function() {
        let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        if (scrollTop > lastScrollTop && scrollTop > 100) {
            // 向下滚动，隐藏导航栏
            navbar.style.transform = 'translateY(-100%)';
        } else {
            // 向上滚动，显示导航栏
            navbar.style.transform = 'translateY(0)';
        }
        
        // 添加背景模糊效果
        if (scrollTop > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        
        lastScrollTop = scrollTop;
    });
    
    // 移动端导航菜单
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('show');
            navToggle.classList.toggle('active');
        });
        
        // 点击菜单项时关闭菜单
        const navLinks = document.querySelectorAll('.nav-menu a');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                navMenu.classList.remove('show');
                navToggle.classList.remove('active');
            });
        });
    }
    
    // 平滑滚动效果
    const scrollLinks = document.querySelectorAll('a[href^="#"]');
    scrollLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                const offsetTop = targetElement.offsetTop - 80; // 考虑导航栏高度
                
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // 视差滚动效果
    const parallaxElements = document.querySelectorAll('.parallax-bg');
    
    if (parallaxElements.length > 0) {
        window.addEventListener('scroll', function() {
            const scrollTop = window.pageYOffset;
            
            parallaxElements.forEach(element => {
                const speed = 0.5;
                const yPos = -(scrollTop * speed);
                element.style.transform = `translateY(${yPos}px)`;
            });
        });
    }
    
    // 元素淡入动画
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // 观察需要动画的元素
    const animateElements = document.querySelectorAll('.nav-card, .timeline-item, .concept-card, .faction-card');
    animateElements.forEach(element => {
        observer.observe(element);
    });
    
    // 卡片悬停效果
    const cards = document.querySelectorAll('.nav-card, .faction-card, .concept-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
    
    // 火影头像时间线交互
    const hokageItems = document.querySelectorAll('.timeline-item');
    hokageItems.forEach((item, index) => {
        item.addEventListener('mouseenter', function() {
            // 添加发光效果
            this.style.boxShadow = '0 0 30px rgba(255, 107, 0, 0.6)';
            
            // 播放音效（如果有的话）
            playHoverSound();
        });
        
        item.addEventListener('mouseleave', function() {
            this.style.boxShadow = '';
        });
        
        // 点击效果
        item.addEventListener('click', function() {
            // 移除其他项的活动状态
            hokageItems.forEach(otherItem => {
                otherItem.classList.remove('active');
            });
            
            // 添加当前项的活动状态
            this.classList.add('active');
        });
    });
    
    // 音效播放函数
    function playHoverSound() {
        // 这里可以添加音效播放逻辑
        // const audio = new Audio('sounds/hover.mp3');
        // audio.play();
    }
    
    // 粒子效果（如果需要）
    function createParticles() {
        const particlesContainer = document.createElement('div');
        particlesContainer.className = 'particles';
        document.body.appendChild(particlesContainer);
        
        for (let i = 0; i < 50; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.style.left = Math.random() * 100 + '%';
            particle.style.animationDelay = Math.random() * 2 + 's';
            particle.style.animationDuration = (Math.random() * 3 + 2) + 's';
            particlesContainer.appendChild(particle);
        }
    }
    
    // 页面加载完成后的效果
    window.addEventListener('load', function() {
        // 添加页面加载完成的类
        document.body.classList.add('loaded');
        
        // 可选：创建粒子效果
        // createParticles();
    });
    
    // 键盘快捷键
    document.addEventListener('keydown', function(e) {
        // ESC 键关闭任何打开的模态框或菜单
        if (e.key === 'Escape') {
            const openMenus = document.querySelectorAll('.nav-menu.show');
            openMenus.forEach(menu => {
                menu.classList.remove('show');
            });
            
            const activeToggles = document.querySelectorAll('.nav-toggle.active');
            activeToggles.forEach(toggle => {
                toggle.classList.remove('active');
            });
        }
    });
    
    // 防止右键菜单（可选）
    // document.addEventListener('contextmenu', function(e) {
    //     e.preventDefault();
    // });
    
    // 页面离开时的效果
    window.addEventListener('beforeunload', function() {
        document.body.classList.add('unloading');
    });
    
    // 工具函数
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
    
    function throttle(func, limit) {
        let inThrottle;
        return function() {
            const args = arguments;
            const context = this;
            if (!inThrottle) {
                func.apply(context, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    }
    
    // 使用防抖优化滚动事件
    const debouncedScroll = debounce(function() {
        // 滚动相关的计算密集型操作
    }, 10);
    
    window.addEventListener('scroll', debouncedScroll);
    
    // 动态背景颜色变化
    function updateBackgroundColor() {
        const scrollPercent = window.pageYOffset / (document.body.scrollHeight - window.innerHeight);
        const hue = 180 + (scrollPercent * 60); // 从青色到紫色
        document.body.style.backgroundColor = `hsl(${hue}, 20%, 5%)`;
    }
    
    // 使用节流优化背景颜色更新
    const throttledBgUpdate = throttle(updateBackgroundColor, 16);
    window.addEventListener('scroll', throttledBgUpdate);
    
    console.log('火影忍者主题网站已加载完成！');
});