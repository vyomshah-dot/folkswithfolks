// Folk with Folks — website UI kit · interactive app shell
// Cart drawer + toast + page assembly. Demonstrates a click-thru add-to-cart flow.

function CartDrawer({ open, items, onClose, onRemove }) {
  const total = items.reduce((s, i) => s + i.price * i.qty, 0);
  return (
    <div className={'drawer-scrim' + (open ? ' is-open' : '')} onClick={onClose}>
      <aside className={'cart-drawer' + (open ? ' is-open' : '')} onClick={e => e.stopPropagation()}>
        <div className="drawer-head">
          <h3 className="h3">Your box</h3>
          <button className="icon-btn" onClick={onClose} aria-label="Close"><i data-lucide="x"></i></button>
        </div>
        {items.length === 0 ? (
          <div className="drawer-empty">
            <Motif type="buti" size={48} color="#C24E3A" />
            <p>No tales yet. Every studio starts with one.</p>
          </div>
        ) : (
          <div className="drawer-items">
            {items.map(i => (
              <div className="drawer-row" key={i.id}>
                <span className="drawer-swatch" style={{ background: i.color }}><Motif type={i.motif} size={26} color="#F4ECDD" /></span>
                <div className="drawer-meta">
                  <strong>{i.name}</strong>
                  <span>Qty {i.qty} · ₹{i.price}</span>
                </div>
                <button className="link-btn" onClick={() => onRemove(i.id)}>Remove</button>
              </div>))}
          </div>
        )}
        <div className="drawer-foot">
          <div className="drawer-total"><span>Total</span><span>₹{total}</span></div>
          <button className="btn btn-primary btn-block" disabled={items.length === 0}>Checkout</button>
          <p className="drawer-note">⚠ Small parts — a grown-up should help with the snipping.</p>
        </div>
      </aside>
    </div>);
}

function Toast({ msg }) {
  if (!msg) return null;
  return <div className="toast"><Motif type="dot" size={14} color="#E8A33D" /> {msg}</div>;
}

function App() {
  const [t, setTweak] = useTweaks(FOLK_DEFAULTS);
  const [cart, setCart] = React.useState([]);
  const [open, setOpen] = React.useState(false);
  const [toast, setToast] = React.useState('');
  const toastTimer = React.useRef(null);

  const addToCart = (kit) => {
    setCart(prev => {
      const ex = prev.find(p => p.id === kit.id);
      if (ex) return prev.map(p => p.id === kit.id ? { ...p, qty: p.qty + 1 } : p);
      return [...prev, { ...kit, qty: 1 }];
    });
    setToast(`Added “${kit.name}” to your box`);
    clearTimeout(toastTimer.current);
    toastTimer.current = setTimeout(() => setToast(''), 2200);
  };
  const removeFromCart = (id) => setCart(prev => prev.filter(p => p.id !== id));
  const count = cart.reduce((s, i) => s + i.qty, 0);

  React.useEffect(() => { if (window.lucide) window.lucide.createIcons(); });

  const COLORS = [
    ['#2A241F', 'Ink'], ['#C24E3A', 'Terracotta'], ['#E8A33D', 'Marigold'], ['#5C7A4A', 'Neem'],
  ];
  const PATTERNS = ['zigzag', 'scallop', 'triangles', 'diamonds', 'vine'];

  return (
    <FolkTweaksContext.Provider value={t}>
    <React.Fragment>
      <SiteHeader cartCount={count} onCart={() => setOpen(true)} />
      <main>
        <Hero onShop={() => { const el = document.querySelector('.kit-section'); if (el) window.scrollTo({ top: el.offsetTop - 80, behavior: 'smooth' }); }} />
        <KitGrid onAdd={addToCart} />
        <HowItWorks />
        <StoryBand />
        <Newsletter />
      </main>
      <SiteFooter />
      <CartDrawer open={open} items={cart} onClose={() => setOpen(false)} onRemove={removeFromCart} />
      <Toast msg={toast} />
      <TweaksPanel title="Tweaks">
        <TweakSection label="Section rule" />
        <TweakToggle label="Show rule" value={t.folkShow}
          onChange={(v) => setTweak('folkShow', v)} />
        <TweakSelect label="Folk pattern" value={t.folkPattern} options={PATTERNS}
          onChange={(v) => setTweak('folkPattern', v)} />
        <TweakColor label="Colour" value={t.folkColor}
          options={COLORS.map(c => c[0])}
          onChange={(v) => setTweak('folkColor', v)} />
        <TweakSlider label="Thickness" value={t.folkThickness} min={1} max={5} step={0.2} unit="px"
          onChange={(v) => setTweak('folkThickness', v)} />
        <TweakSlider label="Length" value={t.folkWidth} min={80} max={420} step={10} unit="px"
          onChange={(v) => setTweak('folkWidth', v)} />
      </TweaksPanel>
    </React.Fragment>
    </FolkTweaksContext.Provider>);
}

ReactDOM.createRoot(document.getElementById('root')).render(<App />);
