var chrsz = 8;
e = {};
t = {};
function str2binl(e) {
for (var t = Array(), a = (1 << chrsz) - 1, r = 0; r < e.length * chrsz; r += chrsz) t[r >> 5] |= (e.charCodeAt(r / chrsz) & a) << r % 32;
return t
}
/////////
function core_md5(e, t) {
e[t >> 5] |= 128 << t % 32,
e[14 + (t + 64 >>> 9 << 4)] = t;
for (var a = 1732584193,
r = -271733879,
i = -1732584194,
o = 271733878,
n = 0; n < e.length; n += 16) {
    var s = a,
    l = r,
    c = i,
    p = o;
    a = md5_ff(a, r, i, o, e[n + 0], 7, -680876936),
    o = md5_ff(o, a, r, i, e[n + 1], 12, -389564586),
    i = md5_ff(i, o, a, r, e[n + 2], 17, 606105819),
    r = md5_ff(r, i, o, a, e[n + 3], 22, -1044525330),
    a = md5_ff(a, r, i, o, e[n + 4], 7, -176418897),
    o = md5_ff(o, a, r, i, e[n + 5], 12, 1200080426),
    i = md5_ff(i, o, a, r, e[n + 6], 17, -1473231341),
    r = md5_ff(r, i, o, a, e[n + 7], 22, -45705983),
    a = md5_ff(a, r, i, o, e[n + 8], 7, 1770035416),
    o = md5_ff(o, a, r, i, e[n + 9], 12, -1958414417),
    i = md5_ff(i, o, a, r, e[n + 10], 17, -42063),
    r = md5_ff(r, i, o, a, e[n + 11], 22, -1990404162),
    a = md5_ff(a, r, i, o, e[n + 12], 7, 1804603682),
    o = md5_ff(o, a, r, i, e[n + 13], 12, -40341101),
    i = md5_ff(i, o, a, r, e[n + 14], 17, -1502002290),
    a = md5_gg(a, r = md5_ff(r, i, o, a, e[n + 15], 22, 1236535329), i, o, e[n + 1], 5, -165796510),
    o = md5_gg(o, a, r, i, e[n + 6], 9, -1069501632),
    i = md5_gg(i, o, a, r, e[n + 11], 14, 643717713),
    r = md5_gg(r, i, o, a, e[n + 0], 20, -373897302),
    a = md5_gg(a, r, i, o, e[n + 5], 5, -701558691),
    o = md5_gg(o, a, r, i, e[n + 10], 9, 38016083),
    i = md5_gg(i, o, a, r, e[n + 15], 14, -660478335),
    r = md5_gg(r, i, o, a, e[n + 4], 20, -405537848),
    a = md5_gg(a, r, i, o, e[n + 9], 5, 568446438),
    o = md5_gg(o, a, r, i, e[n + 14], 9, -1019803690),
    i = md5_gg(i, o, a, r, e[n + 3], 14, -187363961),
    r = md5_gg(r, i, o, a, e[n + 8], 20, 1163531501),
    a = md5_gg(a, r, i, o, e[n + 13], 5, -1444681467),
    o = md5_gg(o, a, r, i, e[n + 2], 9, -51403784),
    i = md5_gg(i, o, a, r, e[n + 7], 14, 1735328473),
    a = md5_hh(a, r = md5_gg(r, i, o, a, e[n + 12], 20, -1926607734), i, o, e[n + 5], 4, -378558),
    o = md5_hh(o, a, r, i, e[n + 8], 11, -2022574463),
    i = md5_hh(i, o, a, r, e[n + 11], 16, 1839030562),
    r = md5_hh(r, i, o, a, e[n + 14], 23, -35309556),
    a = md5_hh(a, r, i, o, e[n + 1], 4, -1530992060),
    o = md5_hh(o, a, r, i, e[n + 4], 11, 1272893353),
    i = md5_hh(i, o, a, r, e[n + 7], 16, -155497632),
    r = md5_hh(r, i, o, a, e[n + 10], 23, -1094730640),
    a = md5_hh(a, r, i, o, e[n + 13], 4, 681279174),
    o = md5_hh(o, a, r, i, e[n + 0], 11, -358537222),
    i = md5_hh(i, o, a, r, e[n + 3], 16, -722521979),
    r = md5_hh(r, i, o, a, e[n + 6], 23, 76029189),
    a = md5_hh(a, r, i, o, e[n + 9], 4, -640364487),
    o = md5_hh(o, a, r, i, e[n + 12], 11, -421815835),
    i = md5_hh(i, o, a, r, e[n + 15], 16, 530742520),
    a = md5_ii(a, r = md5_hh(r, i, o, a, e[n + 2], 23, -995338651), i, o, e[n + 0], 6, -198630844),
    o = md5_ii(o, a, r, i, e[n + 7], 10, 1126891415),
    i = md5_ii(i, o, a, r, e[n + 14], 15, -1416354905),
    r = md5_ii(r, i, o, a, e[n + 5], 21, -57434055),
    a = md5_ii(a, r, i, o, e[n + 12], 6, 1700485571),
    o = md5_ii(o, a, r, i, e[n + 3], 10, -1894986606),
    i = md5_ii(i, o, a, r, e[n + 10], 15, -1051523),
    r = md5_ii(r, i, o, a, e[n + 1], 21, -2054922799),
    a = md5_ii(a, r, i, o, e[n + 8], 6, 1873313359),
    o = md5_ii(o, a, r, i, e[n + 15], 10, -30611744),
    i = md5_ii(i, o, a, r, e[n + 6], 15, -1560198380),
    r = md5_ii(r, i, o, a, e[n + 13], 21, 1309151649),
    a = md5_ii(a, r, i, o, e[n + 4], 6, -145523070),
    o = md5_ii(o, a, r, i, e[n + 11], 10, -1120210379),
    i = md5_ii(i, o, a, r, e[n + 2], 15, 718787259),
    r = md5_ii(r, i, o, a, e[n + 9], 21, -343485551),
    a = safe_add(a, s),
    r = safe_add(r, l),
    i = safe_add(i, c),
    o = safe_add(o, p)
}
return Array(a, r, i, o)
}
function md5_cmn(e, t, a, r, i, o) {
return safe_add(bit_rol(safe_add(safe_add(t, e), safe_add(r, o)), i), a)
}
function md5_ff(e, t, a, r, i, o, n) {
return md5_cmn(t & a | ~t & r, e, t, i, o, n)
}
function md5_gg(e, t, a, r, i, o, n) {
return md5_cmn(t & r | a & ~r, e, t, i, o, n)
}
function md5_hh(e, t, a, r, i, o, n) {
return md5_cmn(t ^ a ^ r, e, t, i, o, n)
}
function md5_ii(e, t, a, r, i, o, n) {
return md5_cmn(a ^ (t | ~r), e, t, i, o, n)
}
function safe_add(e, t) {
var a = (65535 & e) + (65535 & t),
r;
return (e >> 16) + (t >> 16) + (a >> 16) << 16 | 65535 & a
}
function bit_rol(e, t) {
return e << t | e >>> 32 - t
}
function binl2hex(e) {
for (var t = "0123456789abcdef",
a = "",
r = 0; r < 4 * e.length; r++) a += t.charAt(e[r >> 2] >> r % 4 * 8 + 4 & 15) + t.charAt(e[r >> 2] >> r % 4 * 8 & 15);
return a
}
///////////
function md5(e) {

return binl2hex(core_md5(str2binl(e), e.length * chrsz))
}