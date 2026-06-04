// Folk with Folks — website UI kit · folk-pattern section rule
// A block-print decorative line that tiles under section headings.
// Exports (to window): FolkRule, FolkTweaksContext, FOLK_DEFAULTS

const FOLK_DEFAULTS = /*EDITMODE-BEGIN*/{
  "folkShow": true,
  "folkPattern": "zigzag",
  "folkColor": "#2A241F",
  "folkThickness": 2.4,
  "folkWidth": 240
}/*EDITMODE-END*/;

const FolkTweaksContext = React.createContext(FOLK_DEFAULTS);

// Build the repeating <pattern> tile for a given variant.
// Returns { tile, h, content } — content is the SVG inside one tile.
function folkTile(variant, color, w, scale) {
  const h = 24;
  const mid = h / 2;
  const top = 5;
  const bot = h - 5;
  const sw = { stroke: color, strokeWidth: w, fill: 'none', strokeLinecap: 'round', strokeLinejoin: 'round' };

  if (variant === 'scallop') {
    const tile = 30 * scale;
    return { tile, h, content: (
      <path d={`M0 ${mid} Q ${tile * 0.25} ${top} ${tile * 0.5} ${mid} Q ${tile * 0.75} ${bot} ${tile} ${mid}`} {...sw} />
    ) };
  }
  if (variant === 'triangles') {
    const tile = 20 * scale;
    return { tile, h, content: (
      <g>
        <line x1="0" y1={bot} x2={tile} y2={bot} {...sw} />
        <path d={`M2 ${bot} L${tile / 2} ${top} L${tile - 2} ${bot} Z`} fill={color} stroke={color} strokeWidth={w * 0.5} strokeLinejoin="round" />
      </g>
    ) };
  }
  if (variant === 'diamonds') {
    const tile = 28 * scale;
    const r = 5.5;
    return { tile, h, content: (
      <g>
        <line x1="0" y1={mid} x2={tile} y2={mid} {...sw} />
        <path d={`M${tile / 2} ${mid - r} L${tile / 2 + r} ${mid} L${tile / 2} ${mid + r} L${tile / 2 - r} ${mid} Z`} fill={color} stroke="none" />
      </g>
    ) };
  }
  if (variant === 'vine') {
    const tile = 34 * scale;
    return { tile, h, content: (
      <g>
        <path d={`M0 ${mid} Q ${tile * 0.25} ${top} ${tile * 0.5} ${mid} Q ${tile * 0.75} ${bot} ${tile} ${mid}`} {...sw} />
        <circle cx={tile * 0.25} cy={top + 1.5} r={w * 0.9} fill={color} stroke="none" />
        <circle cx={tile * 0.75} cy={bot - 1.5} r={w * 0.9} fill={color} stroke="none" />
      </g>
    ) };
  }
  // zigzag (default)
  const tile = 18 * scale;
  return { tile, h, content: (
    <path d={`M0 ${bot} L${tile / 2} ${top} L${tile} ${bot}`} {...sw} />
  ) };
}

function FolkRule({ align = 'left', onDark = false, width: widthOverride }) {
  const t = React.useContext(FolkTweaksContext);
  const reactId = React.useId().replace(/[:]/g, '');
  if (!t.folkShow) return null;

  // Keep the rule legible on dark (indigo) bands: if the chosen colour is the dark
  // ink, swap to paper so the "black stroke" stays visible against indigo.
  let color = t.folkColor;
  if (onDark && color.toLowerCase() === '#2a241f') color = '#F4ECDD';

  const scale = 1;
  const { tile, h, content } = folkTile(t.folkPattern, color, t.folkThickness, scale);
  const pid = 'folk-' + t.folkPattern + '-' + reactId;
  const len = widthOverride || t.folkWidth;

  const justify = align === 'center' ? 'center' : (align === 'right' ? 'flex-end' : 'flex-start');
  return (
    <div className="folk-rule" style={{ display: 'flex', justifyContent: justify }}>
      <svg height={h} width={len} viewBox={`0 0 ${len} ${h}`} style={{ maxWidth: '100%', display: 'block', overflow: 'visible' }} aria-hidden="true">
        <defs>
          <pattern id={pid} width={tile} height={h} patternUnits="userSpaceOnUse">
            {content}
          </pattern>
        </defs>
        <rect x="0" y="0" width={len} height={h} fill={`url(#${pid})`} />
      </svg>
    </div>);
}

Object.assign(window, { FolkRule, FolkTweaksContext, FOLK_DEFAULTS });
