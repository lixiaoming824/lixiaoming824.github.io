// 忍术卷轴页面特定功能
document.addEventListener('DOMContentLoaded', function() {
    
    // 忍术展示切换
    const jutsuNavBtns = document.querySelectorAll('.jutsu-nav-btn');
    const jutsuItems = document.querySelectorAll('.jutsu-item');
    
    jutsuNavBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const targetJutsu = this.dataset.target;
            switchJutsu(targetJutsu);
            
            // 更新按钮状态
            jutsuNavBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
        });
    });
    
    // 切换忍术展示
    function switchJutsu(jutsuName) {
        jutsuItems.forEach(item => {
            item.classList.remove('active');
            
            if (item.dataset.jutsu === jutsuName) {
                item.classList.add('active');
            }
        });
    }
    
    // 自动轮播忍术
    let currentJutsuIndex = 0;
    const jutsuNames = ['rasengan', 'chidori', 'kage-bunshin', 'shinra-tensei', 'chibaku-tensei'];
    
    function autoSwitchJutsu() {
        currentJutsuIndex = (currentJutsuIndex + 1) % jutsuNames.length;
        const nextJutsu = jutsuNames[currentJutsuIndex];
        
        switchJutsu(nextJutsu);
        
        // 更新导航按钮
        jutsuNavBtns.forEach(btn => btn.classList.remove('active'));
        const activeBtn = document.querySelector(`[data-target="${nextJutsu}"]`);
        if (activeBtn) {
            activeBtn.classList.add('active');
        }
    }
    
    // 启动自动轮播
    setInterval(autoSwitchJutsu, 5000);
    
    // 分类标签页切换
    const categoryTabs = document.querySelectorAll('.tab-btn');
    const categoryPanels = document.querySelectorAll('.category-panel');
    
    categoryTabs.forEach(tab => {
        tab.addEventListener('click', function() {
            const targetCategory = this.dataset.category;
            switchCategory(targetCategory);
            
            // 更新标签状态
            categoryTabs.forEach(t => t.classList.remove('active'));
            this.classList.add('active');
        });
    });
    
    // 切换分类
    function switchCategory(categoryName) {
        categoryPanels.forEach(panel => {
            panel.classList.remove('active');
            
            if (panel.dataset.category === categoryName) {
                panel.classList.add('active');
            }
        });
    }
    
    // 忍术详情展示
    const jutsuEntries = document.querySelectorAll('.jutsu-entry');
    
    jutsuEntries.forEach(entry => {
        entry.addEventListener('click', function() {
            const jutsuName = this.querySelector('.jutsu-name').textContent;
            const jutsuUser = this.querySelector('.jutsu-user').textContent;
            showJutsuDetails(jutsuName, jutsuUser);
        });
        
        // 悬停效果
        entry.addEventListener('mouseenter', function() {
            this.style.transform = 'translateX(5px)';
            this.style.boxShadow = '0 5px 15px rgba(138, 43, 226, 0.3)';
        });
        
        entry.addEventListener('mouseleave', function() {
            this.style.transform = 'translateX(0)';
            this.style.boxShadow = '';
        });
    });
    
    // 显示忍术详情
    function showJutsuDetails(jutsuName, jutsuUser) {
        const jutsuData = {
            '豪火球之术': {
                name: '豪火球之术',
                japanese: 'ごうかきゅうのじゅつ',
                rank: 'C级',
                type: '火遁',
                description: '宇智波一族的标志性忍术，从口中喷出巨大的火球攻击敌人。',
                handSeals: ['巳', '未', '申', '亥', '午', '寅'],
                chakraNature: '火',
                users: ['宇智波佐助', '宇智波鼬', '宇智波斑'],
                requirements: '火属性查克拉',
                weaknesses: '水遁忍术',
                image: 'goukakyuu.gif'
            },
            '螺旋丸': {
                name: '螺旋丸',
                japanese: 'らせんがん',
                rank: 'A级',
                type: '忍术',
                description: '无需结印的高级忍术，将查克拉高速旋转压缩成球状。',
                handSeals: ['无需结印'],
                chakraNature: '无属性',
                users: ['波风水门', '漩涡鸣人', '自来也'],
                requirements: '极高的查克拉控制力',
                weaknesses: '需要近距离接触',
                image: 'rasengan.gif'
            }
        };
        
        const jutsu = jutsuData[jutsuName];
        if (jutsu) {
            showJutsuModal(jutsu);
        }
    }
    
    // 显示忍术模态框
    function showJutsuModal(jutsu) {
        const modalHTML = `
            <div class="modal-overlay jutsu-modal" id="jutsuModal">
                <div class="modal-content">
                    <div class="modal-header">
                        <div class="jutsu-header-info">
                            <h2>${jutsu.name}</h2>
                            <p class="jutsu-japanese">${jutsu.japanese}</p>
                            <div class="jutsu-meta">
                                <span class="jutsu-rank">${jutsu.rank}</span>
                                <span class="jutsu-type">${jutsu.type}</span>
                            </div>
                        </div>
                        <button class="modal-close">&times;</button>
                    </div>
                    <div class="modal-body">
                        <div class="jutsu-visual">
                            <img src="images/${jutsu.image}" alt="${jutsu.name}">
                        </div>
                        <div class="jutsu-details">
                            <p class="jutsu-description">${jutsu.description}</p>
                            
                            <div class="jutsu-info-grid">
                                <div class="info-item">
                                    <h4>结印</h4>
                                    <div class="hand-seals">
                                        ${jutsu.handSeals.map(seal => `
                                            <span class="seal">${seal}</span>
                                        `).join('')}
                                    </div>
                                </div>
                                
                                <div class="info-item">
                                    <h4>查克拉属性</h4>
                                    <span class="chakra-nature">${jutsu.chakraNature}</span>
                                </div>
                                
                                <div class="info-item">
                                    <h4>使用者</h4>
                                    <div class="users-list">
                                        ${jutsu.users.map(user => `
                                            <span class="user-tag">${user}</span>
                                        `).join('')}
                                    </div>
                                </div>
                                
                                <div class="info-item">
                                    <h4>使用要求</h4>
                                    <p>${jutsu.requirements}</p>
                                </div>
                                
                                <div class="info-item">
                                    <h4>弱点</h4>
                                    <p>${jutsu.weaknesses}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;
        
        document.body.insertAdjacentHTML('beforeend', modalHTML);
        
        const modal = document.getElementById('jutsuModal');
        const closeBtn = modal.querySelector('.modal-close');
        
        closeBtn.addEventListener('click', closeJutsuModal);
        modal.addEventListener('click', function(e) {
            if (e.target === modal) {
                closeJutsuModal();
            }
        });
        
        setTimeout(() => modal.classList.add('show'), 10);
    }
    
    // 关闭忍术模态框
    function closeJutsuModal() {
        const modal = document.getElementById('jutsuModal');
        if (modal) {
            modal.classList.remove('show');
            setTimeout(() => modal.remove(), 300);
        }
    }
    
    // 禁术卡片交互
    const forbiddenCards = document.querySelectorAll('.forbidden-card');
    
    forbiddenCards.forEach(card => {
        card.addEventListener('click', function() {
            const jutsuName = this.querySelector('h3').textContent;
            showForbiddenJutsuDetails(jutsuName);
        });
        
        // 危险警告效果
        card.addEventListener('mouseenter', function() {
            this.style.borderColor = '#ff0000';
            this.style.boxShadow = '0 0 30px rgba(255, 0, 0, 0.5)';
            
            // 添加警告音效
            playWarningSound();
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.borderColor = '#660000';
            this.style.boxShadow = '';
        });
    });
    
    // 显示禁术详情
    function showForbiddenJutsuDetails(jutsuName) {
        const forbiddenData = {
            '秽土转生': {
                name: '秽土转生',
                danger: 'S级禁术',
                description: '召唤死者灵魂的终极禁术，被召唤者拥有无限查克拉和不死之身。',
                creator: '千手扉间',
                users: ['千手扉间', '大蛇丸', '兜'],
                requirements: '死者DNA、活人祭品、复杂的封印术',
                consequences: '亵渎死者、破坏生死平衡',
                countermeasures: '封印术、解除印记',
                warnings: [
                    '被召唤者保持生前全部能力',
                    '无限查克拉供应',
                    '不会因伤死亡',
                    '可能失控反噬施术者'
                ]
            },
            '八门遁甲之阵': {
                name: '八门遁甲之阵',
                danger: 'S级禁术',
                description: '开启身体所有限制的究极体术，获得超越影级的力量。',
                creator: '未知',
                users: ['迈特·戴', '迈特·凯'],
                requirements: '极限体术修行、钢铁意志',
                consequences: '必定死亡、身体燃烧殆尽',
                countermeasures: '无法阻止，只能预防',
                warnings: [
                    '第八门必死',
                    '身体会燃烧成灰烬',
                    '短时间内获得神级力量',
                    '青春的最终绽放'
                ]
            }
        };
        
        const jutsu = forbiddenData[jutsuName];
        if (jutsu) {
            showForbiddenModal(jutsu);
        }
    }
    
    // 显示禁术模态框
    function showForbiddenModal(jutsu) {
        const modalHTML = `
            <div class="modal-overlay forbidden-modal" id="forbiddenModal">
                <div class="modal-content">
                    <div class="modal-header">
                        <div class="forbidden-header-info">
                            <h2>${jutsu.name}</h2>
                            <span class="danger-level">${jutsu.danger}</span>
                        </div>
                        <button class="modal-close">&times;</button>
                    </div>
                    <div class="modal-body">
                        <div class="warning-banner">
                            <h3>⚠️ 危险警告 ⚠️</h3>
                            <p>此术式极度危险，切勿轻易尝试</p>
                        </div>
                        
                        <div class="forbidden-description">
                            <p>${jutsu.description}</p>
                        </div>
                        
                        <div class="forbidden-info-grid">
                            <div class="info-section">
                                <h4>创造者</h4>
                                <p>${jutsu.creator}</p>
                            </div>
                            
                            <div class="info-section">
                                <h4>已知使用者</h4>
                                <div class="users-list">
                                    ${jutsu.users.map(user => `
                                        <span class="user-tag forbidden">${user}</span>
                                    `).join('')}
                                </div>
                            </div>
                            
                            <div class="info-section">
                                <h4>使用要求</h4>
                                <p>${jutsu.requirements}</p>
                            </div>
                            
                            <div class="info-section">
                                <h4>后果</h4>
                                <p class="consequences">${jutsu.consequences}</p>
                            </div>
                            
                            <div class="info-section">
                                <h4>对抗措施</h4>
                                <p>${jutsu.countermeasures}</p>
                            </div>
                        </div>
                        
                        <div class="warnings-section">
                            <h4>危险警告</h4>
                            <ul class="warnings-list">
                                ${jutsu.warnings.map(warning => `
                                    <li>${warning}</li>
                                `).join('')}
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        `;
        
        document.body.insertAdjacentHTML('beforeend', modalHTML);
        
        const modal = document.getElementById('forbiddenModal');
        const closeBtn = modal.querySelector('.modal-close');
        
        closeBtn.addEventListener('click', closeForbiddenModal);
        modal.addEventListener('click', function(e) {
            if (e.target === modal) {
                closeForbiddenModal();
            }
        });
        
        setTimeout(() => modal.classList.add('show'), 10);
    }
    
    // 关闭禁术模态框
    function closeForbiddenModal() {
        const modal = document.getElementById('forbiddenModal');
        if (modal) {
            modal.classList.remove('show');
            setTimeout(() => modal.remove(), 300);
        }
    }
    
    // 播放警告音效
    function playWarningSound() {
        // 这里可以添加音效播放逻辑
        // const audio = new Audio('sounds/warning.mp3');
        // audio.play();
    }
    
    // 忍术搜索功能
    const searchInput = document.querySelector('.jutsu-search');
    
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            filterJutsu(searchTerm);
        });
    }
    
    // 过滤忍术
    function filterJutsu(searchTerm) {
        const allJutsuElements = document.querySelectorAll('.jutsu-entry, .forbidden-card, .concept-card');
        
        allJutsuElements.forEach(element => {
            const jutsuName = element.querySelector('h3, h4, .jutsu-name');
            
            if (jutsuName) {
                const name = jutsuName.textContent.toLowerCase();
                
                if (name.includes(searchTerm)) {
                    element.style.display = 'block';
                    element.classList.add('search-highlight');
                } else {
                    element.style.display = 'none';
                    element.classList.remove('search-highlight');
                }
            }
        });
    }
    
    // 忍术等级过滤
    const rankFilters = document.querySelectorAll('.rank-filter');
    
    rankFilters.forEach(filter => {
        filter.addEventListener('click', function() {
            const rank = this.dataset.rank;
            filterByRank(rank);
        });
    });
    
    // 按等级过滤
    function filterByRank(rank) {
        const jutsuElements = document.querySelectorAll('.jutsu-entry, .forbidden-card');
        
        jutsuElements.forEach(element => {
            const jutsuRank = element.querySelector('.jutsu-rank, .danger-level');
            
            if (jutsuRank) {
                const elementRank = jutsuRank.textContent;
                
                if (rank === 'all' || elementRank.includes(rank)) {
                    element.style.display = 'block';
                } else {
                    element.style.display = 'none';
                }
            }
        });
    }
    
    // 键盘快捷键
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            closeJutsuModal();
            closeForbiddenModal();
        }
        
        // 数字键切换忍术
        if (e.key >= '1' && e.key <= '5') {
            const index = parseInt(e.key) - 1;
            if (jutsuNames[index]) {
                switchJutsu(jutsuNames[index]);
                
                // 更新按钮状态
                jutsuNavBtns.forEach(btn => btn.classList.remove('active'));
                const targetBtn = document.querySelector(`[data-target="${jutsuNames[index]}"]`);
                if (targetBtn) {
                    targetBtn.classList.add('active');
                }
            }
        }
    });
    
    console.log('忍术卷轴页面功能已加载！');
});