/**
 * 生成唯一的UUID主键
 *
 */

var UUID = {
  initialize: function() {
    this.id = this.createUUID("-");
    return this;
  },

  valueOf: function() {
    return this.id;
  },

  toString: function() {
    return this.id;
  },

  createUUID: function(split) {
    if (!split) split = "-";
    var dg = new Date(1582, 10, 15, 0, 0, 0, 0);
    var dc = new Date();
    var t = dc.getTime() - dg.getTime();
    var tl = this.getIntegerBits(t, 0, 31);
    var tm = this.getIntegerBits(t, 32, 47);
    var thv = this.getIntegerBits(t, 48, 59) + "1"; // version 1, security version is 2
    var csar = this.getIntegerBits(this.rand(4095), 0, 7);
    var csl = this.getIntegerBits(this.rand(4095), 0, 7);
    var n =
      this.getIntegerBits(this.rand(8191), 0, 7) +
      this.getIntegerBits(this.rand(8191), 8, 15) +
      this.getIntegerBits(this.rand(8191), 0, 7) +
      this.getIntegerBits(this.rand(8191), 8, 15) +
      this.getIntegerBits(this.rand(8191), 0, 15);
    return tl + split + tm + split + thv + split + csar + csl + split + n;
  },

  getIntegerBits: function(val, start, end) {
    var base16 = this.returnBase(val, 16);
    var quadArray = new Array();
    var quadString = "";
    var i = 0;
    for (i = 0; i < base16.length; i++) {
      quadArray.push(base16.substring(i, i + 1));
    }
    for (i = Math.floor(start / 4); i <= Math.floor(end / 4); i++) {
      if (!quadArray[i] || quadArray[i] == "") quadString += "0";
      else quadString += quadArray[i];
    }
    return quadString;
  },

  returnBase: function(number, base) {
    return number.toString(base).toUpperCase();
  },

  rand: function(max) {
    return Math.floor(setTimeout(extrandom, 1) * (max + 1));
  }
};

//随机数
function extrandom() {
  /*	var arr = new Uint32Array(2);
      crypto.getRandomValues(arr);
    // keep all 32 bits of the the first, top 20 of the second for 52 random bits
    var mantissa = (arr[0] * Math.pow(2,20)) + (arr[1] >>> 12)
    // shift all 52 bits to the right of the decimal point
    var extresult = mantissa * Math.pow(2,-52);
    return  extresult ;*/

  var oNow = new Date();

  var extresult =
    oNow.getMilliseconds() / 10e3 +
    oNow.getMilliseconds() / 10e6 +
    oNow.getMilliseconds() / 10e9 +
    oNow.getMilliseconds() / 10e12 +
    oNow.getMilliseconds() / 10e15 +
    oNow.getDate() / 10e17;
  return extresult;
}
