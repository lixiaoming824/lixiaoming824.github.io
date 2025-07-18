// 忍者列传页面特定功能
document.addEventListener('DOMContentLoaded', function() {
    
    // 阵营卡片交互
    const factionCards = document.querySelectorAll('.faction-card');
    
    factionCards.forEach(card => {
        card.addEventListener('click', function() {
            const factionType = this.dataset.faction;
            showFactionDetails(factionType);
        });
        
        // 鼠标悬停时显示成员预览
        card.addEventListener('mouseenter', function() {
            const memberPreviews = this.querySelectorAll('.member-preview img');
            memberPreviews.forEach((img, index) => {
                setTimeout(() => {
                    img.style.transform = 'scale(1.2) translateZ(0)';
                    img.style.zIndex = 10 + index;
                }, index * 100);
            });
        });
        
        card.addEventListener('mouseleave', function() {
            const memberPreviews = this.querySelectorAll('.member-preview img');
            memberPreviews.forEach(img => {
                img.style.transform = 'scale(1) translateZ(0)';
                img.style.zIndex = 1;
            });
        });
    });
    
    // 显示阵营详情
    function showFactionDetails(factionType) {
        const factionData = {
            konoha: {
                name: '木叶隐村',
                description: '火之国的忍者村，由千手柱间和宇智波斑共同建立',
                members: [
                    { name: '漩涡鸣人', role: '七代火影', image: 'naruto.jpg' },
                    { name: '宇智波佐助', role: '鸣人的宿敌', image: 'sasuke.jpg' },
                    { name: '春野樱', role: '医疗忍者', image: 'sakura.jpg' },
                    { name: '旗木卡卡西', role: '六代火影', image: 'kakashi.jpg' }
                ]
            },
            akatsuki: {
                name: '晓组织',
                description: '由长门领导的叛忍组织，目标是收集所有尾兽',
                members: [
                    { name: '佩恩', role: '首领', image: 'pain.jpg' },
                    { name: '宇智波鼬', role: '间谍', image: 'itachi.jpg' },
                    { name: '干柿鬼鲛', role: '忍刀七人众', image: 'kisame.jpg' },
                    { name: '迪达拉', role: '爆遁使用者', image: 'deidara.jpg' }
                ]
            }
        };
        
        const faction = factionData[factionType];
        if (faction) {
            showModal(faction);
        }
    }
    
    // 显示模态框
    function showModal(faction) {
        // 创建模态框HTML
        const modalHTML = `
            <div class="modal-overlay" id="factionModal">
                <div class="modal-content">
                    <div class="modal-header">
                        <h2>${faction.name}</h2>
                        <button class="modal-close">&times;</button>
                    </div>
                    <div class="modal-body">
                        <p>${faction.description}</p>
                        <div class="faction-members-grid">
                            ${faction.members.map(member => `
                                <div class="member-card">
                                    <img src="images/${member.image}" alt="${member.name}">
                                    <h4>${member.name}</h4>
                                    <p>${member.role}</p>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                </div>
            </div>
        `;
        
        // 添加到页面
        document.body.insertAdjacentHTML('beforeend', modalHTML);
        
        // 添加关闭事件
        const modal = document.getElementById('factionModal');
        const closeBtn = modal.querySelector('.modal-close');
        
        closeBtn.addEventListener('click', closeModal);
        modal.addEventListener('click', function(e) {
            if (e.target === modal) {
                closeModal();
            }
        });
        
        // 显示模态框
        setTimeout(() => {
            modal.classList.add('show');
        }, 10);
    }
    
    // 关闭模态框
    function closeModal() {
        const modal = document.getElementById('factionModal');
        if (modal) {
            modal.classList.remove('show');
            setTimeout(() => {
                modal.remove();
            }, 300);
        }
    }
    
    // 人物关系图谱交互
    const characterNodes = document.querySelectorAll('.character-node');
    
    characterNodes.forEach(node => {
        node.addEventListener('click', function() {
            const characterName = this.dataset.character;
            const relation = this.dataset.relation;
            
            // 高亮相关连线
            highlightRelationships(characterName, relation);
            
            // 显示角色信息
            showCharacterInfo(characterName);
        });
        
        node.addEventListener('mouseenter', function() {
            const relation = this.dataset.relation;
            if (relation) {
                // 显示关系线
                showRelationLine(this, relation);
            }
        });
        
        node.addEventListener('mouseleave', function() {
            // 隐藏关系线
            hideRelationLines();
        });
    });
    
    // 高亮关系
    function highlightRelationships(characterName, relation) {
        // 重置所有节点
        characterNodes.forEach(node => {
            node.classList.remove('highlighted', 'connected');
        });
        
        // 高亮当前角色
        const currentNode = document.querySelector(`[data-character="${characterName}"]`);
        if (currentNode) {
            currentNode.classList.add('highlighted');
        }
        
        // 高亮相关角色
        const relatedNodes = document.querySelectorAll(`[data-relation="${relation}"]`);
        relatedNodes.forEach(node => {
            node.classList.add('connected');
        });
    }
    
    // 显示关系线
    function showRelationLine(node, relation) {
        const centerNode = document.querySelector('.center-node');
        if (centerNode && node !== centerNode) {
            const line = createRelationLine(centerNode, node, relation);
            document.querySelector('.relationship-network').appendChild(line);
        }
    }
    
    // 创建关系线
    function createRelationLine(node1, node2, relation) {
        const line = document.createElement('div');
        line.className = `relation-line ${relation}`;
        
        const rect1 = node1.getBoundingClientRect();
        const rect2 = node2.getBoundingClientRect();
        const container = document.querySelector('.relationship-network').getBoundingClientRect();
        
        const x1 = rect1.left + rect1.width / 2 - container.left;
        const y1 = rect1.top + rect1.height / 2 - container.top;
        const x2 = rect2.left + rect2.width / 2 - container.left;
        const y2 = rect2.top + rect2.height / 2 - container.top;
        
        const length = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
        const angle = Math.atan2(y2 - y1, x2 - x1) * 180 / Math.PI;
        
        line.style.position = 'absolute';
        line.style.left = x1 + 'px';
        line.style.top = y1 + 'px';
        line.style.width = length + 'px';
        line.style.height = '3px';
        line.style.transform = `rotate(${angle}deg)`;
        line.style.transformOrigin = '0 50%';
        line.style.zIndex = '1';
        
        return line;
    }
    
    // 隐藏关系线
    function hideRelationLines() {
        const lines = document.querySelectorAll('.relation-line');
        lines.forEach(line => line.remove());
    }
    
    // 显示角色信息
    function showCharacterInfo(characterName) {
        const characterData = {
            naruto: {
                name: '漩涡鸣人',
                title: '七代火影',
                description: '木叶隐村的英雄，九尾人柱力',
                abilities: ['九尾查克拉', '仙人模式', '螺旋丸'],
                quote: '我绝对不会放弃！这就是我的忍道！'
            },
            sasuke: {
                name: '宇智波佐助',
                title: '最后的宇智波',
                description: '复仇者转变为守护者',
                abilities: ['写轮眼', '轮回眼', '千鸟'],
                quote: '我要斩断所有的羁绊！'
            }
        };
        
        const character = characterData[characterName];
        if (character) {
            showCharacterModal(character);
        }
    }
    
    // 显示角色模态框
    function showCharacterModal(character) {
        const modalHTML = `
            <div class="modal-overlay character-modal" id="characterModal">
                <div class="modal-content">
                    <div class="modal-header">
                        <h2>${character.name}</h2>
                        <span class="character-title">${character.title}</span>
                        <button class="modal-close">&times;</button>
                    </div>
                    <div class="modal-body">
                        <p>${character.description}</p>
                        <div class="character-quote">
                            <p>"${character.quote}"</p>
                        </div>
                        <div class="character-abilities">
                            <h4>主要能力：</h4>
                            <div class="abilities-list">
                                ${character.abilities.map(ability => `
                                    <span class="ability-tag">${ability}</span>
                                `).join('')}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;
        
        document.body.insertAdjacentHTML('beforeend', modalHTML);
        
        const modal = document.getElementById('characterModal');
        const closeBtn = modal.querySelector('.modal-close');
        
        closeBtn.addEventListener('click', () => {
            modal.classList.remove('show');
            setTimeout(() => modal.remove(), 300);
        });
        
        modal.addEventListener('click', function(e) {
            if (e.target === modal) {
                modal.classList.remove('show');
                setTimeout(() => modal.remove(), 300);
            }
        });
        
        setTimeout(() => modal.classList.add('show'), 10);
    }
    
    // 焦点人物切换
    const characterTabs = document.querySelectorAll('.character-tab');
    
    characterTabs.forEach(tab => {
        tab.addEventListener('click', function() {
            const targetCharacter = this.dataset.character;
            switchFeaturedCharacter(targetCharacter);
        });
    });
    
    // 切换焦点人物
    function switchFeaturedCharacter(characterName) {
        // 这里可以添加切换焦点人物的逻辑
        console.log(`切换到角色：${characterName}`);
    }
    
    // 搜索功能
    const searchInput = document.querySelector('.character-search');
    
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            filterCharacters(searchTerm);
        });
    }
    
    // 过滤角色
    function filterCharacters(searchTerm) {
        const characterElements = document.querySelectorAll('.character-item');
        
        characterElements.forEach(element => {
            const characterName = element.dataset.name.toLowerCase();
            
            if (characterName.includes(searchTerm)) {
                element.style.display = 'block';
            } else {
                element.style.display = 'none';
            }
        });
    }
    
    console.log('忍者列传页面功能已加载！');
});