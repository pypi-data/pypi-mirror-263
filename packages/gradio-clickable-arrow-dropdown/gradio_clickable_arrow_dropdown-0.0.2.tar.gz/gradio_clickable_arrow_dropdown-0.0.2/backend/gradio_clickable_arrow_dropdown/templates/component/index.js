function we() {
}
function _r(e) {
  return e();
}
function mr(e) {
  e.forEach(_r);
}
function dr(e) {
  return typeof e == "function";
}
function br(e, t) {
  return e != e ? t == t : e !== t || e && typeof e == "object" || typeof e == "function";
}
function gr(e, ...t) {
  if (e == null) {
    for (const i of t)
      i(void 0);
    return we;
  }
  const n = e.subscribe(...t);
  return n.unsubscribe ? () => n.unsubscribe() : n;
}
function pn(e) {
  const t = typeof e == "string" && e.match(/^\s*(-?[\d.]+)([^\s]*)\s*$/);
  return t ? [parseFloat(t[1]), t[2] || "px"] : [
    /** @type {number} */
    e,
    "px"
  ];
}
const Hi = typeof window < "u";
let vn = Hi ? () => window.performance.now() : () => Date.now(), Bi = Hi ? (e) => requestAnimationFrame(e) : we;
const Le = /* @__PURE__ */ new Set();
function Pi(e) {
  Le.forEach((t) => {
    t.c(e) || (Le.delete(t), t.f());
  }), Le.size !== 0 && Bi(Pi);
}
function pr(e) {
  let t;
  return Le.size === 0 && Bi(Pi), {
    promise: new Promise((n) => {
      Le.add(t = { c: e, f: n });
    }),
    abort() {
      Le.delete(t);
    }
  };
}
function vr(e) {
  const t = e - 1;
  return t * t * t + 1;
}
function yn(e, { delay: t = 0, duration: n = 400, easing: i = vr, x: r = 0, y: l = 0, opacity: a = 0 } = {}) {
  const o = getComputedStyle(e), s = +o.opacity, u = o.transform === "none" ? "" : o.transform, f = s * (1 - a), [_, c] = pn(r), [d, v] = pn(l);
  return {
    delay: t,
    duration: n,
    easing: i,
    css: (y, b) => `
			transform: ${u} translate(${(1 - y) * _}${c}, ${(1 - y) * d}${v});
			opacity: ${s - f * b}`
  };
}
const Te = [];
function yr(e, t) {
  return {
    subscribe: it(e, t).subscribe
  };
}
function it(e, t = we) {
  let n;
  const i = /* @__PURE__ */ new Set();
  function r(o) {
    if (br(e, o) && (e = o, n)) {
      const s = !Te.length;
      for (const u of i)
        u[1](), Te.push(u, e);
      if (s) {
        for (let u = 0; u < Te.length; u += 2)
          Te[u][0](Te[u + 1]);
        Te.length = 0;
      }
    }
  }
  function l(o) {
    r(o(e));
  }
  function a(o, s = we) {
    const u = [o, s];
    return i.add(u), i.size === 1 && (n = t(r, l) || we), o(e), () => {
      i.delete(u), i.size === 0 && n && (n(), n = null);
    };
  }
  return { set: r, update: l, subscribe: a };
}
function Ve(e, t, n) {
  const i = !Array.isArray(e), r = i ? [e] : e;
  if (!r.every(Boolean))
    throw new Error("derived() expects stores as input, got a falsy value");
  const l = t.length < 2;
  return yr(n, (a, o) => {
    let s = !1;
    const u = [];
    let f = 0, _ = we;
    const c = () => {
      if (f)
        return;
      _();
      const v = t(i ? u[0] : u, a, o);
      l ? a(v) : _ = dr(v) ? v : we;
    }, d = r.map(
      (v, y) => gr(
        v,
        (b) => {
          u[y] = b, f &= ~(1 << y), s && c();
        },
        () => {
          f |= 1 << y;
        }
      )
    );
    return s = !0, c(), function() {
      mr(d), _(), s = !1;
    };
  });
}
function wn(e) {
  return Object.prototype.toString.call(e) === "[object Date]";
}
function Xt(e, t, n, i) {
  if (typeof n == "number" || wn(n)) {
    const r = i - n, l = (n - t) / (e.dt || 1 / 60), a = e.opts.stiffness * r, o = e.opts.damping * l, s = (a - o) * e.inv_mass, u = (l + s) * e.dt;
    return Math.abs(u) < e.opts.precision && Math.abs(r) < e.opts.precision ? i : (e.settled = !1, wn(n) ? new Date(n.getTime() + u) : n + u);
  } else {
    if (Array.isArray(n))
      return n.map(
        (r, l) => Xt(e, t[l], n[l], i[l])
      );
    if (typeof n == "object") {
      const r = {};
      for (const l in n)
        r[l] = Xt(e, t[l], n[l], i[l]);
      return r;
    } else
      throw new Error(`Cannot spring ${typeof n} values`);
  }
}
function En(e, t = {}) {
  const n = it(e), { stiffness: i = 0.15, damping: r = 0.8, precision: l = 0.01 } = t;
  let a, o, s, u = e, f = e, _ = 1, c = 0, d = !1;
  function v(b, g = {}) {
    f = b;
    const E = s = {};
    return e == null || g.hard || y.stiffness >= 1 && y.damping >= 1 ? (d = !0, a = vn(), u = b, n.set(e = f), Promise.resolve()) : (g.soft && (c = 1 / ((g.soft === !0 ? 0.5 : +g.soft) * 60), _ = 0), o || (a = vn(), d = !1, o = pr((h) => {
      if (d)
        return d = !1, o = null, !1;
      _ = Math.min(_ + c, 1);
      const m = {
        inv_mass: _,
        opts: y,
        settled: !0,
        dt: (h - a) * 60 / 1e3
      }, S = Xt(m, u, e, f);
      return a = h, u = e, n.set(e = S), m.settled && (o = null), !m.settled;
    })), new Promise((h) => {
      o.promise.then(() => {
        E === s && h();
      });
    }));
  }
  const y = {
    set: v,
    update: (b, g) => v(b(f, e), g),
    subscribe: n.subscribe,
    stiffness: i,
    damping: r,
    precision: l
  };
  return y;
}
function wr(e) {
  return e && e.__esModule && Object.prototype.hasOwnProperty.call(e, "default") ? e.default : e;
}
var Er = function(t) {
  return Sr(t) && !Tr(t);
};
function Sr(e) {
  return !!e && typeof e == "object";
}
function Tr(e) {
  var t = Object.prototype.toString.call(e);
  return t === "[object RegExp]" || t === "[object Date]" || Br(e);
}
var Ar = typeof Symbol == "function" && Symbol.for, Hr = Ar ? Symbol.for("react.element") : 60103;
function Br(e) {
  return e.$$typeof === Hr;
}
function Pr(e) {
  return Array.isArray(e) ? [] : {};
}
function Ke(e, t) {
  return t.clone !== !1 && t.isMergeableObject(e) ? De(Pr(e), e, t) : e;
}
function Nr(e, t, n) {
  return e.concat(t).map(function(i) {
    return Ke(i, n);
  });
}
function kr(e, t) {
  if (!t.customMerge)
    return De;
  var n = t.customMerge(e);
  return typeof n == "function" ? n : De;
}
function Cr(e) {
  return Object.getOwnPropertySymbols ? Object.getOwnPropertySymbols(e).filter(function(t) {
    return Object.propertyIsEnumerable.call(e, t);
  }) : [];
}
function Sn(e) {
  return Object.keys(e).concat(Cr(e));
}
function Ni(e, t) {
  try {
    return t in e;
  } catch {
    return !1;
  }
}
function Or(e, t) {
  return Ni(e, t) && !(Object.hasOwnProperty.call(e, t) && Object.propertyIsEnumerable.call(e, t));
}
function Ir(e, t, n) {
  var i = {};
  return n.isMergeableObject(e) && Sn(e).forEach(function(r) {
    i[r] = Ke(e[r], n);
  }), Sn(t).forEach(function(r) {
    Or(e, r) || (Ni(e, r) && n.isMergeableObject(t[r]) ? i[r] = kr(r, n)(e[r], t[r], n) : i[r] = Ke(t[r], n));
  }), i;
}
function De(e, t, n) {
  n = n || {}, n.arrayMerge = n.arrayMerge || Nr, n.isMergeableObject = n.isMergeableObject || Er, n.cloneUnlessOtherwiseSpecified = Ke;
  var i = Array.isArray(t), r = Array.isArray(e), l = i === r;
  return l ? i ? n.arrayMerge(e, t, n) : Ir(e, t, n) : Ke(t, n);
}
De.all = function(t, n) {
  if (!Array.isArray(t))
    throw new Error("first argument should be an array");
  return t.reduce(function(i, r) {
    return De(i, r, n);
  }, {});
};
var Lr = De, Mr = Lr;
const Rr = /* @__PURE__ */ wr(Mr);
var zt = function(e, t) {
  return zt = Object.setPrototypeOf || { __proto__: [] } instanceof Array && function(n, i) {
    n.__proto__ = i;
  } || function(n, i) {
    for (var r in i)
      Object.prototype.hasOwnProperty.call(i, r) && (n[r] = i[r]);
  }, zt(e, t);
};
function At(e, t) {
  if (typeof t != "function" && t !== null)
    throw new TypeError("Class extends value " + String(t) + " is not a constructor or null");
  zt(e, t);
  function n() {
    this.constructor = e;
  }
  e.prototype = t === null ? Object.create(t) : (n.prototype = t.prototype, new n());
}
var R = function() {
  return R = Object.assign || function(t) {
    for (var n, i = 1, r = arguments.length; i < r; i++) {
      n = arguments[i];
      for (var l in n)
        Object.prototype.hasOwnProperty.call(n, l) && (t[l] = n[l]);
    }
    return t;
  }, R.apply(this, arguments);
};
function It(e, t, n) {
  if (n || arguments.length === 2)
    for (var i = 0, r = t.length, l; i < r; i++)
      (l || !(i in t)) && (l || (l = Array.prototype.slice.call(t, 0, i)), l[i] = t[i]);
  return e.concat(l || Array.prototype.slice.call(t));
}
var I;
(function(e) {
  e[e.EXPECT_ARGUMENT_CLOSING_BRACE = 1] = "EXPECT_ARGUMENT_CLOSING_BRACE", e[e.EMPTY_ARGUMENT = 2] = "EMPTY_ARGUMENT", e[e.MALFORMED_ARGUMENT = 3] = "MALFORMED_ARGUMENT", e[e.EXPECT_ARGUMENT_TYPE = 4] = "EXPECT_ARGUMENT_TYPE", e[e.INVALID_ARGUMENT_TYPE = 5] = "INVALID_ARGUMENT_TYPE", e[e.EXPECT_ARGUMENT_STYLE = 6] = "EXPECT_ARGUMENT_STYLE", e[e.INVALID_NUMBER_SKELETON = 7] = "INVALID_NUMBER_SKELETON", e[e.INVALID_DATE_TIME_SKELETON = 8] = "INVALID_DATE_TIME_SKELETON", e[e.EXPECT_NUMBER_SKELETON = 9] = "EXPECT_NUMBER_SKELETON", e[e.EXPECT_DATE_TIME_SKELETON = 10] = "EXPECT_DATE_TIME_SKELETON", e[e.UNCLOSED_QUOTE_IN_ARGUMENT_STYLE = 11] = "UNCLOSED_QUOTE_IN_ARGUMENT_STYLE", e[e.EXPECT_SELECT_ARGUMENT_OPTIONS = 12] = "EXPECT_SELECT_ARGUMENT_OPTIONS", e[e.EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE = 13] = "EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE", e[e.INVALID_PLURAL_ARGUMENT_OFFSET_VALUE = 14] = "INVALID_PLURAL_ARGUMENT_OFFSET_VALUE", e[e.EXPECT_SELECT_ARGUMENT_SELECTOR = 15] = "EXPECT_SELECT_ARGUMENT_SELECTOR", e[e.EXPECT_PLURAL_ARGUMENT_SELECTOR = 16] = "EXPECT_PLURAL_ARGUMENT_SELECTOR", e[e.EXPECT_SELECT_ARGUMENT_SELECTOR_FRAGMENT = 17] = "EXPECT_SELECT_ARGUMENT_SELECTOR_FRAGMENT", e[e.EXPECT_PLURAL_ARGUMENT_SELECTOR_FRAGMENT = 18] = "EXPECT_PLURAL_ARGUMENT_SELECTOR_FRAGMENT", e[e.INVALID_PLURAL_ARGUMENT_SELECTOR = 19] = "INVALID_PLURAL_ARGUMENT_SELECTOR", e[e.DUPLICATE_PLURAL_ARGUMENT_SELECTOR = 20] = "DUPLICATE_PLURAL_ARGUMENT_SELECTOR", e[e.DUPLICATE_SELECT_ARGUMENT_SELECTOR = 21] = "DUPLICATE_SELECT_ARGUMENT_SELECTOR", e[e.MISSING_OTHER_CLAUSE = 22] = "MISSING_OTHER_CLAUSE", e[e.INVALID_TAG = 23] = "INVALID_TAG", e[e.INVALID_TAG_NAME = 25] = "INVALID_TAG_NAME", e[e.UNMATCHED_CLOSING_TAG = 26] = "UNMATCHED_CLOSING_TAG", e[e.UNCLOSED_TAG = 27] = "UNCLOSED_TAG";
})(I || (I = {}));
var U;
(function(e) {
  e[e.literal = 0] = "literal", e[e.argument = 1] = "argument", e[e.number = 2] = "number", e[e.date = 3] = "date", e[e.time = 4] = "time", e[e.select = 5] = "select", e[e.plural = 6] = "plural", e[e.pound = 7] = "pound", e[e.tag = 8] = "tag";
})(U || (U = {}));
var Ue;
(function(e) {
  e[e.number = 0] = "number", e[e.dateTime = 1] = "dateTime";
})(Ue || (Ue = {}));
function Tn(e) {
  return e.type === U.literal;
}
function Dr(e) {
  return e.type === U.argument;
}
function ki(e) {
  return e.type === U.number;
}
function Ci(e) {
  return e.type === U.date;
}
function Oi(e) {
  return e.type === U.time;
}
function Ii(e) {
  return e.type === U.select;
}
function Li(e) {
  return e.type === U.plural;
}
function Ur(e) {
  return e.type === U.pound;
}
function Mi(e) {
  return e.type === U.tag;
}
function Ri(e) {
  return !!(e && typeof e == "object" && e.type === Ue.number);
}
function Zt(e) {
  return !!(e && typeof e == "object" && e.type === Ue.dateTime);
}
var Di = /[ \xA0\u1680\u2000-\u200A\u202F\u205F\u3000]/, Gr = /(?:[Eec]{1,6}|G{1,5}|[Qq]{1,5}|(?:[yYur]+|U{1,5})|[ML]{1,5}|d{1,2}|D{1,3}|F{1}|[abB]{1,5}|[hkHK]{1,2}|w{1,2}|W{1}|m{1,2}|s{1,2}|[zZOvVxX]{1,4})(?=([^']*'[^']*')*[^']*$)/g;
function Fr(e) {
  var t = {};
  return e.replace(Gr, function(n) {
    var i = n.length;
    switch (n[0]) {
      case "G":
        t.era = i === 4 ? "long" : i === 5 ? "narrow" : "short";
        break;
      case "y":
        t.year = i === 2 ? "2-digit" : "numeric";
        break;
      case "Y":
      case "u":
      case "U":
      case "r":
        throw new RangeError("`Y/u/U/r` (year) patterns are not supported, use `y` instead");
      case "q":
      case "Q":
        throw new RangeError("`q/Q` (quarter) patterns are not supported");
      case "M":
      case "L":
        t.month = ["numeric", "2-digit", "short", "long", "narrow"][i - 1];
        break;
      case "w":
      case "W":
        throw new RangeError("`w/W` (week) patterns are not supported");
      case "d":
        t.day = ["numeric", "2-digit"][i - 1];
        break;
      case "D":
      case "F":
      case "g":
        throw new RangeError("`D/F/g` (day) patterns are not supported, use `d` instead");
      case "E":
        t.weekday = i === 4 ? "short" : i === 5 ? "narrow" : "short";
        break;
      case "e":
        if (i < 4)
          throw new RangeError("`e..eee` (weekday) patterns are not supported");
        t.weekday = ["short", "long", "narrow", "short"][i - 4];
        break;
      case "c":
        if (i < 4)
          throw new RangeError("`c..ccc` (weekday) patterns are not supported");
        t.weekday = ["short", "long", "narrow", "short"][i - 4];
        break;
      case "a":
        t.hour12 = !0;
        break;
      case "b":
      case "B":
        throw new RangeError("`b/B` (period) patterns are not supported, use `a` instead");
      case "h":
        t.hourCycle = "h12", t.hour = ["numeric", "2-digit"][i - 1];
        break;
      case "H":
        t.hourCycle = "h23", t.hour = ["numeric", "2-digit"][i - 1];
        break;
      case "K":
        t.hourCycle = "h11", t.hour = ["numeric", "2-digit"][i - 1];
        break;
      case "k":
        t.hourCycle = "h24", t.hour = ["numeric", "2-digit"][i - 1];
        break;
      case "j":
      case "J":
      case "C":
        throw new RangeError("`j/J/C` (hour) patterns are not supported, use `h/H/K/k` instead");
      case "m":
        t.minute = ["numeric", "2-digit"][i - 1];
        break;
      case "s":
        t.second = ["numeric", "2-digit"][i - 1];
        break;
      case "S":
      case "A":
        throw new RangeError("`S/A` (second) patterns are not supported, use `s` instead");
      case "z":
        t.timeZoneName = i < 4 ? "short" : "long";
        break;
      case "Z":
      case "O":
      case "v":
      case "V":
      case "X":
      case "x":
        throw new RangeError("`Z/O/v/V/X/x` (timeZone) patterns are not supported, use `z` instead");
    }
    return "";
  }), t;
}
var xr = /[\t-\r \x85\u200E\u200F\u2028\u2029]/i;
function jr(e) {
  if (e.length === 0)
    throw new Error("Number skeleton cannot be empty");
  for (var t = e.split(xr).filter(function(c) {
    return c.length > 0;
  }), n = [], i = 0, r = t; i < r.length; i++) {
    var l = r[i], a = l.split("/");
    if (a.length === 0)
      throw new Error("Invalid number skeleton");
    for (var o = a[0], s = a.slice(1), u = 0, f = s; u < f.length; u++) {
      var _ = f[u];
      if (_.length === 0)
        throw new Error("Invalid number skeleton");
    }
    n.push({ stem: o, options: s });
  }
  return n;
}
function Vr(e) {
  return e.replace(/^(.*?)-/, "");
}
var An = /^\.(?:(0+)(\*)?|(#+)|(0+)(#+))$/g, Ui = /^(@+)?(\+|#+)?[rs]?$/g, qr = /(\*)(0+)|(#+)(0+)|(0+)/g, Gi = /^(0+)$/;
function Hn(e) {
  var t = {};
  return e[e.length - 1] === "r" ? t.roundingPriority = "morePrecision" : e[e.length - 1] === "s" && (t.roundingPriority = "lessPrecision"), e.replace(Ui, function(n, i, r) {
    return typeof r != "string" ? (t.minimumSignificantDigits = i.length, t.maximumSignificantDigits = i.length) : r === "+" ? t.minimumSignificantDigits = i.length : i[0] === "#" ? t.maximumSignificantDigits = i.length : (t.minimumSignificantDigits = i.length, t.maximumSignificantDigits = i.length + (typeof r == "string" ? r.length : 0)), "";
  }), t;
}
function Fi(e) {
  switch (e) {
    case "sign-auto":
      return {
        signDisplay: "auto"
      };
    case "sign-accounting":
    case "()":
      return {
        currencySign: "accounting"
      };
    case "sign-always":
    case "+!":
      return {
        signDisplay: "always"
      };
    case "sign-accounting-always":
    case "()!":
      return {
        signDisplay: "always",
        currencySign: "accounting"
      };
    case "sign-except-zero":
    case "+?":
      return {
        signDisplay: "exceptZero"
      };
    case "sign-accounting-except-zero":
    case "()?":
      return {
        signDisplay: "exceptZero",
        currencySign: "accounting"
      };
    case "sign-never":
    case "+_":
      return {
        signDisplay: "never"
      };
  }
}
function Xr(e) {
  var t;
  if (e[0] === "E" && e[1] === "E" ? (t = {
    notation: "engineering"
  }, e = e.slice(2)) : e[0] === "E" && (t = {
    notation: "scientific"
  }, e = e.slice(1)), t) {
    var n = e.slice(0, 2);
    if (n === "+!" ? (t.signDisplay = "always", e = e.slice(2)) : n === "+?" && (t.signDisplay = "exceptZero", e = e.slice(2)), !Gi.test(e))
      throw new Error("Malformed concise eng/scientific notation");
    t.minimumIntegerDigits = e.length;
  }
  return t;
}
function Bn(e) {
  var t = {}, n = Fi(e);
  return n || t;
}
function zr(e) {
  for (var t = {}, n = 0, i = e; n < i.length; n++) {
    var r = i[n];
    switch (r.stem) {
      case "percent":
      case "%":
        t.style = "percent";
        continue;
      case "%x100":
        t.style = "percent", t.scale = 100;
        continue;
      case "currency":
        t.style = "currency", t.currency = r.options[0];
        continue;
      case "group-off":
      case ",_":
        t.useGrouping = !1;
        continue;
      case "precision-integer":
      case ".":
        t.maximumFractionDigits = 0;
        continue;
      case "measure-unit":
      case "unit":
        t.style = "unit", t.unit = Vr(r.options[0]);
        continue;
      case "compact-short":
      case "K":
        t.notation = "compact", t.compactDisplay = "short";
        continue;
      case "compact-long":
      case "KK":
        t.notation = "compact", t.compactDisplay = "long";
        continue;
      case "scientific":
        t = R(R(R({}, t), { notation: "scientific" }), r.options.reduce(function(s, u) {
          return R(R({}, s), Bn(u));
        }, {}));
        continue;
      case "engineering":
        t = R(R(R({}, t), { notation: "engineering" }), r.options.reduce(function(s, u) {
          return R(R({}, s), Bn(u));
        }, {}));
        continue;
      case "notation-simple":
        t.notation = "standard";
        continue;
      case "unit-width-narrow":
        t.currencyDisplay = "narrowSymbol", t.unitDisplay = "narrow";
        continue;
      case "unit-width-short":
        t.currencyDisplay = "code", t.unitDisplay = "short";
        continue;
      case "unit-width-full-name":
        t.currencyDisplay = "name", t.unitDisplay = "long";
        continue;
      case "unit-width-iso-code":
        t.currencyDisplay = "symbol";
        continue;
      case "scale":
        t.scale = parseFloat(r.options[0]);
        continue;
      case "integer-width":
        if (r.options.length > 1)
          throw new RangeError("integer-width stems only accept a single optional option");
        r.options[0].replace(qr, function(s, u, f, _, c, d) {
          if (u)
            t.minimumIntegerDigits = f.length;
          else {
            if (_ && c)
              throw new Error("We currently do not support maximum integer digits");
            if (d)
              throw new Error("We currently do not support exact integer digits");
          }
          return "";
        });
        continue;
    }
    if (Gi.test(r.stem)) {
      t.minimumIntegerDigits = r.stem.length;
      continue;
    }
    if (An.test(r.stem)) {
      if (r.options.length > 1)
        throw new RangeError("Fraction-precision stems only accept a single optional option");
      r.stem.replace(An, function(s, u, f, _, c, d) {
        return f === "*" ? t.minimumFractionDigits = u.length : _ && _[0] === "#" ? t.maximumFractionDigits = _.length : c && d ? (t.minimumFractionDigits = c.length, t.maximumFractionDigits = c.length + d.length) : (t.minimumFractionDigits = u.length, t.maximumFractionDigits = u.length), "";
      });
      var l = r.options[0];
      l === "w" ? t = R(R({}, t), { trailingZeroDisplay: "stripIfInteger" }) : l && (t = R(R({}, t), Hn(l)));
      continue;
    }
    if (Ui.test(r.stem)) {
      t = R(R({}, t), Hn(r.stem));
      continue;
    }
    var a = Fi(r.stem);
    a && (t = R(R({}, t), a));
    var o = Xr(r.stem);
    o && (t = R(R({}, t), o));
  }
  return t;
}
var st = {
  AX: [
    "H"
  ],
  BQ: [
    "H"
  ],
  CP: [
    "H"
  ],
  CZ: [
    "H"
  ],
  DK: [
    "H"
  ],
  FI: [
    "H"
  ],
  ID: [
    "H"
  ],
  IS: [
    "H"
  ],
  ML: [
    "H"
  ],
  NE: [
    "H"
  ],
  RU: [
    "H"
  ],
  SE: [
    "H"
  ],
  SJ: [
    "H"
  ],
  SK: [
    "H"
  ],
  AS: [
    "h",
    "H"
  ],
  BT: [
    "h",
    "H"
  ],
  DJ: [
    "h",
    "H"
  ],
  ER: [
    "h",
    "H"
  ],
  GH: [
    "h",
    "H"
  ],
  IN: [
    "h",
    "H"
  ],
  LS: [
    "h",
    "H"
  ],
  PG: [
    "h",
    "H"
  ],
  PW: [
    "h",
    "H"
  ],
  SO: [
    "h",
    "H"
  ],
  TO: [
    "h",
    "H"
  ],
  VU: [
    "h",
    "H"
  ],
  WS: [
    "h",
    "H"
  ],
  "001": [
    "H",
    "h"
  ],
  AL: [
    "h",
    "H",
    "hB"
  ],
  TD: [
    "h",
    "H",
    "hB"
  ],
  "ca-ES": [
    "H",
    "h",
    "hB"
  ],
  CF: [
    "H",
    "h",
    "hB"
  ],
  CM: [
    "H",
    "h",
    "hB"
  ],
  "fr-CA": [
    "H",
    "h",
    "hB"
  ],
  "gl-ES": [
    "H",
    "h",
    "hB"
  ],
  "it-CH": [
    "H",
    "h",
    "hB"
  ],
  "it-IT": [
    "H",
    "h",
    "hB"
  ],
  LU: [
    "H",
    "h",
    "hB"
  ],
  NP: [
    "H",
    "h",
    "hB"
  ],
  PF: [
    "H",
    "h",
    "hB"
  ],
  SC: [
    "H",
    "h",
    "hB"
  ],
  SM: [
    "H",
    "h",
    "hB"
  ],
  SN: [
    "H",
    "h",
    "hB"
  ],
  TF: [
    "H",
    "h",
    "hB"
  ],
  VA: [
    "H",
    "h",
    "hB"
  ],
  CY: [
    "h",
    "H",
    "hb",
    "hB"
  ],
  GR: [
    "h",
    "H",
    "hb",
    "hB"
  ],
  CO: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  DO: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  KP: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  KR: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  NA: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  PA: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  PR: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  VE: [
    "h",
    "H",
    "hB",
    "hb"
  ],
  AC: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  AI: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  BW: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  BZ: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  CC: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  CK: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  CX: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  DG: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  FK: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  GB: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  GG: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  GI: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  IE: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  IM: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  IO: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  JE: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  LT: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  MK: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  MN: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  MS: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  NF: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  NG: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  NR: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  NU: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  PN: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  SH: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  SX: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  TA: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  ZA: [
    "H",
    "h",
    "hb",
    "hB"
  ],
  "af-ZA": [
    "H",
    "h",
    "hB",
    "hb"
  ],
  AR: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  CL: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  CR: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  CU: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  EA: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  "es-BO": [
    "H",
    "h",
    "hB",
    "hb"
  ],
  "es-BR": [
    "H",
    "h",
    "hB",
    "hb"
  ],
  "es-EC": [
    "H",
    "h",
    "hB",
    "hb"
  ],
  "es-ES": [
    "H",
    "h",
    "hB",
    "hb"
  ],
  "es-GQ": [
    "H",
    "h",
    "hB",
    "hb"
  ],
  "es-PE": [
    "H",
    "h",
    "hB",
    "hb"
  ],
  GT: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  HN: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  IC: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  KG: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  KM: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  LK: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  MA: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  MX: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  NI: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  PY: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  SV: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  UY: [
    "H",
    "h",
    "hB",
    "hb"
  ],
  JP: [
    "H",
    "h",
    "K"
  ],
  AD: [
    "H",
    "hB"
  ],
  AM: [
    "H",
    "hB"
  ],
  AO: [
    "H",
    "hB"
  ],
  AT: [
    "H",
    "hB"
  ],
  AW: [
    "H",
    "hB"
  ],
  BE: [
    "H",
    "hB"
  ],
  BF: [
    "H",
    "hB"
  ],
  BJ: [
    "H",
    "hB"
  ],
  BL: [
    "H",
    "hB"
  ],
  BR: [
    "H",
    "hB"
  ],
  CG: [
    "H",
    "hB"
  ],
  CI: [
    "H",
    "hB"
  ],
  CV: [
    "H",
    "hB"
  ],
  DE: [
    "H",
    "hB"
  ],
  EE: [
    "H",
    "hB"
  ],
  FR: [
    "H",
    "hB"
  ],
  GA: [
    "H",
    "hB"
  ],
  GF: [
    "H",
    "hB"
  ],
  GN: [
    "H",
    "hB"
  ],
  GP: [
    "H",
    "hB"
  ],
  GW: [
    "H",
    "hB"
  ],
  HR: [
    "H",
    "hB"
  ],
  IL: [
    "H",
    "hB"
  ],
  IT: [
    "H",
    "hB"
  ],
  KZ: [
    "H",
    "hB"
  ],
  MC: [
    "H",
    "hB"
  ],
  MD: [
    "H",
    "hB"
  ],
  MF: [
    "H",
    "hB"
  ],
  MQ: [
    "H",
    "hB"
  ],
  MZ: [
    "H",
    "hB"
  ],
  NC: [
    "H",
    "hB"
  ],
  NL: [
    "H",
    "hB"
  ],
  PM: [
    "H",
    "hB"
  ],
  PT: [
    "H",
    "hB"
  ],
  RE: [
    "H",
    "hB"
  ],
  RO: [
    "H",
    "hB"
  ],
  SI: [
    "H",
    "hB"
  ],
  SR: [
    "H",
    "hB"
  ],
  ST: [
    "H",
    "hB"
  ],
  TG: [
    "H",
    "hB"
  ],
  TR: [
    "H",
    "hB"
  ],
  WF: [
    "H",
    "hB"
  ],
  YT: [
    "H",
    "hB"
  ],
  BD: [
    "h",
    "hB",
    "H"
  ],
  PK: [
    "h",
    "hB",
    "H"
  ],
  AZ: [
    "H",
    "hB",
    "h"
  ],
  BA: [
    "H",
    "hB",
    "h"
  ],
  BG: [
    "H",
    "hB",
    "h"
  ],
  CH: [
    "H",
    "hB",
    "h"
  ],
  GE: [
    "H",
    "hB",
    "h"
  ],
  LI: [
    "H",
    "hB",
    "h"
  ],
  ME: [
    "H",
    "hB",
    "h"
  ],
  RS: [
    "H",
    "hB",
    "h"
  ],
  UA: [
    "H",
    "hB",
    "h"
  ],
  UZ: [
    "H",
    "hB",
    "h"
  ],
  XK: [
    "H",
    "hB",
    "h"
  ],
  AG: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  AU: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  BB: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  BM: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  BS: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  CA: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  DM: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  "en-001": [
    "h",
    "hb",
    "H",
    "hB"
  ],
  FJ: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  FM: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  GD: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  GM: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  GU: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  GY: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  JM: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  KI: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  KN: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  KY: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  LC: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  LR: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  MH: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  MP: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  MW: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  NZ: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  SB: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  SG: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  SL: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  SS: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  SZ: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  TC: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  TT: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  UM: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  US: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  VC: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  VG: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  VI: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  ZM: [
    "h",
    "hb",
    "H",
    "hB"
  ],
  BO: [
    "H",
    "hB",
    "h",
    "hb"
  ],
  EC: [
    "H",
    "hB",
    "h",
    "hb"
  ],
  ES: [
    "H",
    "hB",
    "h",
    "hb"
  ],
  GQ: [
    "H",
    "hB",
    "h",
    "hb"
  ],
  PE: [
    "H",
    "hB",
    "h",
    "hb"
  ],
  AE: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  "ar-001": [
    "h",
    "hB",
    "hb",
    "H"
  ],
  BH: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  DZ: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  EG: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  EH: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  HK: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  IQ: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  JO: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  KW: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  LB: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  LY: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  MO: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  MR: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  OM: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  PH: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  PS: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  QA: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  SA: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  SD: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  SY: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  TN: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  YE: [
    "h",
    "hB",
    "hb",
    "H"
  ],
  AF: [
    "H",
    "hb",
    "hB",
    "h"
  ],
  LA: [
    "H",
    "hb",
    "hB",
    "h"
  ],
  CN: [
    "H",
    "hB",
    "hb",
    "h"
  ],
  LV: [
    "H",
    "hB",
    "hb",
    "h"
  ],
  TL: [
    "H",
    "hB",
    "hb",
    "h"
  ],
  "zu-ZA": [
    "H",
    "hB",
    "hb",
    "h"
  ],
  CD: [
    "hB",
    "H"
  ],
  IR: [
    "hB",
    "H"
  ],
  "hi-IN": [
    "hB",
    "h",
    "H"
  ],
  "kn-IN": [
    "hB",
    "h",
    "H"
  ],
  "ml-IN": [
    "hB",
    "h",
    "H"
  ],
  "te-IN": [
    "hB",
    "h",
    "H"
  ],
  KH: [
    "hB",
    "h",
    "H",
    "hb"
  ],
  "ta-IN": [
    "hB",
    "h",
    "hb",
    "H"
  ],
  BN: [
    "hb",
    "hB",
    "h",
    "H"
  ],
  MY: [
    "hb",
    "hB",
    "h",
    "H"
  ],
  ET: [
    "hB",
    "hb",
    "h",
    "H"
  ],
  "gu-IN": [
    "hB",
    "hb",
    "h",
    "H"
  ],
  "mr-IN": [
    "hB",
    "hb",
    "h",
    "H"
  ],
  "pa-IN": [
    "hB",
    "hb",
    "h",
    "H"
  ],
  TW: [
    "hB",
    "hb",
    "h",
    "H"
  ],
  KE: [
    "hB",
    "hb",
    "H",
    "h"
  ],
  MM: [
    "hB",
    "hb",
    "H",
    "h"
  ],
  TZ: [
    "hB",
    "hb",
    "H",
    "h"
  ],
  UG: [
    "hB",
    "hb",
    "H",
    "h"
  ]
};
function Zr(e, t) {
  for (var n = "", i = 0; i < e.length; i++) {
    var r = e.charAt(i);
    if (r === "j") {
      for (var l = 0; i + 1 < e.length && e.charAt(i + 1) === r; )
        l++, i++;
      var a = 1 + (l & 1), o = l < 2 ? 1 : 3 + (l >> 1), s = "a", u = Wr(t);
      for ((u == "H" || u == "k") && (o = 0); o-- > 0; )
        n += s;
      for (; a-- > 0; )
        n = u + n;
    } else
      r === "J" ? n += "H" : n += r;
  }
  return n;
}
function Wr(e) {
  var t = e.hourCycle;
  if (t === void 0 && // @ts-ignore hourCycle(s) is not identified yet
  e.hourCycles && // @ts-ignore
  e.hourCycles.length && (t = e.hourCycles[0]), t)
    switch (t) {
      case "h24":
        return "k";
      case "h23":
        return "H";
      case "h12":
        return "h";
      case "h11":
        return "K";
      default:
        throw new Error("Invalid hourCycle");
    }
  var n = e.language, i;
  n !== "root" && (i = e.maximize().region);
  var r = st[i || ""] || st[n || ""] || st["".concat(n, "-001")] || st["001"];
  return r[0];
}
var Lt, Qr = new RegExp("^".concat(Di.source, "*")), Jr = new RegExp("".concat(Di.source, "*$"));
function L(e, t) {
  return { start: e, end: t };
}
var Yr = !!String.prototype.startsWith, Kr = !!String.fromCodePoint, $r = !!Object.fromEntries, el = !!String.prototype.codePointAt, tl = !!String.prototype.trimStart, nl = !!String.prototype.trimEnd, il = !!Number.isSafeInteger, rl = il ? Number.isSafeInteger : function(e) {
  return typeof e == "number" && isFinite(e) && Math.floor(e) === e && Math.abs(e) <= 9007199254740991;
}, Wt = !0;
try {
  var ll = ji("([^\\p{White_Space}\\p{Pattern_Syntax}]*)", "yu");
  Wt = ((Lt = ll.exec("a")) === null || Lt === void 0 ? void 0 : Lt[0]) === "a";
} catch {
  Wt = !1;
}
var Pn = Yr ? (
  // Native
  function(t, n, i) {
    return t.startsWith(n, i);
  }
) : (
  // For IE11
  function(t, n, i) {
    return t.slice(i, i + n.length) === n;
  }
), Qt = Kr ? String.fromCodePoint : (
  // IE11
  function() {
    for (var t = [], n = 0; n < arguments.length; n++)
      t[n] = arguments[n];
    for (var i = "", r = t.length, l = 0, a; r > l; ) {
      if (a = t[l++], a > 1114111)
        throw RangeError(a + " is not a valid code point");
      i += a < 65536 ? String.fromCharCode(a) : String.fromCharCode(((a -= 65536) >> 10) + 55296, a % 1024 + 56320);
    }
    return i;
  }
), Nn = (
  // native
  $r ? Object.fromEntries : (
    // Ponyfill
    function(t) {
      for (var n = {}, i = 0, r = t; i < r.length; i++) {
        var l = r[i], a = l[0], o = l[1];
        n[a] = o;
      }
      return n;
    }
  )
), xi = el ? (
  // Native
  function(t, n) {
    return t.codePointAt(n);
  }
) : (
  // IE 11
  function(t, n) {
    var i = t.length;
    if (!(n < 0 || n >= i)) {
      var r = t.charCodeAt(n), l;
      return r < 55296 || r > 56319 || n + 1 === i || (l = t.charCodeAt(n + 1)) < 56320 || l > 57343 ? r : (r - 55296 << 10) + (l - 56320) + 65536;
    }
  }
), sl = tl ? (
  // Native
  function(t) {
    return t.trimStart();
  }
) : (
  // Ponyfill
  function(t) {
    return t.replace(Qr, "");
  }
), ol = nl ? (
  // Native
  function(t) {
    return t.trimEnd();
  }
) : (
  // Ponyfill
  function(t) {
    return t.replace(Jr, "");
  }
);
function ji(e, t) {
  return new RegExp(e, t);
}
var Jt;
if (Wt) {
  var kn = ji("([^\\p{White_Space}\\p{Pattern_Syntax}]*)", "yu");
  Jt = function(t, n) {
    var i;
    kn.lastIndex = n;
    var r = kn.exec(t);
    return (i = r[1]) !== null && i !== void 0 ? i : "";
  };
} else
  Jt = function(t, n) {
    for (var i = []; ; ) {
      var r = xi(t, n);
      if (r === void 0 || Vi(r) || cl(r))
        break;
      i.push(r), n += r >= 65536 ? 2 : 1;
    }
    return Qt.apply(void 0, i);
  };
var al = (
  /** @class */
  function() {
    function e(t, n) {
      n === void 0 && (n = {}), this.message = t, this.position = { offset: 0, line: 1, column: 1 }, this.ignoreTag = !!n.ignoreTag, this.locale = n.locale, this.requiresOtherClause = !!n.requiresOtherClause, this.shouldParseSkeletons = !!n.shouldParseSkeletons;
    }
    return e.prototype.parse = function() {
      if (this.offset() !== 0)
        throw Error("parser can only be used once");
      return this.parseMessage(0, "", !1);
    }, e.prototype.parseMessage = function(t, n, i) {
      for (var r = []; !this.isEOF(); ) {
        var l = this.char();
        if (l === 123) {
          var a = this.parseArgument(t, i);
          if (a.err)
            return a;
          r.push(a.val);
        } else {
          if (l === 125 && t > 0)
            break;
          if (l === 35 && (n === "plural" || n === "selectordinal")) {
            var o = this.clonePosition();
            this.bump(), r.push({
              type: U.pound,
              location: L(o, this.clonePosition())
            });
          } else if (l === 60 && !this.ignoreTag && this.peek() === 47) {
            if (i)
              break;
            return this.error(I.UNMATCHED_CLOSING_TAG, L(this.clonePosition(), this.clonePosition()));
          } else if (l === 60 && !this.ignoreTag && Yt(this.peek() || 0)) {
            var a = this.parseTag(t, n);
            if (a.err)
              return a;
            r.push(a.val);
          } else {
            var a = this.parseLiteral(t, n);
            if (a.err)
              return a;
            r.push(a.val);
          }
        }
      }
      return { val: r, err: null };
    }, e.prototype.parseTag = function(t, n) {
      var i = this.clonePosition();
      this.bump();
      var r = this.parseTagName();
      if (this.bumpSpace(), this.bumpIf("/>"))
        return {
          val: {
            type: U.literal,
            value: "<".concat(r, "/>"),
            location: L(i, this.clonePosition())
          },
          err: null
        };
      if (this.bumpIf(">")) {
        var l = this.parseMessage(t + 1, n, !0);
        if (l.err)
          return l;
        var a = l.val, o = this.clonePosition();
        if (this.bumpIf("</")) {
          if (this.isEOF() || !Yt(this.char()))
            return this.error(I.INVALID_TAG, L(o, this.clonePosition()));
          var s = this.clonePosition(), u = this.parseTagName();
          return r !== u ? this.error(I.UNMATCHED_CLOSING_TAG, L(s, this.clonePosition())) : (this.bumpSpace(), this.bumpIf(">") ? {
            val: {
              type: U.tag,
              value: r,
              children: a,
              location: L(i, this.clonePosition())
            },
            err: null
          } : this.error(I.INVALID_TAG, L(o, this.clonePosition())));
        } else
          return this.error(I.UNCLOSED_TAG, L(i, this.clonePosition()));
      } else
        return this.error(I.INVALID_TAG, L(i, this.clonePosition()));
    }, e.prototype.parseTagName = function() {
      var t = this.offset();
      for (this.bump(); !this.isEOF() && fl(this.char()); )
        this.bump();
      return this.message.slice(t, this.offset());
    }, e.prototype.parseLiteral = function(t, n) {
      for (var i = this.clonePosition(), r = ""; ; ) {
        var l = this.tryParseQuote(n);
        if (l) {
          r += l;
          continue;
        }
        var a = this.tryParseUnquoted(t, n);
        if (a) {
          r += a;
          continue;
        }
        var o = this.tryParseLeftAngleBracket();
        if (o) {
          r += o;
          continue;
        }
        break;
      }
      var s = L(i, this.clonePosition());
      return {
        val: { type: U.literal, value: r, location: s },
        err: null
      };
    }, e.prototype.tryParseLeftAngleBracket = function() {
      return !this.isEOF() && this.char() === 60 && (this.ignoreTag || // If at the opening tag or closing tag position, bail.
      !ul(this.peek() || 0)) ? (this.bump(), "<") : null;
    }, e.prototype.tryParseQuote = function(t) {
      if (this.isEOF() || this.char() !== 39)
        return null;
      switch (this.peek()) {
        case 39:
          return this.bump(), this.bump(), "'";
        case 123:
        case 60:
        case 62:
        case 125:
          break;
        case 35:
          if (t === "plural" || t === "selectordinal")
            break;
          return null;
        default:
          return null;
      }
      this.bump();
      var n = [this.char()];
      for (this.bump(); !this.isEOF(); ) {
        var i = this.char();
        if (i === 39)
          if (this.peek() === 39)
            n.push(39), this.bump();
          else {
            this.bump();
            break;
          }
        else
          n.push(i);
        this.bump();
      }
      return Qt.apply(void 0, n);
    }, e.prototype.tryParseUnquoted = function(t, n) {
      if (this.isEOF())
        return null;
      var i = this.char();
      return i === 60 || i === 123 || i === 35 && (n === "plural" || n === "selectordinal") || i === 125 && t > 0 ? null : (this.bump(), Qt(i));
    }, e.prototype.parseArgument = function(t, n) {
      var i = this.clonePosition();
      if (this.bump(), this.bumpSpace(), this.isEOF())
        return this.error(I.EXPECT_ARGUMENT_CLOSING_BRACE, L(i, this.clonePosition()));
      if (this.char() === 125)
        return this.bump(), this.error(I.EMPTY_ARGUMENT, L(i, this.clonePosition()));
      var r = this.parseIdentifierIfPossible().value;
      if (!r)
        return this.error(I.MALFORMED_ARGUMENT, L(i, this.clonePosition()));
      if (this.bumpSpace(), this.isEOF())
        return this.error(I.EXPECT_ARGUMENT_CLOSING_BRACE, L(i, this.clonePosition()));
      switch (this.char()) {
        case 125:
          return this.bump(), {
            val: {
              type: U.argument,
              // value does not include the opening and closing braces.
              value: r,
              location: L(i, this.clonePosition())
            },
            err: null
          };
        case 44:
          return this.bump(), this.bumpSpace(), this.isEOF() ? this.error(I.EXPECT_ARGUMENT_CLOSING_BRACE, L(i, this.clonePosition())) : this.parseArgumentOptions(t, n, r, i);
        default:
          return this.error(I.MALFORMED_ARGUMENT, L(i, this.clonePosition()));
      }
    }, e.prototype.parseIdentifierIfPossible = function() {
      var t = this.clonePosition(), n = this.offset(), i = Jt(this.message, n), r = n + i.length;
      this.bumpTo(r);
      var l = this.clonePosition(), a = L(t, l);
      return { value: i, location: a };
    }, e.prototype.parseArgumentOptions = function(t, n, i, r) {
      var l, a = this.clonePosition(), o = this.parseIdentifierIfPossible().value, s = this.clonePosition();
      switch (o) {
        case "":
          return this.error(I.EXPECT_ARGUMENT_TYPE, L(a, s));
        case "number":
        case "date":
        case "time": {
          this.bumpSpace();
          var u = null;
          if (this.bumpIf(",")) {
            this.bumpSpace();
            var f = this.clonePosition(), _ = this.parseSimpleArgStyleIfPossible();
            if (_.err)
              return _;
            var c = ol(_.val);
            if (c.length === 0)
              return this.error(I.EXPECT_ARGUMENT_STYLE, L(this.clonePosition(), this.clonePosition()));
            var d = L(f, this.clonePosition());
            u = { style: c, styleLocation: d };
          }
          var v = this.tryParseArgumentClose(r);
          if (v.err)
            return v;
          var y = L(r, this.clonePosition());
          if (u && Pn(u == null ? void 0 : u.style, "::", 0)) {
            var b = sl(u.style.slice(2));
            if (o === "number") {
              var _ = this.parseNumberSkeletonFromString(b, u.styleLocation);
              return _.err ? _ : {
                val: { type: U.number, value: i, location: y, style: _.val },
                err: null
              };
            } else {
              if (b.length === 0)
                return this.error(I.EXPECT_DATE_TIME_SKELETON, y);
              var g = b;
              this.locale && (g = Zr(b, this.locale));
              var c = {
                type: Ue.dateTime,
                pattern: g,
                location: u.styleLocation,
                parsedOptions: this.shouldParseSkeletons ? Fr(g) : {}
              }, E = o === "date" ? U.date : U.time;
              return {
                val: { type: E, value: i, location: y, style: c },
                err: null
              };
            }
          }
          return {
            val: {
              type: o === "number" ? U.number : o === "date" ? U.date : U.time,
              value: i,
              location: y,
              style: (l = u == null ? void 0 : u.style) !== null && l !== void 0 ? l : null
            },
            err: null
          };
        }
        case "plural":
        case "selectordinal":
        case "select": {
          var h = this.clonePosition();
          if (this.bumpSpace(), !this.bumpIf(","))
            return this.error(I.EXPECT_SELECT_ARGUMENT_OPTIONS, L(h, R({}, h)));
          this.bumpSpace();
          var m = this.parseIdentifierIfPossible(), S = 0;
          if (o !== "select" && m.value === "offset") {
            if (!this.bumpIf(":"))
              return this.error(I.EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE, L(this.clonePosition(), this.clonePosition()));
            this.bumpSpace();
            var _ = this.tryParseDecimalInteger(I.EXPECT_PLURAL_ARGUMENT_OFFSET_VALUE, I.INVALID_PLURAL_ARGUMENT_OFFSET_VALUE);
            if (_.err)
              return _;
            this.bumpSpace(), m = this.parseIdentifierIfPossible(), S = _.val;
          }
          var p = this.tryParsePluralOrSelectOptions(t, o, n, m);
          if (p.err)
            return p;
          var v = this.tryParseArgumentClose(r);
          if (v.err)
            return v;
          var k = L(r, this.clonePosition());
          return o === "select" ? {
            val: {
              type: U.select,
              value: i,
              options: Nn(p.val),
              location: k
            },
            err: null
          } : {
            val: {
              type: U.plural,
              value: i,
              options: Nn(p.val),
              offset: S,
              pluralType: o === "plural" ? "cardinal" : "ordinal",
              location: k
            },
            err: null
          };
        }
        default:
          return this.error(I.INVALID_ARGUMENT_TYPE, L(a, s));
      }
    }, e.prototype.tryParseArgumentClose = function(t) {
      return this.isEOF() || this.char() !== 125 ? this.error(I.EXPECT_ARGUMENT_CLOSING_BRACE, L(t, this.clonePosition())) : (this.bump(), { val: !0, err: null });
    }, e.prototype.parseSimpleArgStyleIfPossible = function() {
      for (var t = 0, n = this.clonePosition(); !this.isEOF(); ) {
        var i = this.char();
        switch (i) {
          case 39: {
            this.bump();
            var r = this.clonePosition();
            if (!this.bumpUntil("'"))
              return this.error(I.UNCLOSED_QUOTE_IN_ARGUMENT_STYLE, L(r, this.clonePosition()));
            this.bump();
            break;
          }
          case 123: {
            t += 1, this.bump();
            break;
          }
          case 125: {
            if (t > 0)
              t -= 1;
            else
              return {
                val: this.message.slice(n.offset, this.offset()),
                err: null
              };
            break;
          }
          default:
            this.bump();
            break;
        }
      }
      return {
        val: this.message.slice(n.offset, this.offset()),
        err: null
      };
    }, e.prototype.parseNumberSkeletonFromString = function(t, n) {
      var i = [];
      try {
        i = jr(t);
      } catch {
        return this.error(I.INVALID_NUMBER_SKELETON, n);
      }
      return {
        val: {
          type: Ue.number,
          tokens: i,
          location: n,
          parsedOptions: this.shouldParseSkeletons ? zr(i) : {}
        },
        err: null
      };
    }, e.prototype.tryParsePluralOrSelectOptions = function(t, n, i, r) {
      for (var l, a = !1, o = [], s = /* @__PURE__ */ new Set(), u = r.value, f = r.location; ; ) {
        if (u.length === 0) {
          var _ = this.clonePosition();
          if (n !== "select" && this.bumpIf("=")) {
            var c = this.tryParseDecimalInteger(I.EXPECT_PLURAL_ARGUMENT_SELECTOR, I.INVALID_PLURAL_ARGUMENT_SELECTOR);
            if (c.err)
              return c;
            f = L(_, this.clonePosition()), u = this.message.slice(_.offset, this.offset());
          } else
            break;
        }
        if (s.has(u))
          return this.error(n === "select" ? I.DUPLICATE_SELECT_ARGUMENT_SELECTOR : I.DUPLICATE_PLURAL_ARGUMENT_SELECTOR, f);
        u === "other" && (a = !0), this.bumpSpace();
        var d = this.clonePosition();
        if (!this.bumpIf("{"))
          return this.error(n === "select" ? I.EXPECT_SELECT_ARGUMENT_SELECTOR_FRAGMENT : I.EXPECT_PLURAL_ARGUMENT_SELECTOR_FRAGMENT, L(this.clonePosition(), this.clonePosition()));
        var v = this.parseMessage(t + 1, n, i);
        if (v.err)
          return v;
        var y = this.tryParseArgumentClose(d);
        if (y.err)
          return y;
        o.push([
          u,
          {
            value: v.val,
            location: L(d, this.clonePosition())
          }
        ]), s.add(u), this.bumpSpace(), l = this.parseIdentifierIfPossible(), u = l.value, f = l.location;
      }
      return o.length === 0 ? this.error(n === "select" ? I.EXPECT_SELECT_ARGUMENT_SELECTOR : I.EXPECT_PLURAL_ARGUMENT_SELECTOR, L(this.clonePosition(), this.clonePosition())) : this.requiresOtherClause && !a ? this.error(I.MISSING_OTHER_CLAUSE, L(this.clonePosition(), this.clonePosition())) : { val: o, err: null };
    }, e.prototype.tryParseDecimalInteger = function(t, n) {
      var i = 1, r = this.clonePosition();
      this.bumpIf("+") || this.bumpIf("-") && (i = -1);
      for (var l = !1, a = 0; !this.isEOF(); ) {
        var o = this.char();
        if (o >= 48 && o <= 57)
          l = !0, a = a * 10 + (o - 48), this.bump();
        else
          break;
      }
      var s = L(r, this.clonePosition());
      return l ? (a *= i, rl(a) ? { val: a, err: null } : this.error(n, s)) : this.error(t, s);
    }, e.prototype.offset = function() {
      return this.position.offset;
    }, e.prototype.isEOF = function() {
      return this.offset() === this.message.length;
    }, e.prototype.clonePosition = function() {
      return {
        offset: this.position.offset,
        line: this.position.line,
        column: this.position.column
      };
    }, e.prototype.char = function() {
      var t = this.position.offset;
      if (t >= this.message.length)
        throw Error("out of bound");
      var n = xi(this.message, t);
      if (n === void 0)
        throw Error("Offset ".concat(t, " is at invalid UTF-16 code unit boundary"));
      return n;
    }, e.prototype.error = function(t, n) {
      return {
        val: null,
        err: {
          kind: t,
          message: this.message,
          location: n
        }
      };
    }, e.prototype.bump = function() {
      if (!this.isEOF()) {
        var t = this.char();
        t === 10 ? (this.position.line += 1, this.position.column = 1, this.position.offset += 1) : (this.position.column += 1, this.position.offset += t < 65536 ? 1 : 2);
      }
    }, e.prototype.bumpIf = function(t) {
      if (Pn(this.message, t, this.offset())) {
        for (var n = 0; n < t.length; n++)
          this.bump();
        return !0;
      }
      return !1;
    }, e.prototype.bumpUntil = function(t) {
      var n = this.offset(), i = this.message.indexOf(t, n);
      return i >= 0 ? (this.bumpTo(i), !0) : (this.bumpTo(this.message.length), !1);
    }, e.prototype.bumpTo = function(t) {
      if (this.offset() > t)
        throw Error("targetOffset ".concat(t, " must be greater than or equal to the current offset ").concat(this.offset()));
      for (t = Math.min(t, this.message.length); ; ) {
        var n = this.offset();
        if (n === t)
          break;
        if (n > t)
          throw Error("targetOffset ".concat(t, " is at invalid UTF-16 code unit boundary"));
        if (this.bump(), this.isEOF())
          break;
      }
    }, e.prototype.bumpSpace = function() {
      for (; !this.isEOF() && Vi(this.char()); )
        this.bump();
    }, e.prototype.peek = function() {
      if (this.isEOF())
        return null;
      var t = this.char(), n = this.offset(), i = this.message.charCodeAt(n + (t >= 65536 ? 2 : 1));
      return i ?? null;
    }, e;
  }()
);
function Yt(e) {
  return e >= 97 && e <= 122 || e >= 65 && e <= 90;
}
function ul(e) {
  return Yt(e) || e === 47;
}
function fl(e) {
  return e === 45 || e === 46 || e >= 48 && e <= 57 || e === 95 || e >= 97 && e <= 122 || e >= 65 && e <= 90 || e == 183 || e >= 192 && e <= 214 || e >= 216 && e <= 246 || e >= 248 && e <= 893 || e >= 895 && e <= 8191 || e >= 8204 && e <= 8205 || e >= 8255 && e <= 8256 || e >= 8304 && e <= 8591 || e >= 11264 && e <= 12271 || e >= 12289 && e <= 55295 || e >= 63744 && e <= 64975 || e >= 65008 && e <= 65533 || e >= 65536 && e <= 983039;
}
function Vi(e) {
  return e >= 9 && e <= 13 || e === 32 || e === 133 || e >= 8206 && e <= 8207 || e === 8232 || e === 8233;
}
function cl(e) {
  return e >= 33 && e <= 35 || e === 36 || e >= 37 && e <= 39 || e === 40 || e === 41 || e === 42 || e === 43 || e === 44 || e === 45 || e >= 46 && e <= 47 || e >= 58 && e <= 59 || e >= 60 && e <= 62 || e >= 63 && e <= 64 || e === 91 || e === 92 || e === 93 || e === 94 || e === 96 || e === 123 || e === 124 || e === 125 || e === 126 || e === 161 || e >= 162 && e <= 165 || e === 166 || e === 167 || e === 169 || e === 171 || e === 172 || e === 174 || e === 176 || e === 177 || e === 182 || e === 187 || e === 191 || e === 215 || e === 247 || e >= 8208 && e <= 8213 || e >= 8214 && e <= 8215 || e === 8216 || e === 8217 || e === 8218 || e >= 8219 && e <= 8220 || e === 8221 || e === 8222 || e === 8223 || e >= 8224 && e <= 8231 || e >= 8240 && e <= 8248 || e === 8249 || e === 8250 || e >= 8251 && e <= 8254 || e >= 8257 && e <= 8259 || e === 8260 || e === 8261 || e === 8262 || e >= 8263 && e <= 8273 || e === 8274 || e === 8275 || e >= 8277 && e <= 8286 || e >= 8592 && e <= 8596 || e >= 8597 && e <= 8601 || e >= 8602 && e <= 8603 || e >= 8604 && e <= 8607 || e === 8608 || e >= 8609 && e <= 8610 || e === 8611 || e >= 8612 && e <= 8613 || e === 8614 || e >= 8615 && e <= 8621 || e === 8622 || e >= 8623 && e <= 8653 || e >= 8654 && e <= 8655 || e >= 8656 && e <= 8657 || e === 8658 || e === 8659 || e === 8660 || e >= 8661 && e <= 8691 || e >= 8692 && e <= 8959 || e >= 8960 && e <= 8967 || e === 8968 || e === 8969 || e === 8970 || e === 8971 || e >= 8972 && e <= 8991 || e >= 8992 && e <= 8993 || e >= 8994 && e <= 9e3 || e === 9001 || e === 9002 || e >= 9003 && e <= 9083 || e === 9084 || e >= 9085 && e <= 9114 || e >= 9115 && e <= 9139 || e >= 9140 && e <= 9179 || e >= 9180 && e <= 9185 || e >= 9186 && e <= 9254 || e >= 9255 && e <= 9279 || e >= 9280 && e <= 9290 || e >= 9291 && e <= 9311 || e >= 9472 && e <= 9654 || e === 9655 || e >= 9656 && e <= 9664 || e === 9665 || e >= 9666 && e <= 9719 || e >= 9720 && e <= 9727 || e >= 9728 && e <= 9838 || e === 9839 || e >= 9840 && e <= 10087 || e === 10088 || e === 10089 || e === 10090 || e === 10091 || e === 10092 || e === 10093 || e === 10094 || e === 10095 || e === 10096 || e === 10097 || e === 10098 || e === 10099 || e === 10100 || e === 10101 || e >= 10132 && e <= 10175 || e >= 10176 && e <= 10180 || e === 10181 || e === 10182 || e >= 10183 && e <= 10213 || e === 10214 || e === 10215 || e === 10216 || e === 10217 || e === 10218 || e === 10219 || e === 10220 || e === 10221 || e === 10222 || e === 10223 || e >= 10224 && e <= 10239 || e >= 10240 && e <= 10495 || e >= 10496 && e <= 10626 || e === 10627 || e === 10628 || e === 10629 || e === 10630 || e === 10631 || e === 10632 || e === 10633 || e === 10634 || e === 10635 || e === 10636 || e === 10637 || e === 10638 || e === 10639 || e === 10640 || e === 10641 || e === 10642 || e === 10643 || e === 10644 || e === 10645 || e === 10646 || e === 10647 || e === 10648 || e >= 10649 && e <= 10711 || e === 10712 || e === 10713 || e === 10714 || e === 10715 || e >= 10716 && e <= 10747 || e === 10748 || e === 10749 || e >= 10750 && e <= 11007 || e >= 11008 && e <= 11055 || e >= 11056 && e <= 11076 || e >= 11077 && e <= 11078 || e >= 11079 && e <= 11084 || e >= 11085 && e <= 11123 || e >= 11124 && e <= 11125 || e >= 11126 && e <= 11157 || e === 11158 || e >= 11159 && e <= 11263 || e >= 11776 && e <= 11777 || e === 11778 || e === 11779 || e === 11780 || e === 11781 || e >= 11782 && e <= 11784 || e === 11785 || e === 11786 || e === 11787 || e === 11788 || e === 11789 || e >= 11790 && e <= 11798 || e === 11799 || e >= 11800 && e <= 11801 || e === 11802 || e === 11803 || e === 11804 || e === 11805 || e >= 11806 && e <= 11807 || e === 11808 || e === 11809 || e === 11810 || e === 11811 || e === 11812 || e === 11813 || e === 11814 || e === 11815 || e === 11816 || e === 11817 || e >= 11818 && e <= 11822 || e === 11823 || e >= 11824 && e <= 11833 || e >= 11834 && e <= 11835 || e >= 11836 && e <= 11839 || e === 11840 || e === 11841 || e === 11842 || e >= 11843 && e <= 11855 || e >= 11856 && e <= 11857 || e === 11858 || e >= 11859 && e <= 11903 || e >= 12289 && e <= 12291 || e === 12296 || e === 12297 || e === 12298 || e === 12299 || e === 12300 || e === 12301 || e === 12302 || e === 12303 || e === 12304 || e === 12305 || e >= 12306 && e <= 12307 || e === 12308 || e === 12309 || e === 12310 || e === 12311 || e === 12312 || e === 12313 || e === 12314 || e === 12315 || e === 12316 || e === 12317 || e >= 12318 && e <= 12319 || e === 12320 || e === 12336 || e === 64830 || e === 64831 || e >= 65093 && e <= 65094;
}
function Kt(e) {
  e.forEach(function(t) {
    if (delete t.location, Ii(t) || Li(t))
      for (var n in t.options)
        delete t.options[n].location, Kt(t.options[n].value);
    else
      ki(t) && Ri(t.style) || (Ci(t) || Oi(t)) && Zt(t.style) ? delete t.style.location : Mi(t) && Kt(t.children);
  });
}
function hl(e, t) {
  t === void 0 && (t = {}), t = R({ shouldParseSkeletons: !0, requiresOtherClause: !0 }, t);
  var n = new al(e, t).parse();
  if (n.err) {
    var i = SyntaxError(I[n.err.kind]);
    throw i.location = n.err.location, i.originalMessage = n.err.message, i;
  }
  return t != null && t.captureLocation || Kt(n.val), n.val;
}
function Mt(e, t) {
  var n = t && t.cache ? t.cache : pl, i = t && t.serializer ? t.serializer : gl, r = t && t.strategy ? t.strategy : ml;
  return r(e, {
    cache: n,
    serializer: i
  });
}
function _l(e) {
  return e == null || typeof e == "number" || typeof e == "boolean";
}
function qi(e, t, n, i) {
  var r = _l(i) ? i : n(i), l = t.get(r);
  return typeof l > "u" && (l = e.call(this, i), t.set(r, l)), l;
}
function Xi(e, t, n) {
  var i = Array.prototype.slice.call(arguments, 3), r = n(i), l = t.get(r);
  return typeof l > "u" && (l = e.apply(this, i), t.set(r, l)), l;
}
function un(e, t, n, i, r) {
  return n.bind(t, e, i, r);
}
function ml(e, t) {
  var n = e.length === 1 ? qi : Xi;
  return un(e, this, n, t.cache.create(), t.serializer);
}
function dl(e, t) {
  return un(e, this, Xi, t.cache.create(), t.serializer);
}
function bl(e, t) {
  return un(e, this, qi, t.cache.create(), t.serializer);
}
var gl = function() {
  return JSON.stringify(arguments);
};
function fn() {
  this.cache = /* @__PURE__ */ Object.create(null);
}
fn.prototype.get = function(e) {
  return this.cache[e];
};
fn.prototype.set = function(e, t) {
  this.cache[e] = t;
};
var pl = {
  create: function() {
    return new fn();
  }
}, Rt = {
  variadic: dl,
  monadic: bl
}, Ge;
(function(e) {
  e.MISSING_VALUE = "MISSING_VALUE", e.INVALID_VALUE = "INVALID_VALUE", e.MISSING_INTL_API = "MISSING_INTL_API";
})(Ge || (Ge = {}));
var Ht = (
  /** @class */
  function(e) {
    At(t, e);
    function t(n, i, r) {
      var l = e.call(this, n) || this;
      return l.code = i, l.originalMessage = r, l;
    }
    return t.prototype.toString = function() {
      return "[formatjs Error: ".concat(this.code, "] ").concat(this.message);
    }, t;
  }(Error)
), Cn = (
  /** @class */
  function(e) {
    At(t, e);
    function t(n, i, r, l) {
      return e.call(this, 'Invalid values for "'.concat(n, '": "').concat(i, '". Options are "').concat(Object.keys(r).join('", "'), '"'), Ge.INVALID_VALUE, l) || this;
    }
    return t;
  }(Ht)
), vl = (
  /** @class */
  function(e) {
    At(t, e);
    function t(n, i, r) {
      return e.call(this, 'Value for "'.concat(n, '" must be of type ').concat(i), Ge.INVALID_VALUE, r) || this;
    }
    return t;
  }(Ht)
), yl = (
  /** @class */
  function(e) {
    At(t, e);
    function t(n, i) {
      return e.call(this, 'The intl string context variable "'.concat(n, '" was not provided to the string "').concat(i, '"'), Ge.MISSING_VALUE, i) || this;
    }
    return t;
  }(Ht)
), X;
(function(e) {
  e[e.literal = 0] = "literal", e[e.object = 1] = "object";
})(X || (X = {}));
function wl(e) {
  return e.length < 2 ? e : e.reduce(function(t, n) {
    var i = t[t.length - 1];
    return !i || i.type !== X.literal || n.type !== X.literal ? t.push(n) : i.value += n.value, t;
  }, []);
}
function El(e) {
  return typeof e == "function";
}
function ct(e, t, n, i, r, l, a) {
  if (e.length === 1 && Tn(e[0]))
    return [
      {
        type: X.literal,
        value: e[0].value
      }
    ];
  for (var o = [], s = 0, u = e; s < u.length; s++) {
    var f = u[s];
    if (Tn(f)) {
      o.push({
        type: X.literal,
        value: f.value
      });
      continue;
    }
    if (Ur(f)) {
      typeof l == "number" && o.push({
        type: X.literal,
        value: n.getNumberFormat(t).format(l)
      });
      continue;
    }
    var _ = f.value;
    if (!(r && _ in r))
      throw new yl(_, a);
    var c = r[_];
    if (Dr(f)) {
      (!c || typeof c == "string" || typeof c == "number") && (c = typeof c == "string" || typeof c == "number" ? String(c) : ""), o.push({
        type: typeof c == "string" ? X.literal : X.object,
        value: c
      });
      continue;
    }
    if (Ci(f)) {
      var d = typeof f.style == "string" ? i.date[f.style] : Zt(f.style) ? f.style.parsedOptions : void 0;
      o.push({
        type: X.literal,
        value: n.getDateTimeFormat(t, d).format(c)
      });
      continue;
    }
    if (Oi(f)) {
      var d = typeof f.style == "string" ? i.time[f.style] : Zt(f.style) ? f.style.parsedOptions : i.time.medium;
      o.push({
        type: X.literal,
        value: n.getDateTimeFormat(t, d).format(c)
      });
      continue;
    }
    if (ki(f)) {
      var d = typeof f.style == "string" ? i.number[f.style] : Ri(f.style) ? f.style.parsedOptions : void 0;
      d && d.scale && (c = c * (d.scale || 1)), o.push({
        type: X.literal,
        value: n.getNumberFormat(t, d).format(c)
      });
      continue;
    }
    if (Mi(f)) {
      var v = f.children, y = f.value, b = r[y];
      if (!El(b))
        throw new vl(y, "function", a);
      var g = ct(v, t, n, i, r, l), E = b(g.map(function(S) {
        return S.value;
      }));
      Array.isArray(E) || (E = [E]), o.push.apply(o, E.map(function(S) {
        return {
          type: typeof S == "string" ? X.literal : X.object,
          value: S
        };
      }));
    }
    if (Ii(f)) {
      var h = f.options[c] || f.options.other;
      if (!h)
        throw new Cn(f.value, c, Object.keys(f.options), a);
      o.push.apply(o, ct(h.value, t, n, i, r));
      continue;
    }
    if (Li(f)) {
      var h = f.options["=".concat(c)];
      if (!h) {
        if (!Intl.PluralRules)
          throw new Ht(`Intl.PluralRules is not available in this environment.
Try polyfilling it using "@formatjs/intl-pluralrules"
`, Ge.MISSING_INTL_API, a);
        var m = n.getPluralRules(t, { type: f.pluralType }).select(c - (f.offset || 0));
        h = f.options[m] || f.options.other;
      }
      if (!h)
        throw new Cn(f.value, c, Object.keys(f.options), a);
      o.push.apply(o, ct(h.value, t, n, i, r, c - (f.offset || 0)));
      continue;
    }
  }
  return wl(o);
}
function Sl(e, t) {
  return t ? R(R(R({}, e || {}), t || {}), Object.keys(e).reduce(function(n, i) {
    return n[i] = R(R({}, e[i]), t[i] || {}), n;
  }, {})) : e;
}
function Tl(e, t) {
  return t ? Object.keys(e).reduce(function(n, i) {
    return n[i] = Sl(e[i], t[i]), n;
  }, R({}, e)) : e;
}
function Dt(e) {
  return {
    create: function() {
      return {
        get: function(t) {
          return e[t];
        },
        set: function(t, n) {
          e[t] = n;
        }
      };
    }
  };
}
function Al(e) {
  return e === void 0 && (e = {
    number: {},
    dateTime: {},
    pluralRules: {}
  }), {
    getNumberFormat: Mt(function() {
      for (var t, n = [], i = 0; i < arguments.length; i++)
        n[i] = arguments[i];
      return new ((t = Intl.NumberFormat).bind.apply(t, It([void 0], n, !1)))();
    }, {
      cache: Dt(e.number),
      strategy: Rt.variadic
    }),
    getDateTimeFormat: Mt(function() {
      for (var t, n = [], i = 0; i < arguments.length; i++)
        n[i] = arguments[i];
      return new ((t = Intl.DateTimeFormat).bind.apply(t, It([void 0], n, !1)))();
    }, {
      cache: Dt(e.dateTime),
      strategy: Rt.variadic
    }),
    getPluralRules: Mt(function() {
      for (var t, n = [], i = 0; i < arguments.length; i++)
        n[i] = arguments[i];
      return new ((t = Intl.PluralRules).bind.apply(t, It([void 0], n, !1)))();
    }, {
      cache: Dt(e.pluralRules),
      strategy: Rt.variadic
    })
  };
}
var Hl = (
  /** @class */
  function() {
    function e(t, n, i, r) {
      var l = this;
      if (n === void 0 && (n = e.defaultLocale), this.formatterCache = {
        number: {},
        dateTime: {},
        pluralRules: {}
      }, this.format = function(a) {
        var o = l.formatToParts(a);
        if (o.length === 1)
          return o[0].value;
        var s = o.reduce(function(u, f) {
          return !u.length || f.type !== X.literal || typeof u[u.length - 1] != "string" ? u.push(f.value) : u[u.length - 1] += f.value, u;
        }, []);
        return s.length <= 1 ? s[0] || "" : s;
      }, this.formatToParts = function(a) {
        return ct(l.ast, l.locales, l.formatters, l.formats, a, void 0, l.message);
      }, this.resolvedOptions = function() {
        return {
          locale: l.resolvedLocale.toString()
        };
      }, this.getAst = function() {
        return l.ast;
      }, this.locales = n, this.resolvedLocale = e.resolveLocale(n), typeof t == "string") {
        if (this.message = t, !e.__parse)
          throw new TypeError("IntlMessageFormat.__parse must be set to process `message` of type `string`");
        this.ast = e.__parse(t, {
          ignoreTag: r == null ? void 0 : r.ignoreTag,
          locale: this.resolvedLocale
        });
      } else
        this.ast = t;
      if (!Array.isArray(this.ast))
        throw new TypeError("A message must be provided as a String or AST.");
      this.formats = Tl(e.formats, i), this.formatters = r && r.formatters || Al(this.formatterCache);
    }
    return Object.defineProperty(e, "defaultLocale", {
      get: function() {
        return e.memoizedDefaultLocale || (e.memoizedDefaultLocale = new Intl.NumberFormat().resolvedOptions().locale), e.memoizedDefaultLocale;
      },
      enumerable: !1,
      configurable: !0
    }), e.memoizedDefaultLocale = null, e.resolveLocale = function(t) {
      var n = Intl.NumberFormat.supportedLocalesOf(t);
      return n.length > 0 ? new Intl.Locale(n[0]) : new Intl.Locale(typeof t == "string" ? t : t[0]);
    }, e.__parse = hl, e.formats = {
      number: {
        integer: {
          maximumFractionDigits: 0
        },
        currency: {
          style: "currency"
        },
        percent: {
          style: "percent"
        }
      },
      date: {
        short: {
          month: "numeric",
          day: "numeric",
          year: "2-digit"
        },
        medium: {
          month: "short",
          day: "numeric",
          year: "numeric"
        },
        long: {
          month: "long",
          day: "numeric",
          year: "numeric"
        },
        full: {
          weekday: "long",
          month: "long",
          day: "numeric",
          year: "numeric"
        }
      },
      time: {
        short: {
          hour: "numeric",
          minute: "numeric"
        },
        medium: {
          hour: "numeric",
          minute: "numeric",
          second: "numeric"
        },
        long: {
          hour: "numeric",
          minute: "numeric",
          second: "numeric",
          timeZoneName: "short"
        },
        full: {
          hour: "numeric",
          minute: "numeric",
          second: "numeric",
          timeZoneName: "short"
        }
      }
    }, e;
  }()
);
function Bl(e, t) {
  if (t == null)
    return;
  if (t in e)
    return e[t];
  const n = t.split(".");
  let i = e;
  for (let r = 0; r < n.length; r++)
    if (typeof i == "object") {
      if (r > 0) {
        const l = n.slice(r, n.length).join(".");
        if (l in i) {
          i = i[l];
          break;
        }
      }
      i = i[n[r]];
    } else
      i = void 0;
  return i;
}
const ge = {}, Pl = (e, t, n) => n && (t in ge || (ge[t] = {}), e in ge[t] || (ge[t][e] = n), n), zi = (e, t) => {
  if (t == null)
    return;
  if (t in ge && e in ge[t])
    return ge[t][e];
  const n = Bt(t);
  for (let i = 0; i < n.length; i++) {
    const r = n[i], l = kl(r, e);
    if (l)
      return Pl(e, t, l);
  }
};
let cn;
const rt = it({});
function Nl(e) {
  return cn[e] || null;
}
function Zi(e) {
  return e in cn;
}
function kl(e, t) {
  if (!Zi(e))
    return null;
  const n = Nl(e);
  return Bl(n, t);
}
function Cl(e) {
  if (e == null)
    return;
  const t = Bt(e);
  for (let n = 0; n < t.length; n++) {
    const i = t[n];
    if (Zi(i))
      return i;
  }
}
function Ol(e, ...t) {
  delete ge[e], rt.update((n) => (n[e] = Rr.all([n[e] || {}, ...t]), n));
}
Ve(
  [rt],
  ([e]) => Object.keys(e)
);
rt.subscribe((e) => cn = e);
const ht = {};
function Il(e, t) {
  ht[e].delete(t), ht[e].size === 0 && delete ht[e];
}
function Wi(e) {
  return ht[e];
}
function Ll(e) {
  return Bt(e).map((t) => {
    const n = Wi(t);
    return [t, n ? [...n] : []];
  }).filter(([, t]) => t.length > 0);
}
function $t(e) {
  return e == null ? !1 : Bt(e).some(
    (t) => {
      var n;
      return (n = Wi(t)) == null ? void 0 : n.size;
    }
  );
}
function Ml(e, t) {
  return Promise.all(
    t.map((i) => (Il(e, i), i().then((r) => r.default || r)))
  ).then((i) => Ol(e, ...i));
}
const ze = {};
function Qi(e) {
  if (!$t(e))
    return e in ze ? ze[e] : Promise.resolve();
  const t = Ll(e);
  return ze[e] = Promise.all(
    t.map(
      ([n, i]) => Ml(n, i)
    )
  ).then(() => {
    if ($t(e))
      return Qi(e);
    delete ze[e];
  }), ze[e];
}
const Rl = {
  number: {
    scientific: { notation: "scientific" },
    engineering: { notation: "engineering" },
    compactLong: { notation: "compact", compactDisplay: "long" },
    compactShort: { notation: "compact", compactDisplay: "short" }
  },
  date: {
    short: { month: "numeric", day: "numeric", year: "2-digit" },
    medium: { month: "short", day: "numeric", year: "numeric" },
    long: { month: "long", day: "numeric", year: "numeric" },
    full: { weekday: "long", month: "long", day: "numeric", year: "numeric" }
  },
  time: {
    short: { hour: "numeric", minute: "numeric" },
    medium: { hour: "numeric", minute: "numeric", second: "numeric" },
    long: {
      hour: "numeric",
      minute: "numeric",
      second: "numeric",
      timeZoneName: "short"
    },
    full: {
      hour: "numeric",
      minute: "numeric",
      second: "numeric",
      timeZoneName: "short"
    }
  }
}, Dl = {
  fallbackLocale: null,
  loadingDelay: 200,
  formats: Rl,
  warnOnMissingMessages: !0,
  handleMissingMessage: void 0,
  ignoreTag: !0
}, Ul = Dl;
function Fe() {
  return Ul;
}
const Ut = it(!1);
var Gl = Object.defineProperty, Fl = Object.defineProperties, xl = Object.getOwnPropertyDescriptors, On = Object.getOwnPropertySymbols, jl = Object.prototype.hasOwnProperty, Vl = Object.prototype.propertyIsEnumerable, In = (e, t, n) => t in e ? Gl(e, t, { enumerable: !0, configurable: !0, writable: !0, value: n }) : e[t] = n, ql = (e, t) => {
  for (var n in t || (t = {}))
    jl.call(t, n) && In(e, n, t[n]);
  if (On)
    for (var n of On(t))
      Vl.call(t, n) && In(e, n, t[n]);
  return e;
}, Xl = (e, t) => Fl(e, xl(t));
let en;
const bt = it(null);
function Ln(e) {
  return e.split("-").map((t, n, i) => i.slice(0, n + 1).join("-")).reverse();
}
function Bt(e, t = Fe().fallbackLocale) {
  const n = Ln(e);
  return t ? [.../* @__PURE__ */ new Set([...n, ...Ln(t)])] : n;
}
function Ee() {
  return en ?? void 0;
}
bt.subscribe((e) => {
  en = e ?? void 0, typeof window < "u" && e != null && document.documentElement.setAttribute("lang", e);
});
const zl = (e) => {
  if (e && Cl(e) && $t(e)) {
    const { loadingDelay: t } = Fe();
    let n;
    return typeof window < "u" && Ee() != null && t ? n = window.setTimeout(
      () => Ut.set(!0),
      t
    ) : Ut.set(!0), Qi(e).then(() => {
      bt.set(e);
    }).finally(() => {
      clearTimeout(n), Ut.set(!1);
    });
  }
  return bt.set(e);
}, lt = Xl(ql({}, bt), {
  set: zl
}), Pt = (e) => {
  const t = /* @__PURE__ */ Object.create(null);
  return (i) => {
    const r = JSON.stringify(i);
    return r in t ? t[r] : t[r] = e(i);
  };
};
var Zl = Object.defineProperty, gt = Object.getOwnPropertySymbols, Ji = Object.prototype.hasOwnProperty, Yi = Object.prototype.propertyIsEnumerable, Mn = (e, t, n) => t in e ? Zl(e, t, { enumerable: !0, configurable: !0, writable: !0, value: n }) : e[t] = n, hn = (e, t) => {
  for (var n in t || (t = {}))
    Ji.call(t, n) && Mn(e, n, t[n]);
  if (gt)
    for (var n of gt(t))
      Yi.call(t, n) && Mn(e, n, t[n]);
  return e;
}, qe = (e, t) => {
  var n = {};
  for (var i in e)
    Ji.call(e, i) && t.indexOf(i) < 0 && (n[i] = e[i]);
  if (e != null && gt)
    for (var i of gt(e))
      t.indexOf(i) < 0 && Yi.call(e, i) && (n[i] = e[i]);
  return n;
};
const $e = (e, t) => {
  const { formats: n } = Fe();
  if (e in n && t in n[e])
    return n[e][t];
  throw new Error(`[svelte-i18n] Unknown "${t}" ${e} format.`);
}, Wl = Pt(
  (e) => {
    var t = e, { locale: n, format: i } = t, r = qe(t, ["locale", "format"]);
    if (n == null)
      throw new Error('[svelte-i18n] A "locale" must be set to format numbers');
    return i && (r = $e("number", i)), new Intl.NumberFormat(n, r);
  }
), Ql = Pt(
  (e) => {
    var t = e, { locale: n, format: i } = t, r = qe(t, ["locale", "format"]);
    if (n == null)
      throw new Error('[svelte-i18n] A "locale" must be set to format dates');
    return i ? r = $e("date", i) : Object.keys(r).length === 0 && (r = $e("date", "short")), new Intl.DateTimeFormat(n, r);
  }
), Jl = Pt(
  (e) => {
    var t = e, { locale: n, format: i } = t, r = qe(t, ["locale", "format"]);
    if (n == null)
      throw new Error(
        '[svelte-i18n] A "locale" must be set to format time values'
      );
    return i ? r = $e("time", i) : Object.keys(r).length === 0 && (r = $e("time", "short")), new Intl.DateTimeFormat(n, r);
  }
), Yl = (e = {}) => {
  var t = e, {
    locale: n = Ee()
  } = t, i = qe(t, [
    "locale"
  ]);
  return Wl(hn({ locale: n }, i));
}, Kl = (e = {}) => {
  var t = e, {
    locale: n = Ee()
  } = t, i = qe(t, [
    "locale"
  ]);
  return Ql(hn({ locale: n }, i));
}, $l = (e = {}) => {
  var t = e, {
    locale: n = Ee()
  } = t, i = qe(t, [
    "locale"
  ]);
  return Jl(hn({ locale: n }, i));
}, es = Pt(
  // eslint-disable-next-line @typescript-eslint/no-non-null-assertion
  (e, t = Ee()) => new Hl(e, t, Fe().formats, {
    ignoreTag: Fe().ignoreTag
  })
), ts = (e, t = {}) => {
  var n, i, r, l;
  let a = t;
  typeof e == "object" && (a = e, e = a.id);
  const {
    values: o,
    locale: s = Ee(),
    default: u
  } = a;
  if (s == null)
    throw new Error(
      "[svelte-i18n] Cannot format a message without first setting the initial locale."
    );
  let f = zi(e, s);
  if (!f)
    f = (l = (r = (i = (n = Fe()).handleMissingMessage) == null ? void 0 : i.call(n, { locale: s, id: e, defaultValue: u })) != null ? r : u) != null ? l : e;
  else if (typeof f != "string")
    return console.warn(
      `[svelte-i18n] Message with id "${e}" must be of type "string", found: "${typeof f}". Gettin its value through the "$format" method is deprecated; use the "json" method instead.`
    ), f;
  if (!o)
    return f;
  let _ = f;
  try {
    _ = es(f, s).format(o);
  } catch (c) {
    c instanceof Error && console.warn(
      `[svelte-i18n] Message "${e}" has syntax error:`,
      c.message
    );
  }
  return _;
}, ns = (e, t) => $l(t).format(e), is = (e, t) => Kl(t).format(e), rs = (e, t) => Yl(t).format(e), ls = (e, t = Ee()) => zi(e, t);
Ve([lt, rt], () => ts);
Ve([lt], () => ns);
Ve([lt], () => is);
Ve([lt], () => rs);
Ve([lt, rt], () => ls);
const {
  SvelteComponent: ss,
  assign: os,
  create_slot: as,
  detach: us,
  element: fs,
  get_all_dirty_from_scope: cs,
  get_slot_changes: hs,
  get_spread_update: _s,
  init: ms,
  insert: ds,
  safe_not_equal: bs,
  set_dynamic_element_data: Rn,
  set_style: W,
  toggle_class: de,
  transition_in: Ki,
  transition_out: $i,
  update_slot_base: gs
} = window.__gradio__svelte__internal;
function ps(e) {
  let t, n, i;
  const r = (
    /*#slots*/
    e[18].default
  ), l = as(
    r,
    e,
    /*$$scope*/
    e[17],
    null
  );
  let a = [
    { "data-testid": (
      /*test_id*/
      e[7]
    ) },
    { id: (
      /*elem_id*/
      e[2]
    ) },
    {
      class: n = "block " + /*elem_classes*/
      e[3].join(" ") + " svelte-1t38q2d"
    }
  ], o = {};
  for (let s = 0; s < a.length; s += 1)
    o = os(o, a[s]);
  return {
    c() {
      t = fs(
        /*tag*/
        e[14]
      ), l && l.c(), Rn(
        /*tag*/
        e[14]
      )(t, o), de(
        t,
        "hidden",
        /*visible*/
        e[10] === !1
      ), de(
        t,
        "padded",
        /*padding*/
        e[6]
      ), de(
        t,
        "border_focus",
        /*border_mode*/
        e[5] === "focus"
      ), de(t, "hide-container", !/*explicit_call*/
      e[8] && !/*container*/
      e[9]), W(
        t,
        "height",
        /*get_dimension*/
        e[15](
          /*height*/
          e[0]
        )
      ), W(t, "width", typeof /*width*/
      e[1] == "number" ? `calc(min(${/*width*/
      e[1]}px, 100%))` : (
        /*get_dimension*/
        e[15](
          /*width*/
          e[1]
        )
      )), W(
        t,
        "border-style",
        /*variant*/
        e[4]
      ), W(
        t,
        "overflow",
        /*allow_overflow*/
        e[11] ? "visible" : "hidden"
      ), W(
        t,
        "flex-grow",
        /*scale*/
        e[12]
      ), W(t, "min-width", `calc(min(${/*min_width*/
      e[13]}px, 100%))`), W(t, "border-width", "var(--block-border-width)");
    },
    m(s, u) {
      ds(s, t, u), l && l.m(t, null), i = !0;
    },
    p(s, u) {
      l && l.p && (!i || u & /*$$scope*/
      131072) && gs(
        l,
        r,
        s,
        /*$$scope*/
        s[17],
        i ? hs(
          r,
          /*$$scope*/
          s[17],
          u,
          null
        ) : cs(
          /*$$scope*/
          s[17]
        ),
        null
      ), Rn(
        /*tag*/
        s[14]
      )(t, o = _s(a, [
        (!i || u & /*test_id*/
        128) && { "data-testid": (
          /*test_id*/
          s[7]
        ) },
        (!i || u & /*elem_id*/
        4) && { id: (
          /*elem_id*/
          s[2]
        ) },
        (!i || u & /*elem_classes*/
        8 && n !== (n = "block " + /*elem_classes*/
        s[3].join(" ") + " svelte-1t38q2d")) && { class: n }
      ])), de(
        t,
        "hidden",
        /*visible*/
        s[10] === !1
      ), de(
        t,
        "padded",
        /*padding*/
        s[6]
      ), de(
        t,
        "border_focus",
        /*border_mode*/
        s[5] === "focus"
      ), de(t, "hide-container", !/*explicit_call*/
      s[8] && !/*container*/
      s[9]), u & /*height*/
      1 && W(
        t,
        "height",
        /*get_dimension*/
        s[15](
          /*height*/
          s[0]
        )
      ), u & /*width*/
      2 && W(t, "width", typeof /*width*/
      s[1] == "number" ? `calc(min(${/*width*/
      s[1]}px, 100%))` : (
        /*get_dimension*/
        s[15](
          /*width*/
          s[1]
        )
      )), u & /*variant*/
      16 && W(
        t,
        "border-style",
        /*variant*/
        s[4]
      ), u & /*allow_overflow*/
      2048 && W(
        t,
        "overflow",
        /*allow_overflow*/
        s[11] ? "visible" : "hidden"
      ), u & /*scale*/
      4096 && W(
        t,
        "flex-grow",
        /*scale*/
        s[12]
      ), u & /*min_width*/
      8192 && W(t, "min-width", `calc(min(${/*min_width*/
      s[13]}px, 100%))`);
    },
    i(s) {
      i || (Ki(l, s), i = !0);
    },
    o(s) {
      $i(l, s), i = !1;
    },
    d(s) {
      s && us(t), l && l.d(s);
    }
  };
}
function vs(e) {
  let t, n = (
    /*tag*/
    e[14] && ps(e)
  );
  return {
    c() {
      n && n.c();
    },
    m(i, r) {
      n && n.m(i, r), t = !0;
    },
    p(i, [r]) {
      /*tag*/
      i[14] && n.p(i, r);
    },
    i(i) {
      t || (Ki(n, i), t = !0);
    },
    o(i) {
      $i(n, i), t = !1;
    },
    d(i) {
      n && n.d(i);
    }
  };
}
function ys(e, t, n) {
  let { $$slots: i = {}, $$scope: r } = t, { height: l = void 0 } = t, { width: a = void 0 } = t, { elem_id: o = "" } = t, { elem_classes: s = [] } = t, { variant: u = "solid" } = t, { border_mode: f = "base" } = t, { padding: _ = !0 } = t, { type: c = "normal" } = t, { test_id: d = void 0 } = t, { explicit_call: v = !1 } = t, { container: y = !0 } = t, { visible: b = !0 } = t, { allow_overflow: g = !0 } = t, { scale: E = null } = t, { min_width: h = 0 } = t, m = c === "fieldset" ? "fieldset" : "div";
  const S = (p) => {
    if (p !== void 0) {
      if (typeof p == "number")
        return p + "px";
      if (typeof p == "string")
        return p;
    }
  };
  return e.$$set = (p) => {
    "height" in p && n(0, l = p.height), "width" in p && n(1, a = p.width), "elem_id" in p && n(2, o = p.elem_id), "elem_classes" in p && n(3, s = p.elem_classes), "variant" in p && n(4, u = p.variant), "border_mode" in p && n(5, f = p.border_mode), "padding" in p && n(6, _ = p.padding), "type" in p && n(16, c = p.type), "test_id" in p && n(7, d = p.test_id), "explicit_call" in p && n(8, v = p.explicit_call), "container" in p && n(9, y = p.container), "visible" in p && n(10, b = p.visible), "allow_overflow" in p && n(11, g = p.allow_overflow), "scale" in p && n(12, E = p.scale), "min_width" in p && n(13, h = p.min_width), "$$scope" in p && n(17, r = p.$$scope);
  }, [
    l,
    a,
    o,
    s,
    u,
    f,
    _,
    d,
    v,
    y,
    b,
    g,
    E,
    h,
    m,
    S,
    c,
    r,
    i
  ];
}
class ws extends ss {
  constructor(t) {
    super(), ms(this, t, ys, vs, bs, {
      height: 0,
      width: 1,
      elem_id: 2,
      elem_classes: 3,
      variant: 4,
      border_mode: 5,
      padding: 6,
      type: 16,
      test_id: 7,
      explicit_call: 8,
      container: 9,
      visible: 10,
      allow_overflow: 11,
      scale: 12,
      min_width: 13
    });
  }
}
const {
  SvelteComponent: Es,
  attr: Ss,
  create_slot: Ts,
  detach: As,
  element: Hs,
  get_all_dirty_from_scope: Bs,
  get_slot_changes: Ps,
  init: Ns,
  insert: ks,
  safe_not_equal: Cs,
  transition_in: Os,
  transition_out: Is,
  update_slot_base: Ls
} = window.__gradio__svelte__internal;
function Ms(e) {
  let t, n;
  const i = (
    /*#slots*/
    e[1].default
  ), r = Ts(
    i,
    e,
    /*$$scope*/
    e[0],
    null
  );
  return {
    c() {
      t = Hs("div"), r && r.c(), Ss(t, "class", "svelte-1hnfib2");
    },
    m(l, a) {
      ks(l, t, a), r && r.m(t, null), n = !0;
    },
    p(l, [a]) {
      r && r.p && (!n || a & /*$$scope*/
      1) && Ls(
        r,
        i,
        l,
        /*$$scope*/
        l[0],
        n ? Ps(
          i,
          /*$$scope*/
          l[0],
          a,
          null
        ) : Bs(
          /*$$scope*/
          l[0]
        ),
        null
      );
    },
    i(l) {
      n || (Os(r, l), n = !0);
    },
    o(l) {
      Is(r, l), n = !1;
    },
    d(l) {
      l && As(t), r && r.d(l);
    }
  };
}
function Rs(e, t, n) {
  let { $$slots: i = {}, $$scope: r } = t;
  return e.$$set = (l) => {
    "$$scope" in l && n(0, r = l.$$scope);
  }, [r, i];
}
class Ds extends Es {
  constructor(t) {
    super(), Ns(this, t, Rs, Ms, Cs, {});
  }
}
const {
  SvelteComponent: Us,
  attr: Dn,
  check_outros: Gs,
  create_component: Fs,
  create_slot: xs,
  destroy_component: js,
  detach: _t,
  element: Vs,
  empty: qs,
  get_all_dirty_from_scope: Xs,
  get_slot_changes: zs,
  group_outros: Zs,
  init: Ws,
  insert: mt,
  mount_component: Qs,
  safe_not_equal: Js,
  set_data: Ys,
  space: Ks,
  text: $s,
  toggle_class: Ae,
  transition_in: We,
  transition_out: dt,
  update_slot_base: eo
} = window.__gradio__svelte__internal;
function Un(e) {
  let t, n;
  return t = new Ds({
    props: {
      $$slots: { default: [to] },
      $$scope: { ctx: e }
    }
  }), {
    c() {
      Fs(t.$$.fragment);
    },
    m(i, r) {
      Qs(t, i, r), n = !0;
    },
    p(i, r) {
      const l = {};
      r & /*$$scope, info*/
      10 && (l.$$scope = { dirty: r, ctx: i }), t.$set(l);
    },
    i(i) {
      n || (We(t.$$.fragment, i), n = !0);
    },
    o(i) {
      dt(t.$$.fragment, i), n = !1;
    },
    d(i) {
      js(t, i);
    }
  };
}
function to(e) {
  let t;
  return {
    c() {
      t = $s(
        /*info*/
        e[1]
      );
    },
    m(n, i) {
      mt(n, t, i);
    },
    p(n, i) {
      i & /*info*/
      2 && Ys(
        t,
        /*info*/
        n[1]
      );
    },
    d(n) {
      n && _t(t);
    }
  };
}
function no(e) {
  let t, n, i, r;
  const l = (
    /*#slots*/
    e[2].default
  ), a = xs(
    l,
    e,
    /*$$scope*/
    e[3],
    null
  );
  let o = (
    /*info*/
    e[1] && Un(e)
  );
  return {
    c() {
      t = Vs("span"), a && a.c(), n = Ks(), o && o.c(), i = qs(), Dn(t, "data-testid", "block-info"), Dn(t, "class", "svelte-22c38v"), Ae(t, "sr-only", !/*show_label*/
      e[0]), Ae(t, "hide", !/*show_label*/
      e[0]), Ae(
        t,
        "has-info",
        /*info*/
        e[1] != null
      );
    },
    m(s, u) {
      mt(s, t, u), a && a.m(t, null), mt(s, n, u), o && o.m(s, u), mt(s, i, u), r = !0;
    },
    p(s, [u]) {
      a && a.p && (!r || u & /*$$scope*/
      8) && eo(
        a,
        l,
        s,
        /*$$scope*/
        s[3],
        r ? zs(
          l,
          /*$$scope*/
          s[3],
          u,
          null
        ) : Xs(
          /*$$scope*/
          s[3]
        ),
        null
      ), (!r || u & /*show_label*/
      1) && Ae(t, "sr-only", !/*show_label*/
      s[0]), (!r || u & /*show_label*/
      1) && Ae(t, "hide", !/*show_label*/
      s[0]), (!r || u & /*info*/
      2) && Ae(
        t,
        "has-info",
        /*info*/
        s[1] != null
      ), /*info*/
      s[1] ? o ? (o.p(s, u), u & /*info*/
      2 && We(o, 1)) : (o = Un(s), o.c(), We(o, 1), o.m(i.parentNode, i)) : o && (Zs(), dt(o, 1, 1, () => {
        o = null;
      }), Gs());
    },
    i(s) {
      r || (We(a, s), We(o), r = !0);
    },
    o(s) {
      dt(a, s), dt(o), r = !1;
    },
    d(s) {
      s && (_t(t), _t(n), _t(i)), a && a.d(s), o && o.d(s);
    }
  };
}
function io(e, t, n) {
  let { $$slots: i = {}, $$scope: r } = t, { show_label: l = !0 } = t, { info: a = void 0 } = t;
  return e.$$set = (o) => {
    "show_label" in o && n(0, l = o.show_label), "info" in o && n(1, a = o.info), "$$scope" in o && n(3, r = o.$$scope);
  }, [l, a, i, r];
}
class er extends Us {
  constructor(t) {
    super(), Ws(this, t, io, no, Js, { show_label: 0, info: 1 });
  }
}
const {
  SvelteComponent: ro,
  append: lo,
  attr: He,
  detach: so,
  init: oo,
  insert: ao,
  noop: Gt,
  safe_not_equal: uo,
  svg_element: Gn
} = window.__gradio__svelte__internal;
function fo(e) {
  let t, n;
  return {
    c() {
      t = Gn("svg"), n = Gn("path"), He(n, "d", "M5 8l4 4 4-4z"), He(t, "class", "dropdown-arrow svelte-1s6atf0"), He(t, "xmlns", "http://www.w3.org/2000/svg"), He(t, "width", "100%"), He(t, "height", "100%"), He(t, "viewBox", "0 0 18 18");
    },
    m(i, r) {
      ao(i, t, r), lo(t, n);
    },
    p: Gt,
    i: Gt,
    o: Gt,
    d(i) {
      i && so(t);
    }
  };
}
class tr extends ro {
  constructor(t) {
    super(), oo(this, t, null, fo, uo, {});
  }
}
const {
  SvelteComponent: co,
  append: ho,
  attr: Ft,
  detach: _o,
  init: mo,
  insert: bo,
  noop: xt,
  safe_not_equal: go,
  svg_element: Fn
} = window.__gradio__svelte__internal;
function po(e) {
  let t, n;
  return {
    c() {
      t = Fn("svg"), n = Fn("path"), Ft(n, "d", "M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"), Ft(t, "xmlns", "http://www.w3.org/2000/svg"), Ft(t, "viewBox", "0 0 24 24");
    },
    m(i, r) {
      bo(i, t, r), ho(t, n);
    },
    p: xt,
    i: xt,
    o: xt,
    d(i) {
      i && _o(t);
    }
  };
}
class nr extends co {
  constructor(t) {
    super(), mo(this, t, null, po, go, {});
  }
}
const vo = [
  { color: "red", primary: 600, secondary: 100 },
  { color: "green", primary: 600, secondary: 100 },
  { color: "blue", primary: 600, secondary: 100 },
  { color: "yellow", primary: 500, secondary: 100 },
  { color: "purple", primary: 600, secondary: 100 },
  { color: "teal", primary: 600, secondary: 100 },
  { color: "orange", primary: 600, secondary: 100 },
  { color: "cyan", primary: 600, secondary: 100 },
  { color: "lime", primary: 500, secondary: 100 },
  { color: "pink", primary: 600, secondary: 100 }
], xn = {
  inherit: "inherit",
  current: "currentColor",
  transparent: "transparent",
  black: "#000",
  white: "#fff",
  slate: {
    50: "#f8fafc",
    100: "#f1f5f9",
    200: "#e2e8f0",
    300: "#cbd5e1",
    400: "#94a3b8",
    500: "#64748b",
    600: "#475569",
    700: "#334155",
    800: "#1e293b",
    900: "#0f172a",
    950: "#020617"
  },
  gray: {
    50: "#f9fafb",
    100: "#f3f4f6",
    200: "#e5e7eb",
    300: "#d1d5db",
    400: "#9ca3af",
    500: "#6b7280",
    600: "#4b5563",
    700: "#374151",
    800: "#1f2937",
    900: "#111827",
    950: "#030712"
  },
  zinc: {
    50: "#fafafa",
    100: "#f4f4f5",
    200: "#e4e4e7",
    300: "#d4d4d8",
    400: "#a1a1aa",
    500: "#71717a",
    600: "#52525b",
    700: "#3f3f46",
    800: "#27272a",
    900: "#18181b",
    950: "#09090b"
  },
  neutral: {
    50: "#fafafa",
    100: "#f5f5f5",
    200: "#e5e5e5",
    300: "#d4d4d4",
    400: "#a3a3a3",
    500: "#737373",
    600: "#525252",
    700: "#404040",
    800: "#262626",
    900: "#171717",
    950: "#0a0a0a"
  },
  stone: {
    50: "#fafaf9",
    100: "#f5f5f4",
    200: "#e7e5e4",
    300: "#d6d3d1",
    400: "#a8a29e",
    500: "#78716c",
    600: "#57534e",
    700: "#44403c",
    800: "#292524",
    900: "#1c1917",
    950: "#0c0a09"
  },
  red: {
    50: "#fef2f2",
    100: "#fee2e2",
    200: "#fecaca",
    300: "#fca5a5",
    400: "#f87171",
    500: "#ef4444",
    600: "#dc2626",
    700: "#b91c1c",
    800: "#991b1b",
    900: "#7f1d1d",
    950: "#450a0a"
  },
  orange: {
    50: "#fff7ed",
    100: "#ffedd5",
    200: "#fed7aa",
    300: "#fdba74",
    400: "#fb923c",
    500: "#f97316",
    600: "#ea580c",
    700: "#c2410c",
    800: "#9a3412",
    900: "#7c2d12",
    950: "#431407"
  },
  amber: {
    50: "#fffbeb",
    100: "#fef3c7",
    200: "#fde68a",
    300: "#fcd34d",
    400: "#fbbf24",
    500: "#f59e0b",
    600: "#d97706",
    700: "#b45309",
    800: "#92400e",
    900: "#78350f",
    950: "#451a03"
  },
  yellow: {
    50: "#fefce8",
    100: "#fef9c3",
    200: "#fef08a",
    300: "#fde047",
    400: "#facc15",
    500: "#eab308",
    600: "#ca8a04",
    700: "#a16207",
    800: "#854d0e",
    900: "#713f12",
    950: "#422006"
  },
  lime: {
    50: "#f7fee7",
    100: "#ecfccb",
    200: "#d9f99d",
    300: "#bef264",
    400: "#a3e635",
    500: "#84cc16",
    600: "#65a30d",
    700: "#4d7c0f",
    800: "#3f6212",
    900: "#365314",
    950: "#1a2e05"
  },
  green: {
    50: "#f0fdf4",
    100: "#dcfce7",
    200: "#bbf7d0",
    300: "#86efac",
    400: "#4ade80",
    500: "#22c55e",
    600: "#16a34a",
    700: "#15803d",
    800: "#166534",
    900: "#14532d",
    950: "#052e16"
  },
  emerald: {
    50: "#ecfdf5",
    100: "#d1fae5",
    200: "#a7f3d0",
    300: "#6ee7b7",
    400: "#34d399",
    500: "#10b981",
    600: "#059669",
    700: "#047857",
    800: "#065f46",
    900: "#064e3b",
    950: "#022c22"
  },
  teal: {
    50: "#f0fdfa",
    100: "#ccfbf1",
    200: "#99f6e4",
    300: "#5eead4",
    400: "#2dd4bf",
    500: "#14b8a6",
    600: "#0d9488",
    700: "#0f766e",
    800: "#115e59",
    900: "#134e4a",
    950: "#042f2e"
  },
  cyan: {
    50: "#ecfeff",
    100: "#cffafe",
    200: "#a5f3fc",
    300: "#67e8f9",
    400: "#22d3ee",
    500: "#06b6d4",
    600: "#0891b2",
    700: "#0e7490",
    800: "#155e75",
    900: "#164e63",
    950: "#083344"
  },
  sky: {
    50: "#f0f9ff",
    100: "#e0f2fe",
    200: "#bae6fd",
    300: "#7dd3fc",
    400: "#38bdf8",
    500: "#0ea5e9",
    600: "#0284c7",
    700: "#0369a1",
    800: "#075985",
    900: "#0c4a6e",
    950: "#082f49"
  },
  blue: {
    50: "#eff6ff",
    100: "#dbeafe",
    200: "#bfdbfe",
    300: "#93c5fd",
    400: "#60a5fa",
    500: "#3b82f6",
    600: "#2563eb",
    700: "#1d4ed8",
    800: "#1e40af",
    900: "#1e3a8a",
    950: "#172554"
  },
  indigo: {
    50: "#eef2ff",
    100: "#e0e7ff",
    200: "#c7d2fe",
    300: "#a5b4fc",
    400: "#818cf8",
    500: "#6366f1",
    600: "#4f46e5",
    700: "#4338ca",
    800: "#3730a3",
    900: "#312e81",
    950: "#1e1b4b"
  },
  violet: {
    50: "#f5f3ff",
    100: "#ede9fe",
    200: "#ddd6fe",
    300: "#c4b5fd",
    400: "#a78bfa",
    500: "#8b5cf6",
    600: "#7c3aed",
    700: "#6d28d9",
    800: "#5b21b6",
    900: "#4c1d95",
    950: "#2e1065"
  },
  purple: {
    50: "#faf5ff",
    100: "#f3e8ff",
    200: "#e9d5ff",
    300: "#d8b4fe",
    400: "#c084fc",
    500: "#a855f7",
    600: "#9333ea",
    700: "#7e22ce",
    800: "#6b21a8",
    900: "#581c87",
    950: "#3b0764"
  },
  fuchsia: {
    50: "#fdf4ff",
    100: "#fae8ff",
    200: "#f5d0fe",
    300: "#f0abfc",
    400: "#e879f9",
    500: "#d946ef",
    600: "#c026d3",
    700: "#a21caf",
    800: "#86198f",
    900: "#701a75",
    950: "#4a044e"
  },
  pink: {
    50: "#fdf2f8",
    100: "#fce7f3",
    200: "#fbcfe8",
    300: "#f9a8d4",
    400: "#f472b6",
    500: "#ec4899",
    600: "#db2777",
    700: "#be185d",
    800: "#9d174d",
    900: "#831843",
    950: "#500724"
  },
  rose: {
    50: "#fff1f2",
    100: "#ffe4e6",
    200: "#fecdd3",
    300: "#fda4af",
    400: "#fb7185",
    500: "#f43f5e",
    600: "#e11d48",
    700: "#be123c",
    800: "#9f1239",
    900: "#881337",
    950: "#4c0519"
  }
};
vo.reduce(
  (e, { color: t, primary: n, secondary: i }) => ({
    ...e,
    [t]: {
      primary: xn[t][n],
      secondary: xn[t][i]
    }
  }),
  {}
);
const {
  SvelteComponent: yo,
  add_render_callback: ir,
  append: ot,
  attr: Q,
  binding_callbacks: jn,
  check_outros: wo,
  create_bidirectional_transition: Vn,
  destroy_each: Eo,
  detach: Je,
  element: pt,
  empty: So,
  ensure_array_like: qn,
  group_outros: To,
  init: Ao,
  insert: Ye,
  listen: tn,
  prevent_default: Ho,
  run_all: Bo,
  safe_not_equal: Po,
  set_data: No,
  set_style: be,
  space: nn,
  text: ko,
  toggle_class: ne,
  transition_in: jt,
  transition_out: Xn
} = window.__gradio__svelte__internal, { createEventDispatcher: Co } = window.__gradio__svelte__internal;
function zn(e, t, n) {
  const i = e.slice();
  return i[24] = t[n], i;
}
function Zn(e) {
  let t, n, i, r, l, a = qn(
    /*filtered_indices*/
    e[1]
  ), o = [];
  for (let s = 0; s < a.length; s += 1)
    o[s] = Wn(zn(e, a, s));
  return {
    c() {
      t = pt("ul");
      for (let s = 0; s < o.length; s += 1)
        o[s].c();
      Q(t, "class", "options svelte-yuohum"), Q(t, "role", "listbox"), be(
        t,
        "top",
        /*top*/
        e[9]
      ), be(
        t,
        "bottom",
        /*bottom*/
        e[10]
      ), be(t, "max-height", `calc(${/*max_height*/
      e[11]}px - var(--window-padding))`), be(
        t,
        "width",
        /*input_width*/
        e[8] + "px"
      );
    },
    m(s, u) {
      Ye(s, t, u);
      for (let f = 0; f < o.length; f += 1)
        o[f] && o[f].m(t, null);
      e[21](t), i = !0, r || (l = tn(t, "mousedown", Ho(
        /*mousedown_handler*/
        e[20]
      )), r = !0);
    },
    p(s, u) {
      if (u & /*filtered_indices, choices, selected_indices, active_index*/
      51) {
        a = qn(
          /*filtered_indices*/
          s[1]
        );
        let f;
        for (f = 0; f < a.length; f += 1) {
          const _ = zn(s, a, f);
          o[f] ? o[f].p(_, u) : (o[f] = Wn(_), o[f].c(), o[f].m(t, null));
        }
        for (; f < o.length; f += 1)
          o[f].d(1);
        o.length = a.length;
      }
      u & /*top*/
      512 && be(
        t,
        "top",
        /*top*/
        s[9]
      ), u & /*bottom*/
      1024 && be(
        t,
        "bottom",
        /*bottom*/
        s[10]
      ), u & /*max_height*/
      2048 && be(t, "max-height", `calc(${/*max_height*/
      s[11]}px - var(--window-padding))`), u & /*input_width*/
      256 && be(
        t,
        "width",
        /*input_width*/
        s[8] + "px"
      );
    },
    i(s) {
      i || (s && ir(() => {
        i && (n || (n = Vn(t, yn, { duration: 200, y: 5 }, !0)), n.run(1));
      }), i = !0);
    },
    o(s) {
      s && (n || (n = Vn(t, yn, { duration: 200, y: 5 }, !1)), n.run(0)), i = !1;
    },
    d(s) {
      s && Je(t), Eo(o, s), e[21](null), s && n && n.end(), r = !1, l();
    }
  };
}
function Wn(e) {
  let t, n, i, r = (
    /*choices*/
    e[0][
      /*index*/
      e[24]
    ][0] + ""
  ), l, a, o, s, u;
  return {
    c() {
      t = pt("li"), n = pt("span"), n.textContent = "✓", i = nn(), l = ko(r), a = nn(), Q(n, "class", "inner-item svelte-yuohum"), ne(n, "hide", !/*selected_indices*/
      e[4].includes(
        /*index*/
        e[24]
      )), Q(t, "class", "item svelte-yuohum"), Q(t, "data-index", o = /*index*/
      e[24]), Q(t, "aria-label", s = /*choices*/
      e[0][
        /*index*/
        e[24]
      ][0]), Q(t, "data-testid", "dropdown-option"), Q(t, "role", "option"), Q(t, "aria-selected", u = /*selected_indices*/
      e[4].includes(
        /*index*/
        e[24]
      )), ne(
        t,
        "selected",
        /*selected_indices*/
        e[4].includes(
          /*index*/
          e[24]
        )
      ), ne(
        t,
        "active",
        /*index*/
        e[24] === /*active_index*/
        e[5]
      ), ne(
        t,
        "bg-gray-100",
        /*index*/
        e[24] === /*active_index*/
        e[5]
      ), ne(
        t,
        "dark:bg-gray-600",
        /*index*/
        e[24] === /*active_index*/
        e[5]
      );
    },
    m(f, _) {
      Ye(f, t, _), ot(t, n), ot(t, i), ot(t, l), ot(t, a);
    },
    p(f, _) {
      _ & /*selected_indices, filtered_indices*/
      18 && ne(n, "hide", !/*selected_indices*/
      f[4].includes(
        /*index*/
        f[24]
      )), _ & /*choices, filtered_indices*/
      3 && r !== (r = /*choices*/
      f[0][
        /*index*/
        f[24]
      ][0] + "") && No(l, r), _ & /*filtered_indices*/
      2 && o !== (o = /*index*/
      f[24]) && Q(t, "data-index", o), _ & /*choices, filtered_indices*/
      3 && s !== (s = /*choices*/
      f[0][
        /*index*/
        f[24]
      ][0]) && Q(t, "aria-label", s), _ & /*selected_indices, filtered_indices*/
      18 && u !== (u = /*selected_indices*/
      f[4].includes(
        /*index*/
        f[24]
      )) && Q(t, "aria-selected", u), _ & /*selected_indices, filtered_indices*/
      18 && ne(
        t,
        "selected",
        /*selected_indices*/
        f[4].includes(
          /*index*/
          f[24]
        )
      ), _ & /*filtered_indices, active_index*/
      34 && ne(
        t,
        "active",
        /*index*/
        f[24] === /*active_index*/
        f[5]
      ), _ & /*filtered_indices, active_index*/
      34 && ne(
        t,
        "bg-gray-100",
        /*index*/
        f[24] === /*active_index*/
        f[5]
      ), _ & /*filtered_indices, active_index*/
      34 && ne(
        t,
        "dark:bg-gray-600",
        /*index*/
        f[24] === /*active_index*/
        f[5]
      );
    },
    d(f) {
      f && Je(t);
    }
  };
}
function Oo(e) {
  let t, n, i, r, l;
  ir(
    /*onwindowresize*/
    e[18]
  );
  let a = (
    /*show_options*/
    e[2] && !/*disabled*/
    e[3] && Zn(e)
  );
  return {
    c() {
      t = pt("div"), n = nn(), a && a.c(), i = So(), Q(t, "class", "reference");
    },
    m(o, s) {
      Ye(o, t, s), e[19](t), Ye(o, n, s), a && a.m(o, s), Ye(o, i, s), r || (l = [
        tn(
          window,
          "scroll",
          /*scroll_listener*/
          e[13]
        ),
        tn(
          window,
          "resize",
          /*onwindowresize*/
          e[18]
        )
      ], r = !0);
    },
    p(o, [s]) {
      /*show_options*/
      o[2] && !/*disabled*/
      o[3] ? a ? (a.p(o, s), s & /*show_options, disabled*/
      12 && jt(a, 1)) : (a = Zn(o), a.c(), jt(a, 1), a.m(i.parentNode, i)) : a && (To(), Xn(a, 1, 1, () => {
        a = null;
      }), wo());
    },
    i(o) {
      jt(a);
    },
    o(o) {
      Xn(a);
    },
    d(o) {
      o && (Je(t), Je(n), Je(i)), e[19](null), a && a.d(o), r = !1, Bo(l);
    }
  };
}
function at(e) {
  let t, n = e[0], i = 1;
  for (; i < e.length; ) {
    const r = e[i], l = e[i + 1];
    if (i += 2, (r === "optionalAccess" || r === "optionalCall") && n == null)
      return;
    r === "access" || r === "optionalAccess" ? (t = n, n = l(n)) : (r === "call" || r === "optionalCall") && (n = l((...a) => n.call(t, ...a)), t = void 0);
  }
  return n;
}
function Io(e, t, n) {
  let { choices: i } = t, { filtered_indices: r } = t, { show_options: l = !1 } = t, { disabled: a = !1 } = t, { selected_indices: o = [] } = t, { active_index: s = null } = t, u, f, _, c, d, v, y, b, g, E;
  function h() {
    const { top: N, bottom: D } = d.getBoundingClientRect();
    n(15, u = N), n(16, f = E - D);
  }
  let m = null;
  function S() {
    l && (m !== null && clearTimeout(m), m = setTimeout(
      () => {
        h(), m = null;
      },
      10
    ));
  }
  const p = Co();
  function k() {
    n(12, E = window.innerHeight);
  }
  function T(N) {
    jn[N ? "unshift" : "push"](() => {
      d = N, n(6, d);
    });
  }
  const B = (N) => p("change", N);
  function F(N) {
    jn[N ? "unshift" : "push"](() => {
      v = N, n(7, v);
    });
  }
  return e.$$set = (N) => {
    "choices" in N && n(0, i = N.choices), "filtered_indices" in N && n(1, r = N.filtered_indices), "show_options" in N && n(2, l = N.show_options), "disabled" in N && n(3, a = N.disabled), "selected_indices" in N && n(4, o = N.selected_indices), "active_index" in N && n(5, s = N.active_index);
  }, e.$$.update = () => {
    if (e.$$.dirty & /*show_options, refElement, listElement, selected_indices, distance_from_bottom, distance_from_top, input_height*/
    229588) {
      if (l && d) {
        if (v && o.length > 0) {
          let D = v.querySelectorAll("li");
          for (const x of Array.from(D))
            if (x.getAttribute("data-index") === o[0].toString()) {
              at([
                v,
                "optionalAccess",
                (V) => V.scrollTo,
                "optionalCall",
                (V) => V(0, x.offsetTop)
              ]);
              break;
            }
        }
        h();
        const N = at([
          d,
          "access",
          (D) => D.parentElement,
          "optionalAccess",
          (D) => D.getBoundingClientRect,
          "call",
          (D) => D()
        ]);
        n(17, _ = at([N, "optionalAccess", (D) => D.height]) || 0), n(8, c = at([N, "optionalAccess", (D) => D.width]) || 0);
      }
      f > u ? (n(9, y = `${u}px`), n(11, g = f), n(10, b = null)) : (n(10, b = `${f + _}px`), n(11, g = u - _), n(9, y = null));
    }
  }, [
    i,
    r,
    l,
    a,
    o,
    s,
    d,
    v,
    c,
    y,
    b,
    g,
    E,
    S,
    p,
    u,
    f,
    _,
    k,
    T,
    B,
    F
  ];
}
class rr extends yo {
  constructor(t) {
    super(), Ao(this, t, Io, Oo, Po, {
      choices: 0,
      filtered_indices: 1,
      show_options: 2,
      disabled: 3,
      selected_indices: 4,
      active_index: 5
    });
  }
}
function Lo(e, t) {
  return (e % t + t) % t;
}
function rn(e, t) {
  return e.reduce((n, i, r) => ((!t || i[0].toLowerCase().includes(t.toLowerCase())) && n.push(r), n), []);
}
function lr(e, t, n) {
  e("change", t), n || e("input");
}
function sr(e, t, n) {
  if (e.key === "Escape")
    return [!1, t];
  if ((e.key === "ArrowDown" || e.key === "ArrowUp") && n.length >= 0)
    if (t === null)
      t = e.key === "ArrowDown" ? n[0] : n[n.length - 1];
    else {
      const i = n.indexOf(t), r = e.key === "ArrowUp" ? -1 : 1;
      t = n[Lo(i + r, n.length)];
    }
  return [!0, t];
}
const {
  SvelteComponent: Mo,
  append: ie,
  attr: j,
  binding_callbacks: Ro,
  check_outros: vt,
  create_component: et,
  destroy_component: tt,
  destroy_each: Do,
  detach: fe,
  element: re,
  ensure_array_like: Qn,
  group_outros: yt,
  init: Uo,
  insert: ce,
  listen: ae,
  mount_component: nt,
  prevent_default: Jn,
  run_all: _n,
  safe_not_equal: Go,
  set_data: mn,
  set_input_value: Yn,
  space: Oe,
  text: dn,
  toggle_class: Be,
  transition_in: q,
  transition_out: J
} = window.__gradio__svelte__internal, { afterUpdate: Fo, createEventDispatcher: xo } = window.__gradio__svelte__internal;
function Kn(e, t, n) {
  const i = e.slice();
  return i[40] = t[n], i;
}
function jo(e) {
  let t;
  return {
    c() {
      t = dn(
        /*label*/
        e[0]
      );
    },
    m(n, i) {
      ce(n, t, i);
    },
    p(n, i) {
      i[0] & /*label*/
      1 && mn(
        t,
        /*label*/
        n[0]
      );
    },
    d(n) {
      n && fe(t);
    }
  };
}
function Vo(e) {
  let t = (
    /*s*/
    e[40] + ""
  ), n;
  return {
    c() {
      n = dn(t);
    },
    m(i, r) {
      ce(i, n, r);
    },
    p(i, r) {
      r[0] & /*selected_indices*/
      4096 && t !== (t = /*s*/
      i[40] + "") && mn(n, t);
    },
    d(i) {
      i && fe(n);
    }
  };
}
function qo(e) {
  let t = (
    /*choices_names*/
    e[15][
      /*s*/
      e[40]
    ] + ""
  ), n;
  return {
    c() {
      n = dn(t);
    },
    m(i, r) {
      ce(i, n, r);
    },
    p(i, r) {
      r[0] & /*choices_names, selected_indices*/
      36864 && t !== (t = /*choices_names*/
      i[15][
        /*s*/
        i[40]
      ] + "") && mn(n, t);
    },
    d(i) {
      i && fe(n);
    }
  };
}
function $n(e) {
  let t, n, i, r, l, a;
  n = new nr({});
  function o() {
    return (
      /*click_handler*/
      e[31](
        /*s*/
        e[40]
      )
    );
  }
  function s(...u) {
    return (
      /*keydown_handler*/
      e[32](
        /*s*/
        e[40],
        ...u
      )
    );
  }
  return {
    c() {
      t = re("div"), et(n.$$.fragment), j(t, "class", "token-remove svelte-xtjjyg"), j(t, "role", "button"), j(t, "tabindex", "0"), j(t, "title", i = /*i18n*/
      e[9]("common.remove") + " " + /*s*/
      e[40]);
    },
    m(u, f) {
      ce(u, t, f), nt(n, t, null), r = !0, l || (a = [
        ae(t, "click", Jn(o)),
        ae(t, "keydown", Jn(s))
      ], l = !0);
    },
    p(u, f) {
      e = u, (!r || f[0] & /*i18n, selected_indices*/
      4608 && i !== (i = /*i18n*/
      e[9]("common.remove") + " " + /*s*/
      e[40])) && j(t, "title", i);
    },
    i(u) {
      r || (q(n.$$.fragment, u), r = !0);
    },
    o(u) {
      J(n.$$.fragment, u), r = !1;
    },
    d(u) {
      u && fe(t), tt(n), l = !1, _n(a);
    }
  };
}
function ei(e) {
  let t, n, i, r;
  function l(u, f) {
    return typeof /*s*/
    u[40] == "number" ? qo : Vo;
  }
  let a = l(e), o = a(e), s = !/*disabled*/
  e[4] && $n(e);
  return {
    c() {
      t = re("div"), n = re("span"), o.c(), i = Oe(), s && s.c(), j(n, "class", "svelte-xtjjyg"), j(t, "class", "token svelte-xtjjyg");
    },
    m(u, f) {
      ce(u, t, f), ie(t, n), o.m(n, null), ie(t, i), s && s.m(t, null), r = !0;
    },
    p(u, f) {
      a === (a = l(u)) && o ? o.p(u, f) : (o.d(1), o = a(u), o && (o.c(), o.m(n, null))), /*disabled*/
      u[4] ? s && (yt(), J(s, 1, 1, () => {
        s = null;
      }), vt()) : s ? (s.p(u, f), f[0] & /*disabled*/
      16 && q(s, 1)) : (s = $n(u), s.c(), q(s, 1), s.m(t, null));
    },
    i(u) {
      r || (q(s), r = !0);
    },
    o(u) {
      J(s), r = !1;
    },
    d(u) {
      u && fe(t), o.d(), s && s.d();
    }
  };
}
function ti(e) {
  let t, n, i, r, l = (
    /*selected_indices*/
    e[12].length > 0 && ni(e)
  );
  return i = new tr({}), {
    c() {
      l && l.c(), t = Oe(), n = re("span"), et(i.$$.fragment), j(n, "class", "icon-wrap svelte-xtjjyg");
    },
    m(a, o) {
      l && l.m(a, o), ce(a, t, o), ce(a, n, o), nt(i, n, null), r = !0;
    },
    p(a, o) {
      /*selected_indices*/
      a[12].length > 0 ? l ? (l.p(a, o), o[0] & /*selected_indices*/
      4096 && q(l, 1)) : (l = ni(a), l.c(), q(l, 1), l.m(t.parentNode, t)) : l && (yt(), J(l, 1, 1, () => {
        l = null;
      }), vt());
    },
    i(a) {
      r || (q(l), q(i.$$.fragment, a), r = !0);
    },
    o(a) {
      J(l), J(i.$$.fragment, a), r = !1;
    },
    d(a) {
      a && (fe(t), fe(n)), l && l.d(a), tt(i);
    }
  };
}
function ni(e) {
  let t, n, i, r, l, a;
  return n = new nr({}), {
    c() {
      t = re("div"), et(n.$$.fragment), j(t, "role", "button"), j(t, "tabindex", "0"), j(t, "class", "token-remove remove-all svelte-xtjjyg"), j(t, "title", i = /*i18n*/
      e[9]("common.clear"));
    },
    m(o, s) {
      ce(o, t, s), nt(n, t, null), r = !0, l || (a = [
        ae(
          t,
          "click",
          /*remove_all*/
          e[21]
        ),
        ae(
          t,
          "keydown",
          /*keydown_handler_1*/
          e[36]
        )
      ], l = !0);
    },
    p(o, s) {
      (!r || s[0] & /*i18n*/
      512 && i !== (i = /*i18n*/
      o[9]("common.clear"))) && j(t, "title", i);
    },
    i(o) {
      r || (q(n.$$.fragment, o), r = !0);
    },
    o(o) {
      J(n.$$.fragment, o), r = !1;
    },
    d(o) {
      o && fe(t), tt(n), l = !1, _n(a);
    }
  };
}
function Xo(e) {
  let t, n, i, r, l, a, o, s, u, f, _, c, d, v, y;
  n = new er({
    props: {
      show_label: (
        /*show_label*/
        e[5]
      ),
      info: (
        /*info*/
        e[1]
      ),
      $$slots: { default: [jo] },
      $$scope: { ctx: e }
    }
  });
  let b = Qn(
    /*selected_indices*/
    e[12]
  ), g = [];
  for (let m = 0; m < b.length; m += 1)
    g[m] = ei(Kn(e, b, m));
  const E = (m) => J(g[m], 1, 1, () => {
    g[m] = null;
  });
  let h = !/*disabled*/
  e[4] && ti(e);
  return c = new rr({
    props: {
      show_options: (
        /*show_options*/
        e[14]
      ),
      choices: (
        /*choices*/
        e[3]
      ),
      filtered_indices: (
        /*filtered_indices*/
        e[11]
      ),
      disabled: (
        /*disabled*/
        e[4]
      ),
      selected_indices: (
        /*selected_indices*/
        e[12]
      ),
      active_index: (
        /*active_index*/
        e[16]
      )
    }
  }), c.$on(
    "change",
    /*handle_option_selected*/
    e[20]
  ), {
    c() {
      t = re("label"), et(n.$$.fragment), i = Oe(), r = re("div"), l = re("div");
      for (let m = 0; m < g.length; m += 1)
        g[m].c();
      a = Oe(), o = re("div"), s = re("input"), f = Oe(), h && h.c(), _ = Oe(), et(c.$$.fragment), j(s, "class", "border-none svelte-xtjjyg"), s.disabled = /*disabled*/
      e[4], j(s, "autocomplete", "off"), s.readOnly = u = !/*filterable*/
      e[8], Be(s, "subdued", !/*choices_names*/
      e[15].includes(
        /*input_text*/
        e[10]
      ) && !/*allow_custom_value*/
      e[7] || /*selected_indices*/
      e[12].length === /*max_choices*/
      e[2]), j(o, "class", "secondary-wrap svelte-xtjjyg"), j(l, "class", "wrap-inner svelte-xtjjyg"), Be(
        l,
        "show_options",
        /*show_options*/
        e[14]
      ), j(r, "class", "wrap svelte-xtjjyg"), j(t, "class", "svelte-xtjjyg"), Be(
        t,
        "container",
        /*container*/
        e[6]
      );
    },
    m(m, S) {
      ce(m, t, S), nt(n, t, null), ie(t, i), ie(t, r), ie(r, l);
      for (let p = 0; p < g.length; p += 1)
        g[p] && g[p].m(l, null);
      ie(l, a), ie(l, o), ie(o, s), Yn(
        s,
        /*input_text*/
        e[10]
      ), e[34](s), ie(o, f), h && h.m(o, null), ie(r, _), nt(c, r, null), d = !0, v || (y = [
        ae(
          s,
          "input",
          /*input_input_handler*/
          e[33]
        ),
        ae(
          s,
          "keydown",
          /*handle_key_down*/
          e[23]
        ),
        ae(
          s,
          "keyup",
          /*keyup_handler*/
          e[35]
        ),
        ae(
          s,
          "blur",
          /*handle_blur*/
          e[18]
        ),
        ae(
          s,
          "focus",
          /*handle_focus*/
          e[22]
        )
      ], v = !0);
    },
    p(m, S) {
      const p = {};
      if (S[0] & /*show_label*/
      32 && (p.show_label = /*show_label*/
      m[5]), S[0] & /*info*/
      2 && (p.info = /*info*/
      m[1]), S[0] & /*label*/
      1 | S[1] & /*$$scope*/
      4096 && (p.$$scope = { dirty: S, ctx: m }), n.$set(p), S[0] & /*i18n, selected_indices, remove_selected_choice, disabled, choices_names*/
      561680) {
        b = Qn(
          /*selected_indices*/
          m[12]
        );
        let T;
        for (T = 0; T < b.length; T += 1) {
          const B = Kn(m, b, T);
          g[T] ? (g[T].p(B, S), q(g[T], 1)) : (g[T] = ei(B), g[T].c(), q(g[T], 1), g[T].m(l, a));
        }
        for (yt(), T = b.length; T < g.length; T += 1)
          E(T);
        vt();
      }
      (!d || S[0] & /*disabled*/
      16) && (s.disabled = /*disabled*/
      m[4]), (!d || S[0] & /*filterable*/
      256 && u !== (u = !/*filterable*/
      m[8])) && (s.readOnly = u), S[0] & /*input_text*/
      1024 && s.value !== /*input_text*/
      m[10] && Yn(
        s,
        /*input_text*/
        m[10]
      ), (!d || S[0] & /*choices_names, input_text, allow_custom_value, selected_indices, max_choices*/
      38020) && Be(s, "subdued", !/*choices_names*/
      m[15].includes(
        /*input_text*/
        m[10]
      ) && !/*allow_custom_value*/
      m[7] || /*selected_indices*/
      m[12].length === /*max_choices*/
      m[2]), /*disabled*/
      m[4] ? h && (yt(), J(h, 1, 1, () => {
        h = null;
      }), vt()) : h ? (h.p(m, S), S[0] & /*disabled*/
      16 && q(h, 1)) : (h = ti(m), h.c(), q(h, 1), h.m(o, null)), (!d || S[0] & /*show_options*/
      16384) && Be(
        l,
        "show_options",
        /*show_options*/
        m[14]
      );
      const k = {};
      S[0] & /*show_options*/
      16384 && (k.show_options = /*show_options*/
      m[14]), S[0] & /*choices*/
      8 && (k.choices = /*choices*/
      m[3]), S[0] & /*filtered_indices*/
      2048 && (k.filtered_indices = /*filtered_indices*/
      m[11]), S[0] & /*disabled*/
      16 && (k.disabled = /*disabled*/
      m[4]), S[0] & /*selected_indices*/
      4096 && (k.selected_indices = /*selected_indices*/
      m[12]), S[0] & /*active_index*/
      65536 && (k.active_index = /*active_index*/
      m[16]), c.$set(k), (!d || S[0] & /*container*/
      64) && Be(
        t,
        "container",
        /*container*/
        m[6]
      );
    },
    i(m) {
      if (!d) {
        q(n.$$.fragment, m);
        for (let S = 0; S < b.length; S += 1)
          q(g[S]);
        q(h), q(c.$$.fragment, m), d = !0;
      }
    },
    o(m) {
      J(n.$$.fragment, m), g = g.filter(Boolean);
      for (let S = 0; S < g.length; S += 1)
        J(g[S]);
      J(h), J(c.$$.fragment, m), d = !1;
    },
    d(m) {
      m && fe(t), tt(n), Do(g, m), e[34](null), h && h.d(), tt(c), v = !1, _n(y);
    }
  };
}
function zo(e, t, n) {
  let { label: i } = t, { info: r = void 0 } = t, { value: l = [] } = t, a = [], { value_is_output: o = !1 } = t, { max_choices: s = null } = t, { choices: u } = t, f, { disabled: _ = !1 } = t, { show_label: c } = t, { container: d = !0 } = t, { allow_custom_value: v = !1 } = t, { filterable: y = !0 } = t, { i18n: b } = t, g, E = "", h = "", m = !1, S, p, k = [], T = null, B = [], F = [];
  const N = xo();
  Array.isArray(l) && l.forEach((w) => {
    const Y = u.map((Ot) => Ot[1]).indexOf(w);
    Y !== -1 ? B.push(Y) : B.push(w);
  });
  function D() {
    v || n(10, E = ""), v && E !== "" && (V(E), n(10, E = "")), n(14, m = !1), n(16, T = null), N("blur");
  }
  function x(w) {
    n(12, B = B.filter((Y) => Y !== w)), N("select", {
      index: typeof w == "number" ? w : -1,
      value: typeof w == "number" ? p[w] : w,
      selected: !1
    });
  }
  function V(w) {
    (s === null || B.length < s) && (n(12, B = [...B, w]), N("select", {
      index: typeof w == "number" ? w : -1,
      value: typeof w == "number" ? p[w] : w,
      selected: !0
    })), B.length === s && (n(14, m = !1), n(16, T = null), g.blur());
  }
  function z(w) {
    const Y = parseInt(w.detail.target.dataset.index);
    oe(Y);
  }
  function oe(w) {
    B.includes(w) ? x(w) : V(w), n(10, E = "");
  }
  function he(w) {
    n(12, B = []), n(10, E = ""), w.preventDefault();
  }
  function _e(w) {
    n(11, k = u.map((Y, Ot) => Ot)), (s === null || B.length < s) && n(14, m = !0), N("focus");
  }
  function me(w) {
    n(14, [m, T] = sr(w, T, k), m, (n(16, T), n(3, u), n(27, f), n(10, E), n(28, h), n(7, v), n(11, k))), w.key === "Enter" && (T !== null ? oe(T) : v && (V(E), n(10, E = ""))), w.key === "Backspace" && E === "" && n(12, B = [...B.slice(0, -1)]), B.length === s && (n(14, m = !1), n(16, T = null));
  }
  function P() {
    l === void 0 ? n(12, B = []) : Array.isArray(l) && n(12, B = l.map((w) => {
      const Y = p.indexOf(w);
      if (Y !== -1)
        return Y;
      if (v)
        return w;
    }).filter((w) => w !== void 0));
  }
  Fo(() => {
    n(25, o = !1);
  });
  const Se = (w) => x(w), A = (w, Y) => {
    Y.key === "Enter" && x(w);
  };
  function H() {
    E = this.value, n(10, E);
  }
  function fr(w) {
    Ro[w ? "unshift" : "push"](() => {
      g = w, n(13, g);
    });
  }
  const cr = (w) => N("key_up", { key: w.key, input_value: E }), hr = (w) => {
    w.key === "Enter" && he(w);
  };
  return e.$$set = (w) => {
    "label" in w && n(0, i = w.label), "info" in w && n(1, r = w.info), "value" in w && n(24, l = w.value), "value_is_output" in w && n(25, o = w.value_is_output), "max_choices" in w && n(2, s = w.max_choices), "choices" in w && n(3, u = w.choices), "disabled" in w && n(4, _ = w.disabled), "show_label" in w && n(5, c = w.show_label), "container" in w && n(6, d = w.container), "allow_custom_value" in w && n(7, v = w.allow_custom_value), "filterable" in w && n(8, y = w.filterable), "i18n" in w && n(9, b = w.i18n);
  }, e.$$.update = () => {
    e.$$.dirty[0] & /*choices*/
    8 && (n(15, S = u.map((w) => w[0])), n(29, p = u.map((w) => w[1]))), e.$$.dirty[0] & /*choices, old_choices, input_text, old_input_text, allow_custom_value, filtered_indices*/
    402656392 && (u !== f || E !== h) && (n(11, k = rn(u, E)), n(27, f = u), n(28, h = E), v || n(16, T = k[0])), e.$$.dirty[0] & /*selected_indices, old_selected_index, choices_values*/
    1610616832 && JSON.stringify(B) != JSON.stringify(F) && (n(24, l = B.map((w) => typeof w == "number" ? p[w] : w)), n(30, F = B.slice())), e.$$.dirty[0] & /*value, old_value, value_is_output*/
    117440512 && JSON.stringify(l) != JSON.stringify(a) && (lr(N, l, o), n(26, a = Array.isArray(l) ? l.slice() : l)), e.$$.dirty[0] & /*value*/
    16777216 && P();
  }, [
    i,
    r,
    s,
    u,
    _,
    c,
    d,
    v,
    y,
    b,
    E,
    k,
    B,
    g,
    m,
    S,
    T,
    N,
    D,
    x,
    z,
    he,
    _e,
    me,
    l,
    o,
    a,
    f,
    h,
    p,
    F,
    Se,
    A,
    H,
    fr,
    cr,
    hr
  ];
}
class Zo extends Mo {
  constructor(t) {
    super(), Uo(
      this,
      t,
      zo,
      Xo,
      Go,
      {
        label: 0,
        info: 1,
        value: 24,
        value_is_output: 25,
        max_choices: 2,
        choices: 3,
        disabled: 4,
        show_label: 5,
        container: 6,
        allow_custom_value: 7,
        filterable: 8,
        i18n: 9
      },
      null,
      [-1, -1]
    );
  }
}
const {
  SvelteComponent: Wo,
  append: ve,
  attr: Z,
  binding_callbacks: Qo,
  check_outros: Jo,
  create_component: ln,
  destroy_component: sn,
  detach: bn,
  element: ke,
  group_outros: Yo,
  init: Ko,
  insert: gn,
  listen: Ze,
  mount_component: on,
  run_all: $o,
  safe_not_equal: ea,
  set_data: ta,
  set_input_value: ii,
  space: Vt,
  text: na,
  toggle_class: Pe,
  transition_in: Ce,
  transition_out: Qe
} = window.__gradio__svelte__internal, { createEventDispatcher: ia, afterUpdate: ra } = window.__gradio__svelte__internal;
function la(e) {
  let t;
  return {
    c() {
      t = na(
        /*label*/
        e[0]
      );
    },
    m(n, i) {
      gn(n, t, i);
    },
    p(n, i) {
      i[0] & /*label*/
      1 && ta(
        t,
        /*label*/
        n[0]
      );
    },
    d(n) {
      n && bn(t);
    }
  };
}
function ri(e) {
  let t, n, i;
  return n = new tr({}), {
    c() {
      t = ke("div"), ln(n.$$.fragment), Z(t, "class", "icon-wrap svelte-1v1qvgk"), Z(t, "id", "custom-dropdown-arrow");
    },
    m(r, l) {
      gn(r, t, l), on(n, t, null), i = !0;
    },
    i(r) {
      i || (Ce(n.$$.fragment, r), i = !0);
    },
    o(r) {
      Qe(n.$$.fragment, r), i = !1;
    },
    d(r) {
      r && bn(t), sn(n);
    }
  };
}
function sa(e) {
  let t, n, i, r, l, a, o, s, u, f, _, c, d, v;
  n = new er({
    props: {
      show_label: (
        /*show_label*/
        e[4]
      ),
      info: (
        /*info*/
        e[1]
      ),
      $$slots: { default: [la] },
      $$scope: { ctx: e }
    }
  });
  let y = !/*disabled*/
  e[3] && ri();
  return _ = new rr({
    props: {
      show_options: (
        /*show_options*/
        e[12]
      ),
      choices: (
        /*choices*/
        e[2]
      ),
      filtered_indices: (
        /*filtered_indices*/
        e[10]
      ),
      disabled: (
        /*disabled*/
        e[3]
      ),
      selected_indices: (
        /*selected_index*/
        e[11] === null ? [] : [
          /*selected_index*/
          e[11]
        ]
      ),
      active_index: (
        /*active_index*/
        e[14]
      )
    }
  }), _.$on(
    "change",
    /*handle_option_selected*/
    e[16]
  ), {
    c() {
      t = ke("div"), ln(n.$$.fragment), i = Vt(), r = ke("div"), l = ke("div"), a = ke("div"), o = ke("input"), u = Vt(), y && y.c(), f = Vt(), ln(_.$$.fragment), Z(o, "role", "listbox"), Z(o, "aria-controls", "dropdown-options"), Z(
        o,
        "aria-expanded",
        /*show_options*/
        e[12]
      ), Z(
        o,
        "aria-label",
        /*label*/
        e[0]
      ), Z(o, "class", "border-none svelte-1v1qvgk"), o.disabled = /*disabled*/
      e[3], Z(o, "autocomplete", "off"), o.readOnly = s = !/*filterable*/
      e[7], Pe(o, "subdued", !/*choices_names*/
      e[13].includes(
        /*input_text*/
        e[9]
      ) && !/*allow_custom_value*/
      e[6]), Z(a, "class", "secondary-wrap svelte-1v1qvgk"), Z(l, "class", "wrap-inner svelte-1v1qvgk"), Pe(
        l,
        "show_options",
        /*show_options*/
        e[12]
      ), Z(r, "class", "wrap svelte-1v1qvgk"), Z(t, "class", "svelte-1v1qvgk"), Pe(
        t,
        "container",
        /*container*/
        e[5]
      );
    },
    m(b, g) {
      gn(b, t, g), on(n, t, null), ve(t, i), ve(t, r), ve(r, l), ve(l, a), ve(a, o), ii(
        o,
        /*input_text*/
        e[9]
      ), e[29](o), ve(a, u), y && y.m(a, null), ve(r, f), on(_, r, null), c = !0, d || (v = [
        Ze(
          o,
          "input",
          /*input_input_handler*/
          e[28]
        ),
        Ze(
          o,
          "keydown",
          /*handle_key_down*/
          e[19]
        ),
        Ze(
          o,
          "keyup",
          /*keyup_handler*/
          e[30]
        ),
        Ze(
          o,
          "blur",
          /*handle_blur*/
          e[18]
        ),
        Ze(
          o,
          "focus",
          /*handle_focus*/
          e[17]
        )
      ], d = !0);
    },
    p(b, g) {
      const E = {};
      g[0] & /*show_label*/
      16 && (E.show_label = /*show_label*/
      b[4]), g[0] & /*info*/
      2 && (E.info = /*info*/
      b[1]), g[0] & /*label*/
      1 | g[1] & /*$$scope*/
      4 && (E.$$scope = { dirty: g, ctx: b }), n.$set(E), (!c || g[0] & /*show_options*/
      4096) && Z(
        o,
        "aria-expanded",
        /*show_options*/
        b[12]
      ), (!c || g[0] & /*label*/
      1) && Z(
        o,
        "aria-label",
        /*label*/
        b[0]
      ), (!c || g[0] & /*disabled*/
      8) && (o.disabled = /*disabled*/
      b[3]), (!c || g[0] & /*filterable*/
      128 && s !== (s = !/*filterable*/
      b[7])) && (o.readOnly = s), g[0] & /*input_text*/
      512 && o.value !== /*input_text*/
      b[9] && ii(
        o,
        /*input_text*/
        b[9]
      ), (!c || g[0] & /*choices_names, input_text, allow_custom_value*/
      8768) && Pe(o, "subdued", !/*choices_names*/
      b[13].includes(
        /*input_text*/
        b[9]
      ) && !/*allow_custom_value*/
      b[6]), /*disabled*/
      b[3] ? y && (Yo(), Qe(y, 1, 1, () => {
        y = null;
      }), Jo()) : y ? g[0] & /*disabled*/
      8 && Ce(y, 1) : (y = ri(), y.c(), Ce(y, 1), y.m(a, null)), (!c || g[0] & /*show_options*/
      4096) && Pe(
        l,
        "show_options",
        /*show_options*/
        b[12]
      );
      const h = {};
      g[0] & /*show_options*/
      4096 && (h.show_options = /*show_options*/
      b[12]), g[0] & /*choices*/
      4 && (h.choices = /*choices*/
      b[2]), g[0] & /*filtered_indices*/
      1024 && (h.filtered_indices = /*filtered_indices*/
      b[10]), g[0] & /*disabled*/
      8 && (h.disabled = /*disabled*/
      b[3]), g[0] & /*selected_index*/
      2048 && (h.selected_indices = /*selected_index*/
      b[11] === null ? [] : [
        /*selected_index*/
        b[11]
      ]), g[0] & /*active_index*/
      16384 && (h.active_index = /*active_index*/
      b[14]), _.$set(h), (!c || g[0] & /*container*/
      32) && Pe(
        t,
        "container",
        /*container*/
        b[5]
      );
    },
    i(b) {
      c || (Ce(n.$$.fragment, b), Ce(y), Ce(_.$$.fragment, b), c = !0);
    },
    o(b) {
      Qe(n.$$.fragment, b), Qe(y), Qe(_.$$.fragment, b), c = !1;
    },
    d(b) {
      b && bn(t), sn(n), e[29](null), y && y.d(), sn(_), d = !1, $o(v);
    }
  };
}
function oa(e, t, n) {
  let { label: i } = t, { info: r = void 0 } = t, { value: l = [] } = t, a = [], { value_is_output: o = !1 } = t, { choices: s } = t, u, { disabled: f = !1 } = t, { show_label: _ } = t, { container: c = !0 } = t, { allow_custom_value: d = !1 } = t, { filterable: v = !0 } = t, y, b = !1, g, E, h = "", m = "", S = !1, p = [], k = null, T = null, B;
  const F = ia();
  l ? (B = s.map((P) => P[1]).indexOf(l), T = B, T === -1 ? (a = l, T = null) : ([h, a] = s[T], m = h), D()) : s.length > 0 && (B = 0, T = 0, [h, l] = s[T], a = l, m = h);
  function N() {
    n(13, g = s.map((P) => P[0])), n(24, E = s.map((P) => P[1]));
  }
  function D() {
    N(), l === void 0 ? (n(9, h = ""), n(11, T = null)) : E.includes(l) ? (n(9, h = g[E.indexOf(l)]), n(11, T = E.indexOf(l))) : d ? (n(9, h = l), n(11, T = null)) : (n(9, h = ""), n(11, T = null)), n(27, B = T);
  }
  function x(P) {
    if (n(11, T = parseInt(P.detail.target.dataset.index)), isNaN(T)) {
      n(11, T = null);
      return;
    }
    n(12, b = !1), n(14, k = null), y.blur();
  }
  function V(P) {
    n(10, p = s.map((Se, A) => A)), n(12, b = !0), F("focus");
  }
  function z() {
    d ? n(20, l = h) : n(9, h = g[E.indexOf(l)]), n(12, b = !1), n(14, k = null), F("blur");
  }
  function oe(P) {
    n(12, [b, k] = sr(P, k, p), b, (n(14, k), n(2, s), n(23, u), n(6, d), n(9, h), n(10, p), n(8, y), n(25, m), n(11, T), n(27, B), n(26, S), n(24, E))), P.key === "Enter" && (k !== null ? (n(11, T = k), n(12, b = !1), y.blur(), n(14, k = null)) : g.includes(h) ? (n(11, T = g.indexOf(h)), n(12, b = !1), n(14, k = null), y.blur()) : d && (n(20, l = h), n(11, T = null), n(12, b = !1), n(14, k = null), y.blur()));
  }
  ra(() => {
    n(21, o = !1), n(26, S = !0);
  });
  function he() {
    h = this.value, n(9, h), n(11, T), n(27, B), n(26, S), n(2, s), n(24, E);
  }
  function _e(P) {
    Qo[P ? "unshift" : "push"](() => {
      y = P, n(8, y);
    });
  }
  const me = (P) => F("key_up", { key: P.key, input_value: h });
  return e.$$set = (P) => {
    "label" in P && n(0, i = P.label), "info" in P && n(1, r = P.info), "value" in P && n(20, l = P.value), "value_is_output" in P && n(21, o = P.value_is_output), "choices" in P && n(2, s = P.choices), "disabled" in P && n(3, f = P.disabled), "show_label" in P && n(4, _ = P.show_label), "container" in P && n(5, c = P.container), "allow_custom_value" in P && n(6, d = P.allow_custom_value), "filterable" in P && n(7, v = P.filterable);
  }, e.$$.update = () => {
    e.$$.dirty[0] & /*selected_index, old_selected_index, initialized, choices, choices_values*/
    218105860 && T !== B && T !== null && S && (n(9, [h, l] = s[T], h, (n(20, l), n(11, T), n(27, B), n(26, S), n(2, s), n(24, E))), n(27, B = T), F("select", {
      index: T,
      value: E[T],
      selected: !0
    })), e.$$.dirty[0] & /*value, old_value, value_is_output*/
    7340032 && l != a && (D(), lr(F, l, o), n(22, a = l)), e.$$.dirty[0] & /*choices*/
    4 && N(), e.$$.dirty[0] & /*choices, old_choices, allow_custom_value, input_text, filtered_indices, filter_input*/
    8390468 && s !== u && (d || D(), n(23, u = s), n(10, p = rn(s, h)), !d && p.length > 0 && n(14, k = p[0]), y == document.activeElement && n(12, b = !0)), e.$$.dirty[0] & /*input_text, old_input_text, choices, allow_custom_value, filtered_indices*/
    33556036 && h !== m && (n(10, p = rn(s, h)), n(25, m = h), !d && p.length > 0 && n(14, k = p[0]));
  }, [
    i,
    r,
    s,
    f,
    _,
    c,
    d,
    v,
    y,
    h,
    p,
    T,
    b,
    g,
    k,
    F,
    x,
    V,
    z,
    oe,
    l,
    o,
    a,
    u,
    E,
    m,
    S,
    B,
    he,
    _e,
    me
  ];
}
class aa extends Wo {
  constructor(t) {
    super(), Ko(
      this,
      t,
      oa,
      sa,
      ea,
      {
        label: 0,
        info: 1,
        value: 20,
        value_is_output: 21,
        choices: 2,
        disabled: 3,
        show_label: 4,
        container: 5,
        allow_custom_value: 6,
        filterable: 7
      },
      null,
      [-1, -1]
    );
  }
}
function Ie(e) {
  let t = ["", "k", "M", "G", "T", "P", "E", "Z"], n = 0;
  for (; e > 1e3 && n < t.length - 1; )
    e /= 1e3, n++;
  let i = t[n];
  return (Number.isInteger(e) ? e : e.toFixed(1)) + i;
}
const {
  SvelteComponent: ua,
  append: ee,
  attr: M,
  component_subscribe: li,
  detach: fa,
  element: ca,
  init: ha,
  insert: _a,
  noop: si,
  safe_not_equal: ma,
  set_style: ut,
  svg_element: te,
  toggle_class: oi
} = window.__gradio__svelte__internal, { onMount: da } = window.__gradio__svelte__internal;
function ba(e) {
  let t, n, i, r, l, a, o, s, u, f, _, c;
  return {
    c() {
      t = ca("div"), n = te("svg"), i = te("g"), r = te("path"), l = te("path"), a = te("path"), o = te("path"), s = te("g"), u = te("path"), f = te("path"), _ = te("path"), c = te("path"), M(r, "d", "M255.926 0.754768L509.702 139.936V221.027L255.926 81.8465V0.754768Z"), M(r, "fill", "#FF7C00"), M(r, "fill-opacity", "0.4"), M(r, "class", "svelte-43sxxs"), M(l, "d", "M509.69 139.936L254.981 279.641V361.255L509.69 221.55V139.936Z"), M(l, "fill", "#FF7C00"), M(l, "class", "svelte-43sxxs"), M(a, "d", "M0.250138 139.937L254.981 279.641V361.255L0.250138 221.55V139.937Z"), M(a, "fill", "#FF7C00"), M(a, "fill-opacity", "0.4"), M(a, "class", "svelte-43sxxs"), M(o, "d", "M255.923 0.232622L0.236328 139.936V221.55L255.923 81.8469V0.232622Z"), M(o, "fill", "#FF7C00"), M(o, "class", "svelte-43sxxs"), ut(i, "transform", "translate(" + /*$top*/
      e[1][0] + "px, " + /*$top*/
      e[1][1] + "px)"), M(u, "d", "M255.926 141.5L509.702 280.681V361.773L255.926 222.592V141.5Z"), M(u, "fill", "#FF7C00"), M(u, "fill-opacity", "0.4"), M(u, "class", "svelte-43sxxs"), M(f, "d", "M509.69 280.679L254.981 420.384V501.998L509.69 362.293V280.679Z"), M(f, "fill", "#FF7C00"), M(f, "class", "svelte-43sxxs"), M(_, "d", "M0.250138 280.681L254.981 420.386V502L0.250138 362.295V280.681Z"), M(_, "fill", "#FF7C00"), M(_, "fill-opacity", "0.4"), M(_, "class", "svelte-43sxxs"), M(c, "d", "M255.923 140.977L0.236328 280.68V362.294L255.923 222.591V140.977Z"), M(c, "fill", "#FF7C00"), M(c, "class", "svelte-43sxxs"), ut(s, "transform", "translate(" + /*$bottom*/
      e[2][0] + "px, " + /*$bottom*/
      e[2][1] + "px)"), M(n, "viewBox", "-1200 -1200 3000 3000"), M(n, "fill", "none"), M(n, "xmlns", "http://www.w3.org/2000/svg"), M(n, "class", "svelte-43sxxs"), M(t, "class", "svelte-43sxxs"), oi(
        t,
        "margin",
        /*margin*/
        e[0]
      );
    },
    m(d, v) {
      _a(d, t, v), ee(t, n), ee(n, i), ee(i, r), ee(i, l), ee(i, a), ee(i, o), ee(n, s), ee(s, u), ee(s, f), ee(s, _), ee(s, c);
    },
    p(d, [v]) {
      v & /*$top*/
      2 && ut(i, "transform", "translate(" + /*$top*/
      d[1][0] + "px, " + /*$top*/
      d[1][1] + "px)"), v & /*$bottom*/
      4 && ut(s, "transform", "translate(" + /*$bottom*/
      d[2][0] + "px, " + /*$bottom*/
      d[2][1] + "px)"), v & /*margin*/
      1 && oi(
        t,
        "margin",
        /*margin*/
        d[0]
      );
    },
    i: si,
    o: si,
    d(d) {
      d && fa(t);
    }
  };
}
function ga(e, t, n) {
  let i, r, { margin: l = !0 } = t;
  const a = En([0, 0]);
  li(e, a, (c) => n(1, i = c));
  const o = En([0, 0]);
  li(e, o, (c) => n(2, r = c));
  let s;
  async function u() {
    await Promise.all([a.set([125, 140]), o.set([-125, -140])]), await Promise.all([a.set([-125, 140]), o.set([125, -140])]), await Promise.all([a.set([-125, 0]), o.set([125, -0])]), await Promise.all([a.set([125, 0]), o.set([-125, 0])]);
  }
  async function f() {
    await u(), s || f();
  }
  async function _() {
    await Promise.all([a.set([125, 0]), o.set([-125, 0])]), f();
  }
  return da(() => (_(), () => s = !0)), e.$$set = (c) => {
    "margin" in c && n(0, l = c.margin);
  }, [l, i, r, a, o];
}
class pa extends ua {
  constructor(t) {
    super(), ha(this, t, ga, ba, ma, { margin: 0 });
  }
}
const {
  SvelteComponent: va,
  append: ye,
  attr: le,
  binding_callbacks: ai,
  check_outros: or,
  create_component: ya,
  create_slot: wa,
  destroy_component: Ea,
  destroy_each: ar,
  detach: C,
  element: ue,
  empty: Xe,
  ensure_array_like: wt,
  get_all_dirty_from_scope: Sa,
  get_slot_changes: Ta,
  group_outros: ur,
  init: Aa,
  insert: O,
  mount_component: Ha,
  noop: an,
  safe_not_equal: Ba,
  set_data: $,
  set_style: pe,
  space: se,
  text: G,
  toggle_class: K,
  transition_in: xe,
  transition_out: je,
  update_slot_base: Pa
} = window.__gradio__svelte__internal, { tick: Na } = window.__gradio__svelte__internal, { onDestroy: ka } = window.__gradio__svelte__internal, Ca = (e) => ({}), ui = (e) => ({});
function fi(e, t, n) {
  const i = e.slice();
  return i[38] = t[n], i[40] = n, i;
}
function ci(e, t, n) {
  const i = e.slice();
  return i[38] = t[n], i;
}
function Oa(e) {
  let t, n = (
    /*i18n*/
    e[1]("common.error") + ""
  ), i, r, l;
  const a = (
    /*#slots*/
    e[29].error
  ), o = wa(
    a,
    e,
    /*$$scope*/
    e[28],
    ui
  );
  return {
    c() {
      t = ue("span"), i = G(n), r = se(), o && o.c(), le(t, "class", "error svelte-1yserjw");
    },
    m(s, u) {
      O(s, t, u), ye(t, i), O(s, r, u), o && o.m(s, u), l = !0;
    },
    p(s, u) {
      (!l || u[0] & /*i18n*/
      2) && n !== (n = /*i18n*/
      s[1]("common.error") + "") && $(i, n), o && o.p && (!l || u[0] & /*$$scope*/
      268435456) && Pa(
        o,
        a,
        s,
        /*$$scope*/
        s[28],
        l ? Ta(
          a,
          /*$$scope*/
          s[28],
          u,
          Ca
        ) : Sa(
          /*$$scope*/
          s[28]
        ),
        ui
      );
    },
    i(s) {
      l || (xe(o, s), l = !0);
    },
    o(s) {
      je(o, s), l = !1;
    },
    d(s) {
      s && (C(t), C(r)), o && o.d(s);
    }
  };
}
function Ia(e) {
  let t, n, i, r, l, a, o, s, u, f = (
    /*variant*/
    e[8] === "default" && /*show_eta_bar*/
    e[18] && /*show_progress*/
    e[6] === "full" && hi(e)
  );
  function _(h, m) {
    if (
      /*progress*/
      h[7]
    )
      return Ra;
    if (
      /*queue_position*/
      h[2] !== null && /*queue_size*/
      h[3] !== void 0 && /*queue_position*/
      h[2] >= 0
    )
      return Ma;
    if (
      /*queue_position*/
      h[2] === 0
    )
      return La;
  }
  let c = _(e), d = c && c(e), v = (
    /*timer*/
    e[5] && di(e)
  );
  const y = [Fa, Ga], b = [];
  function g(h, m) {
    return (
      /*last_progress_level*/
      h[15] != null ? 0 : (
        /*show_progress*/
        h[6] === "full" ? 1 : -1
      )
    );
  }
  ~(l = g(e)) && (a = b[l] = y[l](e));
  let E = !/*timer*/
  e[5] && Ei(e);
  return {
    c() {
      f && f.c(), t = se(), n = ue("div"), d && d.c(), i = se(), v && v.c(), r = se(), a && a.c(), o = se(), E && E.c(), s = Xe(), le(n, "class", "progress-text svelte-1yserjw"), K(
        n,
        "meta-text-center",
        /*variant*/
        e[8] === "center"
      ), K(
        n,
        "meta-text",
        /*variant*/
        e[8] === "default"
      );
    },
    m(h, m) {
      f && f.m(h, m), O(h, t, m), O(h, n, m), d && d.m(n, null), ye(n, i), v && v.m(n, null), O(h, r, m), ~l && b[l].m(h, m), O(h, o, m), E && E.m(h, m), O(h, s, m), u = !0;
    },
    p(h, m) {
      /*variant*/
      h[8] === "default" && /*show_eta_bar*/
      h[18] && /*show_progress*/
      h[6] === "full" ? f ? f.p(h, m) : (f = hi(h), f.c(), f.m(t.parentNode, t)) : f && (f.d(1), f = null), c === (c = _(h)) && d ? d.p(h, m) : (d && d.d(1), d = c && c(h), d && (d.c(), d.m(n, i))), /*timer*/
      h[5] ? v ? v.p(h, m) : (v = di(h), v.c(), v.m(n, null)) : v && (v.d(1), v = null), (!u || m[0] & /*variant*/
      256) && K(
        n,
        "meta-text-center",
        /*variant*/
        h[8] === "center"
      ), (!u || m[0] & /*variant*/
      256) && K(
        n,
        "meta-text",
        /*variant*/
        h[8] === "default"
      );
      let S = l;
      l = g(h), l === S ? ~l && b[l].p(h, m) : (a && (ur(), je(b[S], 1, 1, () => {
        b[S] = null;
      }), or()), ~l ? (a = b[l], a ? a.p(h, m) : (a = b[l] = y[l](h), a.c()), xe(a, 1), a.m(o.parentNode, o)) : a = null), /*timer*/
      h[5] ? E && (E.d(1), E = null) : E ? E.p(h, m) : (E = Ei(h), E.c(), E.m(s.parentNode, s));
    },
    i(h) {
      u || (xe(a), u = !0);
    },
    o(h) {
      je(a), u = !1;
    },
    d(h) {
      h && (C(t), C(n), C(r), C(o), C(s)), f && f.d(h), d && d.d(), v && v.d(), ~l && b[l].d(h), E && E.d(h);
    }
  };
}
function hi(e) {
  let t, n = `translateX(${/*eta_level*/
  (e[17] || 0) * 100 - 100}%)`;
  return {
    c() {
      t = ue("div"), le(t, "class", "eta-bar svelte-1yserjw"), pe(t, "transform", n);
    },
    m(i, r) {
      O(i, t, r);
    },
    p(i, r) {
      r[0] & /*eta_level*/
      131072 && n !== (n = `translateX(${/*eta_level*/
      (i[17] || 0) * 100 - 100}%)`) && pe(t, "transform", n);
    },
    d(i) {
      i && C(t);
    }
  };
}
function La(e) {
  let t;
  return {
    c() {
      t = G("processing |");
    },
    m(n, i) {
      O(n, t, i);
    },
    p: an,
    d(n) {
      n && C(t);
    }
  };
}
function Ma(e) {
  let t, n = (
    /*queue_position*/
    e[2] + 1 + ""
  ), i, r, l, a;
  return {
    c() {
      t = G("queue: "), i = G(n), r = G("/"), l = G(
        /*queue_size*/
        e[3]
      ), a = G(" |");
    },
    m(o, s) {
      O(o, t, s), O(o, i, s), O(o, r, s), O(o, l, s), O(o, a, s);
    },
    p(o, s) {
      s[0] & /*queue_position*/
      4 && n !== (n = /*queue_position*/
      o[2] + 1 + "") && $(i, n), s[0] & /*queue_size*/
      8 && $(
        l,
        /*queue_size*/
        o[3]
      );
    },
    d(o) {
      o && (C(t), C(i), C(r), C(l), C(a));
    }
  };
}
function Ra(e) {
  let t, n = wt(
    /*progress*/
    e[7]
  ), i = [];
  for (let r = 0; r < n.length; r += 1)
    i[r] = mi(ci(e, n, r));
  return {
    c() {
      for (let r = 0; r < i.length; r += 1)
        i[r].c();
      t = Xe();
    },
    m(r, l) {
      for (let a = 0; a < i.length; a += 1)
        i[a] && i[a].m(r, l);
      O(r, t, l);
    },
    p(r, l) {
      if (l[0] & /*progress*/
      128) {
        n = wt(
          /*progress*/
          r[7]
        );
        let a;
        for (a = 0; a < n.length; a += 1) {
          const o = ci(r, n, a);
          i[a] ? i[a].p(o, l) : (i[a] = mi(o), i[a].c(), i[a].m(t.parentNode, t));
        }
        for (; a < i.length; a += 1)
          i[a].d(1);
        i.length = n.length;
      }
    },
    d(r) {
      r && C(t), ar(i, r);
    }
  };
}
function _i(e) {
  let t, n = (
    /*p*/
    e[38].unit + ""
  ), i, r, l = " ", a;
  function o(f, _) {
    return (
      /*p*/
      f[38].length != null ? Ua : Da
    );
  }
  let s = o(e), u = s(e);
  return {
    c() {
      u.c(), t = se(), i = G(n), r = G(" | "), a = G(l);
    },
    m(f, _) {
      u.m(f, _), O(f, t, _), O(f, i, _), O(f, r, _), O(f, a, _);
    },
    p(f, _) {
      s === (s = o(f)) && u ? u.p(f, _) : (u.d(1), u = s(f), u && (u.c(), u.m(t.parentNode, t))), _[0] & /*progress*/
      128 && n !== (n = /*p*/
      f[38].unit + "") && $(i, n);
    },
    d(f) {
      f && (C(t), C(i), C(r), C(a)), u.d(f);
    }
  };
}
function Da(e) {
  let t = Ie(
    /*p*/
    e[38].index || 0
  ) + "", n;
  return {
    c() {
      n = G(t);
    },
    m(i, r) {
      O(i, n, r);
    },
    p(i, r) {
      r[0] & /*progress*/
      128 && t !== (t = Ie(
        /*p*/
        i[38].index || 0
      ) + "") && $(n, t);
    },
    d(i) {
      i && C(n);
    }
  };
}
function Ua(e) {
  let t = Ie(
    /*p*/
    e[38].index || 0
  ) + "", n, i, r = Ie(
    /*p*/
    e[38].length
  ) + "", l;
  return {
    c() {
      n = G(t), i = G("/"), l = G(r);
    },
    m(a, o) {
      O(a, n, o), O(a, i, o), O(a, l, o);
    },
    p(a, o) {
      o[0] & /*progress*/
      128 && t !== (t = Ie(
        /*p*/
        a[38].index || 0
      ) + "") && $(n, t), o[0] & /*progress*/
      128 && r !== (r = Ie(
        /*p*/
        a[38].length
      ) + "") && $(l, r);
    },
    d(a) {
      a && (C(n), C(i), C(l));
    }
  };
}
function mi(e) {
  let t, n = (
    /*p*/
    e[38].index != null && _i(e)
  );
  return {
    c() {
      n && n.c(), t = Xe();
    },
    m(i, r) {
      n && n.m(i, r), O(i, t, r);
    },
    p(i, r) {
      /*p*/
      i[38].index != null ? n ? n.p(i, r) : (n = _i(i), n.c(), n.m(t.parentNode, t)) : n && (n.d(1), n = null);
    },
    d(i) {
      i && C(t), n && n.d(i);
    }
  };
}
function di(e) {
  let t, n = (
    /*eta*/
    e[0] ? `/${/*formatted_eta*/
    e[19]}` : ""
  ), i, r;
  return {
    c() {
      t = G(
        /*formatted_timer*/
        e[20]
      ), i = G(n), r = G("s");
    },
    m(l, a) {
      O(l, t, a), O(l, i, a), O(l, r, a);
    },
    p(l, a) {
      a[0] & /*formatted_timer*/
      1048576 && $(
        t,
        /*formatted_timer*/
        l[20]
      ), a[0] & /*eta, formatted_eta*/
      524289 && n !== (n = /*eta*/
      l[0] ? `/${/*formatted_eta*/
      l[19]}` : "") && $(i, n);
    },
    d(l) {
      l && (C(t), C(i), C(r));
    }
  };
}
function Ga(e) {
  let t, n;
  return t = new pa({
    props: { margin: (
      /*variant*/
      e[8] === "default"
    ) }
  }), {
    c() {
      ya(t.$$.fragment);
    },
    m(i, r) {
      Ha(t, i, r), n = !0;
    },
    p(i, r) {
      const l = {};
      r[0] & /*variant*/
      256 && (l.margin = /*variant*/
      i[8] === "default"), t.$set(l);
    },
    i(i) {
      n || (xe(t.$$.fragment, i), n = !0);
    },
    o(i) {
      je(t.$$.fragment, i), n = !1;
    },
    d(i) {
      Ea(t, i);
    }
  };
}
function Fa(e) {
  let t, n, i, r, l, a = `${/*last_progress_level*/
  e[15] * 100}%`, o = (
    /*progress*/
    e[7] != null && bi(e)
  );
  return {
    c() {
      t = ue("div"), n = ue("div"), o && o.c(), i = se(), r = ue("div"), l = ue("div"), le(n, "class", "progress-level-inner svelte-1yserjw"), le(l, "class", "progress-bar svelte-1yserjw"), pe(l, "width", a), le(r, "class", "progress-bar-wrap svelte-1yserjw"), le(t, "class", "progress-level svelte-1yserjw");
    },
    m(s, u) {
      O(s, t, u), ye(t, n), o && o.m(n, null), ye(t, i), ye(t, r), ye(r, l), e[30](l);
    },
    p(s, u) {
      /*progress*/
      s[7] != null ? o ? o.p(s, u) : (o = bi(s), o.c(), o.m(n, null)) : o && (o.d(1), o = null), u[0] & /*last_progress_level*/
      32768 && a !== (a = `${/*last_progress_level*/
      s[15] * 100}%`) && pe(l, "width", a);
    },
    i: an,
    o: an,
    d(s) {
      s && C(t), o && o.d(), e[30](null);
    }
  };
}
function bi(e) {
  let t, n = wt(
    /*progress*/
    e[7]
  ), i = [];
  for (let r = 0; r < n.length; r += 1)
    i[r] = wi(fi(e, n, r));
  return {
    c() {
      for (let r = 0; r < i.length; r += 1)
        i[r].c();
      t = Xe();
    },
    m(r, l) {
      for (let a = 0; a < i.length; a += 1)
        i[a] && i[a].m(r, l);
      O(r, t, l);
    },
    p(r, l) {
      if (l[0] & /*progress_level, progress*/
      16512) {
        n = wt(
          /*progress*/
          r[7]
        );
        let a;
        for (a = 0; a < n.length; a += 1) {
          const o = fi(r, n, a);
          i[a] ? i[a].p(o, l) : (i[a] = wi(o), i[a].c(), i[a].m(t.parentNode, t));
        }
        for (; a < i.length; a += 1)
          i[a].d(1);
        i.length = n.length;
      }
    },
    d(r) {
      r && C(t), ar(i, r);
    }
  };
}
function gi(e) {
  let t, n, i, r, l = (
    /*i*/
    e[40] !== 0 && xa()
  ), a = (
    /*p*/
    e[38].desc != null && pi(e)
  ), o = (
    /*p*/
    e[38].desc != null && /*progress_level*/
    e[14] && /*progress_level*/
    e[14][
      /*i*/
      e[40]
    ] != null && vi()
  ), s = (
    /*progress_level*/
    e[14] != null && yi(e)
  );
  return {
    c() {
      l && l.c(), t = se(), a && a.c(), n = se(), o && o.c(), i = se(), s && s.c(), r = Xe();
    },
    m(u, f) {
      l && l.m(u, f), O(u, t, f), a && a.m(u, f), O(u, n, f), o && o.m(u, f), O(u, i, f), s && s.m(u, f), O(u, r, f);
    },
    p(u, f) {
      /*p*/
      u[38].desc != null ? a ? a.p(u, f) : (a = pi(u), a.c(), a.m(n.parentNode, n)) : a && (a.d(1), a = null), /*p*/
      u[38].desc != null && /*progress_level*/
      u[14] && /*progress_level*/
      u[14][
        /*i*/
        u[40]
      ] != null ? o || (o = vi(), o.c(), o.m(i.parentNode, i)) : o && (o.d(1), o = null), /*progress_level*/
      u[14] != null ? s ? s.p(u, f) : (s = yi(u), s.c(), s.m(r.parentNode, r)) : s && (s.d(1), s = null);
    },
    d(u) {
      u && (C(t), C(n), C(i), C(r)), l && l.d(u), a && a.d(u), o && o.d(u), s && s.d(u);
    }
  };
}
function xa(e) {
  let t;
  return {
    c() {
      t = G(" /");
    },
    m(n, i) {
      O(n, t, i);
    },
    d(n) {
      n && C(t);
    }
  };
}
function pi(e) {
  let t = (
    /*p*/
    e[38].desc + ""
  ), n;
  return {
    c() {
      n = G(t);
    },
    m(i, r) {
      O(i, n, r);
    },
    p(i, r) {
      r[0] & /*progress*/
      128 && t !== (t = /*p*/
      i[38].desc + "") && $(n, t);
    },
    d(i) {
      i && C(n);
    }
  };
}
function vi(e) {
  let t;
  return {
    c() {
      t = G("-");
    },
    m(n, i) {
      O(n, t, i);
    },
    d(n) {
      n && C(t);
    }
  };
}
function yi(e) {
  let t = (100 * /*progress_level*/
  (e[14][
    /*i*/
    e[40]
  ] || 0)).toFixed(1) + "", n, i;
  return {
    c() {
      n = G(t), i = G("%");
    },
    m(r, l) {
      O(r, n, l), O(r, i, l);
    },
    p(r, l) {
      l[0] & /*progress_level*/
      16384 && t !== (t = (100 * /*progress_level*/
      (r[14][
        /*i*/
        r[40]
      ] || 0)).toFixed(1) + "") && $(n, t);
    },
    d(r) {
      r && (C(n), C(i));
    }
  };
}
function wi(e) {
  let t, n = (
    /*p*/
    (e[38].desc != null || /*progress_level*/
    e[14] && /*progress_level*/
    e[14][
      /*i*/
      e[40]
    ] != null) && gi(e)
  );
  return {
    c() {
      n && n.c(), t = Xe();
    },
    m(i, r) {
      n && n.m(i, r), O(i, t, r);
    },
    p(i, r) {
      /*p*/
      i[38].desc != null || /*progress_level*/
      i[14] && /*progress_level*/
      i[14][
        /*i*/
        i[40]
      ] != null ? n ? n.p(i, r) : (n = gi(i), n.c(), n.m(t.parentNode, t)) : n && (n.d(1), n = null);
    },
    d(i) {
      i && C(t), n && n.d(i);
    }
  };
}
function Ei(e) {
  let t, n;
  return {
    c() {
      t = ue("p"), n = G(
        /*loading_text*/
        e[9]
      ), le(t, "class", "loading svelte-1yserjw");
    },
    m(i, r) {
      O(i, t, r), ye(t, n);
    },
    p(i, r) {
      r[0] & /*loading_text*/
      512 && $(
        n,
        /*loading_text*/
        i[9]
      );
    },
    d(i) {
      i && C(t);
    }
  };
}
function ja(e) {
  let t, n, i, r, l;
  const a = [Ia, Oa], o = [];
  function s(u, f) {
    return (
      /*status*/
      u[4] === "pending" ? 0 : (
        /*status*/
        u[4] === "error" ? 1 : -1
      )
    );
  }
  return ~(n = s(e)) && (i = o[n] = a[n](e)), {
    c() {
      t = ue("div"), i && i.c(), le(t, "class", r = "wrap " + /*variant*/
      e[8] + " " + /*show_progress*/
      e[6] + " svelte-1yserjw"), K(t, "hide", !/*status*/
      e[4] || /*status*/
      e[4] === "complete" || /*show_progress*/
      e[6] === "hidden"), K(
        t,
        "translucent",
        /*variant*/
        e[8] === "center" && /*status*/
        (e[4] === "pending" || /*status*/
        e[4] === "error") || /*translucent*/
        e[11] || /*show_progress*/
        e[6] === "minimal"
      ), K(
        t,
        "generating",
        /*status*/
        e[4] === "generating"
      ), K(
        t,
        "border",
        /*border*/
        e[12]
      ), pe(
        t,
        "position",
        /*absolute*/
        e[10] ? "absolute" : "static"
      ), pe(
        t,
        "padding",
        /*absolute*/
        e[10] ? "0" : "var(--size-8) 0"
      );
    },
    m(u, f) {
      O(u, t, f), ~n && o[n].m(t, null), e[31](t), l = !0;
    },
    p(u, f) {
      let _ = n;
      n = s(u), n === _ ? ~n && o[n].p(u, f) : (i && (ur(), je(o[_], 1, 1, () => {
        o[_] = null;
      }), or()), ~n ? (i = o[n], i ? i.p(u, f) : (i = o[n] = a[n](u), i.c()), xe(i, 1), i.m(t, null)) : i = null), (!l || f[0] & /*variant, show_progress*/
      320 && r !== (r = "wrap " + /*variant*/
      u[8] + " " + /*show_progress*/
      u[6] + " svelte-1yserjw")) && le(t, "class", r), (!l || f[0] & /*variant, show_progress, status, show_progress*/
      336) && K(t, "hide", !/*status*/
      u[4] || /*status*/
      u[4] === "complete" || /*show_progress*/
      u[6] === "hidden"), (!l || f[0] & /*variant, show_progress, variant, status, translucent, show_progress*/
      2384) && K(
        t,
        "translucent",
        /*variant*/
        u[8] === "center" && /*status*/
        (u[4] === "pending" || /*status*/
        u[4] === "error") || /*translucent*/
        u[11] || /*show_progress*/
        u[6] === "minimal"
      ), (!l || f[0] & /*variant, show_progress, status*/
      336) && K(
        t,
        "generating",
        /*status*/
        u[4] === "generating"
      ), (!l || f[0] & /*variant, show_progress, border*/
      4416) && K(
        t,
        "border",
        /*border*/
        u[12]
      ), f[0] & /*absolute*/
      1024 && pe(
        t,
        "position",
        /*absolute*/
        u[10] ? "absolute" : "static"
      ), f[0] & /*absolute*/
      1024 && pe(
        t,
        "padding",
        /*absolute*/
        u[10] ? "0" : "var(--size-8) 0"
      );
    },
    i(u) {
      l || (xe(i), l = !0);
    },
    o(u) {
      je(i), l = !1;
    },
    d(u) {
      u && C(t), ~n && o[n].d(), e[31](null);
    }
  };
}
let ft = [], qt = !1;
async function Va(e, t = !0) {
  if (!(window.__gradio_mode__ === "website" || window.__gradio_mode__ !== "app" && t !== !0)) {
    if (ft.push(e), !qt)
      qt = !0;
    else
      return;
    await Na(), requestAnimationFrame(() => {
      let n = [0, 0];
      for (let i = 0; i < ft.length; i++) {
        const l = ft[i].getBoundingClientRect();
        (i === 0 || l.top + window.scrollY <= n[0]) && (n[0] = l.top + window.scrollY, n[1] = i);
      }
      window.scrollTo({ top: n[0] - 20, behavior: "smooth" }), qt = !1, ft = [];
    });
  }
}
function qa(e, t, n) {
  let i, { $$slots: r = {}, $$scope: l } = t, { i18n: a } = t, { eta: o = null } = t, { queue_position: s } = t, { queue_size: u } = t, { status: f } = t, { scroll_to_output: _ = !1 } = t, { timer: c = !0 } = t, { show_progress: d = "full" } = t, { message: v = null } = t, { progress: y = null } = t, { variant: b = "default" } = t, { loading_text: g = "Loading..." } = t, { absolute: E = !0 } = t, { translucent: h = !1 } = t, { border: m = !1 } = t, { autoscroll: S } = t, p, k = !1, T = 0, B = 0, F = null, N = null, D = 0, x = null, V, z = null, oe = !0;
  const he = () => {
    n(0, o = n(26, F = n(19, P = null))), n(24, T = performance.now()), n(25, B = 0), k = !0, _e();
  };
  function _e() {
    requestAnimationFrame(() => {
      n(25, B = (performance.now() - T) / 1e3), k && _e();
    });
  }
  function me() {
    n(25, B = 0), n(0, o = n(26, F = n(19, P = null))), k && (k = !1);
  }
  ka(() => {
    k && me();
  });
  let P = null;
  function Se(H) {
    ai[H ? "unshift" : "push"](() => {
      z = H, n(16, z), n(7, y), n(14, x), n(15, V);
    });
  }
  function A(H) {
    ai[H ? "unshift" : "push"](() => {
      p = H, n(13, p);
    });
  }
  return e.$$set = (H) => {
    "i18n" in H && n(1, a = H.i18n), "eta" in H && n(0, o = H.eta), "queue_position" in H && n(2, s = H.queue_position), "queue_size" in H && n(3, u = H.queue_size), "status" in H && n(4, f = H.status), "scroll_to_output" in H && n(21, _ = H.scroll_to_output), "timer" in H && n(5, c = H.timer), "show_progress" in H && n(6, d = H.show_progress), "message" in H && n(22, v = H.message), "progress" in H && n(7, y = H.progress), "variant" in H && n(8, b = H.variant), "loading_text" in H && n(9, g = H.loading_text), "absolute" in H && n(10, E = H.absolute), "translucent" in H && n(11, h = H.translucent), "border" in H && n(12, m = H.border), "autoscroll" in H && n(23, S = H.autoscroll), "$$scope" in H && n(28, l = H.$$scope);
  }, e.$$.update = () => {
    e.$$.dirty[0] & /*eta, old_eta, timer_start, eta_from_start*/
    218103809 && (o === null && n(0, o = F), o != null && F !== o && (n(27, N = (performance.now() - T) / 1e3 + o), n(19, P = N.toFixed(1)), n(26, F = o))), e.$$.dirty[0] & /*eta_from_start, timer_diff*/
    167772160 && n(17, D = N === null || N <= 0 || !B ? null : Math.min(B / N, 1)), e.$$.dirty[0] & /*progress*/
    128 && y != null && n(18, oe = !1), e.$$.dirty[0] & /*progress, progress_level, progress_bar, last_progress_level*/
    114816 && (y != null ? n(14, x = y.map((H) => {
      if (H.index != null && H.length != null)
        return H.index / H.length;
      if (H.progress != null)
        return H.progress;
    })) : n(14, x = null), x ? (n(15, V = x[x.length - 1]), z && (V === 0 ? n(16, z.style.transition = "0", z) : n(16, z.style.transition = "150ms", z))) : n(15, V = void 0)), e.$$.dirty[0] & /*status*/
    16 && (f === "pending" ? he() : me()), e.$$.dirty[0] & /*el, scroll_to_output, status, autoscroll*/
    10493968 && p && _ && (f === "pending" || f === "complete") && Va(p, S), e.$$.dirty[0] & /*status, message*/
    4194320, e.$$.dirty[0] & /*timer_diff*/
    33554432 && n(20, i = B.toFixed(1));
  }, [
    o,
    a,
    s,
    u,
    f,
    c,
    d,
    y,
    b,
    g,
    E,
    h,
    m,
    p,
    x,
    V,
    z,
    D,
    oe,
    P,
    i,
    _,
    v,
    S,
    T,
    B,
    F,
    N,
    l,
    r,
    Se,
    A
  ];
}
class Xa extends va {
  constructor(t) {
    super(), Aa(
      this,
      t,
      qa,
      ja,
      Ba,
      {
        i18n: 1,
        eta: 0,
        queue_position: 2,
        queue_size: 3,
        status: 4,
        scroll_to_output: 21,
        timer: 5,
        show_progress: 6,
        message: 22,
        progress: 7,
        variant: 8,
        loading_text: 9,
        absolute: 10,
        translucent: 11,
        border: 12,
        autoscroll: 23
      },
      null,
      [-1, -1]
    );
  }
}
const {
  SvelteComponent: za,
  attr: Za,
  detach: Wa,
  element: Qa,
  init: Ja,
  insert: Ya,
  noop: Si,
  safe_not_equal: Ka,
  toggle_class: Ne
} = window.__gradio__svelte__internal;
function $a(e) {
  let t;
  return {
    c() {
      t = Qa("div"), t.textContent = `${/*names_string*/
      e[2]}`, Za(t, "class", "svelte-1gecy8w"), Ne(
        t,
        "table",
        /*type*/
        e[0] === "table"
      ), Ne(
        t,
        "gallery",
        /*type*/
        e[0] === "gallery"
      ), Ne(
        t,
        "selected",
        /*selected*/
        e[1]
      );
    },
    m(n, i) {
      Ya(n, t, i);
    },
    p(n, [i]) {
      i & /*type*/
      1 && Ne(
        t,
        "table",
        /*type*/
        n[0] === "table"
      ), i & /*type*/
      1 && Ne(
        t,
        "gallery",
        /*type*/
        n[0] === "gallery"
      ), i & /*selected*/
      2 && Ne(
        t,
        "selected",
        /*selected*/
        n[1]
      );
    },
    i: Si,
    o: Si,
    d(n) {
      n && Wa(t);
    }
  };
}
function eu(e) {
  let t, n = e[0], i = 1;
  for (; i < e.length; ) {
    const r = e[i], l = e[i + 1];
    if (i += 2, (r === "optionalAccess" || r === "optionalCall") && n == null)
      return;
    r === "access" || r === "optionalAccess" ? (t = n, n = l(n)) : (r === "call" || r === "optionalCall") && (n = l((...a) => n.call(t, ...a)), t = void 0);
  }
  return n;
}
function tu(e, t, n) {
  let { value: i } = t, { type: r } = t, { selected: l = !1 } = t, { choices: a } = t, u = (i ? Array.isArray(i) ? i : [i] : []).map((f) => eu([a.find((_) => _[1] === f), "optionalAccess", (_) => _[0]])).filter((f) => f !== void 0).join(", ");
  return e.$$set = (f) => {
    "value" in f && n(3, i = f.value), "type" in f && n(0, r = f.type), "selected" in f && n(1, l = f.selected), "choices" in f && n(4, a = f.choices);
  }, [r, l, u, i, a];
}
class gu extends za {
  constructor(t) {
    super(), Ja(this, t, tu, $a, Ka, {
      value: 3,
      type: 0,
      selected: 1,
      choices: 4
    });
  }
}
const {
  SvelteComponent: nu,
  add_flush_callback: Et,
  assign: iu,
  bind: St,
  binding_callbacks: Tt,
  check_outros: ru,
  create_component: Nt,
  destroy_component: kt,
  detach: Ti,
  empty: lu,
  get_spread_object: su,
  get_spread_update: ou,
  group_outros: au,
  init: uu,
  insert: Ai,
  mount_component: Ct,
  safe_not_equal: fu,
  space: cu,
  transition_in: Me,
  transition_out: Re
} = window.__gradio__svelte__internal;
function hu(e) {
  let t, n, i, r;
  function l(s) {
    e[27](s);
  }
  function a(s) {
    e[28](s);
  }
  let o = {
    choices: (
      /*choices*/
      e[9]
    ),
    label: (
      /*label*/
      e[2]
    ),
    info: (
      /*info*/
      e[3]
    ),
    show_label: (
      /*show_label*/
      e[10]
    ),
    filterable: (
      /*filterable*/
      e[11]
    ),
    allow_custom_value: (
      /*allow_custom_value*/
      e[16]
    ),
    container: (
      /*container*/
      e[12]
    ),
    disabled: !/*interactive*/
    e[18]
  };
  return (
    /*value*/
    e[0] !== void 0 && (o.value = /*value*/
    e[0]), /*value_is_output*/
    e[1] !== void 0 && (o.value_is_output = /*value_is_output*/
    e[1]), t = new aa({ props: o }), Tt.push(() => St(t, "value", l)), Tt.push(() => St(t, "value_is_output", a)), t.$on(
      "change",
      /*change_handler_1*/
      e[29]
    ), t.$on(
      "input",
      /*input_handler_1*/
      e[30]
    ), t.$on(
      "select",
      /*select_handler_1*/
      e[31]
    ), t.$on(
      "blur",
      /*blur_handler_1*/
      e[32]
    ), t.$on(
      "focus",
      /*focus_handler_1*/
      e[33]
    ), t.$on(
      "key_up",
      /*key_up_handler_1*/
      e[34]
    ), {
      c() {
        Nt(t.$$.fragment);
      },
      m(s, u) {
        Ct(t, s, u), r = !0;
      },
      p(s, u) {
        const f = {};
        u[0] & /*choices*/
        512 && (f.choices = /*choices*/
        s[9]), u[0] & /*label*/
        4 && (f.label = /*label*/
        s[2]), u[0] & /*info*/
        8 && (f.info = /*info*/
        s[3]), u[0] & /*show_label*/
        1024 && (f.show_label = /*show_label*/
        s[10]), u[0] & /*filterable*/
        2048 && (f.filterable = /*filterable*/
        s[11]), u[0] & /*allow_custom_value*/
        65536 && (f.allow_custom_value = /*allow_custom_value*/
        s[16]), u[0] & /*container*/
        4096 && (f.container = /*container*/
        s[12]), u[0] & /*interactive*/
        262144 && (f.disabled = !/*interactive*/
        s[18]), !n && u[0] & /*value*/
        1 && (n = !0, f.value = /*value*/
        s[0], Et(() => n = !1)), !i && u[0] & /*value_is_output*/
        2 && (i = !0, f.value_is_output = /*value_is_output*/
        s[1], Et(() => i = !1)), t.$set(f);
      },
      i(s) {
        r || (Me(t.$$.fragment, s), r = !0);
      },
      o(s) {
        Re(t.$$.fragment, s), r = !1;
      },
      d(s) {
        kt(t, s);
      }
    }
  );
}
function _u(e) {
  let t, n, i, r;
  function l(s) {
    e[19](s);
  }
  function a(s) {
    e[20](s);
  }
  let o = {
    choices: (
      /*choices*/
      e[9]
    ),
    max_choices: (
      /*max_choices*/
      e[8]
    ),
    label: (
      /*label*/
      e[2]
    ),
    info: (
      /*info*/
      e[3]
    ),
    show_label: (
      /*show_label*/
      e[10]
    ),
    allow_custom_value: (
      /*allow_custom_value*/
      e[16]
    ),
    filterable: (
      /*filterable*/
      e[11]
    ),
    container: (
      /*container*/
      e[12]
    ),
    i18n: (
      /*gradio*/
      e[17].i18n
    ),
    disabled: !/*interactive*/
    e[18]
  };
  return (
    /*value*/
    e[0] !== void 0 && (o.value = /*value*/
    e[0]), /*value_is_output*/
    e[1] !== void 0 && (o.value_is_output = /*value_is_output*/
    e[1]), t = new Zo({ props: o }), Tt.push(() => St(t, "value", l)), Tt.push(() => St(t, "value_is_output", a)), t.$on(
      "change",
      /*change_handler*/
      e[21]
    ), t.$on(
      "input",
      /*input_handler*/
      e[22]
    ), t.$on(
      "select",
      /*select_handler*/
      e[23]
    ), t.$on(
      "blur",
      /*blur_handler*/
      e[24]
    ), t.$on(
      "focus",
      /*focus_handler*/
      e[25]
    ), t.$on(
      "key_up",
      /*key_up_handler*/
      e[26]
    ), {
      c() {
        Nt(t.$$.fragment);
      },
      m(s, u) {
        Ct(t, s, u), r = !0;
      },
      p(s, u) {
        const f = {};
        u[0] & /*choices*/
        512 && (f.choices = /*choices*/
        s[9]), u[0] & /*max_choices*/
        256 && (f.max_choices = /*max_choices*/
        s[8]), u[0] & /*label*/
        4 && (f.label = /*label*/
        s[2]), u[0] & /*info*/
        8 && (f.info = /*info*/
        s[3]), u[0] & /*show_label*/
        1024 && (f.show_label = /*show_label*/
        s[10]), u[0] & /*allow_custom_value*/
        65536 && (f.allow_custom_value = /*allow_custom_value*/
        s[16]), u[0] & /*filterable*/
        2048 && (f.filterable = /*filterable*/
        s[11]), u[0] & /*container*/
        4096 && (f.container = /*container*/
        s[12]), u[0] & /*gradio*/
        131072 && (f.i18n = /*gradio*/
        s[17].i18n), u[0] & /*interactive*/
        262144 && (f.disabled = !/*interactive*/
        s[18]), !n && u[0] & /*value*/
        1 && (n = !0, f.value = /*value*/
        s[0], Et(() => n = !1)), !i && u[0] & /*value_is_output*/
        2 && (i = !0, f.value_is_output = /*value_is_output*/
        s[1], Et(() => i = !1)), t.$set(f);
      },
      i(s) {
        r || (Me(t.$$.fragment, s), r = !0);
      },
      o(s) {
        Re(t.$$.fragment, s), r = !1;
      },
      d(s) {
        kt(t, s);
      }
    }
  );
}
function mu(e) {
  let t, n, i, r, l, a;
  const o = [
    {
      autoscroll: (
        /*gradio*/
        e[17].autoscroll
      )
    },
    { i18n: (
      /*gradio*/
      e[17].i18n
    ) },
    /*loading_status*/
    e[15]
  ];
  let s = {};
  for (let c = 0; c < o.length; c += 1)
    s = iu(s, o[c]);
  t = new Xa({ props: s });
  const u = [_u, hu], f = [];
  function _(c, d) {
    return (
      /*multiselect*/
      c[7] ? 0 : 1
    );
  }
  return i = _(e), r = f[i] = u[i](e), {
    c() {
      Nt(t.$$.fragment), n = cu(), r.c(), l = lu();
    },
    m(c, d) {
      Ct(t, c, d), Ai(c, n, d), f[i].m(c, d), Ai(c, l, d), a = !0;
    },
    p(c, d) {
      const v = d[0] & /*gradio, loading_status*/
      163840 ? ou(o, [
        d[0] & /*gradio*/
        131072 && {
          autoscroll: (
            /*gradio*/
            c[17].autoscroll
          )
        },
        d[0] & /*gradio*/
        131072 && { i18n: (
          /*gradio*/
          c[17].i18n
        ) },
        d[0] & /*loading_status*/
        32768 && su(
          /*loading_status*/
          c[15]
        )
      ]) : {};
      t.$set(v);
      let y = i;
      i = _(c), i === y ? f[i].p(c, d) : (au(), Re(f[y], 1, 1, () => {
        f[y] = null;
      }), ru(), r = f[i], r ? r.p(c, d) : (r = f[i] = u[i](c), r.c()), Me(r, 1), r.m(l.parentNode, l));
    },
    i(c) {
      a || (Me(t.$$.fragment, c), Me(r), a = !0);
    },
    o(c) {
      Re(t.$$.fragment, c), Re(r), a = !1;
    },
    d(c) {
      c && (Ti(n), Ti(l)), kt(t, c), f[i].d(c);
    }
  };
}
function du(e) {
  let t, n;
  return t = new ws({
    props: {
      visible: (
        /*visible*/
        e[6]
      ),
      elem_id: (
        /*elem_id*/
        e[4]
      ),
      elem_classes: (
        /*elem_classes*/
        e[5]
      ),
      padding: (
        /*container*/
        e[12]
      ),
      allow_overflow: !1,
      scale: (
        /*scale*/
        e[13]
      ),
      min_width: (
        /*min_width*/
        e[14]
      ),
      $$slots: { default: [mu] },
      $$scope: { ctx: e }
    }
  }), {
    c() {
      Nt(t.$$.fragment);
    },
    m(i, r) {
      Ct(t, i, r), n = !0;
    },
    p(i, r) {
      const l = {};
      r[0] & /*visible*/
      64 && (l.visible = /*visible*/
      i[6]), r[0] & /*elem_id*/
      16 && (l.elem_id = /*elem_id*/
      i[4]), r[0] & /*elem_classes*/
      32 && (l.elem_classes = /*elem_classes*/
      i[5]), r[0] & /*container*/
      4096 && (l.padding = /*container*/
      i[12]), r[0] & /*scale*/
      8192 && (l.scale = /*scale*/
      i[13]), r[0] & /*min_width*/
      16384 && (l.min_width = /*min_width*/
      i[14]), r[0] & /*choices, max_choices, label, info, show_label, allow_custom_value, filterable, container, gradio, interactive, value, value_is_output, multiselect, loading_status*/
      499599 | r[1] & /*$$scope*/
      16 && (l.$$scope = { dirty: r, ctx: i }), t.$set(l);
    },
    i(i) {
      n || (Me(t.$$.fragment, i), n = !0);
    },
    o(i) {
      Re(t.$$.fragment, i), n = !1;
    },
    d(i) {
      kt(t, i);
    }
  };
}
function bu(e, t, n) {
  let { label: i = "Dropdown" } = t, { info: r = void 0 } = t, { elem_id: l = "" } = t, { elem_classes: a = [] } = t, { visible: o = !0 } = t, { value: s = void 0 } = t, { value_is_output: u = !1 } = t, { multiselect: f = !1 } = t, { max_choices: _ = null } = t, { choices: c } = t, { show_label: d } = t, { filterable: v } = t, { container: y = !0 } = t, { scale: b = null } = t, { min_width: g = void 0 } = t, { loading_status: E } = t, { allow_custom_value: h = !1 } = t, { gradio: m } = t, { interactive: S } = t;
  function p(A) {
    s = A, n(0, s);
  }
  function k(A) {
    u = A, n(1, u);
  }
  const T = () => m.dispatch("change"), B = () => m.dispatch("input"), F = (A) => m.dispatch("select", A.detail), N = () => m.dispatch("blur"), D = () => m.dispatch("focus"), x = () => m.dispatch("key_up");
  function V(A) {
    s = A, n(0, s);
  }
  function z(A) {
    u = A, n(1, u);
  }
  const oe = () => m.dispatch("change"), he = () => m.dispatch("input"), _e = (A) => m.dispatch("select", A.detail), me = () => m.dispatch("blur"), P = () => m.dispatch("focus"), Se = (A) => m.dispatch("key_up", A.detail);
  return e.$$set = (A) => {
    "label" in A && n(2, i = A.label), "info" in A && n(3, r = A.info), "elem_id" in A && n(4, l = A.elem_id), "elem_classes" in A && n(5, a = A.elem_classes), "visible" in A && n(6, o = A.visible), "value" in A && n(0, s = A.value), "value_is_output" in A && n(1, u = A.value_is_output), "multiselect" in A && n(7, f = A.multiselect), "max_choices" in A && n(8, _ = A.max_choices), "choices" in A && n(9, c = A.choices), "show_label" in A && n(10, d = A.show_label), "filterable" in A && n(11, v = A.filterable), "container" in A && n(12, y = A.container), "scale" in A && n(13, b = A.scale), "min_width" in A && n(14, g = A.min_width), "loading_status" in A && n(15, E = A.loading_status), "allow_custom_value" in A && n(16, h = A.allow_custom_value), "gradio" in A && n(17, m = A.gradio), "interactive" in A && n(18, S = A.interactive);
  }, [
    s,
    u,
    i,
    r,
    l,
    a,
    o,
    f,
    _,
    c,
    d,
    v,
    y,
    b,
    g,
    E,
    h,
    m,
    S,
    p,
    k,
    T,
    B,
    F,
    N,
    D,
    x,
    V,
    z,
    oe,
    he,
    _e,
    me,
    P,
    Se
  ];
}
class pu extends nu {
  constructor(t) {
    super(), uu(
      this,
      t,
      bu,
      du,
      fu,
      {
        label: 2,
        info: 3,
        elem_id: 4,
        elem_classes: 5,
        visible: 6,
        value: 0,
        value_is_output: 1,
        multiselect: 7,
        max_choices: 8,
        choices: 9,
        show_label: 10,
        filterable: 11,
        container: 12,
        scale: 13,
        min_width: 14,
        loading_status: 15,
        allow_custom_value: 16,
        gradio: 17,
        interactive: 18
      },
      null,
      [-1, -1]
    );
  }
}
export {
  aa as BaseDropdown,
  gu as BaseExample,
  Zo as BaseMultiselect,
  pu as default
};
