// Katha PDP UI kit · app shell — reuses SiteChrome header/footer + cart toast
function Toast({ msg }) {
  if (!msg) return null;
  return <div className="toast"><Motif type="dot" size={14} color="#E8A33D" /> {msg}</div>;
}

function App() {
  const [count, setCount] = React.useState(0);
  const [toast, setToast] = React.useState('');
  const timer = React.useRef(null);
  const add = (qty) => {
    setCount(c => c + qty);
    setToast(`Added ${qty} × “Chanakya's Kit of Wit” to your box`);
    clearTimeout(timer.current);
    timer.current = setTimeout(() => setToast(''), 2300);
  };
  React.useEffect(() => { if (window.lucide) window.lucide.createIcons(); });
  return (
    <React.Fragment>
      <SiteHeader cartCount={count} onCart={() => {}} />
      <main className="pdp">
        <div className="wrap">
          <Breadcrumb />
          <div className="pdp-top">
            <Gallery />
            <BuyPanel onAdd={add} />
          </div>
          <ContentsList />
          <BuildSteps />
          <ReviewList />
        </div>
      </main>
      <SiteFooter />
      <Toast msg={toast} />
    </React.Fragment>);
}
ReactDOM.createRoot(document.getElementById('root')).render(<App />);
