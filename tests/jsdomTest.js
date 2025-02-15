// Import jsdom and make sure TextEncoder is available
global.TextEncoder = require('util').TextEncoder;
global.TextDecoder = require('util').TextDecoder;

const { JSDOM } = require('jsdom');

// Create a new JSDOM instance, simulating a basic HTML structure
const dom = new JSDOM(`
  <!DOCTYPE html>
  <html>
    <head><title>Test</title></head>
    <body>
      <input id="num1" value="5" />
      <input id="num2" value="3" />
      <button id="addButton">Add</button>
      <button id="subtractButton">Subtract</button>
      <button id="multiplyButton">Multiply</button>
      <button id="divideButton">Divide</button>
      <div id="result"></div>
    </body>
  </html>
`);

// Get the document from the JSDOM instance
const document = dom.window.document;

// Function to simulate adding two numbers
document.getElementById('addButton').addEventListener('click', function () {
  const num1 = parseFloat(document.getElementById('num1').value);
  const num2 = parseFloat(document.getElementById('num2').value);
  const result = num1 + num2;
  document.getElementById('result').textContent = "Result: " + result;
});

document.getElementById('subtractButton').addEventListener('click', function () {
  const num1 = parseFloat(document.getElementById('num1').value);
  const num2 = parseFloat(document.getElementById('num2').value);
  const result = num1 - num2;
  document.getElementById('result').textContent = "Result: " + result;
});

document.getElementById('multiplyButton').addEventListener('click', function () {
  const num1 = parseFloat(document.getElementById('num1').value);
  const num2 = parseFloat(document.getElementById('num2').value);
  const result = num1 * num2;
  document.getElementById('result').textContent = "Result: " + result;
});

document.getElementById('divideButton').addEventListener('click', function () {
  const num1 = parseFloat(document.getElementById('num1').value);
  const num2 = parseFloat(document.getElementById('num2').value);
  const result = num2 === 0 ? "Cannot divide by zero." : num1 / num2;
  document.getElementById('result').textContent = "Result: " + result;
});

describe('Calculator', () => {
  it('should add two numbers correctly', () => {
    document.getElementById('num1').value = '5';
    document.getElementById('num2').value = '3';
    document.getElementById('addButton').click();
    expect(document.getElementById('result').textContent).toBe('Result: 8');
  });

  it('should subtract two numbers correctly', () => {
    document.getElementById('num1').value = '5';
    document.getElementById('num2').value = '3';
    document.getElementById('subtractButton').click();
    expect(document.getElementById('result').textContent).toBe('Result: 2');
  });

  it('should multiply two numbers correctly', () => {
    document.getElementById('num1').value = '5';
    document.getElementById('num2').value = '3';
    document.getElementById('multiplyButton').click();
    expect(document.getElementById('result').textContent).toBe('Result: 15');
  });

  it('should divide two numbers correctly', () => {
    document.getElementById('num1').value = '6';
    document.getElementById('num2').value = '3';
    document.getElementById('divideButton').click();
    expect(document.getElementById('result').textContent).toBe('Result: 2');
  });

  it('should handle division by zero', () => {
    document.getElementById('num1').value = '6';
    document.getElementById('num2').value = '0';
    document.getElementById('divideButton').click();
    expect(document.getElementById('result').textContent).toBe('Result: Cannot divide by zero.');
  });

  it('should handle invalid input for addition', () => {
    document.getElementById('num1').value = 'a';
    document.getElementById('num2').value = '3';
    document.getElementById('addButton').click();
    expect(document.getElementById('result').textContent).toBe('Result: NaN');
  });

  it('should handle negative numbers', () => {
    document.getElementById('num1').value = '-5';
    document.getElementById('num2').value = '3';
    document.getElementById('addButton').click();
    expect(document.getElementById('result').textContent).toBe('Result: -2');
  });
});
