import React from 'react';
import { 
  FaWallet, 
  FaDollarSign, 
  FaRobot, 
  FaArrowTrendUp,
  FaClock,
  FaArrowTrendDown
} from 'react-icons/fa6';
import { BiTrendingUp } from 'react-icons/bi';
import StatCard from '../common/StatCard';
import PerformanceChart from '../common/PerformanceChart';
import GlassCard from '../common/GlassCard';
import TradeTable from '../common/TradeTable';
import {
  portfolioData,
  performanceData,
  recentTrades,
  fnoData,
  watchlistData
} from '../../data/dummyData';

const Dashboard = () => {
  // Quick stats for F&O
  const fnoStats = [
    { label: 'NIFTY 50', value: fnoData.nifty, change: fnoData.niftyChange, type: 'index' },
    { label: 'BANK NIFTY', value: fnoData.bankNifty, change: fnoData.bankNiftyChange, type: 'index' },
    { label: 'SENSEX', value: fnoData.sensex, change: fnoData.sensexChange, type: 'index' },
  ];

  return (
    <div className="space-y-6">
      {/* Welcome Section */}
      <div className="glass-light rounded-2xl p-6 border border-white/5">
        <h2 className="text-xl font-semibold text-white/90">
          Welcome back, Trader 👋
        </h2>
        <p className="text-sm text-gray-400 mt-1">
          Indian Market • Intraday & F&O Trading
        </p>
        <div className="flex flex-wrap gap-4 mt-3">
          {fnoStats.map((stat, index) => (
            <div key={index} className="flex items-center gap-3 bg-white/5 rounded-xl px-4 py-2">
              <span className="text-sm font-medium text-white/80">{stat.label}</span>
              <span className="text-sm text-white/90 font-semibold">
                {stat.value.toLocaleString()}
              </span>
              <span className={`text-xs font-medium ${stat.change.includes('+') ? 'text-emerald-400' : 'text-red-400'}`}>
                {stat.change}
              </span>
            </div>
          ))}
        </div>
      </div>

      {/* Stats Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
        <StatCard
          title="Portfolio Value"
          value={`₹${portfolioData.value.toLocaleString()}`}
          sub="+3.24% today"
          icon={<FaWallet />}
          change={portfolioData.change}
          changeType="up"
        />
        <StatCard
          title="Today's P&L"
          value={`+₹${portfolioData.pnl.toLocaleString()}`}
          sub="vs yesterday +₹21,000"
          icon={<FaDollarSign />}
          change={2.1}
          changeType="up"
        />
        <StatCard
          title="Win Rate"
          value="68.4%"
          sub="Last 30 days"
          icon={<BiTrendingUp />}
          change={1.2}
          changeType="up"
        />
        <StatCard
          title="Active Strategy"
          value="Momentum"
          sub="since Apr 12"
          icon={<FaRobot />}
        />
      </div>

      {/* Chart & Quick Stats */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-5">
        <div className="lg:col-span-2">
          <PerformanceChart data={performanceData} />
        </div>
        <GlassCard title="Watchlist">
          <div className="space-y-2">
            {watchlistData.map((stock, index) => (
              <div key={index} className="flex justify-between items-center py-2 border-b border-white/5 last:border-0">
                <div>
                  <span className="text-sm font-medium text-white/90">{stock.symbol}</span>
                  <span className="text-xs text-gray-400 ml-2">₹{stock.price}</span>
                </div>
                <div className="flex items-center gap-3">
                  <span className={`text-xs font-medium ${stock.change.includes('+') ? 'text-emerald-400' : 'text-red-400'}`}>
                    {stock.change}
                  </span>
                  <span className="text-xs text-gray-400">{stock.volume}</span>
                </div>
              </div>
            ))}
          </div>
        </GlassCard>
      </div>

      {/* Recent Trades */}
      <div>
        <h3 className="text-sm font-medium text-gray-300 mb-3 flex items-center gap-2">
          <FaClock className="text-emerald-400" /> Recent Trades
        </h3>
        <GlassCard>
          <TradeTable
            trades={recentTrades}
            headers={['Symbol', 'Side', 'Price', 'Qty', 'Time', 'P&L']}
            renderRow={(trade, index) => (
              <div key={index} className="grid grid-cols-6 gap-2 py-2 border-b border-white/5 last:border-0 text-sm items-center">
                <span className="font-medium text-white/80">{trade.symbol}</span>
                <span className={`font-medium ${trade.side === 'BUY' ? 'text-emerald-400' : 'text-red-400'}`}>
                  {trade.side}
                </span>
                <span className="text-white/70">₹{trade.price.toFixed(2)}</span>
                <span className="text-white/70">{trade.quantity}</span>
                <span className="text-gray-400 text-xs">{trade.time}</span>
                <span className={`font-medium ${trade.pnl.includes('+') ? 'text-emerald-400' : 'text-red-400'}`}>
                  {trade.pnl}
                </span>
              </div>
            )}
          />
        </GlassCard>
      </div>
    </div>
  );
};

export default Dashboard;