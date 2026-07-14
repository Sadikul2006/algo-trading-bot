import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { 
  FaHome, 
  FaChartBar, 
  FaRobot, 
  FaCog,
  FaChartLine,
  FaTimes 
} from 'react-icons/fa';

const Sidebar = ({ isOpen, toggleSidebar }) => {
  const location = useLocation();

  const navItems = [
    { path: '/', label: 'Dashboard', icon: <FaHome className="text-lg" /> },
    { path: '/backtesting', label: 'Backtesting', icon: <FaChartBar className="text-lg" /> },
    { path: '/live-trading', label: 'Live Trading', icon: <FaRobot className="text-lg" /> },
    { path: '/settings', label: 'Settings', icon: <FaCog className="text-lg" /> },
  ];

  return (
    <>
      {/* Mobile Overlay */}
      {isOpen && (
        <div
          className="fixed inset-0 bg-black/50 backdrop-blur-sm z-40 lg:hidden"
          onClick={toggleSidebar}
        />
      )}

      <aside
        className={`
          fixed top-0 left-0 h-full w-[280px] bg-[#0f131a] border-r border-white/5 z-50
          transition-transform duration-300 ease-in-out
          flex flex-col shadow-2xl
          ${isOpen ? 'translate-x-0' : '-translate-x-full'}
          lg:translate-x-0 lg:static lg:z-auto
        `}
      >
        {/* Logo */}
        <div className="flex items-center justify-between p-5 border-b border-white/5">
          <div className="flex items-center gap-2">
            <FaChartLine className="text-emerald-400 text-2xl" />
            <span className="font-bold text-xl tracking-tight text-white/90">
              IndiaTrade
            </span>
          </div>
          <button
            onClick={toggleSidebar}
            className="lg:hidden text-gray-400 hover:text-white"
          >
            <FaTimes size={20} />
          </button>
        </div>

        {/* Navigation */}
        <nav className="flex-1 p-4 space-y-1.5 overflow-y-auto">
          {navItems.map((item) => {
            const isActive = location.pathname === item.path;
            return (
              <Link
                key={item.path}
                to={item.path}
                onClick={() => {
                  if (window.innerWidth < 1024) toggleSidebar();
                }}
                className={`
                  flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-200
                  ${isActive
                    ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 shadow-lg shadow-emerald-500/5'
                    : 'text-gray-400 hover:bg-white/5 hover:text-white'
                  }
                `}
              >
                {item.icon}
                <span className="font-medium">{item.label}</span>
              </Link>
            );
          })}
        </nav>

        {/* Market Status */}
        <div className="p-4 border-t border-white/5 space-y-2">
          <div className="glass rounded-xl p-3 text-xs text-gray-400 flex items-center gap-2">
            <span className="w-2 h-2 bg-emerald-400 rounded-full animate-pulse"></span>
            Market: Open
          </div>
          <div className="text-xs text-gray-500 text-center">
            NIFTY 50: 19,567.80
          </div>
        </div>
      </aside>
    </>
  );
};

export default Sidebar;