import React from 'react';

const TradeTable = ({ trades, headers, renderRow }) => {
  if (!trades || trades.length === 0) {
    return (
      <div className="text-center text-gray-400 py-8">
        No trades to display
      </div>
    );
  }

  return (
    <div className="overflow-x-auto">
      <div className="min-w-[600px]">
        <div className="grid grid-cols-{headers.length} gap-2 text-xs font-semibold text-gray-400 border-b border-white/5 pb-2 mb-2">
          {headers.map((header, index) => (
            <div key={index} className="px-1 truncate">{header}</div>
          ))}
        </div>
        {trades.map((trade, index) => renderRow(trade, index))}
      </div>
    </div>
  );
};

export default TradeTable;