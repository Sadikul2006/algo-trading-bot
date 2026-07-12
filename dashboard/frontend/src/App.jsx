import { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [backtestData, setBacktestData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/backtest/RELIANCE')
      .then((response) => response.json())
      .then((data) => {
        setBacktestData(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Loading backtest data...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
      <h1>Algo Trading Bot Dashboard</h1>
      <h2>Backtest Results: {backtestData.symbol}</h2>

      <table border="1" cellPadding="8" style={{ borderCollapse: 'collapse', marginBottom: '20px' }}>
        <tbody>
          <tr><td>Total Trades</td><td>{backtestData.performance.total_trades}</td></tr>
          <tr><td>Win Rate</td><td>{backtestData.performance.win_rate}%</td></tr>
          <tr><td>Profit Factor</td><td>{backtestData.performance.profit_factor}</td></tr>
          <tr><td>Max Drawdown</td><td>{backtestData.performance.max_drawdown}%</td></tr>
          <tr><td>Sharpe Ratio</td><td>{backtestData.performance.sharpe_ratio}</td></tr>
          <tr><td>Total P&L</td><td>₹{backtestData.performance.total_pnl}</td></tr>
        </tbody>
      </table>

      <h3>Trades</h3>
      <table border="1" cellPadding="8" style={{ borderCollapse: 'collapse' }}>
        <thead>
          <tr>
            <th>Entry</th>
            <th>Exit</th>
            <th>Quantity</th>
            <th>Reason</th>
            <th>P&L</th>
          </tr>
        </thead>
        <tbody>
          {backtestData.trades.map((trade, index) => (
            <tr key={index}>
              <td>₹{trade.entry_price.toFixed(2)}</td>
              <td>₹{trade.exit_price.toFixed(2)}</td>
              <td>{trade.quantity}</td>
              <td>{trade.exit_reason}</td>
              <td>₹{trade.pnl}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;