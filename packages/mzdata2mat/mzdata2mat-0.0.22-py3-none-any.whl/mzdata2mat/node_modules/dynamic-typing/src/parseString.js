/**
 * Dynamically type a string
 * @param {string} value String to dynamically type
 * @returns {boolean|string|number}
 */
export function parseString(value) {
  if (value.length === 4 || value.length === 5) {
    let lowercase = value.toLowerCase();

    if (lowercase === 'true') return true;
    if (lowercase === 'false') return false;
  }
  let number = Number(value);
  if (number === 0 && !value.includes('0')) {
    return value;
  }
  if (!Number.isNaN(number)) return number;
  return value;
}
