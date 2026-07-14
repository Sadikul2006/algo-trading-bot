import React from 'react';
import { 
  FaMoon, 
  FaSun, 
  FaBuilding, 
  FaTelegramPlane,
  FaBell,
  FaShieldAlt,
  FaUserCog
} from 'react-icons/fa';
import GlassCard from '../common/GlassCard';

const Settings = () => {
  const settingsSections = [
    {
      title: 'Theme',
      icon: <FaMoon className="text-emerald-400" />,
      description: 'Dark mode (default)',
      status: 'Dark',
      statusColor: 'text-emerald-400',
    },
    {
      title: 'Broker',
      icon: <FaBuilding className="text-emerald-400" />,
      description: 'Zerodha (Kite)',
      status: 'Connected',
      statusColor: 'text-emerald-400',
    },
    {
      title: 'Telegram Bot',
      icon: <FaTelegramPlane className="text-emerald-400" />,
      description: '@indiatrade_bot',
      status: 'Active',
      statusColor: 'text-emerald-400',
    },
    {
      title: 'Notifications',
      icon: <FaBell className="text-emerald-400" />,
      description: 'Trade alerts & updates',
      status: 'Enabled',
      statusColor: 'text-emerald-400',
    },
    {
      title: 'Security',
      icon: <FaShieldAlt className="text-emerald-400" />,
      description: '2FA & session management',
      status: 'Secure',
      statusColor: 'text-emerald-400',
    },
    {
      title: 'Account',
      icon: <FaUserCog className="text-emerald-400" />,
      description: 'Profile & preferences',
      status: 'Configured',
      statusColor: 'text-emerald-400',
    },
  ];

  return (
    <div className="space-y-6 max-w-3xl">
      <div className="glass-light rounded-2xl p-6 border border-white/5">
        <h2 className="text-xl font-semibold text-white/90">⚙️ Settings</h2>
        <p className="text-sm text-gray-400 mt-1">
          Configure your trading preferences and integrations
        </p>
      </div>

      {settingsSections.map((section, index) => (
        <GlassCard key={index} className="flex items-center justify-between hover:bg-white/5 transition-colors">
          <div className="flex items-center gap-4">
            <div className="text-2xl">{section.icon}</div>
            <div>
              <h4 className="font-medium text-white/90">{section.title}</h4>
              <p className="text-sm text-gray-400">{section.description}</p>
            </div>
          </div>
          <span className={`bg-white/10 px-3 py-1 rounded-full text-xs ${section.statusColor}`}>
            {section.status}
          </span>
        </GlassCard>
      ))}

      <GlassCard className="text-center text-gray-400 text-sm border border-dashed border-white/10">
        <FaTelegramPlane className="inline mr-2 text-emerald-400" />
        All settings are UI only - ready for backend integration
      </GlassCard>
    </div>
  );
};

export default Settings;