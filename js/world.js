// 世界探秘页面特定功能
document.addEventListener('DOMContentLoaded', function() {
    
    // 地图标记交互
    const locationMarkers = document.querySelectorAll('.location-marker');
    
    locationMarkers.forEach(marker => {
        marker.addEventListener('click', function() {
            const location = this.dataset.location;
            showLocationDetails(location);
        });
        
        // 鼠标悬停时的动画效果
        marker.addEventListener('mouseenter', function() {
            const icon = this.querySelector('.marker-icon');
            if (icon) {
                icon.style.transform = 'scale(1.3) rotate(10deg)';
                icon.style.transition = 'transform 0.3s ease';
            }
        });
        
        marker.addEventListener('mouseleave', function() {
            const icon = this.querySelector('.marker-icon');
            if (icon) {
                icon.style.transform = 'scale(1) rotate(0deg)';
            }
        });
    });
    
    // 显示地点详情
    function showLocationDetails(location) {
        const locationData = {
            fire: {
                name: '火之国',
                village: '木叶隐村',
                description: '五大国中最繁荣的国家，拥有肥沃的土地和强大的军事力量。',
                features: ['木叶隐村', '火之寺', '短册街', '终结之谷'],
                leader: '火之国大名',
                kage: '火影 - 漩涡鸣人',
                specialty: '火遁忍术',
                image: 'fire-country.jpg'
            },
            wind: {
                name: '风之国',
                village: '砂隐村',
                description: '被沙漠包围的国家，资源相对匮乏，但忍者实力强大。',
                features: ['砂隐村', '楼兰遗迹', '风之谷'],
                leader: '风之国大名',
                kage: '风影 - 我爱罗',
                specialty: '风遁忍术、傀儡术',
                image: 'wind-country.jpg'
            },
            water: {
                name: '水之国',
                village: '雾隐村',
                description: '四面环海的岛国，常年被浓雾包围。',
                features: ['雾隐村', '血雾之里', '海之桥'],
                leader: '水之国大名',
                kage: '水影 - 照美冥',
                specialty: '水遁忍术、血继限界',
                image: 'water-country.jpg'
            },
            earth: {
                name: '土之国',
                village: '岩隐村',
                description: '多山的国家，地势险要，以坚固的防御著称。',
                features: ['岩隐村', '土之峡谷', '石之森林'],
                leader: '土之国大名',
                kage: '土影 - 大野木',
                specialty: '土遁忍术',
                image: 'earth-country.jpg'
            },
            lightning: {
                name: '雷之国',
                village: '云隐村',
                description: '山峰险峻的国家，常年雷电交加。',
                features: ['云隐村', '雷之高原', '云之峰'],
                leader: '雷之国大名',
                kage: '雷影 - 艾',
                specialty: '雷遁忍术、体术',
                image: 'lightning-country.jpg'
            }
        };
        
        const locationInfo = locationData[location];
        if (locationInfo) {
            showLocationModal(locationInfo);
        }
    }
    
    // 显示地点模态框
    function showLocationModal(location) {
        const modalHTML = `
            <div class="modal-overlay location-modal" id="locationModal">
                <div class="modal-content">
                    <div class="modal-header">
                        <h2>${location.name}</h2>
                        <button class="modal-close">&times;</button>
                    </div>
                    <div class="modal-body">
                        <div class="location-image">
                            <img src="images/${location.image}" alt="${location.name}">
                        </div>
                        <div class="location-info">
                            <p>${location.description}</p>
                            <div class="location-details">
                                <div class="detail-item">
                                    <strong>忍者村：</strong>
                                    <span>${location.village}</span>
                                </div>
                                <div class="detail-item">
                                    <strong>国家领导：</strong>
                                    <span>${location.leader}</span>
                                </div>
                                <div class="detail-item">
                                    <strong>影：</strong>
                                    <span>${location.kage}</span>
                                </div>
                                <div class="detail-item">
                                    <strong>特色忍术：</strong>
                                    <span>${location.specialty}</span>
                                </div>
                            </div>
                            <div class="location-features">
                                <h4>主要地点：</h4>
                                <div class="features-list">
                                    ${location.features.map(feature => `
                                        <span class="feature-tag">${feature}</span>
                                    `).join('')}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;
        
        document.body.insertAdjacentHTML('beforeend', modalHTML);
        
        const modal = document.getElementById('locationModal');
        const closeBtn = modal.querySelector('.modal-close');
        
        closeBtn.addEventListener('click', closeLocationModal);
        modal.addEventListener('click', function(e) {
            if (e.target === modal) {
                closeLocationModal();
            }
        });
        
        setTimeout(() => modal.classList.add('show'), 10);
    }
    
    // 关闭地点模态框
    function closeLocationModal() {
        const modal = document.getElementById('locationModal');
        if (modal) {
            modal.classList.remove('show');
            setTimeout(() => modal.remove(), 300);
        }
    }
    
    // 历史时间线交互
    const timelineItems = document.querySelectorAll('.timeline-item');
    
    timelineItems.forEach(item => {
        item.addEventListener('click', function() {
            const year = this.dataset.year;
            showHistoryDetails(year, this);
        });
        
        // 滚动到视图中时添加动画
        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate');
                }
            });
        }, { threshold: 0.3 });
        
        observer.observe(item);
    });
    
    // 显示历史详情
    function showHistoryDetails(year, element) {
        // 移除其他活动状态
        timelineItems.forEach(item => {
            item.classList.remove('active');
        });
        
        // 添加当前活动状态
        element.classList.add('active');
        
        // 显示详细信息
        const detailsPanel = element.querySelector('.timeline-details');
        if (detailsPanel) {
            detailsPanel.style.display = 'block';
            detailsPanel.style.animation = 'fadeInUp 0.5s ease';
        }
    }
    
    // 概念卡片交互
    const conceptCards = document.querySelectorAll('.concept-card');
    
    conceptCards.forEach(card => {
        card.addEventListener('click', function() {
            const concept = this.dataset.concept;
            showConceptDetails(concept);
        });
        
        // 卡片翻转效果
        card.addEventListener('mouseenter', function() {
            const details = this.querySelector('.concept-details');
            if (details) {
                details.style.transform = 'rotateY(0deg)';
                details.style.opacity = '1';
            }
        });
        
        card.addEventListener('mouseleave', function() {
            const details = this.querySelector('.concept-details');
            if (details) {
                details.style.transform = 'rotateY(90deg)';
                details.style.opacity = '0';
            }
        });
    });
    
    // 显示概念详情
    function showConceptDetails(concept) {
        const conceptData = {
            chakra: {
                name: '查克拉',
                description: '忍者施展忍术的基础能量',
                details: '查克拉是由身体能量和精神能量混合而成的超自然能量...',
                properties: ['身体能量', '精神能量', '自然能量'],
                types: ['火', '水', '土', '风', '雷']
            },
            ninja_ranks: {
                name: '忍者等级',
                description: '忍者按实力划分的等级制度',
                details: '忍者等级制度确保了任务分配的合理性...',
                ranks: ['下忍', '中忍', '上忍', '影']
            }
        };
        
        const conceptInfo = conceptData[concept];
        if (conceptInfo) {
            showConceptModal(conceptInfo);
        }
    }
    
    // 显示概念模态框
    function showConceptModal(concept) {
        const modalHTML = `
            <div class="modal-overlay concept-modal" id="conceptModal">
                <div class="modal-content">
                    <div class="modal-header">
                        <h2>${concept.name}</h2>
                        <button class="modal-close">&times;</button>
                    </div>
                    <div class="modal-body">
                        <p>${concept.description}</p>
                        <div class="concept-details-full">
                            <p>${concept.details}</p>
                            ${concept.properties ? `
                                <div class="concept-properties">
                                    <h4>组成要素：</h4>
                                    <ul>
                                        ${concept.properties.map(prop => `<li>${prop}</li>`).join('')}
                                    </ul>
                                </div>
                            ` : ''}
                            ${concept.types ? `
                                <div class="concept-types">
                                    <h4>属性类型：</h4>
                                    <div class="types-grid">
                                        ${concept.types.map(type => `
                                            <span class="type-tag">${type}</span>
                                        `).join('')}
                                    </div>
                                </div>
                            ` : ''}
                            ${concept.ranks ? `
                                <div class="concept-ranks">
                                    <h4>等级划分：</h4>
                                    <div class="ranks-grid">
                                        ${concept.ranks.map(rank => `
                                            <span class="rank-tag">${rank}</span>
                                        `).join('')}
                                    </div>
                                </div>
                            ` : ''}
                        </div>
                    </div>
                </div>
            </div>
        `;
        
        document.body.insertAdjacentHTML('beforeend', modalHTML);
        
        const modal = document.getElementById('conceptModal');
        const closeBtn = modal.querySelector('.modal-close');
        
        closeBtn.addEventListener('click', closeConceptModal);
        modal.addEventListener('click', function(e) {
            if (e.target === modal) {
                closeConceptModal();
            }
        });
        
        setTimeout(() => modal.classList.add('show'), 10);
    }
    
    // 关闭概念模态框
    function closeConceptModal() {
        const modal = document.getElementById('conceptModal');
        if (modal) {
            modal.classList.remove('show');
            setTimeout(() => modal.remove(), 300);
        }
    }
    
    // 地图缩放功能
    const worldMap = document.querySelector('.world-map');
    let isZoomed = false;
    
    if (worldMap) {
        worldMap.addEventListener('dblclick', function(e) {
            if (!isZoomed) {
                // 放大地图
                const rect = this.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                
                this.style.transform = `scale(2) translate(${-x/2}px, ${-y/2}px)`;
                this.style.transformOrigin = `${x}px ${y}px`;
                isZoomed = true;
            } else {
                // 还原地图
                this.style.transform = 'scale(1) translate(0, 0)';
                isZoomed = false;
            }
        });
    }
    
    // 键盘控制
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            closeLocationModal();
            closeConceptModal();
        }
    });
    
    // 地图图例交互
    const legendItems = document.querySelectorAll('.legend-item');
    
    legendItems.forEach(item => {
        item.addEventListener('click', function() {
            const colorClass = this.querySelector('.legend-color').classList[1];
            highlightCountry(colorClass);
        });
    });
    
    // 高亮国家
    function highlightCountry(countryType) {
        const markers = document.querySelectorAll('.location-marker');
        
        markers.forEach(marker => {
            if (marker.classList.contains(countryType + '-country')) {
                marker.classList.add('highlighted');
                setTimeout(() => {
                    marker.classList.remove('highlighted');
                }, 2000);
            }
        });
    }
    
    console.log('世界探秘页面功能已加载！');
});