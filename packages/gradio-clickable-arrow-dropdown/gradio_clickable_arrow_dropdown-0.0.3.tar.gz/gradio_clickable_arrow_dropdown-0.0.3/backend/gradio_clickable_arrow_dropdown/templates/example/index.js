const {
  SvelteComponent: _,
  attr: d,
  detach: y,
  element: g,
  init: v,
  insert: m,
  noop: u,
  safe_not_equal: h,
  toggle_class: s
} = window.__gradio__svelte__internal;
function A(n) {
  let e;
  return {
    c() {
      e = g("div"), e.textContent = `${/*names_string*/
      n[2]}`, d(e, "class", "svelte-1gecy8w"), s(
        e,
        "table",
        /*type*/
        n[0] === "table"
      ), s(
        e,
        "gallery",
        /*type*/
        n[0] === "gallery"
      ), s(
        e,
        "selected",
        /*selected*/
        n[1]
      );
    },
    m(l, t) {
      m(l, e, t);
    },
    p(l, [t]) {
      t & /*type*/
      1 && s(
        e,
        "table",
        /*type*/
        l[0] === "table"
      ), t & /*type*/
      1 && s(
        e,
        "gallery",
        /*type*/
        l[0] === "gallery"
      ), t & /*selected*/
      2 && s(
        e,
        "selected",
        /*selected*/
        l[1]
      );
    },
    i: u,
    o: u,
    d(l) {
      l && y(e);
    }
  };
}
function C(n) {
  let e, l = n[0], t = 1;
  for (; t < n.length; ) {
    const i = n[t], c = n[t + 1];
    if (t += 2, (i === "optionalAccess" || i === "optionalCall") && l == null)
      return;
    i === "access" || i === "optionalAccess" ? (e = l, l = c(l)) : (i === "call" || i === "optionalCall") && (l = c((...f) => l.call(e, ...f)), e = void 0);
  }
  return l;
}
function b(n, e, l) {
  let { value: t } = e, { type: i } = e, { selected: c = !1 } = e, { choices: f } = e, r = (t ? Array.isArray(t) ? t : [t] : []).map((a) => C([f.find((o) => o[1] === a), "optionalAccess", (o) => o[0]])).filter((a) => a !== void 0).join(", ");
  return n.$$set = (a) => {
    "value" in a && l(3, t = a.value), "type" in a && l(0, i = a.type), "selected" in a && l(1, c = a.selected), "choices" in a && l(4, f = a.choices);
  }, [i, c, r, t, f];
}
class S extends _ {
  constructor(e) {
    super(), v(this, e, b, A, h, {
      value: 3,
      type: 0,
      selected: 1,
      choices: 4
    });
  }
}
export {
  S as default
};
