// Folk with Folks — website UI kit · site chrome (header + footer)
// Exports: SiteHeader, SiteFooter, Motif

function Motif({ type, size = 22, color = '#C24E3A' }) {
  // tiny inline folk motifs used as punctuation
  const s = { width: size, height: size, display: 'inline-block', verticalAlign: 'middle' };
  if (type === 'sun') return (
    <svg style={s} viewBox="0 0 48 48"><circle cx="24" cy="24" r="9" fill="#E8A33D"/>
      <g stroke="#2A241F" strokeWidth="2.2" strokeLinecap="round">
        <line x1="24" y1="4" x2="24" y2="9"/><line x1="24" y1="39" x2="24" y2="44"/>
        <line x1="4" y1="24" x2="9" y2="24"/><line x1="39" y1="24" x2="44" y2="24"/>
        <line x1="10" y1="10" x2="14" y2="14"/><line x1="34" y1="34" x2="38" y2="38"/>
        <line x1="34" y1="10" x2="38" y2="14"/><line x1="10" y1="38" x2="14" y2="34"/></g></svg>);
  if (type === 'leaf') return (
    <svg style={s} viewBox="0 0 48 48"><path d="M24 42 C8 30 8 14 24 4 C40 14 40 30 24 42 Z" fill={color}/>
      <line x1="24" y1="40" x2="24" y2="8" stroke="#F4ECDD" strokeWidth="2"/></svg>);
  if (type === 'buti') return (
    <svg style={s} viewBox="0 0 48 48"><g transform="translate(24,24)">
      <ellipse cx="0" cy="-13" rx="5" ry="9" fill={color}/><ellipse cx="0" cy="13" rx="5" ry="9" fill={color}/>
      <ellipse cx="-13" cy="0" rx="9" ry="5" fill={color}/><ellipse cx="13" cy="0" rx="9" ry="5" fill={color}/>
      <circle r="5" fill="#E8A33D"/></g></svg>);
  // dot
  return <svg style={s} viewBox="0 0 48 48"><circle cx="24" cy="24" r="12" fill={color}/></svg>;
}

function BrandLockup({ height = 56 }) {
  // Official Folk with Folks lockup — torana symbol + stacked wordmark
  return (
    <img src="logo-lockup.png" alt="Folk with Folks"
         style={{ height, width: 'auto', display: 'block' }} />);
}

function BrandWordmarkDark({ height = 78 }) {
  // Cream wordmark on dark ink ground — for use on indigo / ink footers
  return (
    <img src="logo-wordmark-on-dark.png" alt="Folk with Folks"
         style={{ height, width: 'auto', display: 'block' }} />);
}

function SiteHeader({ cartCount, onCart }) {
  const [open, setOpen] = React.useState(false);
  const links = ['Kits', 'Workshops', 'Folk Tales', 'About'];
  return (
    <header className="site-header">
      <div className="wrap header-inner">
        <a className="brand" href="#" aria-label="Folk with Folks — home">
          <BrandLockup height={56} />
        </a>
        <nav className="nav-links">
          {links.map(l => <a key={l} href="#" className="nav-link">{l}</a>)}
        </nav>
        <div className="header-actions">
          <button className="icon-btn" aria-label="Search"><i data-lucide="search"></i></button>
          <button className="icon-btn cart" aria-label="Cart" onClick={onCart}>
            <i data-lucide="shopping-bag"></i>
            {cartCount > 0 && <span className="cart-badge">{cartCount}</span>}
          </button>
          <button className="icon-btn menu-only" aria-label="Menu" onClick={() => setOpen(o => !o)}>
            <i data-lucide={open ? 'x' : 'menu'}></i>
          </button>
        </div>
      </div>
      {open && <div className="mobile-menu">{links.map(l => <a key={l} href="#" className="nav-link">{l}</a>)}</div>}
    </header>);
}

function SiteFooter() {
  const cols = [
    { h: 'Shop', items: ['Katha kits', 'Workshops', 'Gift a tale', 'Stockists'] },
    { h: 'Studio', items: ['Our story', 'The makers', 'Press', 'Careers'] },
    { h: 'Help', items: ['How kits work', 'Shipping', 'Returns', 'Contact'] },
  ];
  return (
    <footer className="site-footer">
      <div className="wrap footer-inner">
        <div className="footer-brand">
          <BrandWordmarkDark height={150} />
          <p className="footer-tag">Tales you can hold.</p>
          <div className="footer-motifs">
            <Motif type="sun" size={26} /><Motif type="buti" size={26} color="#E8A33D" /><Motif type="leaf" size={26} color="#5C7A4A" />
          </div>
        </div>
        <div className="footer-cols">
          {cols.map(c => (
            <div key={c.h} className="footer-col">
              <h4>{c.h}</h4>
              {c.items.map(i => <a key={i} href="#">{i}</a>)}
            </div>))}
        </div>
      </div>
      <div className="wrap footer-base">
        <span>© 2026 Folk with Folks — made by hand in India.</span>
        <span>Katha · DIY puppet kits</span>
      </div>
    </footer>);
}

// Decorative torana symbol — used as illustrative figures inside the hero puppet-stage
// (NOT the brand logo; the logo lockup/wordmark live in the header & footer).
function ToranaMarkLight({ height = 44 }) {
  return (
    <svg height={height} viewBox="0 0 240 240" fill="none" aria-hidden="true">
      <g stroke="#F4ECDD" strokeWidth="3.6" strokeLinecap="round" strokeLinejoin="round">
        <circle cx="120" cy="50" r="7" fill="#E8A33D" stroke="#F4ECDD" strokeWidth="2.6"/>
        <path d="M52 178 L52 96 L74 96 L74 78 L106 78 L106 64 L134 64 L134 78 L166 78 L166 96 L188 96 L188 178"/>
        <line x1="58" y1="178" x2="182" y2="178"/>
        <line x1="98" y1="78" x2="98" y2="95" strokeWidth="1.6"/><line x1="142" y1="78" x2="142" y2="95" strokeWidth="1.6"/>
        <circle cx="98" cy="104" r="8.5" fill="#C24E3A" stroke="#F4ECDD"/><path d="M86 118 L110 118 L98 138 Z"/><path d="M98 138 L86 158 L110 158 Z"/><line x1="92" y1="158" x2="88" y2="178"/><line x1="104" y1="158" x2="108" y2="178"/><path d="M86 118 L74 134"/><path d="M110 119 L120 139"/>
        <circle cx="142" cy="104" r="8.5" fill="#C24E3A" stroke="#F4ECDD"/><path d="M130 118 L154 118 L142 138 Z"/><path d="M142 138 L130 158 L154 158 Z"/><line x1="136" y1="158" x2="132" y2="178"/><line x1="148" y1="158" x2="152" y2="178"/><path d="M154 118 L166 134"/><path d="M130 119 L120 139"/>
        <circle cx="120" cy="140" r="4.5" fill="#E8A33D" stroke="#F4ECDD" strokeWidth="2.4"/>
      </g>
    </svg>);
}

Object.assign(window, { Motif, BrandLockup, BrandWordmarkDark, ToranaMarkLight, SiteHeader, SiteFooter });
