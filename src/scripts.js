

function setupEventListeners() {
  document.getElementById('addButton').addEventListener('click', function () {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    const result = MathUtils.operate(num1, num2, 'add');
    document.getElementById('result').textContent = "Result: " + result;
  });

  document.getElementById('subtractButton').addEventListener('click', function () {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    const result = MathUtils.operate(num1, num2, 'subtract');
    document.getElementById('result').textContent = "Result: " + result;
  });

  document.getElementById('multiplyButton').addEventListener('click', function () {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    const result = MathUtils.operate(num1, num2, 'multiply');
    document.getElementById('result').textContent = "Result: " + result;
  });

  document.getElementById('divideButton').addEventListener('click', function () {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    const result = MathUtils.operate(num1, num2, 'divide');
    document.getElementById('result').textContent = "Result: " + result;
  });
}

// Initialize event listeners
setupEventListeners();