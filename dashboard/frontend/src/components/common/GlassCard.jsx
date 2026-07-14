import React from 'react';

const GlassCard = ({ children, className = '', title, titleIcon }) => {
  return (
    <div className={`glass rounded-2xl p-5 ${className}`}>
      {title && (
        <h3 className="text-sm font-medium text-gray-300 mb-4 flex items-center gap-2">
          {titleIcon && <span className="text-emerald-400">{titleIcon}</span>}
          {title}
        </h3>
      )}
      {children}
    </div>
  );
};

export default GlassCard;