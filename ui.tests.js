const addNumbers = require('./src/math');

describe('addNumbers', () => {
  it('should add two positive numbers correctly', () => {
    expect(addNumbers(3, 5)).toBe(8);
  });

  it('should add a positive and a negative number correctly', () => {
    expect(addNumbers(10, -3)).toBe(7);
  });

  it('should add two negative numbers correctly', () => {
    expect(addNumbers(-2, -3)).toBe(-5);
  });

  it('should return NaN if a non-number is passed', () => {
    expect(addNumbers('a', 5)).toBeNaN();
  });
});
