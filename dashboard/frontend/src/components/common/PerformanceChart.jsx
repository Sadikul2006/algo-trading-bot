import React from 'react';
import GlassCard from './GlassCard';

const PerformanceChart = ({ data, height = 36 }) => {
  const max = Math.max(...data.map(d => d.value));

  return (
    <GlassCard title="Performance (7d)" titleIcon={<span>📈</span>}>
      <div className={`flex items-end justify-between h-${height} gap-2`}>
        {data.map((item, index) => {
          const barHeight = (item.value / max) * 100;
          return (
            <div key={index} className="flex flex-col items-center w-full">
              <div
                className="w-full rounded-md bg-gradient-to-t from-emerald-500/30 to-emerald-400/80 transition-all duration-500 hover:opacity-80 chart-bar"
                style={{ height: `${Math.max(barHeight, 8)}%`, minHeight: '8px' }}
              />
              <span className="text-[10px] text-gray-400 mt-1.5">{item.label}</span>
            </div>
          );
        })}
      </div>
    </GlassCard>
  );
};

export default PerformanceChart;