/**
 * ═══════════════════════════════════════════════════════════════════════════════
 * DENSITY FIELD DYNAMICS - IMMERSIVE WEB EXPERIENCE
 * Gravity is Light | A Journey Through Revolutionary Physics
 * ═══════════════════════════════════════════════════════════════════════════════
 */

// ─────────────────────────────────────────────────────────────────────────────
// GLOBAL STATE
// ─────────────────────────────────────────────────────────────────────────────
const state = {
    scrollProgress: 0,
    mouseX: 0,
    mouseY: 0,
    isLoaded: false,
    activeGalaxy: 'ngc3198'
};

// Galaxy rotation curve data (simplified SPARC-like data)
const galaxyData = {
    ngc3198: {
        name: 'NGC 3198',
        radii: [0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        observed: [80, 120, 148, 152, 150, 149, 150, 148, 147, 146, 145],
        newton: [80, 120, 100, 82, 71, 63, 58, 54, 50, 47, 45]
    },
    ngc2403: {
        name: 'NGC 2403',
        radii: [0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        observed: [60, 95, 120, 128, 130, 132, 130, 128, 127, 126, 125],
        newton: [60, 95, 80, 65, 56, 50, 46, 43, 40, 38, 36]
    },
    ugc128: {
        name: 'UGC 128',
        radii: [0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        observed: [40, 70, 100, 115, 125, 130, 132, 133, 132, 131, 130],
        newton: [40, 70, 58, 48, 41, 37, 34, 31, 29, 27, 26]
    }
};

// ─────────────────────────────────────────────────────────────────────────────
// THREE.JS COSMIC BACKGROUND
// ─────────────────────────────────────────────────────────────────────────────
class CosmicBackground {
    constructor() {
        this.container = document.getElementById('canvas-container');
        this.scene = new THREE.Scene();
        this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
        this.particles = null;
        this.nebula = null;
        this.clock = new THREE.Clock();
        
        this.init();
    }
    
    init() {
        // Renderer setup
        this.renderer.setSize(window.innerWidth, window.innerHeight);
        this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        this.container.appendChild(this.renderer.domElement);
        
        // Camera position
        this.camera.position.z = 30;
        
        // Create elements
        this.createStarField();
        this.createNebula();
        this.createGalaxySpiral();
        
        // Events
        window.addEventListener('resize', () => this.onResize());
        
        // Start animation
        this.animate();
    }
    
    createStarField() {
        const geometry = new THREE.BufferGeometry();
        const count = 5000;
        const positions = new Float32Array(count * 3);
        const colors = new Float32Array(count * 3);
        const sizes = new Float32Array(count);
        
        for (let i = 0; i < count; i++) {
            const i3 = i * 3;
            
            // Position - spread in a large sphere
            const radius = 50 + Math.random() * 150;
            const theta = Math.random() * Math.PI * 2;
            const phi = Math.acos(2 * Math.random() - 1);
            
            positions[i3] = radius * Math.sin(phi) * Math.cos(theta);
            positions[i3 + 1] = radius * Math.sin(phi) * Math.sin(theta);
            positions[i3 + 2] = radius * Math.cos(phi);
            
            // Color - mix of white, gold, and purple
            const colorChoice = Math.random();
            if (colorChoice < 0.7) {
                // White stars
                colors[i3] = 1;
                colors[i3 + 1] = 1;
                colors[i3 + 2] = 1;
            } else if (colorChoice < 0.85) {
                // Gold stars
                colors[i3] = 0.96;
                colors[i3 + 1] = 0.63;
                colors[i3 + 2] = 0.13;
            } else {
                // Purple stars
                colors[i3] = 0.61;
                colors[i3 + 1] = 0.35;
                colors[i3 + 2] = 0.71;
            }
            
            // Varied sizes
            sizes[i] = Math.random() * 2 + 0.5;
        }
        
        geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
        geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));
        geometry.setAttribute('size', new THREE.BufferAttribute(sizes, 1));
        
        // Custom shader material for better stars
        const material = new THREE.PointsMaterial({
            size: 0.5,
            vertexColors: true,
            transparent: true,
            opacity: 0.8,
            sizeAttenuation: true
        });
        
        this.particles = new THREE.Points(geometry, material);
        this.scene.add(this.particles);
    }
    
    createNebula() {
        // Create multiple nebula planes
        const nebulaGroup = new THREE.Group();
        
        for (let i = 0; i < 3; i++) {
            const geometry = new THREE.PlaneGeometry(100, 100);
            
            // Gradient texture for nebula effect
            const canvas = document.createElement('canvas');
            canvas.width = 256;
            canvas.height = 256;
            const ctx = canvas.getContext('2d');
            
            const gradient = ctx.createRadialGradient(128, 128, 0, 128, 128, 128);
            gradient.addColorStop(0, 'rgba(107, 45, 123, 0.3)');
            gradient.addColorStop(0.5, 'rgba(244, 160, 32, 0.1)');
            gradient.addColorStop(1, 'rgba(10, 10, 26, 0)');
            
            ctx.fillStyle = gradient;
            ctx.fillRect(0, 0, 256, 256);
            
            const texture = new THREE.CanvasTexture(canvas);
            
            const material = new THREE.MeshBasicMaterial({
                map: texture,
                transparent: true,
                blending: THREE.AdditiveBlending,
                side: THREE.DoubleSide
            });
            
            const mesh = new THREE.Mesh(geometry, material);
            mesh.position.set(
                (Math.random() - 0.5) * 50,
                (Math.random() - 0.5) * 50,
                -50 - i * 20
            );
            mesh.rotation.z = Math.random() * Math.PI;
            
            nebulaGroup.add(mesh);
        }
        
        this.nebula = nebulaGroup;
        this.scene.add(this.nebula);
    }
    
    createGalaxySpiral() {
        const geometry = new THREE.BufferGeometry();
        const count = 3000;
        const positions = new Float32Array(count * 3);
        const colors = new Float32Array(count * 3);
        
        for (let i = 0; i < count; i++) {
            const i3 = i * 3;
            
            // Spiral arms
            const angle = i * 0.02;
            const radius = 0.5 + i * 0.008;
            const armOffset = (i % 2) * Math.PI;
            const spread = (Math.random() - 0.5) * 2;
            
            positions[i3] = Math.cos(angle + armOffset) * radius + spread;
            positions[i3 + 1] = Math.sin(angle + armOffset) * radius + spread;
            positions[i3 + 2] = (Math.random() - 0.5) * 2;
            
            // Color gradient from center (gold) to edge (purple)
            const t = i / count;
            colors[i3] = 0.96 - t * 0.35;
            colors[i3 + 1] = 0.63 - t * 0.28;
            colors[i3 + 2] = 0.13 + t * 0.58;
        }
        
        geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
        geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));
        
        const material = new THREE.PointsMaterial({
            size: 0.1,
            vertexColors: true,
            transparent: true,
            opacity: 0.6
        });
        
        this.galaxySpiral = new THREE.Points(geometry, material);
        this.galaxySpiral.position.set(30, -20, -40);
        this.galaxySpiral.rotation.x = Math.PI * 0.3;
        this.scene.add(this.galaxySpiral);
    }
    
    onResize() {
        this.camera.aspect = window.innerWidth / window.innerHeight;
        this.camera.updateProjectionMatrix();
        this.renderer.setSize(window.innerWidth, window.innerHeight);
    }
    
    animate() {
        requestAnimationFrame(() => this.animate());
        
        const elapsed = this.clock.getElapsedTime();
        
        // Rotate star field slowly
        if (this.particles) {
            this.particles.rotation.y = elapsed * 0.02;
            this.particles.rotation.x = Math.sin(elapsed * 0.01) * 0.1;
        }
        
        // Pulse nebula
        if (this.nebula) {
            this.nebula.children.forEach((mesh, i) => {
                mesh.rotation.z += 0.0005 * (i + 1);
                mesh.material.opacity = 0.3 + Math.sin(elapsed + i) * 0.1;
            });
        }
        
        // Rotate galaxy spiral
        if (this.galaxySpiral) {
            this.galaxySpiral.rotation.z = elapsed * 0.1;
        }
        
        // Camera subtle movement based on scroll
        this.camera.position.y = -state.scrollProgress * 20;
        this.camera.lookAt(0, -state.scrollProgress * 15, 0);
        
        this.renderer.render(this.scene, this.camera);
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// GSAP SCROLL ANIMATIONS
// ─────────────────────────────────────────────────────────────────────────────
function initScrollAnimations() {
    gsap.registerPlugin(ScrollTrigger);
    
    // Progress bar
    gsap.to('#progress-bar', {
        width: '100%',
        ease: 'none',
        scrollTrigger: {
            trigger: 'body',
            start: 'top top',
            end: 'bottom bottom',
            scrub: 0.3
        }
    });
    
    // Update state scroll progress
    ScrollTrigger.create({
        trigger: 'body',
        start: 'top top',
        end: 'bottom bottom',
        onUpdate: (self) => {
            state.scrollProgress = self.progress;
        }
    });
    
    // Show nav after scrolling past hero
    ScrollTrigger.create({
        trigger: '#problem',
        start: 'top 80%',
        onEnter: () => document.getElementById('nav').classList.add('visible'),
        onLeaveBack: () => document.getElementById('nav').classList.remove('visible')
    });
    
    // Hide scroll indicator
    ScrollTrigger.create({
        trigger: '#hero',
        start: 'bottom 80%',
        onEnter: () => {
            gsap.to('#scroll-indicator', { opacity: 0, duration: 0.5 });
        },
        onLeaveBack: () => {
            gsap.to('#scroll-indicator', { opacity: 1, duration: 0.5 });
        }
    });
    
    // Fade in content blocks
    gsap.utils.toArray('.fade-in').forEach(block => {
        ScrollTrigger.create({
            trigger: block,
            start: 'top 85%',
            onEnter: () => block.classList.add('visible'),
            once: true
        });
    });
    
    // Timeline items
    gsap.utils.toArray('.timeline-item').forEach((item, i) => {
        ScrollTrigger.create({
            trigger: item,
            start: 'top 80%',
            onEnter: () => {
                setTimeout(() => item.classList.add('visible'), i * 200);
            },
            once: true
        });
    });
    
    // Pie chart legend items
    gsap.utils.toArray('.legend-item').forEach((item, i) => {
        ScrollTrigger.create({
            trigger: '#cosmic-pie',
            start: 'top 60%',
            onEnter: () => {
                setTimeout(() => item.classList.add('visible'), i * 400);
            },
            once: true
        });
    });
    
    // Invisible counter animation
    ScrollTrigger.create({
        trigger: '.dramatic-stat',
        start: 'top 80%',
        onEnter: () => animateCounter('invisible-counter', 0, 95, 2000),
        once: true
    });
    
    // Test cards
    gsap.utils.toArray('.test-card').forEach((card, i) => {
        ScrollTrigger.create({
            trigger: card,
            start: 'top 85%',
            onEnter: () => {
                setTimeout(() => card.classList.add('visible'), i * 150);
            },
            once: true
        });
    });
    
    // Falsification tests
    gsap.utils.toArray('.falsify-test').forEach((test, i) => {
        ScrollTrigger.create({
            trigger: test,
            start: 'top 85%',
            onEnter: () => {
                setTimeout(() => test.classList.add('visible'), i * 200);
            },
            once: true
        });
    });
    
    // Chapter headers parallax
    gsap.utils.toArray('.chapter-header').forEach(header => {
        gsap.to(header, {
            y: -50,
            ease: 'none',
            scrollTrigger: {
                trigger: header,
                start: 'top bottom',
                end: 'bottom top',
                scrub: 1
            }
        });
    });
}

// ─────────────────────────────────────────────────────────────────────────────
// COUNTER ANIMATION
// ─────────────────────────────────────────────────────────────────────────────
function animateCounter(elementId, start, end, duration) {
    const element = document.getElementById(elementId);
    if (!element) return;
    
    const startTime = performance.now();
    
    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        
        // Easing function
        const eased = 1 - Math.pow(1 - progress, 3);
        const current = Math.floor(start + (end - start) * eased);
        
        element.textContent = current;
        
        if (progress < 1) {
            requestAnimationFrame(update);
        }
    }
    
    requestAnimationFrame(update);
}

// ─────────────────────────────────────────────────────────────────────────────
// GALAXY ROTATION DEMO
// ─────────────────────────────────────────────────────────────────────────────
class GalaxyDemo {
    constructor() {
        this.canvas = document.getElementById('galaxy-canvas');
        this.velocityCanvas = document.getElementById('velocity-canvas');
        if (!this.canvas || !this.velocityCanvas) return;
        
        this.ctx = this.canvas.getContext('2d');
        this.velCtx = this.velocityCanvas.getContext('2d');
        
        this.starRadius = 150;
        this.starAngle = Math.PI / 4;
        this.isDragging = false;
        this.centerX = this.canvas.width / 2;
        this.centerY = this.canvas.height / 2;
        
        this.init();
    }
    
    init() {
        this.canvas.addEventListener('mousedown', (e) => this.onMouseDown(e));
        this.canvas.addEventListener('mousemove', (e) => this.onMouseMove(e));
        this.canvas.addEventListener('mouseup', () => this.onMouseUp());
        this.canvas.addEventListener('mouseleave', () => this.onMouseUp());
        
        // Touch events
        this.canvas.addEventListener('touchstart', (e) => this.onTouchStart(e));
        this.canvas.addEventListener('touchmove', (e) => this.onTouchMove(e));
        this.canvas.addEventListener('touchend', () => this.onMouseUp());
        
        this.draw();
    }
    
    onMouseDown(e) {
        const rect = this.canvas.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        // Check if clicking near the star
        const starX = this.centerX + Math.cos(this.starAngle) * this.starRadius;
        const starY = this.centerY + Math.sin(this.starAngle) * this.starRadius;
        
        const dist = Math.sqrt((x - starX) ** 2 + (y - starY) ** 2);
        if (dist < 30) {
            this.isDragging = true;
        }
    }
    
    onMouseMove(e) {
        if (!this.isDragging) return;
        
        const rect = this.canvas.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        // Calculate new angle and radius
        const dx = x - this.centerX;
        const dy = y - this.centerY;
        
        this.starAngle = Math.atan2(dy, dx);
        this.starRadius = Math.max(50, Math.min(200, Math.sqrt(dx * dx + dy * dy)));
        
        this.draw();
    }
    
    onTouchStart(e) {
        e.preventDefault();
        const touch = e.touches[0];
        this.onMouseDown({ clientX: touch.clientX, clientY: touch.clientY });
    }
    
    onTouchMove(e) {
        e.preventDefault();
        const touch = e.touches[0];
        this.onMouseMove({ clientX: touch.clientX, clientY: touch.clientY });
    }
    
    onMouseUp() {
        this.isDragging = false;
    }
    
    draw() {
        const ctx = this.ctx;
        const width = this.canvas.width;
        const height = this.canvas.height;
        
        // Clear
        ctx.fillStyle = 'rgba(10, 10, 26, 0.95)';
        ctx.fillRect(0, 0, width, height);
        
        // Draw galaxy center glow
        const gradient = ctx.createRadialGradient(
            this.centerX, this.centerY, 0,
            this.centerX, this.centerY, 80
        );
        gradient.addColorStop(0, 'rgba(244, 160, 32, 0.8)');
        gradient.addColorStop(0.5, 'rgba(244, 160, 32, 0.2)');
        gradient.addColorStop(1, 'transparent');
        
        ctx.fillStyle = gradient;
        ctx.fillRect(0, 0, width, height);
        
        // Draw spiral arms (simplified)
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.1)';
        ctx.lineWidth = 20;
        
        for (let arm = 0; arm < 2; arm++) {
            ctx.beginPath();
            for (let i = 0; i < 100; i++) {
                const angle = i * 0.1 + arm * Math.PI;
                const r = 30 + i * 1.5;
                const x = this.centerX + Math.cos(angle) * r;
                const y = this.centerY + Math.sin(angle) * r;
                
                if (i === 0) ctx.moveTo(x, y);
                else ctx.lineTo(x, y);
            }
            ctx.stroke();
        }
        
        // Draw orbit circle
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
        ctx.lineWidth = 1;
        ctx.setLineDash([5, 5]);
        ctx.beginPath();
        ctx.arc(this.centerX, this.centerY, this.starRadius, 0, Math.PI * 2);
        ctx.stroke();
        ctx.setLineDash([]);
        
        // Draw the draggable star
        const starX = this.centerX + Math.cos(this.starAngle) * this.starRadius;
        const starY = this.centerY + Math.sin(this.starAngle) * this.starRadius;
        
        // Star glow
        const starGradient = ctx.createRadialGradient(starX, starY, 0, starX, starY, 20);
        starGradient.addColorStop(0, 'rgba(255, 255, 255, 1)');
        starGradient.addColorStop(0.3, 'rgba(244, 160, 32, 0.8)');
        starGradient.addColorStop(1, 'transparent');
        
        ctx.fillStyle = starGradient;
        ctx.beginPath();
        ctx.arc(starX, starY, 20, 0, Math.PI * 2);
        ctx.fill();
        
        // Star core
        ctx.fillStyle = '#fff';
        ctx.beginPath();
        ctx.arc(starX, starY, 6, 0, Math.PI * 2);
        ctx.fill();
        
        // Velocity arrow
        const velocityScale = this.getObservedVelocity() / 150 * 40;
        const perpAngle = this.starAngle + Math.PI / 2;
        
        ctx.strokeStyle = '#f4a020';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(starX, starY);
        ctx.lineTo(
            starX + Math.cos(perpAngle) * velocityScale,
            starY + Math.sin(perpAngle) * velocityScale
        );
        ctx.stroke();
        
        // Arrowhead
        const arrowX = starX + Math.cos(perpAngle) * velocityScale;
        const arrowY = starY + Math.sin(perpAngle) * velocityScale;
        ctx.fillStyle = '#f4a020';
        ctx.beginPath();
        ctx.moveTo(arrowX, arrowY);
        ctx.lineTo(
            arrowX - Math.cos(perpAngle - 0.3) * 10,
            arrowY - Math.sin(perpAngle - 0.3) * 10
        );
        ctx.lineTo(
            arrowX - Math.cos(perpAngle + 0.3) * 10,
            arrowY - Math.sin(perpAngle + 0.3) * 10
        );
        ctx.closePath();
        ctx.fill();
        
        // Draw velocity chart
        this.drawVelocityChart();
    }
    
    getObservedVelocity() {
        // Flat rotation curve (what we actually see)
        const normalizedRadius = this.starRadius / 200;
        return 80 + 70 * (1 - Math.exp(-normalizedRadius * 3));
    }
    
    getNewtonVelocity() {
        // Keplerian decline (what Newton predicts)
        const normalizedRadius = this.starRadius / 200;
        if (normalizedRadius < 0.3) {
            return 80 + 70 * normalizedRadius / 0.3;
        }
        return 150 * Math.sqrt(0.3 / normalizedRadius);
    }
    
    drawVelocityChart() {
        const ctx = this.velCtx;
        const width = this.velocityCanvas.width;
        const height = this.velocityCanvas.height;
        
        // Clear
        ctx.fillStyle = 'rgba(10, 10, 26, 0.95)';
        ctx.fillRect(0, 0, width, height);
        
        const padding = 40;
        const chartWidth = width - padding * 2;
        const chartHeight = height - padding * 2;
        
        // Axes
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(padding, padding);
        ctx.lineTo(padding, height - padding);
        ctx.lineTo(width - padding, height - padding);
        ctx.stroke();
        
        // Labels
        ctx.fillStyle = 'rgba(255, 255, 255, 0.5)';
        ctx.font = '12px Inter';
        ctx.fillText('Velocity', padding, padding - 10);
        ctx.fillText('Distance from center', width - padding - 80, height - padding + 25);
        
        // Newton prediction curve (red, declining)
        ctx.strokeStyle = 'rgba(231, 76, 60, 0.6)';
        ctx.lineWidth = 2;
        ctx.beginPath();
        for (let i = 0; i <= 100; i++) {
            const x = padding + (i / 100) * chartWidth;
            const r = (i / 100);
            let v;
            if (r < 0.3) {
                v = r / 0.3;
            } else {
                v = Math.sqrt(0.3 / r);
            }
            const y = height - padding - v * chartHeight * 0.9;
            
            if (i === 0) ctx.moveTo(x, y);
            else ctx.lineTo(x, y);
        }
        ctx.stroke();
        
        // Observed curve (gold, flat)
        ctx.strokeStyle = '#f4a020';
        ctx.lineWidth = 2;
        ctx.beginPath();
        for (let i = 0; i <= 100; i++) {
            const x = padding + (i / 100) * chartWidth;
            const r = (i / 100);
            const v = 0.5 + 0.5 * (1 - Math.exp(-r * 5));
            const y = height - padding - v * chartHeight * 0.9;
            
            if (i === 0) ctx.moveTo(x, y);
            else ctx.lineTo(x, y);
        }
        ctx.stroke();
        
        // Current position marker
        const normalizedRadius = this.starRadius / 200;
        const markerX = padding + normalizedRadius * chartWidth;
        
        // Vertical line at current position
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
        ctx.setLineDash([5, 5]);
        ctx.beginPath();
        ctx.moveTo(markerX, padding);
        ctx.lineTo(markerX, height - padding);
        ctx.stroke();
        ctx.setLineDash([]);
        
        // Observed point
        const obsV = 0.5 + 0.5 * (1 - Math.exp(-normalizedRadius * 5));
        const obsY = height - padding - obsV * chartHeight * 0.9;
        
        ctx.fillStyle = '#f4a020';
        ctx.beginPath();
        ctx.arc(markerX, obsY, 6, 0, Math.PI * 2);
        ctx.fill();
        
        // Newton point
        let newV;
        if (normalizedRadius < 0.3) {
            newV = normalizedRadius / 0.3;
        } else {
            newV = Math.sqrt(0.3 / normalizedRadius);
        }
        const newY = height - padding - newV * chartHeight * 0.9;
        
        ctx.fillStyle = 'rgba(231, 76, 60, 0.8)';
        ctx.beginPath();
        ctx.arc(markerX, newY, 6, 0, Math.PI * 2);
        ctx.fill();
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// PSI FIELD VISUALIZATION
// ─────────────────────────────────────────────────────────────────────────────
class PsiFieldVisualization {
    constructor() {
        this.canvas = document.getElementById('psi-canvas');
        if (!this.canvas) return;
        
        this.ctx = this.canvas.getContext('2d');
        this.mass = 1;
        this.time = 0;
        
        this.slider = document.getElementById('mass-slider');
        this.valueDisplay = document.getElementById('mass-value');
        
        if (this.slider) {
            this.slider.addEventListener('input', (e) => {
                this.mass = parseFloat(e.target.value);
                if (this.valueDisplay) {
                    this.valueDisplay.innerHTML = `${this.mass.toFixed(1)} M<sub>⊕</sub>`;
                }
            });
        }
        
        this.animate();
    }
    
    animate() {
        this.time += 0.02;
        this.draw();
        requestAnimationFrame(() => this.animate());
    }
    
    draw() {
        const ctx = this.ctx;
        const width = this.canvas.width;
        const height = this.canvas.height;
        const centerX = width / 2;
        const centerY = height / 2;
        
        // Clear
        ctx.fillStyle = 'rgba(10, 10, 26, 0.1)';
        ctx.fillRect(0, 0, width, height);
        
        // Draw ψ field contours
        for (let r = 20; r < 250; r += 20) {
            const psi = this.mass / (r / 100);
            const intensity = Math.min(1, psi * 0.3);
            const hue = 30 + (1 - intensity) * 240; // Gold to purple
            
            ctx.strokeStyle = `hsla(${hue}, 70%, 50%, ${intensity * 0.5})`;
            ctx.lineWidth = 2;
            
            // Animated wave effect
            ctx.beginPath();
            for (let angle = 0; angle < Math.PI * 2; angle += 0.1) {
                const wave = Math.sin(angle * 6 + this.time * 2) * 3;
                const x = centerX + Math.cos(angle) * (r + wave);
                const y = centerY + Math.sin(angle) * (r + wave);
                
                if (angle === 0) ctx.moveTo(x, y);
                else ctx.lineTo(x, y);
            }
            ctx.closePath();
            ctx.stroke();
        }
        
        // Draw Earth at center
        const earthGradient = ctx.createRadialGradient(
            centerX, centerY, 0,
            centerX, centerY, 30 + this.mass * 10
        );
        earthGradient.addColorStop(0, '#4a90d9');
        earthGradient.addColorStop(0.8, '#2d5a87');
        earthGradient.addColorStop(1, 'transparent');
        
        ctx.fillStyle = earthGradient;
        ctx.beginPath();
        ctx.arc(centerX, centerY, 30 + this.mass * 10, 0, Math.PI * 2);
        ctx.fill();
        
        // ψ value label
        ctx.fillStyle = '#f4a020';
        ctx.font = '16px "JetBrains Mono"';
        ctx.textAlign = 'center';
        ctx.fillText(`ψ ∝ ${this.mass.toFixed(1)}`, centerX, height - 30);
        
        // Draw light ray being bent
        this.drawLightRay(ctx, width, height, centerX, centerY);
    }
    
    drawLightRay(ctx, width, height, centerX, centerY) {
        const rayProgress = (this.time % 4) / 4;
        const startX = 50;
        const startY = centerY - 100;
        const endX = width - 50;
        const endY = centerY + 100;
        
        // Calculate bent path
        ctx.strokeStyle = '#f4a020';
        ctx.lineWidth = 3;
        ctx.beginPath();
        
        for (let t = 0; t <= rayProgress; t += 0.02) {
            const x = startX + (endX - startX) * t;
            const baseY = startY + (endY - startY) * t;
            
            // Bending toward mass
            const distToCenter = Math.abs(x - centerX);
            const maxBend = 50 * this.mass;
            const bendAmount = maxBend * Math.exp(-(distToCenter * distToCenter) / 10000);
            const y = baseY + bendAmount;
            
            if (t === 0) ctx.moveTo(x, y);
            else ctx.lineTo(x, y);
        }
        ctx.stroke();
        
        // Photon at the end
        const photonT = rayProgress;
        const photonX = startX + (endX - startX) * photonT;
        const photonBaseY = startY + (endY - startY) * photonT;
        const distToCenter = Math.abs(photonX - centerX);
        const maxBend = 50 * this.mass;
        const bendAmount = maxBend * Math.exp(-(distToCenter * distToCenter) / 10000);
        const photonY = photonBaseY + bendAmount;
        
        const photonGradient = ctx.createRadialGradient(
            photonX, photonY, 0,
            photonX, photonY, 15
        );
        photonGradient.addColorStop(0, 'rgba(255, 255, 255, 1)');
        photonGradient.addColorStop(0.3, 'rgba(244, 160, 32, 0.8)');
        photonGradient.addColorStop(1, 'transparent');
        
        ctx.fillStyle = photonGradient;
        ctx.beginPath();
        ctx.arc(photonX, photonY, 15, 0, Math.PI * 2);
        ctx.fill();
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// THROTTLE FUNCTION VISUALIZATION
// ─────────────────────────────────────────────────────────────────────────────
class ThrottleVisualization {
    constructor() {
        this.canvas = document.getElementById('throttle-canvas');
        if (!this.canvas) return;
        
        this.ctx = this.canvas.getContext('2d');
        this.draw();
    }
    
    draw() {
        const ctx = this.ctx;
        const width = this.canvas.width;
        const height = this.canvas.height;
        
        const padding = 50;
        const chartWidth = width - padding * 2;
        const chartHeight = height - padding * 2;
        
        // Clear
        ctx.fillStyle = 'rgba(10, 10, 26, 0.95)';
        ctx.fillRect(0, 0, width, height);
        
        // Grid
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.1)';
        ctx.lineWidth = 1;
        
        for (let i = 0; i <= 4; i++) {
            const y = padding + (i / 4) * chartHeight;
            ctx.beginPath();
            ctx.moveTo(padding, y);
            ctx.lineTo(width - padding, y);
            ctx.stroke();
        }
        
        // Axes
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.5)';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(padding, padding);
        ctx.lineTo(padding, height - padding);
        ctx.lineTo(width - padding, height - padding);
        ctx.stroke();
        
        // μ(x) = x / (1 + x) curve
        ctx.strokeStyle = '#f4a020';
        ctx.lineWidth = 3;
        ctx.beginPath();
        
        for (let i = 0; i <= 100; i++) {
            const x = padding + (i / 100) * chartWidth;
            const xVal = (i / 100) * 5; // x from 0 to 5
            const mu = xVal / (1 + xVal);
            const y = height - padding - mu * chartHeight;
            
            if (i === 0) ctx.moveTo(x, y);
            else ctx.lineTo(x, y);
        }
        ctx.stroke();
        
        // μ = 1 asymptote
        ctx.strokeStyle = 'rgba(244, 160, 32, 0.3)';
        ctx.setLineDash([5, 5]);
        ctx.beginPath();
        ctx.moveTo(padding, padding);
        ctx.lineTo(width - padding, padding);
        ctx.stroke();
        ctx.setLineDash([]);
        
        // Labels
        ctx.fillStyle = '#f4a020';
        ctx.font = '14px "JetBrains Mono"';
        ctx.fillText('μ = 1', width - padding + 10, padding + 5);
        ctx.fillText('μ(x)', padding - 35, padding - 10);
        ctx.fillText('x', width - padding, height - padding + 25);
        
        // x = 1 marker (transition point)
        const x1 = padding + (1 / 5) * chartWidth;
        const y1 = height - padding - (1 / 2) * chartHeight;
        
        ctx.fillStyle = '#f4a020';
        ctx.beginPath();
        ctx.arc(x1, y1, 6, 0, Math.PI * 2);
        ctx.fill();
        
        ctx.fillStyle = 'rgba(255, 255, 255, 0.7)';
        ctx.font = '12px "JetBrains Mono"';
        ctx.fillText('x = 1', x1 - 15, height - padding + 20);
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// TOPOLOGY VISUALIZATION (Abstract 7D representation)
// ─────────────────────────────────────────────────────────────────────────────
class TopologyVisualization {
    constructor() {
        this.canvas = document.getElementById('topology-canvas');
        if (!this.canvas) return;
        
        this.ctx = this.canvas.getContext('2d');
        this.time = 0;
        
        this.animate();
    }
    
    animate() {
        this.time += 0.01;
        this.draw();
        requestAnimationFrame(() => this.animate());
    }
    
    draw() {
        const ctx = this.ctx;
        const width = this.canvas.width;
        const height = this.canvas.height;
        const centerX = width / 2;
        const centerY = height / 2;
        
        // Clear with fade trail
        ctx.fillStyle = 'rgba(10, 10, 26, 0.1)';
        ctx.fillRect(0, 0, width, height);
        
        // Draw multiple interleaved torus-like shapes (abstract CP2 x S3)
        for (let layer = 0; layer < 3; layer++) {
            const layerOffset = layer * Math.PI * 2 / 3;
            const layerSize = 100 + layer * 20;
            
            ctx.strokeStyle = `hsla(${30 + layer * 60}, 70%, 50%, 0.5)`;
            ctx.lineWidth = 2;
            
            ctx.beginPath();
            for (let i = 0; i < 200; i++) {
                const t = (i / 200) * Math.PI * 2;
                
                // Parametric equations for a complex torus-like shape
                const r1 = layerSize;
                const r2 = 40 + 20 * Math.sin(this.time + layer);
                
                // Add 7D-inspired oscillations
                const x = centerX + (r1 + r2 * Math.cos(t * 3 + this.time * 2 + layerOffset)) * Math.cos(t);
                const y = centerY + (r1 + r2 * Math.cos(t * 3 + this.time * 2 + layerOffset)) * Math.sin(t) * 0.5;
                
                if (i === 0) ctx.moveTo(x, y);
                else ctx.lineTo(x, y);
            }
            ctx.closePath();
            ctx.stroke();
        }
        
        // Central glow
        const gradient = ctx.createRadialGradient(centerX, centerY, 0, centerX, centerY, 50);
        gradient.addColorStop(0, 'rgba(244, 160, 32, 0.8)');
        gradient.addColorStop(0.5, 'rgba(107, 45, 123, 0.4)');
        gradient.addColorStop(1, 'transparent');
        
        ctx.fillStyle = gradient;
        ctx.beginPath();
        ctx.arc(centerX, centerY, 50, 0, Math.PI * 2);
        ctx.fill();
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MONTE CARLO VISUALIZATION
// ─────────────────────────────────────────────────────────────────────────────
class MonteCarloVisualization {
    constructor() {
        this.canvas = document.getElementById('mc-canvas');
        if (!this.canvas) return;
        
        this.ctx = this.canvas.getContext('2d');
        this.samples = [];
        this.isRunning = false;
        this.targetValue = 137.036;
        
        const runBtn = document.getElementById('mc-run');
        if (runBtn) {
            runBtn.addEventListener('click', () => this.run());
        }
        
        this.draw();
    }
    
    run() {
        if (this.isRunning) return;
        
        this.isRunning = true;
        this.samples = [];
        
        const totalSamples = 86;
        let currentSample = 0;
        
        const addSample = () => {
            if (currentSample >= totalSamples) {
                this.isRunning = false;
                return;
            }
            
            // Generate sample converging toward 137.036
            const noise = (Math.random() - 0.5) * 20 * Math.exp(-currentSample / 30);
            const value = this.targetValue + noise;
            
            this.samples.push({
                x: Math.random() * 0.8 + 0.1,
                y: value,
                alpha: 0
            });
            
            // Animate sample appearance
            gsap.to(this.samples[this.samples.length - 1], {
                alpha: 1,
                duration: 0.3
            });
            
            currentSample++;
            
            // Update stats
            const samplesEl = document.getElementById('mc-samples');
            const resultEl = document.getElementById('mc-result');
            
            if (samplesEl) samplesEl.textContent = currentSample;
            
            if (resultEl) {
                const avg = this.samples.reduce((a, b) => a + b.y, 0) / this.samples.length;
                resultEl.textContent = avg.toFixed(3);
            }
            
            setTimeout(addSample, 50);
        };
        
        addSample();
    }
    
    draw() {
        const ctx = this.ctx;
        const width = this.canvas.width;
        const height = this.canvas.height;
        
        // Clear
        ctx.fillStyle = 'rgba(10, 10, 26, 0.95)';
        ctx.fillRect(0, 0, width, height);
        
        const padding = 60;
        const chartWidth = width - padding * 2;
        const chartHeight = height - padding * 2;
        
        // Y axis range
        const yMin = 130;
        const yMax = 145;
        
        // Grid
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.1)';
        ctx.lineWidth = 1;
        
        for (let v = 130; v <= 145; v += 5) {
            const y = padding + (1 - (v - yMin) / (yMax - yMin)) * chartHeight;
            ctx.beginPath();
            ctx.moveTo(padding, y);
            ctx.lineTo(width - padding, y);
            ctx.stroke();
            
            ctx.fillStyle = 'rgba(255, 255, 255, 0.5)';
            ctx.font = '12px "JetBrains Mono"';
            ctx.textAlign = 'right';
            ctx.fillText(v.toString(), padding - 10, y + 4);
        }
        
        // Target line at 137.036
        const targetY = padding + (1 - (this.targetValue - yMin) / (yMax - yMin)) * chartHeight;
        
        ctx.strokeStyle = '#f4a020';
        ctx.lineWidth = 2;
        ctx.setLineDash([5, 5]);
        ctx.beginPath();
        ctx.moveTo(padding, targetY);
        ctx.lineTo(width - padding, targetY);
        ctx.stroke();
        ctx.setLineDash([]);
        
        ctx.fillStyle = '#f4a020';
        ctx.textAlign = 'left';
        ctx.fillText('α⁻¹ = 137.036', width - padding + 10, targetY + 4);
        
        // Draw samples
        this.samples.forEach(sample => {
            const x = padding + sample.x * chartWidth;
            const y = padding + (1 - (sample.y - yMin) / (yMax - yMin)) * chartHeight;
            
            ctx.fillStyle = `rgba(107, 45, 123, ${sample.alpha})`;
            ctx.beginPath();
            ctx.arc(x, y, 6, 0, Math.PI * 2);
            ctx.fill();
            
            ctx.fillStyle = `rgba(244, 160, 32, ${sample.alpha})`;
            ctx.beginPath();
            ctx.arc(x, y, 3, 0, Math.PI * 2);
            ctx.fill();
        });
        
        // Axes labels
        ctx.fillStyle = 'rgba(255, 255, 255, 0.7)';
        ctx.font = '14px Inter';
        ctx.textAlign = 'center';
        ctx.fillText('Random samples from CP² × S³ topology', width / 2, height - 15);
        
        requestAnimationFrame(() => this.draw());
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// SPARC GALAXY ROTATION CURVES
// ─────────────────────────────────────────────────────────────────────────────
class SparcVisualization {
    constructor() {
        this.canvas = document.getElementById('sparc-canvas');
        if (!this.canvas) return;
        
        this.ctx = this.canvas.getContext('2d');
        this.currentGalaxy = 'ngc3198';
        
        // Add button listeners
        document.querySelectorAll('.galaxy-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                document.querySelectorAll('.galaxy-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                this.currentGalaxy = btn.dataset.galaxy;
                this.draw();
            });
        });
        
        this.draw();
    }
    
    draw() {
        const ctx = this.ctx;
        const width = this.canvas.width;
        const height = this.canvas.height;
        const data = galaxyData[this.currentGalaxy];
        
        const padding = 50;
        const chartWidth = width - padding * 2;
        const chartHeight = height - padding * 2;
        
        // Clear
        ctx.fillStyle = 'rgba(10, 10, 26, 0.95)';
        ctx.fillRect(0, 0, width, height);
        
        // Grid
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.1)';
        ctx.lineWidth = 1;
        
        for (let i = 0; i <= 5; i++) {
            const y = padding + (i / 5) * chartHeight;
            ctx.beginPath();
            ctx.moveTo(padding, y);
            ctx.lineTo(width - padding, y);
            ctx.stroke();
        }
        
        // Axes
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.5)';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(padding, padding);
        ctx.lineTo(padding, height - padding);
        ctx.lineTo(width - padding, height - padding);
        ctx.stroke();
        
        // Labels
        ctx.fillStyle = 'rgba(255, 255, 255, 0.7)';
        ctx.font = '12px Inter';
        ctx.fillText('V (km/s)', padding - 10, padding - 15);
        ctx.fillText('Radius (kpc)', width - padding - 30, height - padding + 30);
        
        // Scale values
        const maxV = 160;
        const maxR = 10;
        
        // Newton prediction (dashed red)
        ctx.strokeStyle = 'rgba(231, 76, 60, 0.7)';
        ctx.lineWidth = 2;
        ctx.setLineDash([5, 5]);
        ctx.beginPath();
        
        data.radii.forEach((r, i) => {
            const x = padding + (r / maxR) * chartWidth;
            const y = height - padding - (data.newton[i] / maxV) * chartHeight;
            
            if (i === 0) ctx.moveTo(x, y);
            else ctx.lineTo(x, y);
        });
        ctx.stroke();
        ctx.setLineDash([]);
        
        // DFD prediction (solid gold)
        ctx.strokeStyle = '#f4a020';
        ctx.lineWidth = 3;
        ctx.beginPath();
        
        data.radii.forEach((r, i) => {
            const x = padding + (r / maxR) * chartWidth;
            const y = height - padding - (data.observed[i] / maxV) * chartHeight;
            
            if (i === 0) ctx.moveTo(x, y);
            else ctx.lineTo(x, y);
        });
        ctx.stroke();
        
        // Data points
        data.radii.forEach((r, i) => {
            const x = padding + (r / maxR) * chartWidth;
            const y = height - padding - (data.observed[i] / maxV) * chartHeight;
            
            // Error bars (simulated)
            ctx.strokeStyle = 'rgba(255, 255, 255, 0.5)';
            ctx.lineWidth = 1;
            ctx.beginPath();
            ctx.moveTo(x, y - 10);
            ctx.lineTo(x, y + 10);
            ctx.stroke();
            
            // Point
            ctx.fillStyle = '#fff';
            ctx.beginPath();
            ctx.arc(x, y, 4, 0, Math.PI * 2);
            ctx.fill();
        });
        
        // Legend
        ctx.fillStyle = '#f4a020';
        ctx.fillRect(width - 150, padding + 10, 20, 3);
        ctx.fillStyle = 'rgba(255, 255, 255, 0.7)';
        ctx.font = '11px Inter';
        ctx.fillText('DFD (no dark matter)', width - 125, padding + 15);
        
        ctx.strokeStyle = 'rgba(231, 76, 60, 0.7)';
        ctx.setLineDash([5, 5]);
        ctx.beginPath();
        ctx.moveTo(width - 150, padding + 35);
        ctx.lineTo(width - 130, padding + 35);
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillText('Newton (visible only)', width - 125, padding + 38);
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// INITIALIZATION
// ─────────────────────────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
    // Initialize Three.js background
    const cosmicBg = new CosmicBackground();
    
    // Initialize GSAP animations
    initScrollAnimations();
    
    // Initialize interactive demos
    const galaxyDemo = new GalaxyDemo();
    const psiViz = new PsiFieldVisualization();
    const throttleViz = new ThrottleVisualization();
    const topoViz = new TopologyVisualization();
    const mcViz = new MonteCarloVisualization();
    const sparcViz = new SparcVisualization();
    
    // Mouse tracking for parallax effects
    document.addEventListener('mousemove', (e) => {
        state.mouseX = (e.clientX / window.innerWidth - 0.5) * 2;
        state.mouseY = (e.clientY / window.innerHeight - 0.5) * 2;
    });
    
    // Smooth scroll for nav links
    document.querySelectorAll('.nav-links a').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = link.getAttribute('href');
            const target = document.querySelector(targetId);
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
    
    // Mark as loaded
    state.isLoaded = true;
    document.body.classList.add('loaded');
    
    console.log('✨ Density Field Dynamics - Immersive Experience Loaded');
    console.log('🌌 Gravity is Light');
});

// ─────────────────────────────────────────────────────────────────────────────
// PERFORMANCE OPTIMIZATION
// ─────────────────────────────────────────────────────────────────────────────
// Intersection Observer for lazy loading heavy visualizations
const lazyLoadObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('lazy-loaded');
            // Trigger any initialization needed when element becomes visible
        }
    });
}, { threshold: 0.1 });

// Observe elements that should lazy load
document.querySelectorAll('.interactive-demo, .monte-carlo-demo, .sparc-gallery').forEach(el => {
    lazyLoadObserver.observe(el);
});
