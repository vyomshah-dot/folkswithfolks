// Katha PDP UI kit · product-detail components
// Exports: Breadcrumb, Gallery, BuyPanel, QtyStepper, ContentsList, BuildSteps, ReviewList, CharBadge

function Breadcrumb() {
  return (
    <nav className="crumb">
      <a href="#">Kits</a><i data-lucide="chevron-right"></i>
      <a href="#">Wit &amp; Wisdom</a><i data-lucide="chevron-right"></i>
      <span>Chanakya's Kit of Wit</span>
    </nav>);
}

function CharBadge({ size = 92 }) {
  // character badge: symbol-style figure on marigold disc
  return (
    <span className="char-badge" style={{ width: size, height: size }}>
      <svg viewBox="0 0 240 240" width={size * 0.74} fill="none">
        <g stroke="#2A241F" strokeWidth="5" strokeLinecap="round" strokeLinejoin="round">
          <circle cx="120" cy="62" r="16" fill="#2A241F"/>
          <path d="M96 86 L144 86 L120 128 Z" fill="none"/><path d="M120 128 L96 170 L144 170 Z" fill="none"/>
          <line x1="104" y1="170" x2="98" y2="206"/><line x1="136" y1="170" x2="142" y2="206"/>
          <path d="M96 88 L66 120"/><path d="M144 88 L174 120"/>
          <circle cx="66" cy="120" r="6" fill="#2A241F"/><circle cx="174" cy="120" r="6" fill="#2A241F"/>
        </g>
      </svg>
    </span>);
}

function Gallery() {
  const views = ['box', 'puppets', 'stage', 'cards'];
  const [active, setActive] = React.useState(0);
  const labels = { box: 'The box', puppets: 'Puppets', stage: 'Stepped stage', cards: 'Story cards' };
  const motifFor = { box: 'buti', puppets: 'sun', stage: 'leaf', cards: 'dot' };
  return (
    <div className="gallery">
      <div className="gallery-main">
        <span className="gallery-tag">{labels[views[active]]}</span>
        <div className="gallery-stage">
          {views[active] === 'box' ? (
            <div className="box-face">
              <span className="box-line">Chanakya's</span>
              <span className="box-title">KIT OF WIT</span>
              <span className="box-sub">a folk with folks kit</span>
              <CharBadge size={70} />
            </div>
          ) : (
            <Motif type={motifFor[views[active]]} size={120} color="#F4ECDD" />
          )}
        </div>
      </div>
      <div className="gallery-thumbs">
        {views.map((v, i) => (
          <button key={v} className={'thumb' + (i === active ? ' is-active' : '')} onClick={() => setActive(i)} aria-label={labels[v]}>
            <Motif type={motifFor[v]} size={26} color={i === active ? '#F4ECDD' : '#2A241F'} />
          </button>))}
      </div>
    </div>);
}

function QtyStepper({ qty, setQty }) {
  return (
    <div className="qty">
      <button onClick={() => setQty(q => Math.max(1, q - 1))} aria-label="Less"><i data-lucide="minus"></i></button>
      <span>{qty}</span>
      <button onClick={() => setQty(q => q + 1)} aria-label="More"><i data-lucide="plus"></i></button>
    </div>);
}

function BuyPanel({ onAdd }) {
  const [qty, setQty] = React.useState(1);
  return (
    <div className="buy">
      <span className="eyebrow"><Motif type="dot" size={13} color="#C24E3A" /> KATHA · AGES 7+</span>
      <h1 className="pdp-title">Chanakya's Kit of Wit</h1>
      <p className="pdp-lead">He outwitted kings. You're about to out-wit a cardboard box.
        Build a shadow-puppet minister and stage his nine cleverest schemes.</p>
      <div className="badge-row">
        <span className="badge badge-mar">Bestseller</span>
        <span className="badge badge-leaf">Plastic-free</span>
        <span className="badge badge-line">No glue needed</span>
      </div>
      <div className="price-row">
        <span className="price">₹699</span>
        <span className="price-note">free shipping over ₹999</span>
      </div>
      <div className="buy-actions">
        <QtyStepper qty={qty} setQty={setQty} />
        <button className="btn btn-primary buy-btn" onClick={() => onAdd(qty)}>Add to box</button>
      </div>
      <button className="btn btn-ghost wish"><i data-lucide="heart"></i> Save for later</button>
      <ul className="ship">
        <li><i data-lucide="package"></i> Ships in 2–3 days, wrapped in recycled paper</li>
        <li><i data-lucide="scissors"></i> One stage · two puppets · nine story cards</li>
      </ul>
    </div>);
}

function ContentsList() {
  const items = [
    { t: 'A stepped torana stage', d: 'Punch-out and fold — your theatre in five folds.' },
    { t: 'Two shadow puppets', d: 'Chanakya and a very nervous king. Articulated arms.' },
    { t: 'Nine story cards', d: 'One scheme per card, in our cheekiest handwriting.' },
    { t: 'A length of string & a stick', d: 'For working the puppets. Wonky is welcome.' },
  ];
  const [open, setOpen] = React.useState(0);
  return (
    <section className="contents">
      <h2 className="h2">In the box</h2>
      <div className="accordion">
        {items.map((it, i) => (
          <div key={i} className={'acc-row' + (open === i ? ' is-open' : '')}>
            <button className="acc-head" onClick={() => setOpen(open === i ? -1 : i)}>
              <span>{it.t}</span><i data-lucide={open === i ? 'minus' : 'plus'}></i>
            </button>
            {open === i && <p className="acc-body">{it.d}</p>}
          </div>))}
      </div>
    </section>);
}

function BuildSteps() {
  const steps = [
    { n: '1', t: 'Punch & fold', d: 'Pop the pieces out and crease along the dotted lines.' },
    { n: '2', t: 'String the puppets', d: 'Loop the string through the arms. Give them a wiggle.' },
    { n: '3', t: 'Raise the curtain', d: 'Stand the stage up and read scheme one aloud.' },
  ];
  return (
    <section className="build">
      <h2 className="h2 build-title">How you'll make it</h2>
      <div className="build-grid">
        {steps.map(s => (
          <div key={s.n} className="build-step">
            <span className="build-num">{s.n}</span>
            <h4>{s.t}</h4><p>{s.d}</p>
          </div>))}
      </div>
    </section>);
}

function ReviewList() {
  const rev = [
    { n: 'Meera, mum of one', q: '“My seven-year-old ran the whole show for her grandparents. Twice.”', m: 'sun' },
    { n: 'Arjun, age 8', q: '“The king puppet is my favourite because he is scared of everything.”', m: 'buti' },
    { n: 'Devi, teacher', q: '“Finally, a craft kit that respects the kid AND the folk tale.”', m: 'leaf' },
  ];
  return (
    <section className="reviews">
      <div className="rev-head">
        <h2 className="h2">What folks say</h2>
        <span className="rev-stars">★★★★★ <em>4.9 · 212 makers</em></span>
      </div>
      <div className="rev-grid">
        {rev.map((r, i) => (
          <figure key={i} className="rev-card">
            <Motif type={r.m} size={26} color="#C24E3A" />
            <blockquote>{r.q}</blockquote>
            <figcaption>{r.n}</figcaption>
          </figure>))}
      </div>
    </section>);
}

Object.assign(window, { Breadcrumb, Gallery, BuyPanel, QtyStepper, ContentsList, BuildSteps, ReviewList, CharBadge });
