import React, { useState } from 'react';
import { FaPlay, FaStop, FaRobot, FaChartLine } from 'react-icons/fa';
import GlassCard from '../common/GlassCard';
import TradeTable from '../common/TradeTable';
import { openPositions, recentOrders } from '../../data/dummyData';

const LiveTrading = () => {
  const [isBotActive, setIsBotActive] = useState(true);

  const toggleBot = (action) => {
    if (action === 'start') {
      setIsBotActive(true);
    } else {
      setIsBotActive(false);
    }
  };

  return (
    <div className="space-y-6">
      {/* Bot Status */}
      <div className="flex flex-wrap gap-4 items-center">
        <GlassCard className="flex-1 min-w-[200px]">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-gray-400">Bot Status</p>
              <div className="flex items-center gap-2 mt-1">
                <span className={`w-2.5 h-2.5 ${isBotActive ? 'bg-emerald-400' : 'bg-red-400'} rounded-full animate-pulse`}></span>
                <span className="text-lg font-bold text-white/90">
                  {isBotActive ? 'Active' : 'Stopped'}
                </span>
              </div>
            </div>
            <FaRobot className="text-3xl text-emerald-400/60" />
          </div>
        </GlassCard>

        <div className="flex gap-3">
          <button
            onClick={() => toggleBot('start')}
            className="bg-emerald-500 hover:bg-emerald-600 text-white px-6 py-2.5 rounded-xl font-medium transition shadow-lg shadow-emerald-500/20 flex items-center gap-2"
          >
            <FaPlay className="text-sm" /> Start Bot
          </button>
          <button
            onClick={() => toggleBot('stop')}
            className="bg-red-500/20 hover:bg-red-500/30 text-red-400 px-6 py-2.5 rounded-xl font-medium transition border border-red-500/20 flex items-center gap-2"
          >
            <FaStop className="text-sm" /> Stop Bot
          </button>
        </div>
      </div>

      {/* Open Positions */}
      <div>
        <h3 className="text-sm font-medium text-gray-300 mb-3 flex items-center gap-2">
          <FaChartLine className="text-emerald-400" /> Open Positions
        </h3>
        <GlassCard>
          <TradeTable
            trades={openPositions}
            headers={['Symbol', 'Type', 'Qty', 'Entry', 'Current', 'P&L']}
            renderRow={(position, index) => (
              <div key={index} className="grid grid-cols-6 gap-2 py-2 border-b border-white/5 last:border-0 text-sm items-center">
                <span className="font-medium text-white/80">{position.symbol}</span>
                <span className={`font-medium ${position.type === 'LONG' ? 'text-emerald-400' : 'text-red-400'}`}>
                  {position.type}
                </span>
                <span className="text-white/70">{position.quantity}</span>
                <span className="text-white/70">₹{position.entry.toLocaleString()}</span>
                <span className="text-white/70">₹{position.current.toLocaleString()}</span>
                <span className={`font-medium ${position.pnl.includes('+') ? 'text-emerald-400' : 'text-red-400'}`}>
                  {position.pnl} ({position.pnlPercent})
                </span>
              </div>
            )}
          />
        </GlassCard>
      </div>

      {/* Recent Orders */}
      <div>
        <h3 className="text-sm font-medium text-gray-300 mb-3">Recent Orders</h3>
        <GlassCard>
          <TradeTable
            trades={recentOrders}
            headers={['Symbol', 'Type', 'Side', 'Price', 'Filled', 'Status', 'Time']}
            renderRow={(order, index) => (
              <div key={index} className="grid grid-cols-7 gap-2 py-2 border-b border-white/5 last:border-0 text-sm items-center">
                <span className="font-medium text-white/80">{order.symbol}</span>
                <span className="text-white/70">{order.type}</span>
                <span className={`font-medium ${order.side === 'BUY' ? 'text-emerald-400' : 'text-red-400'}`}>
                  {order.side}
                </span>
                <span className="text-white/70">₹{order.price}</span>
                <span className="text-white/70">{order.filled}</span>
                <span className={`text-xs font-medium px-2 py-0.5 rounded-full ${
                  order.status === 'FILLED' 
                    ? 'text-emerald-400 bg-emerald-500/10' 
                    : 'text-yellow-400 bg-yellow-500/10'
                }`}>
                  {order.status}
                </span>
                <span className="text-gray-400 text-xs">{order.time}</span>
              </div>
            )}
          />
        </GlassCard>
      </div>
    </div>
  );
};

export default LiveTrading;