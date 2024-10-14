import React from "react";
import "./styles.css"; // Estilos do modal

function Modal({ isOpen, onClose, children }) {
  // Retorna null quando o modal está fechado
  if (!isOpen) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        {/* Botão de fechar */}
        <button className="modal-close" onClick={onClose}>
          &times;
        </button>
        
        {/* Conteúdo do modal */}
        {children}
      </div>
    </div>
  );
}

export default Modal;
