// Function to move between steps
function nextStep(step) {
  // Hide all steps
  document.querySelectorAll('.step').forEach(s => s.classList.remove('active'));
  // Show the requested step
  document.getElementById('step' + step).classList.add('active');

  // When reaching the summary step
  if (step === 6) {
    const food1 = document.getElementById('foodType1').value;
    const cuisine = document.getElementById('cuisine').value;
    const food2 = document.getElementById('foodType2').value;
    const flavor = document.getElementById('flavor').value;
    const extras = Array.from(document.querySelectorAll('#step4 input[type=checkbox]:checked'))
                        .map(cb => cb.value).join(', ');

    document.getElementById('summary').innerHTML = `
      <strong>Food Type:</strong> ${food1} / ${food2}<br>
      <strong>Cuisine:</strong> ${cuisine}<br>
      <strong>Flavor:</strong> ${flavor}<br>
      <strong>Extras:</strong> ${extras || 'None'}<br>
      <strong>Dishes:</strong> Special Curry, Chef’s Recommended Dish, Seasonal Delight
    `;
  }
}

// Function to finish the order
function finishOrder() {
  // Hide all steps
  document.querySelectorAll('.step').forEach(s => s.classList.remove('active'));
  // Show confirmation
  document.getElementById('step8').classList.add('active');
}