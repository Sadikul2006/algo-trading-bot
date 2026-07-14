import React, { useState } from 'react';
import { Outlet, useLocation } from 'react-router-dom';
import Sidebar from './Sidebar';
import Topbar from './Topbar';

const Layout = () => {
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const location = useLocation();

  const pageTitles = {
    '/': 'Dashboard',
    '/backtesting': 'Backtesting',
    '/live-trading': 'Live Trading',
    '/settings': 'Settings',
  };

  const title = pageTitles[location.pathname] || 'Dashboard';

  return (
    <div className="flex min-h-screen bg-[#0b0e14]">
      <Sidebar isOpen={sidebarOpen} toggleSidebar={() => setSidebarOpen(!sidebarOpen)} />
      <div className="flex-1 flex flex-col min-h-screen">
        <Topbar title={title} toggleSidebar={() => setSidebarOpen(!sidebarOpen)} />
        <main className="flex-1 p-5 lg:p-7 overflow-y-auto page-enter">
          <Outlet />
        </main>
      </div>
    </div>
  );
};

export default Layout;