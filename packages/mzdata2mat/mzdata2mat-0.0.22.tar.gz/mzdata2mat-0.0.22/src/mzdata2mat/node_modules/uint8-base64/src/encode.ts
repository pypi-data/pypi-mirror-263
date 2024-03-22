const base64codes = Uint8Array.from([
  65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
  84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106,
  107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121,
  122, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 43, 47,
]);

/**
 * Convert a Uint8Array containing bytes to a Uint8Array containing the base64 encoded values
 * @returns a Uint8Array containing the encoded bytes
 */

export function encode(input: Uint8Array): Uint8Array {
  const output = new Uint8Array(Math.ceil(input.length / 3) * 4);
  let i, j;
  for (i = 2, j = 0; i < input.length; i += 3, j += 4) {
    output[j] = base64codes[input[i - 2] >> 2];
    output[j + 1] =
      base64codes[((input[i - 2] & 0x03) << 4) | (input[i - 1] >> 4)];
    output[j + 2] = base64codes[((input[i - 1] & 0x0f) << 2) | (input[i] >> 6)];
    output[j + 3] = base64codes[input[i] & 0x3f];
  }
  if (i === input.length + 1) {
    // 1 octet yet to write
    output[j] = base64codes[input[i - 2] >> 2];
    output[j + 1] = base64codes[(input[i - 2] & 0x03) << 4];
    output[j + 2] = 61;
    output[j + 3] = 61;
  }
  if (i === input.length) {
    // 2 octets yet to write
    output[j] = base64codes[input[i - 2] >> 2];
    output[j + 1] =
      base64codes[((input[i - 2] & 0x03) << 4) | (input[i - 1] >> 4)];
    output[j + 2] = base64codes[(input[i - 1] & 0x0f) << 2];
    output[j + 3] = 61;
  }
  return output;
}
