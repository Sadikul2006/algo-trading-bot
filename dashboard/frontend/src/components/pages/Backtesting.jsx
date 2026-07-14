import React, { useState } from 'react';
import { FaPlay, FaChartLine, FaWallet } from 'react-icons/fa';
import GlassCard from '../common/GlassCard';
import StatCard from '../common/StatCard';
import { backtestResults } from '../../data/dummyData';

const Backtesting = () => {
  const [symbol, setSymbol] = useState('NIFTY 50');
  const [dateRange, setDateRange] = useState('Last 30 Days');
  const [capital, setCapital] = useState('₹1,00,000');
  const [strategy, setStrategy] = useState('Momentum Scalper');

  const handleRunBacktest = (e) => {
    e.preventDefault();
    // UI only - no functionality
    console.log('Running backtest...');
  };

  return (
    <div className="space-y-6">
      {/* Configuration */}
      <GlassCard title="Backtest Configuration" titleIcon={<FaWallet />}>
        <form onSubmit={handleRunBacktest}>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            <div>
              <label className="text-xs text-gray-400 block mb-1">Symbol</label>
              <select
                value={symbol}
                onChange={(e) => setSymbol(e.target.value)}
                className="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-2.5 text-white/90 text-sm focus:outline-none focus:border-emerald-400/50"
              >
                <option>NIFTY 50</option>
                <option>BANK NIFTY</option>
                <option>SENSEX</option>
                <option>RELIANCE</option>
                <option>TCS</option>
                <option>HDFC BANK</option>
              </select>
            </div>
            <div>
              <label className="text-xs text-gray-400 block mb-1">Date Range</label>
              <select
                value={dateRange}
                onChange={(e) => setDateRange(e.target.value)}
                className="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-2.5 text-white/90 text-sm focus:outline-none focus:border-emerald-400/50"
              >
                <option>Last 7 Days</option>
                <option>Last 30 Days</option>
                <option>Last 90 Days</option>
                <option>Last 180 Days</option>
                <option>Last 365 Days</option>
              </select>
            </div>
            <div>
              <label className="text-xs text-gray-400 block mb-1">Initial Capital</label>
              <input
                type="text"
                value={capital}
                onChange={(e) => setCapital(e.target.value)}
                className="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-2.5 text-white/90 text-sm focus:outline-none focus:border-emerald-400/50"
              />
            </div>
            <div>
              <label className="text-xs text-gray-400 block mb-1">Strategy</label>
              <select
                value={strategy}
                onChange={(e) => setStrategy(e.target.value)}
                className="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-2.5 text-white/90 text-sm focus:outline-none focus:border-emerald-400/50"
              >
                <option>Momentum Scalper</option>
                <option>Mean Reversion</option>
                <option>Trend Follower</option>
                <option>Breakout Strategy</option>
                <option>Options Selling</option>
              </select>
            </div>
          </div>
          <button
            type="submit"
            className="mt-5 bg-emerald-500 hover:bg-emerald-600 text-white font-medium px-8 py-2.5 rounded-xl transition shadow-lg shadow-emerald-500/20 flex items-center gap-2"
          >
            <FaPlay className="text-sm" /> Run Backtest
          </button>
        </form>
      </GlassCard>

      {/* Results */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5">
        <StatCard
          title="Total Return"
          value={`+${backtestResults.totalReturn}%`}
          icon={<FaChartLine />}
          change={backtestResults.totalReturn}
          changeType="up"
        />
        <StatCard
          title="Sharpe Ratio"
          value={backtestResults.sharpeRatio}
          icon={<span>📊</span>}
        />
        <StatCard
          title="Max Drawdown"
          value={`${backtestResults.maxDrawdown}%`}
          icon={<span>📉</span>}
          change={Math.abs(backtestResults.maxDrawdown)}
          changeType="down"
        />
        <StatCard
          title="Win Rate"
          value={`${backtestResults.winRate}%`}
          sub={`${backtestResults.profitableTrades}/${backtestResults.totalTrades} trades`}
          icon={<span>🎯</span>}
          change={backtestResults.winRate}
          changeType="up"
        />
      </div>

      {/* Chart Placeholder */}
      <GlassCard className="text-center">
        <div className="py-8 text-gray-400 text-sm border border-dashed border-white/10 rounded-xl">
          <FaChartLine className="inline mr-2 text-emerald-400 text-2xl" />
          <p>Backtest results chart visualization</p>
          <p className="text-xs mt-1">(UI only - dummy data)</p>
        </div>
      </GlassCard>
    </div>
  );
};

export default Backtesting;