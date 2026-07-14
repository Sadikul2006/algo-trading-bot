// Indian Stock Market focused dummy data
export const portfolioData = {
  value: 2845075,
  change: 3.24,
  pnl: 89240,
  dayChange: 1.8,
};

export const watchlistData = [
  { symbol: 'RELIANCE', price: 2456.75, change: '+1.2%', volume: '2.3M' },
  { symbol: 'TCS', price: 3567.80, change: '-0.5%', volume: '1.8M' },
  { symbol: 'HDFC BANK', price: 1678.90, change: '+0.8%', volume: '3.1M' },
  { symbol: 'INFY', price: 1432.50, change: '+2.1%', volume: '2.7M' },
  { symbol: 'ICICI BANK', price: 987.65, change: '-0.3%', volume: '4.2M' },
];

export const fnoData = {
  nifty: 19567.80,
  niftyChange: '+0.75%',
  bankNifty: 45234.50,
  bankNiftyChange: '+1.2%',
  sensex: 65432.10,
  sensexChange: '+0.65%',
};

export const performanceData = [
  { label: 'Mon', value: 1200 },
  { label: 'Tue', value: 900 },
  { label: 'Wed', value: 1500 },
  { label: 'Thu', value: 800 },
  { label: 'Fri', value: 2100 },
  { label: 'Sat', value: 1700 },
  { label: 'Sun', value: 1300 },
];

export const recentTrades = [
  { symbol: 'RELIANCE', side: 'BUY', price: 2456.75, quantity: 25, time: '14:32', pnl: '+₹1,250' },
  { symbol: 'TCS', side: 'SELL', price: 3567.80, quantity: 15, time: '13:15', pnl: '-₹450' },
  { symbol: 'HDFC BANK', side: 'BUY', price: 1678.90, quantity: 30, time: '12:05', pnl: '+₹2,100' },
  { symbol: 'INFY', side: 'SELL', price: 1432.50, quantity: 20, time: '11:20', pnl: '+₹980' },
  { symbol: 'ICICI BANK', side: 'BUY', price: 987.65, quantity: 50, time: '10:45', pnl: '-₹320' },
];

export const openPositions = [
  { symbol: 'RELIANCE', type: 'LONG', quantity: 25, entry: 2450, current: 2456.75, pnl: '+₹168.75', pnlPercent: '+0.28%' },
  { symbol: 'TCS', type: 'SHORT', quantity: 15, entry: 3580, current: 3567.80, pnl: '+₹183', pnlPercent: '+0.34%' },
  { symbol: 'BANK NIFTY', type: 'LONG', quantity: 2, entry: 45000, current: 45234.50, pnl: '+₹469', pnlPercent: '+0.52%' },
];

export const recentOrders = [
  { symbol: 'RELIANCE', type: 'LIMIT', side: 'BUY', price: 2450, filled: 25, status: 'FILLED', time: '14:30' },
  { symbol: 'TCS', type: 'MARKET', side: 'SELL', price: 3567, filled: 15, status: 'FILLED', time: '13:10' },
  { symbol: 'HDFC BANK', type: 'LIMIT', side: 'BUY', price: 1675, filled: 0, status: 'PENDING', time: '12:00' },
  { symbol: 'INFY', type: 'STOP LOSS', side: 'SELL', price: 1420, filled: 20, status: 'FILLED', time: '11:15' },
];

export const backtestResults = {
  totalReturn: 18.4,
  sharpeRatio: 1.82,
  maxDrawdown: -6.2,
  winRate: 68.4,
  totalTrades: 124,
  profitableTrades: 85,
};