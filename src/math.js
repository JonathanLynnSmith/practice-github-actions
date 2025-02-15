// math.js
const MathUtils = {
    operate: function(a, b, operator) {
      if (isNaN(a) || isNaN(b)) {
        return "Please enter valid numbers.";
      }
  
      switch (operator) {
        case 'add':
          return a + b;
        case 'subtract':
          return a - b;
        case 'multiply':
          return a * b;
        case 'divide':
          if (b === 0) {
            return "Cannot divide by zero.";
          }
          return a / b;
        default:
          return "Invalid operation";
      }
    }
  };
  
  // Attach the MathUtils object to the global window object
  window.MathUtils = MathUtils;
  