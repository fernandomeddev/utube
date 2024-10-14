import React from 'react';
import logo from '../../assets/img/logo.png';
import './styles.css';

function Header() {
  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <div className="header">
      <div className="logo">
        <img src={logo} alt="Logo" />
      </div>

      <div className="user-section">
        <div className="nav-item" onClick={scrollToTop}>
          <p>Inicio</p>
        </div>
        <div className="user-avatar">
          <img src="https://randomuser.me/api/portraits/men/1.jpg" alt="User Avatar" />
        </div>
      </div>
    </div>
  );
}

export default Header;
