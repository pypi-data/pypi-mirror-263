# uint8-base64

[![NPM version][npm-image]][npm-url]
[![build status][ci-image]][ci-url]
[![Test coverage][codecov-image]][codecov-url]
[![npm download][download-image]][download-url]

You can find a lot of NPM libraries dealing with base64 encoding and decoding.

However we could not find one that would have as input AND output an Uint8Array. This library does exactly this.

This library is pretty fast and will convert over 500 Mb per second in nodejs as well as in the browser.

## Installation

`$ npm i uint8-base64`

## Usage

### encode

```js
import { encode } from 'uint8-base64';

const result = encode(Uint8Array.from([65])); // an array containing 'A'
// result is Uint8Array(4) [ 81, 81, 61, 61 ] ('QQ==')
```

### decode

```js
import { decode } from '..';

const result = decode(Uint8Array.from([81, 81, 61, 61])); // an array containing 'QQ=='
// result is Uint8Array(1) [ 65 ] ('A')
```

## License

The code was largely inspired by: https://gist.github.com/enepomnyaschih/72c423f727d395eeaa09697058238727

[MIT](./LICENSE)

[npm-image]: https://img.shields.io/npm/v/uint8-base64.svg
[npm-url]: https://www.npmjs.com/package/uint8-base64
[ci-image]: https://github.com/cheminfo/uint8-base64/workflows/Node.js%20CI/badge.svg?branch=main
[ci-url]: https://github.com/cheminfo/uint8-base64/actions?query=workflow%3A%22Node.js+CI%22
[codecov-image]: https://img.shields.io/codecov/c/github/cheminfo/uint8-base64.svg
[codecov-url]: https://codecov.io/gh/cheminfo/uint8-base64
[download-image]: https://img.shields.io/npm/dm/uint8-base64.svg
[download-url]: https://www.npmjs.com/package/uint8-base64
