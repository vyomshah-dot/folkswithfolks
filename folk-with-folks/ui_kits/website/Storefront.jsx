// Folk with Folks — website UI kit · storefront sections
// Exports: Hero, KitGrid, KitCard, StoryBand, HowItWorks, Newsletter

function Hero({ onShop }) {
  return (
    <section className="hero">
      <div className="wrap hero-inner">
        <div className="hero-copy">
          <span className="eyebrow"><Motif type="dot" size={14} color="#C24E3A" /> KATHA · DIY PUPPET KITS</span>
          <h1 className="hero-title">Tales you can <span className="mark-band">hold</span>.</h1>
          <p className="hero-lead">Open a box. Snip, fold, and string up a folk-tale puppet — then put on a show.
            Made by a little studio in India, for clever hands aged 7 and up.</p>
          <div className="hero-actions">
            <button className="btn btn-primary" onClick={onShop}>Open the box</button>
            <button className="btn btn-ghost">Watch a tale <i data-lucide="play"></i></button>
          </div>
          <div className="hero-trust">
            <span><i data-lucide="scissors"></i> Hand-cut kits</span>
            <span><Motif type="leaf" size={16} color="#5C7A4A" /> Recycled paper & clay</span>
            <span>Ages 7+</span>
          </div>
        </div>
        <div className="hero-stage">
          <div className="stage-card">
            <img src="../../assets/chanakya-hero.jpg" alt="Hand-sculpted Chanakya puppet on a tabletop village set" className="stage-photo" />
            <span className="stage-badge">Katha kit · 01</span>
            <div className="stage-floor">Tonight's show: <em>Chanakya &amp; the Nandas</em></div>
          </div>
          <Motif type="sun" size={48} />
          <span className="float-buti"><Motif type="buti" size={40} color="#E8A33D" /></span>
        </div>
      </div>
    </section>);
}

const KITS = [
  { id: 'chanakya', tag: 'BESTSELLER', name: "Chanakya's Kit of Wit", desc: 'He outwitted kings. You’re about to out-wit a cardboard box — shadow puppets and nine clever schemes inside.', price: 699, color: '#2E3A59', motif: 'buti' },
  { id: 'tenali', tag: 'NEW', name: "Tenali's Kit of Mischief", desc: 'The court joker who fooled everyone but the cat. A string puppet with a grin you fold yourself.', price: 899, color: '#C24E3A', motif: 'sun' },
  { id: 'birbal', tag: '', name: "Birbal's Kit of Cleverness", desc: 'Nine riddles, one quick courtier, and a stepped stage to perform them on.', price: 999, color: '#5C7A4A', motif: 'leaf' },
];

function KitCard({ kit, onAdd }) {
  return (
    <article className="kit-card">
      <div className="kit-thumb" style={{ background: kit.color }}>
        <span className="kit-thumb-motif"><Motif type={kit.motif} size={64} color="#F4ECDD" /></span>
        {kit.tag && <span className="kit-tag">{kit.tag}</span>}
      </div>
      <div className="kit-body">
        <h3 className="kit-name">{kit.name}</h3>
        <p className="kit-desc">{kit.desc}</p>
        <div className="kit-foot">
          <span className="kit-price">₹{kit.price}</span>
          <button className="btn btn-primary btn-sm" onClick={() => onAdd(kit)}>Add to box</button>
        </div>
      </div>
    </article>);
}

function KitGrid({ onAdd }) {
  return (
    <section className="wrap kit-section">
      <div className="section-head">
        <div className="head-with-rule">
          <h2 className="h2">Pick a tale to make</h2>
          <FolkRule align="left" />
        </div>
        <a href="#" className="see-all">All kits <i data-lucide="arrow-right"></i></a>
      </div>
      <div className="kit-grid">
        {KITS.map(k => <KitCard key={k.id} kit={k} onAdd={onAdd} />)}
      </div>
    </section>);
}

function HowItWorks() {
  const steps = [
    { n: '1', t: 'Open the box', d: 'Stage, puppets, string, and a story card. No glue, no screens.' },
    { n: '2', t: 'Snip & fold', d: 'Punch out the pieces and fold along the dotted lines. Wonky is welcome.' },
    { n: '3', t: 'Put on a show', d: 'Raise the curtain on your stepped stage and tell the tale your way.' },
  ];
  return (
    <section className="how-band">
      <div className="wrap">
        <div className="how-title-wrap">
          <h2 className="h2 how-title">Three steps to a show</h2>
          <FolkRule align="center" onDark={true} />
        </div>
        <div className="how-grid">
          {steps.map(s => (
            <div key={s.n} className="how-step">
              <span className="how-num">{s.n}</span>
              <h4>{s.t}</h4>
              <p>{s.d}</p>
            </div>))}
        </div>
      </div>
    </section>);
}

function StoryBand() {
  return (
    <section className="story-band">
      <div className="wrap story-inner">
        <Motif type="buti" size={36} color="#E8A33D" />
        <blockquote className="story-quote">
          “Once, in the court of a clever king, the joker bowed so low he found a coin
          no one else had thought to look for.”
        </blockquote>
        <span className="story-by">— from the Katha story card, <em>Tenali's Kit of Mischief</em></span>
      </div>
    </section>);
}

function Newsletter() {
  const [done, setDone] = React.useState(false);
  return (
    <section className="wrap news-section">
      <div className="news-card">
        <div>
          <h3 className="h3">A new tale in your inbox</h3>
          <FolkRule align="left" width={180} />
          <p className="news-sub">One folk story and one tiny make, once a month. No noise.</p>
        </div>
        {done ? (
          <p className="news-done"><i data-lucide="check"></i> Lovely — check your inbox for a tale.</p>
        ) : (
          <form className="news-form" onSubmit={e => { e.preventDefault(); setDone(true); }}>
            <input type="email" required placeholder="you@home.in" aria-label="Email" />
            <button className="btn btn-primary" type="submit">Send me a tale</button>
          </form>
        )}
      </div>
    </section>);
}

Object.assign(window, { Hero, KitCard, KitGrid, HowItWorks, StoryBand, Newsletter, KITS });
