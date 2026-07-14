import React from 'react';

const StatCard = ({ title, value, sub, icon, change, changeType, className = '' }) => {
  return (
    <div className={`glass rounded-2xl p-5 stat-card ${className}`}>
      <div className="flex justify-between items-start">
        <div className="flex-1">
          <p className="text-sm text-gray-400 font-medium">{title}</p>
          <p className="text-2xl font-bold mt-1 text-white/90">{value}</p>
          {sub && <p className="text-xs text-gray-400 mt-0.5">{sub}</p>}
          {change !== undefined && (
            <span className={`text-xs font-medium ${changeType === 'up' ? 'text-emerald-400' : 'text-red-400'}`}>
              {changeType === 'up' ? '↑' : '↓'} {Math.abs(change)}%
            </span>
          )}
        </div>
        <div className="text-emerald-400/80 text-2xl ml-3">
          {icon}
        </div>
      </div>
    </div>
  );
};

export default StatCard;