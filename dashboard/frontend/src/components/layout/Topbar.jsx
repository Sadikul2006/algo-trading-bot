import React from 'react';
import { FaBars, FaBell, FaUserCircle } from 'react-icons/fa';

const Topbar = ({ title, toggleSidebar }) => {
  return (
    <header className="bg-[#0f131a]/80 backdrop-blur-md border-b border-white/5 sticky top-0 z-30">
      <div className="flex items-center justify-between px-6 py-4">
        <div className="flex items-center gap-4">
          <button
            onClick={toggleSidebar}
            className="lg:hidden text-gray-400 hover:text-white"
          >
            <FaBars size={22} />
          </button>
          <h1 className="text-xl font-semibold tracking-tight text-white/90">
            {title}
          </h1>
        </div>

        <div className="flex items-center gap-4">
          {/* Notifications */}
          <button className="relative text-gray-400 hover:text-white transition">
            <FaBell size={20} />
            <span className="absolute -top-0.5 -right-0.5 w-2 h-2 bg-red-500 rounded-full"></span>
          </button>

          {/* User Profile */}
          <div className="flex items-center gap-2 cursor-pointer hover:opacity-80">
            <FaUserCircle size={28} className="text-emerald-400" />
            <span className="hidden sm:inline text-sm text-gray-300">
              Trader
            </span>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Topbar;