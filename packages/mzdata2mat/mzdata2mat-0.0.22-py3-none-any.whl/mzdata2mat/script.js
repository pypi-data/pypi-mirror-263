
// mzData files
function mzMLread(name, directory) {
    let parseMZ = require(directory+'node_modules/mzdata') 
    let fs = require('fs');
    const mzDataFile = fs.readFileSync(name);
    var response = parseMZ.parseMZ(mzDataFile);
    return response
}
