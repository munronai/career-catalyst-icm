---
id: 004-proposals-selection
title: Checkpoint — select proposals to build
type: interactive
stage: 2
status: blocked
---
<div style="font-family:system-ui, -apple-system, sans-serif;padding:12px;color:#1d1e1b">
  <p style="margin:0 0 10px;font-size:13px;line-height:1.4"><b>Select which proposals to build into value-add packages for Cint:</b></p>
  <form id="proposal-form" onsubmit="submitSelection(event)">
    <div id="proposal-list" style="margin-bottom:12px">
      <label style="display:flex;align-items:flex-start;gap:8px;margin-bottom:8px;cursor:pointer;font-size:12px">
        <input type="checkbox" name="proposals" value="1" checked style="margin-top:2px">
        <span><b>Proposal 1:</b> <span id="p1-text">Self-Serve Developer Portal & Sandbox Wizard</span></span>
      </label>
      <label style="display:flex;align-items:flex-start;gap:8px;margin-bottom:8px;cursor:pointer;font-size:12px">
        <input type="checkbox" name="proposals" value="2" style="margin-top:2px">
        <span><b>Proposal 2:</b> <span id="p2-text">Webhook Integrity Framework ("Ghost Complete Shield")</span></span>
      </label>
      <label style="display:flex;align-items:flex-start;gap:8px;margin-bottom:8px;cursor:pointer;font-size:12px">
        <input type="checkbox" name="proposals" value="3" style="margin-top:2px">
        <span><b>Proposal 3:</b> <span id="p3-text">Unified Supply API SDK Wrappers</span></span>
      </label>
    </div>
    <div style="display:flex;gap:6px">
      <button type="submit" style="font:inherit;font-size:11px;padding:5px 10px;border:none;border-radius:4px;background:#3b82f6;color:#fff;cursor:pointer;font-weight:600">Submit Selection</button>
      <button type="button" onclick="selectAll()" style="font:inherit;font-size:11px;padding:5px 10px;border:1px solid #c2bfb6;border-radius:4px;background:#fff;cursor:pointer">Select All</button>
    </div>
  </form>
  <p id="ack" style="margin:10px 0 0;font-size:11px;color:#22c55e;font-weight:500;min-height:1.2em"></p>
  <script>
    function selectAll() {
      const checkboxes = document.getElementsByName('proposals');
      checkboxes.forEach(cb => cb.checked = true);
    }
    function submitSelection(e) {
      e.preventDefault();
      const checkboxes = document.getElementsByName('proposals');
      const selected = [];
      checkboxes.forEach(cb => {
        if (cb.checked) {
          const textSpan = document.getElementById('p' + cb.value + '-text');
          selected.push({
            index: parseInt(cb.value),
            title: textSpan ? textSpan.innerText : 'Proposal ' + cb.value
          });
        }
      });
      if (selected.length === 0) {
        document.getElementById('ack').style.color = '#ef4444';
        document.getElementById('ack').textContent = 'Please select at least one proposal.';
        return;
      }
      respond({ selectedProposals: selected });
    }
    window.onResponded = function(e) {
      document.getElementById('ack').style.color = '#22c55e';
      const titles = e.value.selectedProposals.map(p => p.title).join(', ');
      document.getElementById('ack').textContent = '✓ Saved selection: ' + titles;
    };
  </script>
</div>
