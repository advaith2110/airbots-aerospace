/**
 * AIRBOTS Aerospace — Interactive UI Engine
 */

document.addEventListener('DOMContentLoaded', () => {
  initNavbarScroll();
  initMobileMenu();
  updateCalculator();
  startTelemetryTicker();
});

/* ==========================================================================
   1. Navbar Scroll Elevation
   ========================================================================== */
function initNavbarScroll() {
  const navbar = document.getElementById('navbar');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 30) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  });
}

/* ==========================================================================
   2. Mobile Drawer Navigation
   ========================================================================== */
function initMobileMenu() {
  const toggleBtn = document.getElementById('menuToggle');
  const drawer = document.getElementById('mobileDrawer');

  if (toggleBtn && drawer) {
    toggleBtn.addEventListener('click', () => {
      drawer.classList.toggle('open');
    });
  }
}

function closeDrawer() {
  const drawer = document.getElementById('mobileDrawer');
  if (drawer) {
    drawer.classList.remove('open');
  }
}

/* ==========================================================================
   3. Product Interactive Feature Tabs
   ========================================================================== */
function switchProductTab(tabId) {
  // Update button active state
  const buttons = document.querySelectorAll('.ptab-btn');
  buttons.forEach(btn => {
    btn.classList.remove('active');
  });

  // Target button
  const activeBtn = Array.from(buttons).find(btn => 
    btn.getAttribute('onclick').includes(tabId)
  );
  if (activeBtn) activeBtn.classList.add('active');

  // Update content panels
  const panels = document.querySelectorAll('.ptab-content');
  panels.forEach(panel => {
    panel.classList.remove('active');
  });

  const targetPanel = document.getElementById(`tab-${tabId}`);
  if (targetPanel) {
    targetPanel.classList.add('active');
  }
}

/* ==========================================================================
   4. Agricultural ROI & Savings Calculator
   ========================================================================== */
function formatINR(number) {
  return new Intl.NumberFormat('en-IN', {
    style: 'currency',
    currency: 'INR',
    maximumFractionDigits: 0
  }).format(number);
}

function updateCalculator() {
  const acres = parseInt(document.getElementById('farmSize').value, 10);
  const crop = document.getElementById('cropType').value;
  const cycles = parseInt(document.getElementById('sprayCycles').value, 10);
  const manualLaborRate = parseInt(document.getElementById('manualCost').value, 10);

  // Update slider label displays
  document.getElementById('farmSizeVal').innerText = `${acres} Acres`;
  document.getElementById('cyclesVal').innerText = `${cycles} Sprays`;
  document.getElementById('laborCostVal').innerText = `₹ ${manualLaborRate}`;

  // Crop multiplier metrics (chemical intensity)
  const cropData = {
    cotton: { chemPerAcrePerCycle: 900, waterPerAcreManual: 200, yieldFactor: 1.12 },
    paddy: { chemPerAcrePerCycle: 700, waterPerAcreManual: 180, yieldFactor: 1.09 },
    sugarcane: { chemPerAcrePerCycle: 1100, waterPerAcreManual: 220, yieldFactor: 1.10 },
    wheat: { chemPerAcrePerCycle: 600, waterPerAcreManual: 150, yieldFactor: 1.08 },
    horticulture: { chemPerAcrePerCycle: 1400, waterPerAcreManual: 250, yieldFactor: 1.15 }
  };

  const currentCrop = cropData[crop] || cropData.paddy;

  // Traditional Costs
  const totalSprayEvents = acres * cycles;
  const traditionalLaborTotal = totalSprayEvents * manualLaborRate;
  const traditionalChemTotal = totalSprayEvents * currentCrop.chemPerAcrePerCycle;
  const traditionalWaterLiters = totalSprayEvents * currentCrop.waterPerAcreManual;

  // Drone Economics
  // Chemical saved: 30%
  const chemicalSavings = Math.round(traditionalChemTotal * 0.30);
  
  // Drone spray service / operating cost: ~₹350 / acre vs manual
  const droneOperatingCost = totalSprayEvents * 350;
  const laborSavings = Math.max(0, traditionalLaborTotal - droneOperatingCost);

  // Water conservation: 90%
  const waterSavedLiters = Math.round(traditionalWaterLiters * 0.90);

  // Hours saved: Manual spray ~ 1 acre = 4 hours. Drone ~ 1 acre = 7 mins (0.12 hrs).
  const hoursSaved = Math.round(totalSprayEvents * 3.8);

  // Net Annual Monetary Savings
  const netSavings = chemicalSavings + laborSavings;

  // Update DOM elements
  document.getElementById('totalSavings').innerText = formatINR(netSavings);
  document.getElementById('chemSaved').innerText = `${formatINR(chemicalSavings)} (30% less)`;
  document.getElementById('waterSaved').innerText = `${waterSavedLiters.toLocaleString('en-IN')} Liters (90%)`;
  document.getElementById('timeSaved').innerText = `${hoursSaved} Hours Saved`;
}

/* ==========================================================================
   5. Telemetry HUD Mission Control Simulator
   ========================================================================== */
let telemetryTimer = null;
let currentFlightMode = 'auto';

function setFlightMode(mode) {
  currentFlightMode = mode;

  // Update mode buttons
  const btns = document.querySelectorAll('.mode-btn');
  btns.forEach(b => b.classList.remove('active'));

  const clickedBtn = Array.from(btns).find(b => 
    b.getAttribute('onclick') && b.getAttribute('onclick').includes(mode)
  );
  if (clickedBtn) clickedBtn.classList.add('active');

  const hudAlt = document.getElementById('hudAlt');
  const hudSpeed = document.getElementById('hudSpeed');
  const hudTank = document.getElementById('hudTank');
  const hudFlow = document.getElementById('hudFlow');
  const altBar = document.getElementById('altBar');
  const speedBar = document.getElementById('speedBar');

  if (mode === 'hover') {
    hudAlt.innerHTML = '2.8 <span class="unit">m AGL</span>';
    hudSpeed.innerHTML = '0.0 <span class="unit">m/s</span>';
    hudFlow.innerText = '0.0 L/min';
    altBar.style.width = '35%';
    speedBar.style.width = '0%';
  } else if (mode === 'spray') {
    hudAlt.innerHTML = '3.0 <span class="unit">m AGL</span>';
    hudSpeed.innerHTML = '5.2 <span class="unit">m/s</span>';
    hudFlow.innerText = '4.5 L/min (High Swath)';
    altBar.style.width = '42%';
    speedBar.style.width = '68%';
  } else if (mode === 'rtl') {
    hudAlt.innerHTML = '15.0 <span class="unit">m AGL (Transit)</span>';
    hudSpeed.innerHTML = '8.0 <span class="unit">m/s</span>';
    hudFlow.innerText = '0.0 L/min (Pumps Disengaged)';
    altBar.style.width = '85%';
    speedBar.style.width = '90%';
  } else {
    // auto waypoint
    hudAlt.innerHTML = '3.2 <span class="unit">m AGL</span>';
    hudSpeed.innerHTML = '4.5 <span class="unit">m/s</span>';
    hudFlow.innerText = '3.2 L/min';
    altBar.style.width = '45%';
    speedBar.style.width = '55%';
  }
}

function triggerSimulatorTick() {
  const tankElem = document.getElementById('hudTank');
  const blip = document.getElementById('droneBlip');

  if (tankElem) {
    let current = parseFloat(tankElem.innerText);
    if (isNaN(current) || current <= 1.0) current = 15.0;
    const nextVal = (current - 0.4).toFixed(1);
    tankElem.innerHTML = `${nextVal} <span class="unit">/ 15 L</span>`;
    
    const pct = Math.round((nextVal / 15.0) * 100);
    const tankBar = document.getElementById('tankBar');
    if (tankBar) tankBar.style.width = `${pct}%`;
  }

  // Jiggle blip slightly to simulate waypoint flight
  if (blip) {
    const rx = 50 + (Math.random() * 8 - 4);
    const ry = 48 + (Math.random() * 6 - 3);
    blip.style.left = `${rx}%`;
    blip.style.top = `${ry}%`;
  }
}

function startTelemetryTicker() {
  if (telemetryTimer) clearInterval(telemetryTimer);
  telemetryTimer = setInterval(() => {
    if (currentFlightMode === 'spray' || currentFlightMode === 'auto') {
      triggerSimulatorTick();
    }
  }, 4000);
}

/* ==========================================================================
   6. Form & Modal Handlers
   ========================================================================== */
function handleFormSubmit(e) {
  e.preventDefault();
  const name = document.getElementById('cName').value;
  const phone = document.getElementById('cPhone').value;
  const feedback = document.getElementById('formFeedback');
  const btn = document.getElementById('submitBtn');

  btn.disabled = true;
  btn.innerText = 'Transmitting to Flight Operations...';

  setTimeout(() => {
    feedback.className = 'form-feedback success';
    feedback.innerHTML = `<strong>Thank you, ${name}!</strong> Your request has been logged. Our Maharashtra regional flight coordinator will connect via WhatsApp/Call at <strong>${phone}</strong> within 4 business hours.`;
    feedback.classList.remove('hidden');

    btn.disabled = false;
    btn.innerText = 'Inquiry Received ✓';
    document.getElementById('contactForm').reset();
  }, 1000);
}

function openModal(type) {
  const modal = document.getElementById('genericModal');
  const content = document.getElementById('modalContent');

  if (!modal || !content) return;

  if (type === 'demo') {
    content.innerHTML = `
      <div style="text-align: center; margin-bottom: 24px;">
        <span style="font-size: 2.5rem;">🚁</span>
        <h3 style="font-size: 1.5rem; margin-top: 8px; font-family: var(--font-heading);">Schedule a Field Flight Demo</h3>
        <p style="color: var(--slate-500); font-size: 0.875rem;">Experience the DGCA-Certified Surya Shakti 15L live on your farmland.</p>
      </div>
      <form onsubmit="handleModalSubmit(event)">
        <div style="margin-bottom: 12px;">
          <label style="display:block; font-size: 0.8125rem; font-weight:600; margin-bottom:4px;">Full Name</label>
          <input type="text" class="form-input" required placeholder="Your Name" />
        </div>
        <div style="margin-bottom: 12px;">
          <label style="display:block; font-size: 0.8125rem; font-weight:600; margin-bottom:4px;">Mobile / WhatsApp</label>
          <input type="tel" class="form-input" required placeholder="+91 98765 43210" />
        </div>
        <div style="margin-bottom: 16px;">
          <label style="display:block; font-size: 0.8125rem; font-weight:600; margin-bottom:4px;">District / Village & Crop</label>
          <input type="text" class="form-input" required placeholder="e.g. Nashik - Grapes / Onion" />
        </div>
        <button type="submit" class="btn btn-primary w-100 btn-lg">Confirm Live Demo Request</button>
      </form>
    `;
  } else if (type === 'brochure') {
    content.innerHTML = `
      <div style="text-align: center; margin-bottom: 24px;">
        <span style="font-size: 2.5rem;">📄</span>
        <h3 style="font-size: 1.5rem; margin-top: 8px; font-family: var(--font-heading);">Surya Shakti 15L Technical Datasheet</h3>
        <p style="color: var(--slate-500); font-size: 0.875rem;">Complete DGCA certification specs, payload diagram, and battery maintenance schedule.</p>
      </div>
      <form onsubmit="handleModalSubmit(event, 'brochure')">
        <div style="margin-bottom: 12px;">
          <label style="display:block; font-size: 0.8125rem; font-weight:600; margin-bottom:4px;">WhatsApp Number</label>
          <input type="tel" class="form-input" required placeholder="+91 98765 43210" />
        </div>
        <button type="submit" class="btn btn-primary w-100 btn-lg">Instant Download PDF & Send to WhatsApp</button>
      </form>
    `;
  } else {
    content.innerHTML = `
      <div style="text-align: center; margin-bottom: 24px;">
        <span style="font-size: 2.5rem;">📊</span>
        <h3 style="font-size: 1.5rem; margin-top: 8px; font-family: var(--font-heading);">Custom Farm Subsidy & Quotation</h3>
        <p style="color: var(--slate-500); font-size: 0.875rem;">Get exact SMAM government subsidy calculation for your district.</p>
      </div>
      <form onsubmit="handleModalSubmit(event)">
        <div style="margin-bottom: 12px;">
          <label style="display:block; font-size: 0.8125rem; font-weight:600; margin-bottom:4px;">Name</label>
          <input type="text" class="form-input" required placeholder="Your Name" />
        </div>
        <div style="margin-bottom: 16px;">
          <label style="display:block; font-size: 0.8125rem; font-weight:600; margin-bottom:4px;">Phone</label>
          <input type="tel" class="form-input" required placeholder="+91 98765 43210" />
        </div>
        <button type="submit" class="btn btn-primary w-100 btn-lg">Receive Personalized Proposal</button>
      </form>
    `;
  }

  modal.classList.add('active');
}

function closeModal() {
  const modal = document.getElementById('genericModal');
  if (modal) modal.classList.remove('active');
}

function handleModalSubmit(e, type) {
  e.preventDefault();
  const content = document.getElementById('modalContent');
  content.innerHTML = `
    <div style="text-align: center; padding: 20px 0;">
      <span style="font-size: 3rem; color: var(--primary-green);">✓</span>
      <h3 style="font-size: 1.5rem; margin: 12px 0 8px 0; font-family: var(--font-heading);">Request Confirmed</h3>
      <p style="color: var(--slate-600); font-size: 0.9375rem; margin-bottom: 20px;">
        ${type === 'brochure' 
          ? 'Datasheet link sent to WhatsApp! Downloading digital copy...' 
          : 'Our flight specialist has received your application and will contact you shortly.'}
      </p>
      <button class="btn btn-secondary" onclick="closeModal()">Close</button>
    </div>
  `;
}

// Close modal when clicking on overlay background
document.addEventListener('click', (e) => {
  const modal = document.getElementById('genericModal');
  if (e.target === modal) {
    closeModal();
  }
});
